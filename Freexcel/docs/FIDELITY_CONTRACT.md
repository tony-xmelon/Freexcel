# Freexcel XLSX Fidelity Contract

**Status:** v1 working contract  
**Last updated:** 2026-05-19

Freexcel saves supported `.xlsx` workbook content from the in-memory model. For workbooks opened from native `.xlsx`, it also keeps a source package snapshot and merges package entries the model writer did not produce, along with content type declarations and relationships to copied targets. This is package-preserving best effort, not byte-for-byte editing of every OOXML node.

## XLSX Feature Coverage Summary

| Feature Category | Status | Notes |
|---|---|---|
| Cell values (blank/number/text/bool/date/error) | Implemented | |
| Formulas and cached values | Implemented | |
| Row heights / column widths | Implemented | |
| Hidden rows/columns/sheets | Implemented | |
| Freeze panes | Implemented | |
| Worksheet tab colors | Implemented | |
| Custom sheet views | Partial | Native worksheet `customSheetViews` blocks are retained after ordinary model edits; custom-view editing UI is deferred |
| Worksheet scenarios | Partial | Native What-If Analysis `scenarios` blocks are retained after ordinary model edits; Scenario Manager UI and calculation behavior are deferred |
| Worksheet extension lists | Partial | Unknown worksheet `extLst` entries are merged back after ordinary model edits, including alongside rewritten modeled sparkline extensions |
| Workbook extension lists | Partial | Unknown workbook `extLst` entries are merged back after ordinary model edits; payloads are retained but not interpreted |
| Workbook file version | Partial | Native `fileVersion` metadata is retained after ordinary model edits |
| Workbook file sharing | Partial | Native `fileSharing` reservation/read-only metadata is retained after ordinary model edits |
| Workbook file recovery | Partial | Native `fileRecoveryPr` autorecovery metadata is retained after ordinary model edits |
| Document properties | Partial | Stable native `docProps/core.xml` and `docProps/app.xml` fields are retained after ordinary model edits; volatile timestamps and revision counters remain writer-owned |
| Workbook smart tags | Partial | Native workbook `smartTagPr` and `smartTagTypes` metadata is retained after ordinary model edits; smart-tag editing UI is deferred |
| Workbook function groups | Partial | Native `functionGroups` metadata is retained after ordinary model edits; custom function group editing UI is deferred |
| Workbook views | Partial | Additional native `workbookView` entries and native-only metadata on the primary workbook view are retained after ordinary model edits; workbook-window view editing is deferred |
| Custom workbook views | Partial | Native `customWorkbookViews` blocks are retained after ordinary model edits; custom-view editing is deferred |
| Workbook properties | Partial | Unsupported native `workbookPr` attributes and child elements are retained without overwriting modeled workbook properties |
| Worksheet sheet properties | Partial | Unsupported native `sheetPr` attributes and child elements are retained without overwriting modeled sheet properties |
| Worksheet sheet format properties | Partial | Native-only `sheetFormatPr` attributes such as `zeroHeight`, `thickTop`, and outline-level metadata are retained without overwriting modeled row/column sizing |
| Worksheet column metadata | Partial | Native-only column attributes are retained by column span after ordinary model edits when the column span remains in the saved worksheet |
| Worksheet row metadata | Partial | Native-only row attributes are retained by row number after ordinary model edits when the row remains in the saved sheet data |
| Worksheet cell metadata | Partial | Native-only cell attributes are retained by cell reference after ordinary model edits when the cell remains in the saved sheet data |
| Worksheet ignored errors | Partial | Supported active `ignoredError` cell refs/ranges load into `Cell.IgnoreFormulaError` and save back as modeled worksheet `ignoredErrors`; detailed native flags/unsupported refs remain retained or merged best-effort after ordinary model edits |
| Worksheet cell watches | Partial | Supported worksheet `cellWatches/cellWatch[@r]` single-cell A1 refs load into `Workbook.WatchedCells` and save back as modeled worksheet `cellWatches`; malformed refs are skipped, watched cells do not create blank cells, and native-only watch attributes/unsupported entries are retained or merged best-effort after ordinary model edits |
| Worksheet calculation properties | Partial | Native `sheetCalcPr` blocks are retained after ordinary model edits; per-sheet calculation UI is deferred |
| Worksheet phonetic properties | Partial | Native `phoneticPr` blocks are retained after ordinary model edits; phonetic display editing is deferred |
| Worksheet sort state | Partial | Native `sortState` blocks are retained after ordinary model edits; sort execution/editing UI is deferred |
| Worksheet data consolidation | Partial | Native `dataConsolidate` blocks are retained after ordinary model edits; Data Consolidate execution/editing UI is deferred |
| Advanced worksheet protection metadata | Partial | Unsupported native `sheetProtection` attributes and child elements are retained without overwriting modeled protection state |
| Advanced workbook protection metadata | Partial | Unsupported native `workbookProtection` attributes and child elements are retained without overwriting modeled workbook protection state |
| Protected range metadata | Partial | Supported single-area worksheet `protectedRange/@sqref` entries load into `Sheet.AllowEditRanges` and are model-authoritative on save; native attributes and child elements are retained by matching modeled `sqref`, while malformed, missing, or multi-area native-only entries are retained best-effort; advanced allow-edit-range UI is deferred |
| Custom XML parts | Partial | Native `customXml/*` package parts are retained after ordinary model edits; custom XML mapping/editing UI is deferred |
| Header/footer legacy drawings | Partial | Native worksheet `legacyDrawingHF` references and linked VML/media package parts are retained after ordinary model edits; header/footer image editing UI is deferred |
| Worksheet custom properties | Partial | Native worksheet `customProperties` blocks are retained after ordinary model edits; worksheet custom-property editing UI is deferred |
| Worksheet smart tags | Partial | Native worksheet `smartTags` blocks are retained after ordinary model edits; smart-tag editing UI is deferred |
| Sheet-level AutoFilter metadata | Partial | Native worksheet `autoFilter` blocks are retained after ordinary model edits; filter execution/editing UI is deferred |
| Additional worksheet views | Partial | Additional native worksheet `sheetView` entries and native-only metadata on the primary worksheet view are retained after ordinary model edits; multi-view editing UI is deferred |
| Worksheet page-break metadata | Partial | Supported row/column break IDs are model-authoritative: native attributes are retained only for modeled matching break `id`s, removed modeled breaks are not resurrected, and malformed/native-only break entries are retained best-effort; advanced page-break editing UI is deferred |
| Worksheet print options metadata | Partial | Native-only `printOptions` attributes are retained after ordinary model edits; modeled print gridline/headings/centering attributes are never restored from the source package over `Sheet` state |
| Worksheet page setup metadata | Partial | Native-only `pageSetup` attributes are retained after ordinary model edits; modeled orientation, scaling, paper, first-page-number, print-quality, comments/errors, black-and-white, and draft attributes are never restored from the source package over `Sheet` state, while printer-setting relationships remain handled by the dedicated relationship-retention path |
| Basic cell styles (font/fill/border/alignment/number format) | Implemented | |
| Stylesheet native metadata | Partial | Native stylesheet `colors`, custom `tableStyles`, and unknown stylesheet `extLst` entries are retained after ordinary model edits; deep style-table editing semantics remain modeled through Freexcel styles |
| Named ranges | Implemented | Simple range names are modeled; unsupported/native `definedName` elements are retained after ordinary model edits |
| Merged regions | Implemented | |
| Conditional formatting (cell-value/formula/top-bottom/color-scale/data-bar) | Implemented | |
| Data validation rules | Implemented | |
| Comments/notes | Implemented | |
| Hyperlinks | Implemented | |
| Page layout settings (margins/orientation/paper/print-area/headers/footers) | Implemented | |
| Workbook structure protection + sheet protection + allow-edit ranges | Implemented | |
| Charts (column/bar/line/area/scatter/bubble/pie/doughnut/radar/stock) | Implemented | |
| Sparklines | Implemented | |
| Text boxes + basic drawing shapes | Implemented | |
| Pictures/images | Implemented | |
| PivotTable + pivot-cache metadata (load/save; native parts retained) | Partial | Creation from same-sheet and cross-sheet source ranges, refresh, undoable command-level field layout/source/view/options changes, package retention, authored pivot package parts, values-only and column-only layouts, multiple row/column/value fields, Compact/Outline/Tabular report-layout state with Compact row-label rendering, nested column-field matrices, common and statistical summaries, single/multi-select page/row/column checked-item filters, date/number grouping, row/column label filters including comparison/between variants, row/column value filters with field targets including between/not-between and above/below-average variants, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants with base field/item settings, value/label sorting including column label/value sorting, separate row/column grand-total visibility, repeated-label suppression, blank-line spacing, PivotTable style names and style flags with rendered header/subtotal/grand-total/banded formatting, top/bottom subtotals, calculated fields/items, GETPIVOTDATA, ribbon/double-click Show Details drill-down sheets for item/subtotal/grand-total/matrix/column-only data cells, PivotChart sync, Field List drag/drop, Insert Slicer/Insert Timeline authoring, slicer/timeline pane controls, cache relationships, refresh flags, shared-item edge metadata, native pivot cache records relationship retention, and retained slicer/timeline floating drawing anchors are implemented; exact full-gallery PivotStyle theme semantics and external/OLAP/data-model pivot cache behavior remain partial or excluded |
| PivotCharts | Partial | Existing/native and authored PivotCharts bind to modeled PivotTables, refresh their materialized output range, render through the chart surface, read/write chart `pivotSource`, support undoable bound chart-type changes, and expose field-button menus through the PivotTable filter/sort UI; full Excel PivotChart Tools layout/design editing remains partial |
| Structured tables (load/save; native parts retained) | Partial | Metadata, style flags, totals-row labels/functions, simple value AutoFilter metadata, authored table parts, and native references are retained; full Excel table formula/filter execution semantics deferred |
| Workbook theme (load/save; cell-style color resolution; chart/shape rendering) | Partial | Deep OOXML effects deferred |
| Conditional formatting (icon sets) | Partial | Model scaffold; rendering partial |
| Advanced chart families (surface/treemap/waterfall/etc.) | Partial | Combo/radar/stock are modeled; surface, histogram/Pareto, waterfall, treemap, sunburst, box-whisker, funnel, map, and 3D column are recognized as deferred chart models when their package parts are parseable; unparseable chart parts still use the unsupported-feature warning path; authoring/rendering and lossless mixed drawing-part writing remain deferred |
| Advanced chart formatting (rich per-series dialogs) | Partial | Baseline implemented; full format pane deferred |
| Slicer metadata | Partial | Load/save, authored selection state, cache relationships, pane tiles, and connected PivotTable filtering implemented; native Excel floating drawing object fidelity remains partial |
| Timeline metadata | Partial | Load/save, authored range state, cache relationships, pane controls, and connected PivotTable filtering implemented; native Excel floating drawing object fidelity remains partial |
| External workbook link metadata | Partial | Load/save; formula resolution deferred |
| VBA macros | Excluded | Retained as package part; not executed |
| Power Query | Excluded | Retained as package part; not executed |
| Data Model / Power Pivot | Excluded | Retained as package part; not executed |
| Linked data types | Excluded | Retained as package part |
| Threaded comments | Excluded | Retained as package part |
| Track changes / revision history | Excluded | Retained as package part |
| Form controls / ActiveX | Excluded | Retained as package part |
| Digital signatures | Excluded | Retained as package part |
| Custom ribbon UI | Excluded | Retained as package part |
| Office add-ins / web extensions | Excluded | Retained as package part |
| Embedded / OLE objects | Excluded | Retained as package part |
| Live web queries / web publishing | Excluded | Retained as package part; not executed |
| Sensitivity labels / IRM | Excluded | Retained as package part |
| SmartArt diagrams | Excluded | Retained as package part |
| Printer settings | Partial | Native `xl/printerSettings/*.bin` parts and worksheet `pageSetup` relationships are retained; binary DEVMODE payload is not interpreted |
| Unsupported sheet types (chart/dialog/macro sheets) | Excluded | Retained as package part |

