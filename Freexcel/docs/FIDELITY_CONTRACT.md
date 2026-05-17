# Freexcel XLSX Fidelity Contract

**Status:** v1 working contract  
**Last updated:** 2026-05-17

Freexcel saves supported `.xlsx` workbook content from the in-memory model. For workbooks opened from native `.xlsx`, it also keeps a source package snapshot and merges package entries the model writer did not produce, along with content type declarations and relationships to copied targets. This is package-preserving best effort, not byte-for-byte editing of every OOXML node.

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

## Best-Effort Or Partial

- Conditional formatting beyond modeled rules may be skipped.
- Data validation formulas are preserved only for supported rule shapes.
- PivotTable creation, refresh, aggregation, layout editing, slicers, and timelines are deferred to later PivotTable phases; existing PivotTable package parts and basic metadata are retained.
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
