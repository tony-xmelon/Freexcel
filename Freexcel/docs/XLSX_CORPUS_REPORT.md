# Freexcel XLSX Corpus Report

**Last updated:** 2026-05-18  
**Status:** Executable parity harness with model-first XLSX retention, expanded PivotTable fidelity slices, and PivotChart binding round-trip

## Current Corpus

| Source type | Count | Status |
|---|---:|---|
| Generated deterministic supported-pass fixtures | 16 | Passing through in-memory XLSX save/load with stronger per-feature summary comparison |
| Generated deterministic supported-metadata-pass fixtures | 3 | Slicers, timelines, and external workbook links load metadata and retain native package references after ordinary edits |
| Generated deterministic known-gap fixtures | 18 | Declared with expected warnings and notes; warning detector covers unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, printer settings, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, embedded objects, and custom XML |
| Public redistributed workbooks | 25 | Open-license Tealeg XLSX public corpus; files open, save, and reload through the runner |
| Local private workbooks | 0 | Supported by runner; missing files are skipped |
| Regression workbooks | 0 | Pending first issue-specific binary fixture |

Total manifest rows: 62.

## Current Result

| Check | Result |
|---|---|
| Manifest schema and policy tests | Pass |
| Generated fixture factory coverage | 16/16 supported-pass manifest rows |
| Generated XLSX save/load round-trip with supported-feature summary comparison | 16/16 pass |
| Generated known-gap warning/notes coverage | 18/18 pass |
| Generated known-gap package warning execution | 18/18 pass |
| Generated known-gap package retention after model edit | 18/18 pass for critical package parts |
| Unsupported feature detector known-gap coverage | Unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, printer settings, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, embedded objects, and custom XML detected |
| Missing local-private files | Skipped without failure |
| Workbook structure protection XLSX round-trip | Pass; `workbookPassword` is written as legacy hash text, not raw password text |
| Structured table XLSX retention | Pass; table metadata loads, authored table parts save, and native table references are preserved after edits |
| PivotTable XLSX parity slice | Pass; PivotTable/cache metadata loads, native package references are preserved, authored pivot package parts save, selected-range creation and refresh work, undoable command-level field layout changes work, values-only and column-only layouts materialize, multiple row/column/value fields materialize, nested column-field matrices render, common summaries evaluate, single/multi-select page-field filters apply, date/number grouping, row/column top/bottom/threshold value filters with field targets, row/column label filters, value/label sorting including column-label sorting, separate row/column grand-total visibility round-trips, repeated-label suppression, blank-line spacing, PivotTable style names, subtotals, calculated fields, and calculated items round-trip, Show Details creates source-row detail sheets from the ribbon or pivot-value double-click for item/subtotal/grand-total/matrix/column-only cells, and the Insert ribbon exposes creation/refresh/detail commands |
| PivotChart XLSX parity slice | Pass; bound PivotCharts can be authored from PivotTables, refresh with the PivotTable materialized output range, and read/write chart `pivotSource` metadata |
| Advanced conditional formatting metadata | Pass; color scales, data bars, icon sets, and long-tail rule metadata load/save through worksheet XML |
| Conditional formatting differential styles | Pass; advanced rules preserve `dxf` font, fill, border, and number format styling |
| Unknown conditional formatting retention | Pass; unsupported/future `cfRule` blocks are sanitized out of the ClosedXML load copy and merged back into the saved worksheet XML |
| Unsupported chart drawing retention | Pass; unsupported chart package parts and worksheet drawing relationships stay attached after model edits |
| Native chart family expansion | Pass for authored/read radar and stock chart package parts, alongside existing supported chart families |
| Picture/image XLSX fidelity | Pass for PNG image drawing metadata/bytes load, authored image save, and native picture package retention after model edits |
| Sparkline XLSX fidelity | Pass for worksheet extension sparkline group load/save |
| Text box and shape XLSX fidelity | Pass for native/authored text boxes and basic rectangle/ellipse/line drawing shapes |
| Slicer/timeline metadata | Pass; metadata loads and native package parts are retained after ordinary edits |
| External workbook link metadata | Pass; metadata loads and workbook `externalReferences`/relationships are retained after ordinary edits |
| Worksheet edge-case metadata | Pass; veryHidden sheet state, worksheet `codeName`, and `calcChain.xml` package retention survive ordinary edits |
| Public workbook corpus | 25/25 public/open-license Tealeg workbooks open, save, and reload |

Verification commands:

```powershell
dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj
dotnet test tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj
dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj
dotnet build Freexcel.slnx
```

Results: Model tests 638/638 pass, IO tests 267/267 pass, full solution build succeeds with 0 warnings and 0 errors. Full Formula tests remain blocked by 5 unrelated Phase B distribution failures (`KURT`, `GAMMA.DIST`, `BETA.DIST`, `SKEW`, `T.TEST`) and are not a PivotTable regression.

## Feature Buckets Exercised

| Bucket | Generated fixture |
|---|---|
| Basic grid data | `generated-grid-basic-001` |
| Formulas | `generated-formulas-001` |
| Cross-sheet formulas and named ranges | `generated-cross-sheet-001` |
| Formatting | `generated-formatting-001` |
| Structure | `generated-structure-001` |
| Data validation | `generated-validation-001` |
| Conditional formatting | `generated-conditional-formatting-001` |
| Color scale conditional formatting | `generated-color-scales-001` |
| Data bar conditional formatting | `generated-data-bars-001` |
| Conditional formatting long-tail metadata and `dxf` styling | `generated-conditional-formatting-001` plus smoke tests |
| Objects and links | `generated-objects-001` |
| Images and sparklines | `generated-images-sparklines-001` |
| Text boxes and basic drawing shapes | `generated-text-boxes-shapes-001` |
| Charts, including radar and stock | `generated-charts-001` |
| PivotTables, pivot caches, and PivotChart binding | `generated-pivots-001` plus PivotTable/PivotChart command, refresh, field layout command, aggregation, nested column fields, page filters, label/value filters, grouping, sorting, layout/style options, calculated-field/item, Show Details, and OOXML smoke tests |
| Structured tables | `generated-structured-tables-001` |
| Protection and page setup | `generated-protection-page-setup-001` |
| Slicers, timelines, external links | Metadata-pass manifest rows plus package retention smoke tests |
| Public real-world workbook structures | 25 Tealeg XLSX workbooks covering hyperlinks, merged cells, inline/shared strings, styles, chartsheets, empty rows/cells, WPS/Google/Numbers/Excel variants, and workbook relationship edge cases |

## Gaps Before 95% Fidelity Claim

- Add local-private workbook rows for user-approved samples; keep files ignored.
- Continue expanding the runner from structural save/load smoke checks into deeper per-feature semantic comparisons.
- Add issue-specific regression workbooks when a failing XLSX round-trip is fixed.
- Continue PivotTable fidelity past the current functional core: full field-list drag/drop pane, richer advanced filters/layouts, slicer/timeline interaction, and native Excel pivot cache edge cases.
- Keep excluded Microsoft/Office integration features as warning-only/out-of-scope: VBA projects, OLE/embedded objects, Power Query, Data Model/Power Pivot, linked data types, threaded comments, track changes/revision history, ActiveX/form controls, digital signatures, custom Ribbon UI, Office add-ins/web extensions, live web queries/web publish items, and sensitivity labels.