**Coverage: 19 Implemented + 48 Partial = 67 documented in-scope feature categories with at least partial support.**
**15 Excluded feature categories are retained as opaque package parts where safe (package-preserving save).**

| Status | Count |
|---|---:|
| Implemented | 19 |
| Partial | 48 |
| Excluded (retained) | 15 |
| Excluded (not retained) | 0 |

## Preserved On XLSX Round-Trip

- Workbook sheets and Excel-compatible sheet names (unique, <=31 chars, no `: \ / ? * [ ]`)
- Cell values: blank, number, text, boolean, date/time, and error values
- Formulas and cached formula values where available, including quoted cross-sheet references Freexcel can parse
- Row heights and column widths
- Hidden sheets, hidden rows/columns, freeze panes, worksheet tab colors, native custom sheet views, and native worksheet scenarios
- Basic styles: font weight, font color, fill color, borders, alignment, wrap text, and number format IDs we model
- Native stylesheet `colors`, custom `tableStyles`, and unknown stylesheet `extLst` entries from source `.xlsx` packages
- Named ranges that can be mapped to Freexcel ranges
- Unsupported/native workbook `definedName` entries that are not mapped to Freexcel range names
- Stable native core and extended document properties, excluding volatile timestamps/revision counters
- Cell-value conditional formatting rules we model
- Data validation rules we model
- Merged regions
- Modeled page layout settings: print area, margins, orientation, paper size, print gridlines/headings, and scale-to-fit
- Worksheet background images
- Modeled worksheet objects: comments, hyperlinks, basic charts, sparklines, text boxes, and basic drawing shapes
- PivotTable and pivot-cache metadata plus native PivotTable package references for workbooks opened from `.xlsx`
- PivotChart bindings for supported chart families via chart `pivotSource` metadata
- VeryHidden worksheet state, worksheet code names, and calculation-chain package parts when opened from native `.xlsx`
- Workbook calculation properties such as full-calc-on-load, force-full-calc, iterative calculation settings, and native-only calculation metadata
- Native printer settings package parts and worksheet `pageSetup` relationship pointers
- Native worksheet `customSheetViews` blocks
- Native worksheet `scenarios` blocks
- Unknown worksheet `extLst` extension entries alongside modeled sparkline extensions
- Unknown workbook `extLst` extension entries
- Native workbook file-version metadata
- Native workbook file-sharing metadata
- Native workbook file-recovery metadata
- Native workbook smart-tag metadata
- Native workbook function-group metadata
- Additional native workbook view entries
- Native custom workbook views
- Unsupported native workbook `workbookPr` attributes and child elements
- Unsupported native worksheet `sheetPr` attributes and child elements
- Native worksheet ignored-error metadata
- Native worksheet cell-watch metadata
- Native worksheet calculation metadata
- Native worksheet phonetic-property metadata
- Native worksheet sort-state metadata
- Native worksheet data-consolidation metadata
- Advanced native worksheet protection metadata
- Advanced native workbook protection metadata
- Native protected-range metadata
- Native custom XML package parts
- Native header/footer legacy drawing references and linked VML/media parts
- Native worksheet custom-property metadata
- Native worksheet smart-tag metadata
- Native sheet-level AutoFilter metadata
- Additional native worksheet view entries

