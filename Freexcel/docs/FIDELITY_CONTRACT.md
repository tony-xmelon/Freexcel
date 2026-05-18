# Freexcel XLSX Fidelity Contract

**Status:** v1 working contract  
**Last updated:** 2026-05-18

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
| Basic cell styles (font/fill/border/alignment/number format) | Implemented | |
| Named ranges | Implemented | |
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
| PivotTable + pivot-cache metadata (load/save; native parts retained) | Partial | Creation, refresh, undoable command-level field layout changes, package retention, authored pivot package parts, multiple row/value fields, common summaries, single/multi-select page filters, date/number grouping, label filters, top/bottom/threshold value filters, value/label sorting, subtotals, calculated fields/items, ribbon/double-click Show Details drill-down sheets, and PivotChart sync are implemented; full drag/drop field-list pane, richer filters, and advanced layouts are deferred |
| PivotCharts | Partial | Existing/native and authored PivotCharts bind to modeled PivotTables, refresh their materialized output range, render through the chart surface, and read/write chart `pivotSource`; field buttons, PivotChart filtering UI, and full Excel PivotChart layout editing are deferred |
| Structured tables (load/save; native parts retained) | Partial | Full Excel table semantics deferred |
| Workbook theme (load/save; cell-style color resolution; chart/shape rendering) | Partial | Deep OOXML effects deferred |
| Conditional formatting (icon sets) | Partial | Model scaffold; rendering partial |
| Advanced chart families (surface/treemap/waterfall/etc.) | Partial | Native parts retained; authoring/rendering deferred |
| Advanced chart formatting (rich per-series dialogs) | Partial | Baseline implemented; full format pane deferred |
| Slicer metadata | Partial | Load/save; UI/filtering deferred |
| Timeline metadata | Partial | Load/save; UI/filtering deferred |
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
| Custom XML parts | Excluded | Retained as package part |
| Sensitivity labels / IRM | Excluded | Retained as package part |
| SmartArt diagrams | Excluded | Retained as package part |
| Printer settings | Excluded | Retained as package part |
| Unsupported sheet types (chart/dialog/macro sheets) | Excluded | Retained as package part |

**Coverage: 20 Implemented + 11 Partial = 31/41 in-scope features (76%)**  
**11 Excluded features are retained as opaque package parts (package-preserving save).**

| Status | Count |
|---|---:|
| Implemented | 20 |
| Partial | 11 |
| Excluded (retained) | 11 |
| Excluded (not retained) | 0 |

## Preserved On XLSX Round-Trip

- Workbook sheets and Excel-compatible sheet names (unique, <=31 chars, no `: \ / ? * [ ]`)
- Cell values: blank, number, text, boolean, date/time, and error values
- Formulas and cached formula values where available, including quoted cross-sheet references Freexcel can parse
- Row heights and column widths
- Hidden sheets, hidden rows/columns, freeze panes, worksheet tab colors
- Basic styles: font weight, font color, fill color, borders, alignment, wrap text, and number format IDs we model
- Named ranges that can be mapped to Freexcel ranges
- Cell-value conditional formatting rules we model
- Data validation rules we model
- Merged regions
- Modeled page layout settings: print area, margins, orientation, paper size, print gridlines/headings, and scale-to-fit
- Worksheet background images
- Modeled worksheet objects: comments, hyperlinks, basic charts, sparklines, text boxes, and basic drawing shapes
- PivotTable and pivot-cache metadata plus native PivotTable package references for workbooks opened from `.xlsx`
- PivotChart bindings for supported chart families via chart `pivotSource` metadata
- VeryHidden worksheet state, worksheet code names, and calculation-chain package parts when opened from native `.xlsx`

## Best-Effort Or Partial

- Conditional formatting beyond modeled rules may be skipped.
- Data validation formulas are preserved only for supported rule shapes.
- PivotTable metadata load/save, native package retention, authored pivot package parts, creation, refresh, undoable command-level field layout editing, multiple row fields, multiple data fields, common summary functions, single/multi-select page-field filtering, date/number grouping, label filters, top/bottom/threshold value filters, value/label sorting, subtotals, calculated fields/items, ribbon/double-click Show Details drill-down detail-sheet creation, and PivotChart output-range sync are implemented. Full drag/drop field-list pane, richer advanced filters, slicer/timeline filtering UI, and advanced layout/style controls remain deferred.
- PivotCharts are modeled as bound charts and round-trip native `pivotSource` metadata. Field buttons, PivotChart filter controls, and Excel's full PivotChart layout/editing surface remain deferred.
- Freexcel has a native workbook theme model scaffold, maps `.xlsx` theme parts to/from it, resolves loaded cell-style theme colors/tints against it, renders persisted drawing-object plus chart theme color references, renders Subtle/Refined drawing-object shadow effects, and has undoable Page Layout Themes/Colors/Fonts/Effects preset menus plus a custom theme dialog for name, heading/body fonts, effects, and core color slots. `Core.IO` can parse DrawingML `schemeClr`/`srgbClr` colors and load/save simple embedded package parts for every current native chart type through worksheet/drawing relationships with `twoCellAnchor` bounds/EMU offsets, `oneCellAnchor` bounds, `absoluteAnchor` bounds, no-header and no-category-column series range semantics, chart title/range with title text color/font size, axis titles with text color/font size, value-axis bounds/units/log-scale/number formats, axis gridline visibility/color/thickness, tick marks, axis label visibility, axis line color/thickness, legend visibility/position/text/fill/border/theme-text/font-size, global data-label visibility/position/content/number-format/fill/border/text/font/rotation/callout baseline, per-point data-label fill/border/text/font formatting, trendline type/equation/R-squared/line formatting, common column/area combo line-overlay and column/area/line/scatter secondary-value-axis package state, chart/plot area fill and plot border, bar direction/grouping, scatter/bubble X/Y ranges and value-axis pairs, bubble-size ranges, pie/doughnut first-slice angle and exploded-slice package state, doughnut hole size, line/scatter series color-width-dash-marker and marker-fill package formatting, and filled-series fill/outline color-width-dash package formatting, but richer XLSX chart-package formatting and deeper OOXML effect semantics remain deferred, so chart theme/indexed colors from unsupported `.xlsx` chart parts may still be incomplete until those adapters consume the theme model end to end.
- Formula compatibility depends on the current parser/function library. Unsupported Excel syntax may load as text/formula text but fail Freexcel calculation.

## Retained As Unsupported Package Parts

These feature assets are retained best-effort when the workbook was opened from `.xlsx`, even though Freexcel does not execute or deeply edit them:

- VBA macros and VBA projects
- Slicers and timelines
- Unsupported charts and chart formatting
- Deeper OOXML effect semantics and full XLSX chart-theme extraction beyond the current native/XLSX workbook theme model, loaded-cell-style color-resolution, drawing-object theme-rendering/effect baseline, simple embedded native-chart package loading, chart theme-color rendering, preset menus, and custom theme dialog baseline
- External workbook links and linked data model artifacts
- Embedded/OLE objects
- Custom OOXML package parts not represented in `Core.Model`
- Unsupported workbook, worksheet, view, print, protection, and metadata settings

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

- Add a curated XLSX corpus and report pass/fail per feature class.
- Add XML-level preservation tests for unsupported feature references embedded in workbook/worksheet/drawing parts.
- Extend unsupported-feature detection and user warnings as new unsupported OOXML classes are discovered.
- Keep this contract aligned with executable tests in `tests/Freexcel.Core.IO.Tests`.
