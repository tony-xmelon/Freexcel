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
- **Core.Formula**: Lexer → Parser → AST → Evaluator; 339 in-scope Excel built-in functions; dynamic arrays; LET/LAMBDA higher-order functions; cross-sheet reference support (`Sheet1!A1`)
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
| [007](DECISIONS/007-commands-parity-closeout.md) | Commands parity closeout: model-backed gaps can go green; renderer/package/locale gaps stay explicit |

## Commands Parity Architecture

The May 2026 commands parity closeout keeps command mutation in `Core.Commands` and UI orchestration in `App.Host`.
Clipboard, paste, Format Painter, AutoFit, Format Cells, and Flash Fill are command-first features with undoable
model changes and focused planner/service tests. Rendering-only concerns, such as clipboard marquee, shrink-to-fit
text bounds, and deferred chart display, stay in `App.UI` or `App.Host`.
Border gallery presets are modeled as reusable `StyleDiff` planners in `Core.Commands`; `App.Host` only maps menu
choices to those planners and batches perimeter presets into one undoable command.
Cell Style gallery commands use `App.Host` preset planners that return deterministic `StyleDiff` values for supported
font, fill, border, number-format, and alignment fields. They intentionally do not create workbook named styles or bind
to the workbook theme model, so theme-aware named-style semantics remain a parity gap.

Conditional Formatting authoring is split between lightweight WPF dialogs in `App.Host` and the `Core.Model`
`ConditionalFormat` model consumed by commands and XLSX IO. The rule manager clones the full modeled rule state
when editing or reordering so advanced rules such as color scales, data bars, icon sets, Top/Bottom, text, and date
rules do not lose fields even though full Excel manager UI and icon rendering taxonomy remain partial.

Advanced chart families are recognized as `ChartType` values and marked non-renderable through `ChartTypeSupport`.
Authoring commands reject them before mutation, `ChartRenderer` returns no plot model for them, and the Insert UI routes
them to a deferred message. XLSX parsing recognizes common advanced chart package shapes where enough range metadata is
available, but lossless mixed drawing-part writing remains deferred until each family has a data model and writer.

PDF export is intentionally XPS-backed. The WPF managed print APIs cannot deterministically set a Microsoft Print to PDF
output path, so requested PDF paths are exported as deterministic `.xps` files with explicit user messaging.

Flash Fill remains a deterministic pattern service, not an Excel-like ML inference engine. It supports conservative
single-column transforms plus a small multi-column pattern set and returns no result when the examples are ambiguous.

Spell Check remains a deterministic known-corrections service in `Core.Commands`, not dictionary-backed proofing. It
scans literal text cells in sheet/row/column order and plans undoable replacement edits while leaving formula cells alone.

Accessibility Checker remains a deterministic model-backed audit in `Core.Commands`, not a full WCAG or screen-reader
engine. It reports issues supported by current workbook state, including merged cells, missing object alternate text,
hidden sheets/rows/columns with content, unclear hyperlink display text, and charts whose title is missing as the
current accessible label.

The Backstage File > Info panel is a host-only summary surface over existing model services. It reads
`WorkbookStatisticsService` and `AccessibilityCheckerService`, then formats protection/status copy through
`InfoPanelSummaryPlanner` when the Info view opens. It does not introduce cloud account, version-history,
template, Document Inspector, or extended document-metadata subsystems.

Error Checking remains a deterministic model-backed audit in `Core.Commands`, not a full Excel heuristic inference
engine. It reports cached formula error values, text cells that parse as finite invariant-culture numbers, and formulas
whose direct parser-extracted precedents include missing or blank cells. Rule toggles use
`Workbook.DisabledFormulaErrorCodes`, and per-cell ignore state reuses `Cell.IgnoreFormulaError` for both formula-error
and non-error issue kinds.

XLSX worksheet `ignoredErrors` fidelity uses that same `Cell.IgnoreFormulaError` bit as the modeled state. `Core.IO`
loads supported active `ignoredError` `sqref` cells/ranges into the bit and authors a conservative modeled
`ignoredErrors` block on save; detailed native ignored-error flags and unsupported reference forms are retained or
merged best-effort from the source package rather than fully interpreted.

XLSX worksheet `cellWatches` fidelity uses `Workbook.WatchedCells` as the durable modeled state shared with the
Watch Window services. `Core.IO` loads supported single-cell A1 `cellWatch/@r` refs with sheet IDs, skips malformed
refs without creating cells, and authors grouped worksheet `cellWatches` blocks on save. Native-only watch attributes
and unsupported entries are merged best-effort from the source package by matching `r` refs so modeled watches do not
duplicate retained source watches.

XLSX custom-view fidelity uses `Workbook.CustomViews` as the durable modeled state shared with Custom Views commands,
Native JSON, and the host dialog. `Core.IO` loads workbook `customWorkbookView` name/GUID entries only when matching
worksheet `customSheetView` entries provide view state that Freexcel can represent: view mode, simple frozen/split
panes, gridline/headings/ruler/formula visibility, and zoom. The optional custom-view ID is persisted in the model for
stable XLSX GUID round-trip. Source-package merge treats modeled GUIDs as authoritative while preserving native-only
attributes and retaining unmatched native custom views best-effort; print settings, filter state, hidden row/column
snapshots, selections, personal-view metadata, and window geometry stay outside the modeled subset.

