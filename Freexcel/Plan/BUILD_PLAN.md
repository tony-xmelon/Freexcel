# Excel Clone for Windows — Build Plan

> **Purpose of this document**
> This is the canonical build plan for a free, open-source Microsoft Excel clone targeting Windows. It is written to be handed directly to Claude Code (or any AI coding assistant) as the working specification. It encodes architectural decisions, sequencing, contracts, and explicit non-goals. When in doubt, follow this document over any other source.

---

## 1. Vision & Scope

### 1.1 What we are building
A free, native Windows desktop spreadsheet application with strong `.xlsx` compatibility, a real formula engine, and a clean separation between UI, calculation, file I/O, and (eventually) AI features.

### 1.2 What we are explicitly NOT building (in v1)
- A web version, mobile version, or cross-platform port.
- Real-time multi-user collaboration.
- VBA macro compatibility.
- An AI copilot (Phase 5+ only).
- A pivot table engine (Phase 4).
- 100% Excel feature parity. Target the 90% of features that 90% of users actually use.

### 1.3 Definition of success for MVP (Phase 1)
A user can open the app, type numbers and text into cells, write formulas including `=SUM(A1:A10)`, save to a native file, reopen it, undo/redo any action, and navigate a 100,000-cell sheet without UI lag.

---

## 2. Architectural Principles

These are non-negotiable. Every PR should be reviewable against them.

1. **UI depends on Core; Core never depends on UI.** The formula engine and workbook model must be runnable from a unit test or CLI with no UI present.
2. **One source of truth: the engine.** UI never edits workbook state directly. UI sends commands; engine mutates state; engine emits events; UI re-renders.
3. **Every mutation is a command.** No direct setters on the workbook from outside the engine. This is what makes undo/redo, future collaboration, and future AI actions tractable.
4. **The engine owns the dependency graph.** Do NOT trust the `calc-chain` part inside an `.xlsx` file — Microsoft's own docs state it represents only the order of the last calculation, not the authoritative dependency tree. Build your own.
5. **File adapters never define business rules for calc.** XLSX reading/writing is a translation layer between the on-disk format and the canonical in-memory model. Nothing more.
6. **Defer complexity ruthlessly.** When in doubt, choose the simpler implementation. Sparse columnar storage, multi-process IPC, Rust FFI — these are all valid eventually, but not now.
7. **Layered modular monolith.** One process, one solution, clean project boundaries. No microservices. No sidecars. No FFI in v1.

---

## 3. Technology Stack (v1)

| Layer | Choice | Rationale |
|---|---|---|
| Language | **C# 12 / .NET 8** | Best Windows fit, productive, single toolchain, excellent ecosystem for the hard parts (file I/O, UI). |
| UI framework | **WPF** (preferred) or WinUI 3 | WPF is more mature and stable for complex custom controls like a virtualized grid. WinUI 3 is acceptable if the team prefers it, but expect more friction. |
| Grid rendering | Custom canvas-based virtualized grid | Standard `DataGrid` will not scale. We must own this control. |
| File I/O (.xlsx) | **ClosedXML** initially, replaceable later | Free, MIT-licensed, good-enough fidelity for v1. Keep behind an adapter interface so we can swap it. |
| Charts (Phase 3) | **OxyPlot** or **LiveChartsCore** | Both free, both adequate for v1 chart types. |
| Testing | **xUnit** + **FluentAssertions** | Standard. |
| DI container | **Microsoft.Extensions.DependencyInjection** | Built-in, sufficient. |
| Logging | **Serilog** | Console + rolling file sink. |
| Packaging | **MSIX** | Modern Windows install story. |