## Best-Effort Or Partial

- Conditional formatting beyond modeled rules may be skipped.
- Native custom sheet views are retained, but Freexcel does not yet expose creation or editing for custom views.
- Native What-If Analysis scenarios are retained, but Freexcel does not yet expose Scenario Manager creation/editing or scenario-driven recalculation.
- Unknown worksheet extension-list entries are retained by extension URI; Freexcel does not interpret those extension payloads.
- Unknown workbook extension-list entries are retained by extension URI; Freexcel does not interpret those extension payloads.
- Native workbook file-version metadata is retained but not interpreted.
- Native workbook file-sharing metadata is retained but not interpreted.
- Native workbook file-recovery metadata is retained but not interpreted.
- Native workbook smart-tag metadata is retained, but Freexcel does not expose smart-tag editing.
- Native workbook function-group metadata is retained, but Freexcel does not expose custom function group editing.
- Additional workbook views are retained, but Freexcel does not yet expose workbook-window view editing.
- Native custom workbook views are retained, but Freexcel does not expose custom-view editing.
- Unsupported workbook `workbookPr` details are retained, but Freexcel does not expose every native workbook-property switch.
- Unsupported worksheet `sheetPr` details are retained, but Freexcel does not expose every native sheet-property switch.
- Supported ignored-error refs are model-backed through `Cell.IgnoreFormulaError`; detailed native flags and unsupported refs remain best-effort retained.
- Supported cell-watch refs are model-backed through `Workbook.WatchedCells` and the Watch Window UI; native-only watch attributes and unsupported entries remain best-effort retained.
- Native worksheet calculation metadata is retained, but Freexcel does not expose per-sheet calculation settings.
- Native worksheet phonetic-property metadata is retained, but Freexcel does not expose phonetic display editing.
- Native worksheet sort-state metadata is retained, but Freexcel does not expose the full sort-state editing surface.
- Native worksheet data-consolidation metadata is retained, but Freexcel does not expose Data Consolidate execution or editing.
- Unsupported native `sheetProtection` details are retained, but Freexcel does not expose every native protection option or strong-hash setting.
- Unsupported native `workbookProtection` details are retained, but Freexcel does not expose every native workbook protection option or strong-hash setting.
- Supported protected ranges are model-backed through `Sheet.AllowEditRanges`; native-only advanced allow-edit-range security options remain partial.
- Native custom XML package parts are retained, but Freexcel does not expose XML mapping or custom XML editing.
- Native header/footer legacy drawing references and linked VML/media parts are retained, but Freexcel does not expose header/footer image editing.
- Native worksheet custom-property metadata is retained, but Freexcel does not expose worksheet custom-property editing.
- Native worksheet smart-tag metadata is retained, but Freexcel does not expose smart-tag editing.
- Native sheet-level AutoFilter metadata is retained, but Freexcel does not expose the full worksheet filter execution/editing surface.
- Additional worksheet views are retained, but Freexcel does not expose multi-view editing.
- Worksheet `printOptions` and `pageSetup` source-package merges are model-authoritative for fields represented on `Sheet`; native-only attributes are copied only when they do not conflict with modeled state.
- Data validation formulas are preserved only for supported rule shapes.
- PivotTable metadata load/save, native package retention, authored pivot package parts, same-sheet/cross-sheet creation, refresh, undoable command-level field layout/source editing, values-only and column-only layouts, multiple row fields, multiple column fields with nested matrix headers, Compact/Outline/Tabular report-layout state with Compact row-label rendering, multiple data fields, common/statistical summary functions, single/multi-select page/row/column checked-item filtering, date/number grouping, row/column label filters including comparison/between variants, row/column value filters with field-target round-trip including between/not-between and above/below-average variants, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants with base field/item settings, value/label sorting including column label/value sorting, separate row/column grand-total visibility, repeated-label suppression, blank-line spacing, style-name/style-option round-trip with rendered header/subtotal/grand-total/banded formatting, top/bottom subtotals, calculated fields/items, ribbon/double-click Show Details drill-down detail-sheet creation for item/subtotal/grand-total/matrix/column-only data cells, PivotChart output-range sync, Field List drag/drop, PivotChart field-button menus, slicer/timeline filtering UI, authored slicer/timeline state/cache relationships, and pivot-cache refresh/shared-item edge metadata are implemented. Exact full-gallery PivotStyle theme semantics remain partial.
- PivotCharts are modeled as bound charts and round-trip native `pivotSource` metadata. Field buttons are rendered and route to PivotTable sort/filter/value-settings menus, and bound chart type changes preserve the PivotTable connection; Excel's full PivotChart layout/editing surface remains partial.
- Freexcel has a native workbook theme model scaffold, maps `.xlsx` theme parts to/from it, resolves loaded cell-style theme colors/tints against it, renders persisted drawing-object plus chart theme color references, renders Subtle/Refined drawing-object shadow effects, and has undoable Page Layout Themes/Colors/Fonts/Effects preset menus plus a custom theme dialog for name, heading/body fonts, effects, and core color slots. `Core.IO` can parse DrawingML `schemeClr`/`srgbClr` colors and load/save simple embedded package parts for every current native chart type through worksheet/drawing relationships with `twoCellAnchor` bounds/EMU offsets, `oneCellAnchor` bounds, `absoluteAnchor` bounds, no-header and no-category-column series range semantics, chart title/range with title text color/font size, axis titles with text color/font size, value-axis bounds/units/log-scale/number formats, axis gridline visibility/color/thickness, tick marks, axis label visibility, axis line color/thickness, legend visibility/position/text/fill/border/theme-text/font-size, global data-label visibility/position/content/number-format/fill/border/text/font/rotation/callout baseline, per-point data-label fill/border/text/font formatting, trendline type/equation/R-squared/line formatting, common column/area combo line-overlay and column/area/line/scatter secondary-value-axis package state, chart/plot area fill and plot border, bar direction/grouping, scatter/bubble X/Y ranges and value-axis pairs, bubble-size ranges, pie/doughnut first-slice angle and exploded-slice package state, doughnut hole size, line/scatter series color-width-dash-marker and marker-fill package formatting, and filled-series fill/outline color-width-dash package formatting, but richer XLSX chart-package formatting and deeper OOXML effect semantics remain deferred, so chart theme/indexed colors from unsupported `.xlsx` chart parts may still be incomplete until those adapters consume the theme model end to end.
- Formula compatibility depends on the current parser/function library. Unsupported Excel syntax may load as text/formula text but fail Freexcel calculation.

