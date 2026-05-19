# Freexcel XLSX Corpus Report

**Last updated:** 2026-05-19  
**Status:** Executable parity harness with model-first XLSX retention, relationship-target retention checks, expanded PivotTable/PivotChart fidelity slices, and private/regression corpus scaffolding

## Current Corpus

| Source type | Count | Status |
|---|---:|---|
| Generated deterministic supported-pass fixtures | 16 | Passing through in-memory XLSX save/load with stronger per-feature summary comparison |
| Generated deterministic supported-metadata-pass fixtures | 4 | Slicers, timelines, external workbook links, and printer settings retain native package references after ordinary edits |
| Generated deterministic known-gap fixtures | 17 | Declared with expected warnings and notes; warning detector covers unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, embedded objects, and custom XML |
| Public redistributed workbooks | 25 | Open-license Tealeg XLSX public corpus; files open, save, and reload through the runner |
| Local private workbooks | 20 | Optional user-approved torture rows are in the manifest; missing files are skipped |
| Regression workbooks | 0 | `test-corpus/regressions/` bucket is present; pending first issue-specific binary fixture |

Total manifest rows: 82.

## Current Result

| Check | Result |
|---|---|
| Manifest schema and policy tests | Pass |
| Generated fixture factory coverage | 16/16 supported-pass manifest rows |
| Generated XLSX save/load round-trip with supported-feature summary comparison | 16/16 pass |
| Generated known-gap warning/notes coverage | 17/17 pass |
| Generated known-gap package warning execution | 17/17 pass |
| Generated known-gap package retention after model edit | 17/17 pass for critical package parts and retained relationship targets |
| Unsupported feature detector known-gap coverage | Unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, embedded objects, and custom XML detected |
| Missing local-private files | Skipped without failure |
| Workbook structure protection XLSX round-trip | Pass; `workbookPassword` is written as legacy hash text, not raw password text |
| Structured table XLSX retention | Pass; table metadata loads, authored table parts save, totals-row column metadata and simple value AutoFilter metadata round-trip, and native table references are preserved after edits |
| PivotTable XLSX parity slice | Pass; PivotTable/cache metadata loads, native package references are preserved, authored pivot package parts save, same-sheet and cross-sheet creation/refresh/source changes work, undoable command-level field layout changes work, values-only and column-only layouts materialize, multiple row/column/value fields materialize, Compact/Outline/Tabular report-layout state round-trips with Compact row-label rendering, nested column-field matrices render, common/statistical summaries evaluate, single/multi-select page/row/column checked-item filters apply and round-trip, date/number grouping, row/column top/bottom/threshold value filters with field targets, row/column label filters, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants calculate and round-trip with base field/item metadata, value/label sorting including column label/value sorting, separate row/column grand-total visibility round-trips, repeated-label suppression, blank-line spacing, PivotTable style names and style-option flags round-trip, top/bottom subtotals, calculated fields, and calculated items round-trip, native pivot cache records relationships are retained, pivot cache shared-item edge metadata round-trips, GETPIVOTDATA evaluates same-sheet and cross-sheet PivotTable references, rendered PivotTable header/subtotal/grand-total/banded styles are applied for built-in presets, Show Details creates source-row detail sheets from the ribbon or pivot-value double-click for item/subtotal/grand-total/matrix/column-only data cells, and the Insert/contextual ribbons expose creation/refresh/detail/slicer/timeline commands |
| PivotChart XLSX parity slice | Pass; bound PivotCharts can be authored from PivotTables, refresh with the PivotTable materialized output range, support undoable type changes that preserve the binding, and read/write chart `pivotSource` metadata |
| Advanced conditional formatting metadata | Pass; color scales, data bars, icon sets, and long-tail rule metadata load/save through worksheet XML |
| Conditional formatting differential styles | Pass; advanced rules preserve `dxf` font, fill, border, and number format styling |
| Unknown conditional formatting retention | Pass; unsupported/future `cfRule` blocks are sanitized out of the ClosedXML load copy and merged back into the saved worksheet XML |
| Unsupported chart drawing retention | Pass; unsupported chart package parts and worksheet drawing relationships stay attached after model edits |
| Native chart family expansion | Pass for authored/read combo, radar, and stock chart package parts alongside existing supported chart families; surface, histogram, waterfall, treemap, sunburst, box-whisker, funnel, and map are explicitly detected as unsupported chart families and stay in the retention/warning path |
| Picture/image XLSX fidelity | Pass for PNG image drawing metadata/bytes load, authored image save, and native picture package retention after model edits |
| Sparkline XLSX fidelity | Pass for worksheet extension sparkline group load/save, with unknown sibling worksheet `extLst` entries merged back after model edits |
| Text box and shape XLSX fidelity | Pass for native/authored text boxes and basic rectangle/ellipse/line drawing shapes |
| Slicer/timeline metadata | Pass; metadata loads, native package parts are retained after ordinary edits, native floating drawing anchors merge with Freexcel-authored drawing objects, authored slicer/timeline state, Insert Slicer/Insert Timeline commands, connected PivotTable filtering, and cross-sheet source data handling are implemented |
| External workbook link metadata | Pass; metadata loads and workbook `externalReferences`/relationships are retained after ordinary edits |
| Worksheet/workbook edge-case metadata | Pass; veryHidden sheet state, worksheet `codeName`, unsupported worksheet `sheetPr` metadata, per-sheet calculation properties, worksheet phonetic properties, ignored worksheet errors, worksheet cell watches, workbook file version/sharing metadata, unsupported workbook properties, workbook calculation properties, additional workbook views, custom workbook views, unsupported workbook defined names, printer settings package references, worksheet `customSheetViews`, worksheet scenarios, unknown worksheet/workbook extension-list entries, and `calcChain.xml` package retention survive ordinary edits |
| Public workbook corpus | 25/25 public/open-license Tealeg workbooks open, save, reload, and satisfy tag-level semantic assertions where applicable |
| Local-private workbook corpus | 20 optional manifest rows skipped when files are absent |

