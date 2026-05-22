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
- **Core.Formula**: Lexer → Parser → AST → Evaluator; 345 in-scope Excel built-in functions; dynamic arrays; LET/LAMBDA higher-order functions; cross-sheet reference support (`Sheet1!A1`)
- **Core.Calc**: `DependencyGraph` (topological sort, Kahn's algorithm, cycle detection), `RecalcEngine` (volatile-cell support), `ViewportService`
- **Core.Commands**: `ICommandBus` with undo/redo stack, `EditCellsCommand`, `AddSheetCommand`, `RenameSheetCommand`, `FindReplaceService`
- **Core.IO**: `NativeJsonAdapter` (.fxl), `XlsxFileAdapter` (ClosedXML 0.105.0), `CsvFileAdapter`
- **App.UI**: `GridView` — virtualized DrawingContext rendering, selection, row/column headers
- **App.Host**: `MainWindow` — formula bar, scrollbars, open/save dialogs, keyboard navigation, Find & Replace

Native `.fxl` files are versioned JSON documents. Current files declare `FileFormat = Freexcel.NativeJsonWorkbook`,
`SchemaVersion = 1`, and `MinimumReaderVersion = 1`; unversioned legacy files remain readable and are migrated to the
current header on save, while future schema versions are rejected until an explicit migration is implemented.

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

Custom number formatting remains centralized in `Core.Calc.NumberFormatter`. It parses semicolon-delimited sections
into color, optional invariant numeric condition, and cleaned format text before delegating to the existing numeric,
date/time, fraction, scientific, and text renderers. This keeps display behavior deterministic across machines while
supporting common Excel custom-format constructs such as conditional sections, named colors, default indexed `ColorN`
color prefixes, escaped literals including escaped layout directive characters, comma scaling, fixed and variable-denominator fractions, date/time, elapsed-time,
active percent scaling that preserves token placement and ignores quoted and escaped percent literals, and text-section spacing/fill directives, and visible currency symbols carried by LCID tokens; localized currency names, workbook palette/theme overrides, and exact
accounting layout width fidelity remain explicit parity gaps. Color prefixes and invariant numeric conditions are parsed at the section boundary and can
color numeric, date/time, and text-section display results. Date/time format conversion supports long and compact
AM/PM markers, disambiguates Excel `m`/`mm` tokens as minutes when adjacent to hour or second tokens across quoted
literals and bracket metadata, maps five-`m` month tokens to month initials, and rounds `.0`/`.00`/`.000`
fractional-second display to the requested precision for both clock time and elapsed-time formats. The formatter also maps modeled LCIDs `401`, `402`, `404`, `405`, `406`,
`407`, `408`, `409`, `40A`, `40B`, `40C`, `40D`, `40E`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `418`, `419`, `41A`, `41B`, `41D`, `41E`, `41F`, `420`, `421`, `422`, `424`, `425`, `426`, `427`, `429`, `42A`, `42B`, `42C`, `434`, `435`, `436`, `437`, `439`, `43F`, `440`, `441`, `443`, `43E`, `450`, `453`, `454`, `455`, `45B`, `45E`, `461`, `463`, `468`, `46A`, `470`, `492`, `804`, `807`, `809`, `80A`, `813`, `816`, `100A`, `C01`, `C04`, `C09`, `C0C`, `C0A`, `1009`, `100C`, `1409`, `140A`, `1801`, `1809`, `180A`, `1C09`, `1C0A`, `200A`, `241A`, `240A`, `280A`, `280C`, `2C0A`, `300A`, `340A`, `3801`, `380A`, `380C`, `3C0A`, `400A`, `4009`, `445`, `447`, `449`, `44A`, `44E`, `440A`, and `500A` to deterministic decimal/group/date separators without depending on the user's OS culture. The catalog can also carry non-Western group-size patterns, currently used for Indian grouping under `4009` (`en-IN`) plus native Indian LCIDs such as `439`, `445`, `449`, `44A`, and `44E`. The table-driven catalog deliberately stores resolved separators and group sizes rather than calling OS culture services during rendering, keeping workbook display deterministic across machines. The default indexed custom-format palette maps `Color1` through `Color56`; workbook
palette and theme overrides remain outside the formatter boundary. If an LCID token is not in the curated catalog,
`NumberFormatter` falls back to .NET `CultureInfo` number/date separators for that LCID. Curated entries stay
authoritative because they model Excel-specific or tested Freexcel decisions; the fallback only broadens display for
otherwise-unknown locale tokens and may still differ from Excel where platform globalization data differs.
The Format Cells Number tab uses the same formatter for its sample preview instead of a separate hardcoded preview
table when category controls synthesize a number format. Representative number, date/time, and text values keep the
dialog preview aligned with the grid rendering path while avoiding any new UI-specific formatter behavior.

Conditional Formatting authoring is split between lightweight WPF dialogs in `App.Host` and the `Core.Model`
`ConditionalFormat` model consumed by commands and XLSX IO. The rule manager clones the full modeled rule state
when editing or reordering so advanced rules such as color scales, data bars, icon sets, Top/Bottom, text, and date
rules do not lose fields even though full Excel manager UI and icon rendering taxonomy remain partial.

Advanced chart families are recognized as `ChartType` values and marked non-renderable through `ChartTypeSupport`.
Authoring commands reject them before mutation, `ChartRenderer` returns no plot model for them, and the Insert UI routes
them to a deferred message. XLSX parsing recognizes common advanced chart package shapes where enough range metadata is
available, but lossless mixed drawing-part writing remains deferred until each family has a data model and writer.

PDF and XPS export share the WPF `PrintRenderer` so exported files match print preview layout. PDF export is implemented
through `PDFsharp-WPF` by rasterizing each `FixedDocument` page into a same-sized PDF page; this gives deterministic
local `.pdf` files without depending on Windows virtual-printer UI. XPS export remains a separate ReachFramework-backed
path for Windows print-pipeline workflows. `ExportOptions` models active-sheet, selected-range, entire-workbook, and
one-based page-range scopes; selected-range export is implemented by passing a `GridRange` override into `PrintRenderer`,
workbook export combines visible worksheet documents rendered through the same sheet-level path, PDF page ranges subset
the fixed-document pages directly, XPS page ranges wrap the renderer's `DocumentPaginator`, and the Excel-style
standard/minimum-size quality option is modeled explicitly. The Excel-style "Ignore print areas" option is modeled on
`ExportOptions` and flows into `PrintRenderer`; selected-range export still wins by passing an explicit range override,
while active-sheet and workbook export can bypass each sheet's stored `PrintArea` and render the used range. PDF export
honors the quality choice by changing raster page DPI while preserving the physical page size; XPS keeps the
print-pipeline paginator path. `ExportPlanner`
validates requested page ranges against the rendered page count before file creation, so out-of-range requests surface
as export-option errors instead of half-written files. Extensionless export paths are normalized to `.pdf` when PDF is
inferred and to `.xps` when the save dialog explicitly selects XPS, avoiding generated export content saved without a
discoverable file extension. PDF sheet-name bookmarks are modeled on `ExportOptions` and written through
`PdfDocument.Outlines`; bookmark targets are filtered and re-indexed after page-range selection so exported outlines
only point at pages that exist in the final PDF. Full Excel document-property fidelity, heading/bookmark variants, full
Excel PDF publish options, and selectable/vector PDF text remain parity gaps.
When `IncludeDocumentProperties` is selected for PDF output, `App.Host` maps the current `Workbook` into
`PdfDocumentProperties` and writes the supported PDF Info dictionary fields. The current modeled subset is intentionally
small: workbook name becomes the PDF title and deterministic Freexcel values fill author, subject, keywords, and creator.
PDF creator metadata still identifies Freexcel on all generated PDFs; the option controls the additional
workbook-derived fields. XPS export writes the same modeled title/creator/subject/keywords subset into the package core
properties when the option is selected. This keeps document-property export useful without introducing a full Office
document-property subsystem.

PivotTable authoring remains model-first and worksheet-range only. `Core.Commands` owns undoable creation and refresh:
current-sheet insertion uses `AddPivotTableCommand`, while new-worksheet insertion uses `AddPivotTableToNewWorksheetCommand`
to create a unique PivotTable sheet, anchor the report at `A3`, and delegate cache/table materialization to the same
refresh path. `PivotTableRefreshService` also owns materialized value-cell formatting: supported built-in value-field
`numFmtId` values are resolved to `CellStyle.NumberFormat` codes before PivotStyle visual styling is merged in, so
number formats survive body, subtotal, grand-total, and stripe styling. Custom PivotTable value-field number formats use
`Workbook.NumberFormatCatalog` for XLSX `numFmtId >= 164` entries; loaded data fields keep both the ID and resolved
format code, and authored catalogs are written back to `styles.xml`. When a generated stylesheet already uses a requested
custom ID for another format, the PivotTable catalog entry is remapped to the next free custom ID and authored or
source-preserved PivotTable XML is rewritten to match. The Value Field Settings dialog exposes a broad set of common
Excel-style built-in format presets covering number, currency/accounting, date/time, percentage, fraction, scientific,
and text formats while keeping the raw `numFmtId` override for loaded or advanced cases and editing custom format codes,
assigning authored custom codes to the workbook catalog path. Duplicate preset aliases keep loaded or typed labels
compatible, but the first preset for a built-in ID is the canonical display label used when reopening the dialog.
`PivotTableModel.EmptyValueText` models Excel's "For empty cells show" option for generated matrix reports:
`PivotTableRefreshService` writes the configured text only for row/column intersections with no source rows, while
real zero aggregates, row totals, column totals, and grand totals remain numeric so formatting and calculations stay
predictable. Sheet cloning carries the option with the rest of the PivotTable model state. `PivotTableOptionsDialog`
and `ConfigurePivotTableOptionsCommand` are the command surface for editing this value; both normalize whitespace-only
input back to `null`, and the command snapshots the option with the rest of the PivotTable settings so undo restores
the previous rendered matrix.
Pivot cache data options remain owned by `PivotCacheModel`, not duplicated onto `PivotTableModel`. `PivotTableOptionsDialog`
reads the cache connected by `PivotTableModel.CacheId`, and `ConfigurePivotTableOptionsCommand` updates the cache's
`RefreshOnLoad` and `SaveData` flags with undoable snapshots. This keeps XLSX cache metadata, dialog state, and command
mutation aligned while leaving external/OLAP cache execution out of scope.
The PivotTable Options style picker exposes the built-in `PivotStyleLight1..28`, `PivotStyleMedium1..28`, and
`PivotStyleDark1..28` name ranges and appends the workbook's current authored style name when it is outside that
built-in list. This avoids destructive style-name fallback when a loaded workbook uses a custom style while keeping the
visual renderer intentionally lightweight: `PivotStylePaletteResolver` maps selected built-in names to modeled header,
subtotal, grand-total, stripe, and border colors, with exact Excel theme/style XML semantics still out of scope.
External/OLAP/data-model caches stay excluded from
execution; their package metadata is retained where covered by XLSX fidelity paths.
PivotCharts remain normal `ChartModel` instances bound back to `PivotTableModel` by name/cache metadata. The chart model
keeps a master `ShowPivotChartFieldButtons` switch plus per-button report-filter, axis-field, and value-field visibility
flags. `ChartRenderer` and `GridView` both honor the same flags, so rendered annotations and click targets stay aligned
when a user hides only one class of PivotChart field button. The PivotChart Options command is the owning mutation path
for these flags: `ConfigurePivotChartOptionsCommand` snapshots the master and per-button visibility booleans with the
chart style ID so undo restores the complete field-button state, while the host dialog exposes the same booleans rather
than keeping hidden UI-only state. Native JSON persists the PivotChart binding fields, chart style ID, field-button
visibility flags, and modeled chart design metadata such as pivot format XML, date-system/language, manual layouts,
external-data pointers, protection, print settings, rounded corners, blank display, and hidden-row display flags so
Freexcel-authored workbooks do not lose chart option state outside XLSX.

Structured table authoring stays command-owned. `CreateStructuredTableCommand` creates the model metadata and
`CreateStyledStructuredTableCommand` layers visible banding as one undoable operation. Loaded table totals metadata is
materialized by `RefreshStructuredTableTotalsCommand`, which writes totals-row labels, explicit totals formulas as text,
and common Excel totals functions (`sum`, `average`, `count`, `countNums`, `min`, and `max`) from the table data rows.
The command snapshots affected totals-row cells for undo. Basic structured-reference formulas are resolved from
`StructuredTableModel` metadata at formula evaluation and dependency-registration time through
`StructuredReferenceResolver`; formulas keep their `TableName[ColumnName]` shape instead of being rewritten to A1 ranges.
The evaluator carries the formula cell address in its context so current-row references can resolve relative to the
hosting table data row. The supported slice covers same-workbook data-body column references such as `Sales[Amount]`,
whole-table section selectors `#Headers`, `#Data`, `#All`, and `#Totals`, common section-column intersections such as
`Sales[[#Totals],[Amount]]`, and scalar current-row references such as `[@Amount]` or `Sales[@Amount]` when the formula
cell is inside the table data body. Data-body and section-scoped multi-column ranges such as `Sales[[Amount]:[Tax]]`
and `Sales[[#Data],[Amount]:[Tax]]` resolve to rectangular table ranges. Excel's `#This Row` selector resolves through
the same current-cell context as `[@Column]`, including row-scoped column ranges such as
`Sales[[#This Row],[Amount]:[Tax]]`. Unqualified `#This Row` selectors bind to the containing table for calculated
column-style formulas, for example `[[#This Row],[Amount]:[Tax]]`. Current-row references outside a table data row,
external workbook structured references, and full table style theme semantics remain outside this slice.

Flash Fill remains a deterministic pattern service, not an Excel-like ML inference engine. It supports conservative
single-column transforms including dotted/underscored/hyphenated email display-name cleanup, plus a small multi-column
pattern set. First/last-name, first-initial/last-name, and last-name/first-initial email generation learn constant
domains and modeled `.`, `_`, or `-` separators from examples. It returns no result when the examples are ambiguous.

Spell Check remains a deterministic known-corrections service in `Core.Commands`, not dictionary-backed proofing. It
scans literal text cells in sheet/row/column order and plans undoable replacement edits while leaving formula cells alone.

Accessibility Checker remains a deterministic model-backed audit in `Core.Commands`, not a full WCAG or screen-reader
engine. It reports issues supported by current workbook state, including merged cells, missing object alternate text,
hidden sheets/rows/columns with content, unclear hyperlink display text, and charts whose title is missing as the
current accessible label.

Selection Pane object editing uses lightweight `Name` fields on charts, pictures, text boxes, and drawing shapes.
Generated names remain the fallback when no explicit name is modeled. Visibility, z-order, and rename edits stay in
`Core.Commands`; `RenameSelectionPaneObjectCommand` snapshots the previous name for undo, while the host dialog only
plans rename/visibility/move changes and applies them through the command bus as one `CompositeWorkbookCommand`, so a
single dialog acceptance is one undo step. Native JSON persists modeled object names. XLSX drawing object name
load/save maps the drawing non-visual `cNvPr/@name` value for charts, pictures, text boxes, and drawing shapes to
the modeled object name, while deeper Office drawing IDs and other non-visual metadata remain best-effort package
details rather than first-class model state.

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

XLSX worksheet phonetic-property fidelity uses `Sheet.PhoneticProperties` as raw worksheet-level metadata for
`phoneticPr` fontId/type/alignment attributes. Freexcel does not render or edit phonetic text, but `Core.IO` loads,
writes, and persists those stable attributes through Native JSON. Source-package merge treats the modeled attributes as
authoritative while preserving native-only phonetic attributes and child elements best-effort.

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
