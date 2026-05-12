# Architecture

Freexcel is a free, native Windows desktop spreadsheet application. See [BUILD_PLAN.md](../Plan/BUILD_PLAN.md) for the full specification and phased build plan.

## Layered Architecture

```
App.Host (composition root, DI, startup)
  └── App.UI (WPF controls — GridView, dialogs)
       └── Core.Commands (command bus, undo/redo, find/replace service)
       └── Core.Calc (dependency graph, recalc engine, viewport service)
            └── Core.Formula (lexer, parser, AST, evaluator, built-in functions)
                 └── Core.Model (pure data types — Workbook, Sheet, Cell, ScalarValue, CellStyle)
       └── Core.IO (file adapters — XLSX via ClosedXML, CSV, native JSON)
            └── Core.Model
```

**Dependency rule**: No `Core.*` project may reference any `App.*` project. This is enforced by project references.

## Key Principles

1. **UI depends on Core; Core never depends on UI.** The formula engine and workbook model run from unit tests with no UI.
2. **One source of truth: the engine.** UI sends commands; the engine mutates state; UI re-renders from `IViewportService`.
3. **Every mutation is a command.** No direct setters on the workbook from outside the engine. This gives undo/redo for free.
4. **The engine owns the dependency graph.** The `calc-chain` in `.xlsx` files is ignored — we build our own.
5. **File adapters are translation layers only.** No business logic in `Core.IO`.

## Phase 1 — What Was Built

- **Core.Model**: `Workbook`, `Sheet`, `Cell`, `ScalarValue` hierarchy (`BlankValue`, `NumberValue`, `BoolValue`, `TextValue`, `DateTimeValue`, `ErrorValue`), `CellAddress` (A1 notation), `GridRange`, `CellStyle` with `StyleId` registry
- **Core.Formula**: Lexer → Parser → AST → Evaluator; 16 built-in functions; cross-sheet reference support (`Sheet1!A1`)
- **Core.Calc**: `DependencyGraph` (topological sort, Kahn's algorithm, cycle detection), `RecalcEngine` (volatile-cell support), `ViewportService`
- **Core.Commands**: `ICommandBus` with undo/redo stack, `EditCellsCommand`, `AddSheetCommand`, `RenameSheetCommand`, `FindReplaceService`
- **Core.IO**: `NativeJsonAdapter` (.fxl), `XlsxFileAdapter` (ClosedXML 0.105.0), `CsvFileAdapter`
- **App.UI**: `GridView` — virtualized DrawingContext rendering, selection, row/column headers
- **App.Host**: `MainWindow` — formula bar, scrollbars, open/save dialogs, keyboard navigation, Find & Replace

## Phase 2 — Key Architectural Decisions

See `docs/DECISIONS/` for the full ADRs. Summary:

| ADR | Decision |
|-----|----------|
| [001](DECISIONS/001-csharp-dotnet10-wpf.md) | C# 12 / .NET 10 / WPF for v1 |
| [002](DECISIONS/002-style-registry.md) | Style registry: deduplicate by structural equality, `StyleId 0` = Default |
| [003](DECISIONS/003-xlsx-fidelity.md) | XLSX fidelity contract: preserve unknown features, map theme colors to black |
| [004](DECISIONS/004-volatile-functions.md) | Volatile functions: dirty-first evaluation order |
| [005](DECISIONS/005-cross-sheet-references.md) | Cross-sheet refs: `Workbook?` threaded through evaluator chain |
| [006](DECISIONS/006-find-replace.md) | Find & Replace: service in `Core.Commands`, `Func<Workbook>` in dialog |

## Known Phase 2 Limitations

- Quoted sheet names in cross-sheet references (`'My Sheet'!A1`) are not supported
- Theme and indexed colors in `.xlsx` files are mapped to black (no theme context)
- CSV adapter does not handle quoted fields or multi-line cells
- Volatile function tracking is not thread-safe (single UI thread assumed)
- Style registry uses linear scan (acceptable for v1 style counts)