## Retained As Unsupported Package Parts

These feature assets are retained best-effort when the workbook was opened from `.xlsx`, even though Freexcel does not execute or deeply edit them:

- VBA macros and VBA projects
- Unmodeled slicer/timeline OOXML package details beyond Freexcel's modeled metadata, authored selection state, connected filtering, and retained floating drawing anchors
- Unsupported charts and chart formatting
- Deeper OOXML effect semantics and full XLSX chart-theme extraction beyond the current native/XLSX workbook theme model, loaded-cell-style color-resolution, drawing-object theme-rendering/effect baseline, simple embedded native-chart package loading, chart theme-color rendering, preset menus, and custom theme dialog baseline
- External workbook links and linked data model artifacts
- Embedded/OLE objects
- Custom OOXML package parts not represented in `Core.Model`
- Unsupported workbook, worksheet, view, protection, and metadata settings

Microsoft 365 Share/co-authoring state, cloud permissions, presence, version history, and other cloud/service state are outside local XLSX package fidelity.

## Explicit Product Exclusions

The following Excel features are not Freexcel parity targets unless a future design document explicitly brings them into scope:

- Microsoft 365 Share/co-authoring, OneDrive/SharePoint permissions, Teams-linked sharing, and live collaborator presence.
- VBA compatibility, macro execution, COM add-ins, and Office Scripts.
- Power Query, Power Pivot, OLAP/data model features, and Microsoft linked data types.
- Enterprise Microsoft 365 controls such as sensitivity labels and IRM.

See [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md) for the command-level parity matrix.
See [XLSX_TEST_CORPUS_PLAN.md](XLSX_TEST_CORPUS_PLAN.md) for the Sprint 2 corpus collection and reporting plan.
See [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md) for the current executable corpus status.

## Required Before Claiming Higher Fidelity

- Add more committed issue-specific regression workbooks and local-private user torture samples.
- Complete manual desktop Excel open/save/reopen review for representative native samples.
- Extend unsupported-feature detection and user warnings as new unsupported OOXML classes are discovered.
- Keep this contract aligned with executable tests in `tests/Freexcel.Core.IO.Tests`.
