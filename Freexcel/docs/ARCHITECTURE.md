# Architecture

Freexcel is a free, native Windows desktop spreadsheet application with a WPF shell, a command-driven workbook engine, and explicit `.xlsx` fidelity boundaries. Current outstanding work is tracked in [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md), with command-level scope in [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md) and file-format scope in [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md).

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

## Current Implemented Baseline

- **Core.Model**: `Workbook`, `Sheet`, `Cell`, `ScalarValue` hierarchy (`BlankValue`, `NumberValue`, `BoolValue`, `TextValue`, `DateTimeValue`, `ErrorValue`), `CellAddress` (A1 notation), `GridRange`, `CellStyle` with `StyleId` registry
- **Core.Formula**: Lexer → Parser → AST → Evaluator; 16 built-in functions; cross-sheet reference support (`Sheet1!A1`)
- **Core.Calc**: `DependencyGraph` (topological sort, Kahn's algorithm, cycle detection), `RecalcEngine` (volatile-cell support), `ViewportService`
- **Core.Commands**: `ICommandBus` with undo/redo stack, `EditCellsCommand`, `AddSheetCommand`, `RenameSheetCommand`, `FindReplaceService`
- **Core.IO**: `NativeJsonAdapter` (.fxl), `XlsxFileAdapter` (ClosedXML 0.105.0), `CsvFileAdapter`
- **App.UI**: `GridView` — virtualized DrawingContext rendering, selection, row/column headers
- **App.Host**: `MainWindow` — formula bar, scrollbars, open/save dialogs, keyboard navigation, Find & Replace

## Key Architectural Decisions

See `docs/DECISIONS/` for the full ADRs. Summary:

| ADR | Decision |
|-----|----------|
| [001](DECISIONS/001-csharp-dotnet10-wpf.md) | C# 12 / .NET 10 / WPF for v1 |
| [002](DECISIONS/002-style-registry.md) | Style registry: deduplicate by structural equality, `StyleId 0` = Default |
| [003](DECISIONS/003-xlsx-fidelity.md) | XLSX fidelity contract: preserve modeled features, warn on unsupported package parts, and keep chart/shape theme-color fidelity partial until those adapters consume the workbook theme model |
| [004](DECISIONS/004-volatile-functions.md) | Volatile functions: dirty-first evaluation order |
| [005](DECISIONS/005-cross-sheet-references.md) | Cross-sheet refs: `Workbook?` threaded through evaluator chain |
| [006](DECISIONS/006-find-replace.md) | Find & Replace: service in `Core.Commands`, `Func<Workbook>` in dialog |

## Current Architectural Limitations

- Sheet rename rewrites existing sheet-qualified formula references through the formula AST/serializer path
- `Core.Model` has a workbook theme scaffold with native and XLSX theme-part persistence, loaded-cell-style theme-color resolution, drawing-object theme color references, chart theme-color references/rendering, and an undoable `SetWorkbookThemeCommand`; `Core.IO` has reusable DrawingML color parsing plus minimal worksheet/drawing relationship-based load/save for embedded package parts for every current native chart type, including `twoCellAnchor` chart bounds/EMU offsets, `oneCellAnchor` bounds, `absoluteAnchor` bounds, no-header and no-category-column series range semantics, chart title/range with title text color/font size, axis titles with text color/font size, value-axis bounds/units/log-scale/number formats, axis gridline visibility/color/thickness, tick marks, axis label visibility, axis line color/thickness, legend visibility/position/text/fill/border/theme-text/font-size, global data-label visibility/position/content/number-format/fill/border/text/font/rotation/callout baseline, per-point data-label fill/border/text/font formatting, trendline type/equation/R-squared/line formatting, common column/area combo line-overlay and column/area/line/scatter secondary-value-axis package state, chart/plot area fill and plot border, bar direction/grouping, scatter/bubble X/Y ranges and value-axis pairs, bubble-size ranges, pie/doughnut first-slice angle and exploded-slice package state, doughnut hole size, line/scatter series color-width-dash-marker and marker-fill package formatting, and filled-series fill/outline color-width-dash package formatting; `App.Host` exposes initial Page Layout Themes, Colors, Fonts, and Effects preset dropdowns plus a custom theme dialog for name, heading/body fonts, effects, and core color slots, and `App.UI` renders Subtle/Refined drawing-object shadow effects while deeper OOXML effect semantics and richer chart formatting remain future work
- CSV adapter does not handle quoted fields or multi-line cells
- Volatile function tracking is not thread-safe (single UI thread assumed)
- Style registry uses linear scan (acceptable for v1 style counts)