Verification commands:

```powershell
dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj
dotnet test tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj
dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj
dotnet build Freexcel.slnx
```

Results: IO tests 304/304 pass, Model tests 698/698 pass, App Host tests 414/414 pass, focused ChartRenderer tests 48/48 pass, and full solution build succeeds with 0 warnings and 0 errors.

## Feature Buckets Exercised

| Bucket | Generated fixture |
|---|---|
| Basic grid data | `generated-grid-basic-001` |
| Formulas | `generated-formulas-001` |
| Cross-sheet formulas and named ranges | `generated-cross-sheet-001` plus unsupported `definedName` retention smoke test |
| Formatting | `generated-formatting-001` |
| Structure | `generated-structure-001` |
| Data validation | `generated-validation-001` |
| Conditional formatting | `generated-conditional-formatting-001` |
| Color scale conditional formatting | `generated-color-scales-001` |
| Data bar conditional formatting | `generated-data-bars-001` |
| Conditional formatting long-tail metadata and `dxf` styling | `generated-conditional-formatting-001` plus smoke tests |
| Objects and links | `generated-objects-001` |
| Images and sparklines | `generated-images-sparklines-001` plus unknown worksheet `extLst` merge smoke test |
| Text boxes and basic drawing shapes | `generated-text-boxes-shapes-001` |
| Charts, including radar and stock | `generated-charts-001` |
| PivotTables, pivot caches, and PivotChart binding | `generated-pivots-001` plus PivotTable/PivotChart command, refresh, field layout command, aggregation, nested column fields, page filters, label/value filters, grouping, sorting, layout/style options, calculated-field/item, Show Details, pivot cache shared-item edge metadata, and OOXML smoke tests |
| Structured tables | `generated-structured-tables-001` plus totals-row and AutoFilter metadata smoke tests |
| Protection, calculation, page setup, and worksheet/workbook view/error/what-if metadata | `generated-protection-page-setup-001` plus workbook file-version/sharing/property, workbook calculation-property, worksheet calculation-property, workbook-view, custom-workbook-view, worksheet `sheetPr`, phonetic-property, ignored-errors, cell-watch, `customSheetViews`, scenario, and workbook `extLst` smoke tests |
| Slicers, timelines, external links, printer settings | Metadata-pass manifest rows plus package retention smoke tests |
| Public real-world workbook structures | 25 Tealeg XLSX workbooks covering hyperlinks, merged cells, inline/shared strings, styles, chartsheets, empty rows/cells, WPS/Google/Numbers/Excel variants, and workbook relationship edge cases |

## Gaps Before 95% Fidelity Claim

- Add local-private workbook rows for user-approved samples; keep files ignored.
- Continue expanding the runner from structural save/load smoke checks into deeper per-feature semantic comparisons.
- Add issue-specific regression workbooks when a failing XLSX round-trip is fixed.
- Complete manual desktop Excel interop review: open native samples in Freexcel, save, reopen in desktop Excel, and verify no repair dialog or feature loss for the sampled features.
- Continue PivotTable fidelity past the current functional core only in the remaining native-fidelity gaps: deeper per-element PivotStyle gallery semantics and full PivotChart layout/design editing.
- Keep excluded Microsoft/Office integration features as warning-only/out-of-scope: VBA projects, OLE/embedded objects, Power Query, Data Model/Power Pivot, linked data types, threaded comments, track changes/revision history, ActiveX/form controls, digital signatures, custom Ribbon UI, Office add-ins/web extensions, live web queries/web publish items, and sensitivity labels.