XLSX worksheet `scenarios` fidelity uses `Workbook.Scenarios` as the durable modeled state shared with the Scenario
Manager commands and UI. `Core.IO` loads supported worksheet `scenario` entries only when every `inputCells/@r` is a
same-sheet A1 cell reference and every changing value is a literal `@val`; load records definitions without applying
them. On save, workbook scenarios are grouped by sheet, so a cross-sheet model scenario becomes one worksheet scenario
entry per touched sheet with the shared scenario name. Source-package merge treats supported scenario names as
model-authoritative, preserving native attributes and safe children for still-modeled scenarios while avoiding
resurrection of removed supported entries; malformed or unsupported native-only scenario entries remain best-effort.

XLSX worksheet custom-property fidelity uses `Sheet.CustomProperties` as the durable modeled state. `Core.IO` loads
supported `customProperties/customPr` name/id pairs, writes them back on save, and persists them through Native JSON.
During source-package merge, supported modeled names are authoritative: matching native attributes and child elements
are copied onto still-modeled properties, removed supported entries are not resurrected, and malformed native-only
property entries remain best-effort.

XLSX worksheet calculation-property fidelity uses `Sheet.FullCalculationOnLoad` as the modeled subset of
`sheetCalcPr`. `Core.IO` loads and writes `sheetCalcPr/@fullCalcOnLoad`, persists it through Native JSON, and treats
the modeled flag as authoritative during source-package merge: native-only attributes and child elements are retained,
but a cleared modeled flag is not restored from the source worksheet.

XLSX worksheet allow-edit range fidelity uses `Sheet.AllowEditRanges` as the durable modeled state. `Core.IO` loads
supported single-area `protectedRange/@sqref` entries, skips malformed or multi-area entries as native-only metadata,
and writes modeled `protectedRanges` on save. During source-package merge, modeled supported `sqref`s are authoritative:
matching native attributes and child elements are copied onto still-modeled ranges, removed modeled ranges are not
resurrected, and unsupported native-only `protectedRange` entries are retained best-effort.

XLSX worksheet page-break fidelity uses `Sheet.RowPageBreaks` and `Sheet.ColumnPageBreaks` as the durable modeled
state. `Core.IO` lets ClosedXML load and author supported manual row/column break IDs, then merges native attributes
only onto still-modeled matching `<brk>` entries. Removed modeled breaks are not resurrected from the source package,
while malformed or native-only break entries are retained best-effort.

XLSX worksheet print/layout fidelity uses the `Sheet` print options and page setup fields as the durable modeled state.
During source-package metadata merge, `Core.IO` retains only native-only `printOptions` and `pageSetup` attributes such as
printer defaults or copy counts. Modeled attributes for gridlines, headings, centering, orientation, paper, scale,
first-page number, print quality, comment/error printing, black-and-white, and draft quality are not copied back from the
source worksheet when ClosedXML omits or rewrites them. Printer settings binary parts and `pageSetup` relationships stay
owned by the dedicated printer-settings retention path.

## Current Architectural Limitations

- Sheet rename rewrites existing sheet-qualified formula references through the formula AST/serializer path
- `Core.Model` has a workbook theme scaffold with native and XLSX theme-part persistence, loaded-cell-style theme-color resolution, drawing-object theme color references, chart theme-color references/rendering, and an undoable `SetWorkbookThemeCommand`; `Core.IO` has reusable DrawingML color parsing plus minimal worksheet/drawing relationship-based load/save for embedded package parts for every current native chart type, including `twoCellAnchor` chart bounds/EMU offsets, `oneCellAnchor` bounds, `absoluteAnchor` bounds, no-header and no-category-column series range semantics, chart title/range with title text color/font size, axis titles with text color/font size, value-axis bounds/units/log-scale/number formats, axis gridline visibility/color/thickness, tick marks, axis label visibility, axis line color/thickness, legend visibility/position/text/fill/border/theme-text/font-size, global data-label visibility/position/content/number-format/fill/border/text/font/rotation/callout baseline, per-point data-label fill/border/text/font formatting, trendline type/equation/R-squared/line formatting, common column/area combo line-overlay and column/area/line/scatter secondary-value-axis package state, chart/plot area fill and plot border, bar direction/grouping, scatter/bubble X/Y ranges and value-axis pairs, bubble-size ranges, pie/doughnut first-slice angle and exploded-slice package state, doughnut hole size, line/scatter series color-width-dash-marker and marker-fill package formatting, and filled-series fill/outline color-width-dash package formatting; `App.Host` exposes initial Page Layout Themes, Colors, Fonts, and Effects preset dropdowns plus a custom theme dialog for name, heading/body fonts, effects, and core color slots, and `App.UI` renders Subtle/Refined drawing-object shadow effects while deeper OOXML effect semantics and richer chart formatting remain future work
- CSV adapter does not handle quoted fields or multi-line cells
- Volatile function tracking is not thread-safe (single UI thread assumed)
- Style registry uses linear scan (acceptable for v1 style counts)