### 3.1 Stack decisions deliberately deferred
- **Rust calc engine**: Rejected for v1. May be revisited in Phase 4+ if profiling shows .NET is genuinely the bottleneck. Keep the `Core.Formula` and `Core.Calc` contracts language-neutral (no C#-specific types leaking) so this port remains possible.
- **Multi-process architecture**: Rejected for v1. The whole app runs in one process.
- **AI sidecar**: Rejected for v1. See Phase 5.

---

## 4. Solution Structure

```
Freexcel/
├── src/
│   ├── Freexcel.Core.Model/         # Workbook, Sheet, Cell, Range, Styles (pure data)
│   ├── Freexcel.Core.Formula/       # Lexer, parser, AST, binder, functions
│   ├── Freexcel.Core.Calc/          # Dependency graph, recalc scheduler, evaluator
│   ├── Freexcel.Core.Commands/      # Command bus, transaction journal, undo/redo
│   ├── Freexcel.Core.IO/            # File adapters (xlsx, csv, native)
│   ├── Freexcel.App.UI/             # WPF shell, grid, ribbon, dialogs
│   └── Freexcel.App.Host/           # Composition root, DI, settings, startup
├── tests/
│   ├── Freexcel.Core.Model.Tests/
│   ├── Freexcel.Core.Formula.Tests/
│   ├── Freexcel.Core.Calc.Tests/
│   ├── Freexcel.Core.IO.Tests/
│   ├── Freexcel.Integration.Tests/  # Cross-layer scenarios
│   └── Freexcel.Fixtures/           # Sample .xlsx files for round-trip testing
├── docs/
│   ├── ARCHITECTURE.md
│   ├── FORMULA_ENGINE.md
│   └── DECISIONS/                     # ADRs (architecture decision records)
└── build/
    └── ci/                            # GitHub Actions or Azure Pipelines
```

### 4.1 Dependency rules (enforced by project references)
- `Core.Model` depends on nothing.
- `Core.Formula` depends on `Core.Model`.
- `Core.Calc` depends on `Core.Model`, `Core.Formula`.
- `Core.Commands` depends on `Core.Model`.
- `Core.IO` depends on `Core.Model`.
- `App.UI` depends on all Core projects.
- `App.Host` depends on everything; it is the composition root.
- **NO Core project may reference any `App.*` project. Ever.**

---

## 5. Core Interface Contracts

These contracts are the spine of the system. Define them early; implementations come second. Names are stable — they form the public surface of the engine.

### 5.1 Workbook services

```csharp
public interface IWorkbookService
{
    WorkbookId CreateWorkbook(NewWorkbookOptions options);
    Task<WorkbookId> OpenWorkbookAsync(DocumentSource source, CancellationToken ct);
    Task SaveWorkbookAsync(WorkbookId workbook, DocumentTarget target, CancellationToken ct);
    void CloseWorkbook(WorkbookId workbook);

    WorkbookMeta GetWorkbookMeta(WorkbookId workbook);
    IReadOnlyList<SheetMeta> ListSheets(WorkbookId workbook);
}

public interface IWorksheetService
{
    CellBlock GetRange(WorkbookId wb, SheetId sheet, GridRange range);
    EditResult SetRange(WorkbookId wb, SheetId sheet, GridRange range, CellInputBlock input);
    EditResult ClearRange(WorkbookId wb, SheetId sheet, GridRange range);

    void InsertRows(WorkbookId wb, SheetId sheet, uint at, uint count);
    void DeleteRows(WorkbookId wb, SheetId sheet, uint at, uint count);
    void InsertColumns(WorkbookId wb, SheetId sheet, uint at, uint count);
    void DeleteColumns(WorkbookId wb, SheetId sheet, uint at, uint count);
}
```

### 5.2 Formula services

```csharp
public interface IFormulaService
{
    ParsedFormula ParseFormula(string formulaText, FormulaContext ctx);
    BoundFormula BindFormula(WorkbookId wb, SheetId sheet, ParsedFormula formula);
    FormulaExplanation ExplainFormula(WorkbookId wb, SheetId sheet, CellAddress address);
    IReadOnlyList<CellAddress> TracePrecedents(WorkbookId wb, SheetId sheet, CellAddress address);
    IReadOnlyList<CellAddress> TraceDependents(WorkbookId wb, SheetId sheet, CellAddress address);
}

public interface ICalculationService
{
    void MarkDirty(WorkbookId wb, IReadOnlyList<CellAddress> changes);
    RecalcReport RecalcWorkbook(WorkbookId wb, RecalcMode mode);
    RecalcReport RecalcRange(WorkbookId wb, SheetId sheet, GridRange range);
    CalcStateSnapshot GetCalcState(WorkbookId wb);
}
```

### 5.3 Viewport service (UI's window into the engine)

```csharp
public interface IViewportService
{
    ViewportModel GetViewport(WorkbookId wb, SheetId sheet, ViewportRequest request);
    HitTestResult HitTest(WorkbookId wb, SheetId sheet, PixelPoint point, float zoom);
}

public sealed record ViewportRequest(
    uint TopRow,
    uint LeftCol,
    uint RowCount,
    uint ColCount,
    bool IncludeFormulas,
    bool IncludeStyles,
    bool IncludeObjects);

public sealed record ViewportModel(
    IReadOnlyList<DisplayCell> Cells,
    IReadOnlyList<RowMetric> RowMetrics,
    IReadOnlyList<ColMetric> ColMetrics,
    FrozenPaneState? FrozenPanes,
    IReadOnlyList<OverlayPrimitive> Overlays);
```

### 5.4 Command bus (every mutation goes through here)

```csharp
public interface ICommandBus
{
    TransactionId BeginTransaction(string label);
    CommandOutcome Execute(TransactionId tx, IWorkbookCommand command);
    CommitSummary Commit(TransactionId tx);
    void Rollback(TransactionId tx);

    UndoSummary Undo(WorkbookId wb);
    RedoSummary Redo(WorkbookId wb);
}

public interface IWorkbookCommand
{
    string Label { get; }
    CommandOutcome Apply(IEngineContext ctx);
    void Revert(IEngineContext ctx);
}

// Concrete commands (Phase 1 minimum set):
public sealed record EditCellsCommand(...);
public sealed record ApplyStyleCommand(...);
public sealed record InsertRowsCommand(...);
public sealed record DeleteRowsCommand(...);
public sealed record InsertColumnsCommand(...);
public sealed record DeleteColumnsCommand(...);
public sealed record AddSheetCommand(...);
public sealed record RenameSheetCommand(...);
```

### 5.5 Engine event stream

```csharp
public interface IEngineEventBus
{
    IObservable<EngineEvent> Events { get; }
}

public abstract record EngineEvent;
public sealed record WorkbookOpenedEvent(WorkbookId WorkbookId) : EngineEvent;
public sealed record CellsChangedEvent(WorkbookId WorkbookId, SheetId SheetId, IReadOnlyList<CellAddress> Changed) : EngineEvent;
public sealed record RecalcStartedEvent(WorkbookId WorkbookId) : EngineEvent;
public sealed record RecalcCompletedEvent(WorkbookId WorkbookId, RecalcReport Report) : EngineEvent;
public sealed record ErrorRaisedEvent(string Code, string Message) : EngineEvent;
```

### 5.6 File adapter (xlsx)

```csharp
public interface IXlsxReader
{
    Task<WorkbookPackageModel> ReadPackageAsync(DocumentSource source, CancellationToken ct);
    WorkbookAggregate MapToDomain(WorkbookPackageModel package);
}

public interface IXlsxWriter
{
    WorkbookPackageModel MapFromDomain(WorkbookAggregate workbook);
    Task WritePackageAsync(WorkbookPackageModel package, DocumentTarget target, CancellationToken ct);
}
```

### 5.7 Core DTOs

```csharp
public readonly record struct CellAddress(SheetId Sheet, uint Row, uint Col);
public readonly record struct GridRange(CellAddress Start, CellAddress End);

public sealed record DisplayCell(
    uint Row,
    uint Col,
    ScalarValue? RawValue,
    string DisplayText,
    string? Formula,
    StyleId StyleId,
    CellError? Error);

public abstract record ScalarValue;
public sealed record BlankValue() : ScalarValue;
public sealed record NumberValue(double Value) : ScalarValue;
public sealed record BoolValue(bool Value) : ScalarValue;
public sealed record TextValue(string Value) : ScalarValue;
public sealed record DateTimeValue(double Value) : ScalarValue;
public sealed record ErrorValue(string Code) : ScalarValue;

public sealed record EditResult(
    IReadOnlyList<CellAddress> ChangedCells,
    IReadOnlyList<CellAddress> DirtyCells,
    bool RequiresRecalc);
```

---

## 6. Build Phases

Each phase ends with a working, demoable build. Do not start Phase N+1 until Phase N is genuinely complete (passing tests, no known critical bugs).

### Phase 0 — Foundations (~1 week)

**Goal**: Empty solution that compiles, has CI, runs tests, and opens a blank window.

- [ ] Initialize git repo with `.gitignore` for .NET and Visual Studio.
- [ ] Create solution with all 7 projects from §4 (Core projects empty, App.UI shows a blank window).
- [ ] Set up project references per §4.1 dependency rules.
- [ ] Add xUnit test projects with one passing smoke test each.
- [ ] Set up CI (GitHub Actions or Azure Pipelines): build + test on every push.
- [ ] Add Serilog with console + rolling file sinks.
- [ ] Set up DI container in `App.Host` and resolve a single service end-to-end.
- [ ] Write `docs/ARCHITECTURE.md` stub linking back to this build plan.
- [ ] Add first ADR: "Why C#/.NET 8 and WPF for v1" (referencing this doc).

**Done when**: `dotnet build && dotnet test` is green in CI, and the app opens a window titled "Freexcel".

---

### Phase 1 — MVP: It's a spreadsheet (4–6 weeks)

**Goal**: A user could call this a spreadsheet without laughing.

#### 1.1 Core model
- [ ] `Workbook`, `Sheet`, `Cell`, `Style`, `NamedRange` types.
- [ ] Storage: `Dictionary<CellAddress, Cell>` per sheet. NOT sparse columnar — that's premature.
- [ ] `CellAddress`, `GridRange` value types with A1-notation parsing/formatting helpers.

#### 1.2 Formula engine
- [ ] Lexer: tokens for numbers, strings, cell refs, range refs, operators, function names, parens, commas.
- [ ] Parser: recursive descent or shunting-yard producing an AST.
- [ ] Binder: resolves cell/range references to engine identities, validates function arities.
- [ ] Evaluator: walks the AST against the workbook.
- [ ] Functions in v1 (15 minimum): `SUM`, `AVERAGE`, `MIN`, `MAX`, `COUNT`, `COUNTA`, `IF`, `AND`, `OR`, `NOT`, `ROUND`, `ABS`, `CONCAT`, `LEN`, `LEFT`, `RIGHT`.
- [ ] **First test you write**: `Evaluate("=SUM(A1:A3)")` with A1=1, A2=2, A3=3 returns 6. This single test exercises tokenizer, parser, range expansion, and evaluator.

#### 1.3 Dependency graph & recalc
- [ ] Build dependency graph as cells reference each other.
- [ ] Mark dirty on change; recalc in topological order; never recalc the whole sheet.
- [ ] Cycle detection with `#CIRCULAR!` error result.
- [ ] **Test corpus**: 50+ unit tests covering operator precedence, range expansion, cycle detection, error propagation.

#### 1.4 Command bus & undo/redo
- [ ] `ICommandBus` implementation with transaction journal.
- [ ] Per-workbook undo/redo stack (depth: 100 minimum).
- [ ] Commands implemented: `EditCellsCommand`, `InsertRowsCommand`, `DeleteRowsCommand`, `InsertColumnsCommand`, `DeleteColumnsCommand`, `AddSheetCommand`, `RenameSheetCommand`.
- [ ] Every UI action goes through the command bus. No exceptions.

#### 1.5 Virtualized grid (the hardest UI piece)
- [ ] Custom WPF control rendering only the visible viewport.
- [ ] Asks the engine for cells via `IViewportService.GetViewport()`.
- [ ] Scroll, select (single cell, range, full row, full column, Ctrl+A), keyboard nav (arrows, Tab, Enter, Ctrl+arrows, Home, End, PageUp/PageDown), edit-in-place with F2 or double-click, formula bar synced to active cell.
- [ ] Copy/paste/cut within the sheet (Ctrl+C/X/V, internal clipboard format + plain text fallback).
- [ ] **Performance bar**: smooth scrolling on a 100k-cell sheet on a mid-range laptop. If it stutters, fix it before moving on.

#### 1.6 Native save/load format
- [ ] NOT xlsx yet. Use JSON or MessagePack for the native format. We're getting the model right first; xlsx comes in Phase 2.
- [ ] Round-trip test: open file → no changes → save → byte-identical (or semantically identical).

**Done when**: User can launch app, type values and formulas, save, close, reopen, see the same content, undo and redo any action, and scroll a 100k-cell sheet without lag.

---

### Phase 2 — File compatibility (3–4 weeks)

**Goal**: Open and save real `.xlsx` files.

- [ ] `Core.IO.Xlsx.Reader` using ClosedXML behind the `IXlsxReader` interface.
- [ ] `Core.IO.Xlsx.Writer` using ClosedXML behind the `IXlsxWriter` interface.
- [ ] `Core.IO.Csv` reader/writer (simpler, build it first as a warmup).
- [ ] **Critical**: ignore the `calc-chain` part when reading. We build our own dependency graph from the formulas.
- [ ] **Test fixture corpus**: 20+ real `.xlsx` files from public sources, varied: simple data, formulas, multiple sheets, formatting. Round-trip them in CI.
- [ ] Define and document the "fidelity contract": what we preserve, what we may lose (e.g. v1 may drop charts, pivot tables, conditional formatting on read — but must not corrupt them on write if a user re-saves a file we couldn't fully parse).

**Done when**: User can open a real-world `.xlsx` file, edit it, save it, and reopen it in Excel without data loss for content within our supported feature set.

---

### Phase 3 — Formatting & UX polish (3–4 weeks)

**Goal**: It looks and feels like a real spreadsheet.

- [ ] Number formats: General, Number, Currency, Percentage, Date, Time, Custom (subset).
- [ ] Cell formatting: font family/size/weight/style/color, fill color, borders (per-edge), alignment (horizontal/vertical), wrap text.
- [ ] Column/row resize (drag handles, double-click to autofit).
- [ ] Multiple sheets with tab bar (add, delete, rename, reorder, color).
- [ ] Freeze panes (rows, columns, both).
- [ ] Find & replace (within sheet, within workbook, with options).
- [ ] Basic charts (column, line, pie) via OxyPlot or LiveChartsCore — embedded in sheet as objects.

**Done when**: A user could use this app for daily light-to-medium spreadsheet work and not feel they're missing something obvious.

---

### Phase 4 — Power features (ongoing, 2–3 months)

- [ ] Conditional formatting.
- [ ] Data validation.
- [ ] Sort & filter.
- [ ] Named ranges (UI for managing them; engine support already exists from Phase 1).
- [ ] Autofill / flash fill.
- [ ] Print & PDF export.
- [ ] Pivot tables. **Hard.** Budget 4+ weeks alone.
- [ ] Expand function library toward ~200 functions to cover 95% of real-world usage.
- [ ] Dynamic arrays (`FILTER`, `SORT`, `UNIQUE`, spill behavior). Touches the calc engine — design carefully.

**Optional revisit point**: profile recalc on huge workbooks. If .NET genuinely can't keep up, this is when a Rust calc-core port is on the table. Until profiling proves it, don't do it.

---

### Phase 5 — Scripting & AI (optional, later)

#### 5.1 Scripting
- [ ] Embed C# scripting via Roslyn, OR Lua via NLua.
- [ ] Expose a narrow, sandboxed API surface to scripts.
- [ ] Do NOT attempt VBA compatibility.

#### 5.2 AI copilot (only if there's appetite)
The AI layer, when built, follows these rules absolutely:

- AI never mutates workbook state directly. Every AI action goes through `ICommandBus` like every other mutation.
- AI has a narrow tool surface: `GetSelectionContext`, `GetSheetSchema`, `ProposeFormula`, `ApplyFormulaToRange`, `ExplainFormula`, `CreateChart`, `NormalizeColumn`, `PreviewBulkEdit`, `CommitTransaction`, `RollbackTransaction`.
- Every AI action is previewable, undoable, and audit-logged.
- Three-part design: context extractor → planner (LLM) → action executor.
- Sensitive workbook content never leaves the machine without explicit user consent.

---

## 7. Cross-Cutting Rules

### 7.1 Testing
- Every Core project has a corresponding test project.
- Formula engine: aim for 200+ unit tests by end of Phase 1. The formula engine is where bugs hide and where regressions are most painful.
- Round-trip xlsx tests run in CI on every PR from Phase 2 onward.
- Integration tests live in `Freexcel.Integration.Tests` and exercise full workflows (open → edit → save → reopen).
- UI is harder to test; minimum bar is automated smoke tests of key user flows via WPF UI automation by end of Phase 3.

### 7.2 Performance budgets
- Cell edit → screen update: < 16ms (60fps).
- Recalc on a 10k-cell workbook with typical formula density: < 100ms.
- Open a 1MB `.xlsx` file: < 2 seconds.
- Memory: a 100k-cell workbook should fit comfortably in < 200MB.
- These are budgets, not aspirations. If you blow one, fix it before adding features.

### 7.3 Code style
- Standard .NET conventions; enable `nullable` everywhere; warnings as errors in CI.
- Public APIs in Core projects have XML doc comments.
- No `internal` for things that should be tested — make them `public` or use `InternalsVisibleTo`.
- Prefer records and read-only structs for DTOs.
- No `static` mutable state. Ever.

### 7.4 Decision records
Every significant architectural decision gets an ADR in `docs/DECISIONS/`. Format: short, one decision per file, dated, with context / decision / consequences sections.

---

## 8. The Five Hard-Won Warnings

Read these before starting. They are where most spreadsheet clones die.

1. **The grid is the hardest UI component.** Off-the-shelf .NET grids choke past ~10k rows. We're building our own from day one. This is not optional. If we don't, we will discover in Phase 3 that we have to rewrite the entire UI layer.

2. **The formula engine deserves its own design doc.** Before writing a line of parser code, write `docs/FORMULA_ENGINE.md` describing the tokenizer rules, parser approach, evaluation model, and dependency graph design. Two days of design saves two months of refactoring.

3. **Test files matter more than test code.** Build a corpus of real `.xlsx` files in `tests/Freexcel.Fixtures/` and run round-trip tests in CI from Phase 2 day one. Get them from public sources (government open data, Wikipedia, sample financial models).

4. **Don't aim for full Excel parity.** Excel has 30+ years and thousands of engineers behind it. Aim for "covers what 90% of users actually do." That's already a massive product.

5. **The calc-chain in `.xlsx` is a hint, not a contract.** Build your own dependency graph. Anyone telling you otherwise has not shipped a spreadsheet.

---

## 9. First Concrete Step

For Claude Code, after reading this document:

1. Create the solution and 7 projects per §4.
2. Set up project references per §4.1.
3. Add xUnit test projects.
4. Write this failing test in `Freexcel.Core.Formula.Tests`:
   ```csharp
   [Fact]
   public void SumOfRange_ReturnsExpectedTotal()
   {
       var workbook = new Workbook();
       var sheet = workbook.AddSheet("Sheet1");
       sheet.SetCell(new CellAddress(sheet.Id, 1, 1), new NumberValue(1));
       sheet.SetCell(new CellAddress(sheet.Id, 2, 1), new NumberValue(2));
       sheet.SetCell(new CellAddress(sheet.Id, 3, 1), new NumberValue(3));

       var result = new FormulaEvaluator().Evaluate("=SUM(A1:A3)", sheet);

       result.Should().Be(new NumberValue(6));
   }
   ```
5. Make it pass. Everything else grows from this point.

---

## 10. Glossary

- **A1 notation**: Excel-style cell addressing, e.g. `B7` (column B, row 7) or `A1:C10` (a range).
- **AST**: Abstract syntax tree, the parsed-but-not-yet-evaluated form of a formula.
- **Binder**: The component that resolves names and references in a parsed formula to actual workbook entities.
- **Calc-chain**: Optional part of an `.xlsx` file recording the order cells were last calculated. NOT a dependency graph.
- **Dirty marking**: Flagging cells that need recalculation because their inputs changed.
- **Dynamic array / spill**: An Excel-2019+ feature where a single formula can return multiple values that "spill" into adjacent cells.
- **OOXML / SpreadsheetML**: The XML-based file format inside `.xlsx`.
- **Recalc**: The process of recomputing dependent cells after a change.
- **Topological order**: An ordering where each item comes before everything that depends on it. Used to recalculate cells in a valid sequence.
- **Volatile function**: A function that must recalculate every time anything changes (e.g. `NOW()`, `RAND()`).

---

*Document version: 1.0. Maintained as `BUILD_PLAN.md` at the repository root. Update via PR with reasoning in the commit message.*
