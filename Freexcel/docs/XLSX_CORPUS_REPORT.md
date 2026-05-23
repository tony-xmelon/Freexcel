# Freexcel XLSX Corpus Report

**Last updated:** 2026-05-23
**Status:** Executable parity harness with 101 workbook manifest rows, model-first XLSX retention, URI-aware package-health checks, stronger semantic corpus tag assertions, public-corpus model-summary stability checks, expanded generated feature coverage, expanded PivotTable/PivotChart fidelity slices, deeper worksheet native-metadata preservation, and private/regression corpus scaffolding

## Current Corpus

| Source type | Count | Status |
|---|---:|---|
| Generated deterministic supported-pass fixtures | 27 | Passing through in-memory XLSX save/load with stronger per-feature summary comparison |
| Generated deterministic supported-metadata-pass fixtures | 5 | Slicers, timelines, external workbook links, printer settings, and custom XML parts retain native package references after ordinary edits |
| Generated deterministic known-gap fixtures | 16 | Declared with expected warnings and notes; warning detector covers unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, and embedded objects |
| Public redistributed workbooks | 25 | Open-license Tealeg XLSX public corpus; files open, save, and reload through the runner |
| Local private workbooks | 20 | Optional user-approved torture rows are in the manifest; missing files are skipped |
| Regression workbooks | 8 | Excel-authored cached formula-result fixtures covering basics, coercion/errors, date serials, date/time edge cases, engineering bitwise/base conversions, financial price/yield pairs, lookup/reference edges, dynamic-array scalar/range composition, scalar-array coercion, statistical inverse/distribution round trips, and array comparison/arithmetic expressions |

Total manifest rows: 101.

## Current Result

| Check | Result |
|---|---|
| Manifest schema and policy tests | Pass |
| Generated fixture factory coverage | 27/27 supported-pass manifest rows |
| Generated XLSX save/load round-trip with supported-feature summary comparison | 27/27 pass with saved-package health validation and per-tag semantic assertions for formulas, cross-sheet references, named ranges, validation, conditional formatting, color scales, data bars, icon sets, style-only blank cells, comments, hyperlinks, drawings, tables, pivots, protection, and page setup |
| Generated known-gap warning/notes coverage | 16/16 pass |
| Generated known-gap package warning execution | 16/16 pass with retained-opaque messaging |
| Generated known-gap package retention after model edit | 16/16 pass for critical package parts and retained relationship targets |
| Generated metadata-pass package retention after model edit | 5/5 pass for critical package parts, retained relationship targets, no unsupported-feature warnings, and saved-package health validation |
| Unsupported feature detector known-gap coverage | Unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, and embedded objects detected |
| Missing local-private files | Skipped without failure |
| Workbook structure protection XLSX round-trip | Pass; `workbookPassword` is written as legacy hash text, not raw password text |
| Structured table XLSX retention | Pass; table metadata loads, authored table parts save, totals-row column metadata and simple value AutoFilter metadata round-trip, and native table references are preserved after edits |
| PivotTable XLSX parity slice | Pass; PivotTable/cache metadata loads, native package references are preserved, authored pivot package parts save, same-sheet and cross-sheet creation/refresh/source changes work, undoable command-level field layout changes work, values-only and column-only layouts materialize, multiple row/column/value fields materialize, Compact/Outline/Tabular report-layout state round-trips with Compact row-label rendering, nested column-field matrices render, common/statistical summaries evaluate, single/multi-select page/row/column checked-item filters apply and round-trip, date/number grouping, row/column top/bottom/threshold value filters with field targets, row/column label filters, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants calculate and round-trip with base field/item metadata, value/label sorting including column label/value sorting, separate row/column grand-total visibility round-trips, repeated-label suppression, blank-line spacing, PivotTable style names, custom PivotStyle definitions, and style-option flags round-trip, top/bottom subtotals, calculated fields, and calculated items round-trip, native pivot cache records relationships are retained, pivot cache shared-item edge metadata round-trips, external/OLAP pivot cache source metadata round-trips, GETPIVOTDATA evaluates same-sheet and cross-sheet PivotTable references, rendered PivotTable header/subtotal/grand-total/banded styles are applied for built-in presets, Show Details creates source-row detail sheets from the ribbon or pivot-value double-click for item/subtotal/grand-total/matrix/column-only data cells, and the Insert/contextual ribbons expose creation/refresh/detail/slicer/timeline commands |
| PivotChart XLSX parity slice | Pass; bound PivotCharts can be authored from PivotTables, refresh with the PivotTable materialized output range, support undoable type changes that preserve the binding, read/write chart `pivotSource` metadata, round-trip PivotChart `pivotFmts`, chart external-data relationship pointers plus package relationship type/target/target-mode metadata, plot-area and legend manual layout metadata, date-system/language, color-map overrides, print settings, style ids, protection flags, rounded-corner, auto-title-deleted, hidden-row-data visibility, blank-display, data-table options, and data-label-over-maximum chart-space metadata from chart package design metadata, expose editable PivotChart Options for field buttons, data-table/legend-key display, rounded corners, hidden-row data visibility, and blank-cell display mode, and native same-sheet/cross-sheet PivotChart package graphs resolve back to their PivotTable cache binding after load/save |
| Advanced conditional formatting metadata | Pass; color scales, data bars, icon sets, and long-tail rule metadata load/save through worksheet XML |
| Conditional formatting differential styles | Pass; advanced rules preserve `dxf` font, fill, border, and number format styling |
| Unknown conditional formatting retention | Pass; unsupported/future `cfRule` blocks are sanitized out of the ClosedXML load copy and merged back into the saved worksheet XML |
| Unsupported chart drawing retention | Pass; unsupported chart package parts and worksheet drawing relationships stay attached after model edits |
| Native chart family expansion | Pass for authored/read combo, radar, stock high-low-close/open-high-low-close/volume stock package parts, volume stock rendering, date-axis stock rendering, stock up/down-bar candlestick rendering, and 3D clustered column/bar `bar3DChart` package/rendering paths, alongside existing supported chart families; surface, histogram, waterfall, treemap, sunburst, box-whisker, funnel, and map are explicitly detected as unsupported chart families and stay in the retention/warning path |
| Picture/image XLSX fidelity | Pass for PNG image drawing metadata/bytes load, authored image save, and native picture package retention after model edits |
| Sparkline XLSX fidelity | Pass for worksheet extension sparkline group load/save, with unknown sibling worksheet `extLst` entries merged back after model edits |
| Text box and shape XLSX fidelity | Pass for native/authored text boxes, basic rectangle/ellipse/line drawing shapes, and retained native connector/group-shape anchors alongside Freexcel-authored drawing objects |
| Slicer/timeline metadata | Pass; metadata loads, native package parts and worksheet floating drawing anchors are retained after ordinary edits, native caption/style metadata round-trips, native floating drawing anchors merge with Freexcel-authored drawing objects, authored slicer/timeline state, Insert Slicer/Insert Timeline commands, connected PivotTable filtering, and cross-sheet source data handling are implemented |
| External workbook link metadata | Pass; metadata loads and workbook `externalReferences`/relationships are retained after ordinary edits |
| Stylesheet native metadata | Pass; native stylesheet `colors`, custom `tableStyles`, native `tableStyles` child payloads, and unknown stylesheet `extLst` payloads survive ordinary edits without replacing Freexcel's generated style tables |
| Document property metadata | Pass; stable native `docProps/core.xml` and `docProps/app.xml` fields survive ordinary edits and are counted by corpus critical-part retention checks |
| Worksheet/workbook edge-case metadata | Pass; veryHidden sheet state, worksheet `codeName`, unsupported worksheet `sheetPr` metadata, worksheet `sheetFormatPr` native attributes/children, worksheet dimension metadata, worksheet `sheetData`/row/cell/`cols`/column native attributes plus row/cell native child payloads, worksheet formula element metadata, merged-cell metadata, worksheet page-break native attributes, worksheet print-option/page-setup/header-footer native attributes and native-only child payloads, primary worksheet sheet-view native metadata, advanced worksheet/workbook protection metadata, protected-range native attributes, additional worksheet sheet views, header/footer legacy drawing references, worksheet custom properties, worksheet smart tags, sheet-level AutoFilter metadata, per-sheet calculation properties, worksheet phonetic properties, worksheet sort state, worksheet data-consolidation settings, ignored worksheet errors, worksheet cell watches, workbook file version/sharing/recovery/smart-tag/function-group metadata, unsupported workbook properties, workbook calculation native metadata, additional/primary workbook views, custom workbook views, unsupported workbook defined names, printer settings package references, worksheet `customSheetViews`, worksheet scenarios, unknown worksheet/workbook extension-list entries, and `calcChain.xml` package retention survive ordinary edits |
| Public workbook corpus | 25/25 public/open-license Tealeg workbooks open, save, reload, pass saved-package health validation, retain model-visible workbook summaries, and satisfy tag-level semantic assertions where applicable |
| Local-private workbook corpus | 20 optional manifest rows skipped when files are absent |

## Pass Rate Summary

| Workbook set | Executed | Passing | Pass rate |
|---|---:|---:|---:|
| Generated supported-pass workbooks | 27 | 27 | 100% |
| Generated supported-metadata-pass workbooks | 5 | 5 | 100% |
| Generated known-gap warning workbooks | 16 | 16 | 100% |
| Generated known-gap retention workbooks | 16 | 16 | 100% |
| Public redistributed workbooks | 25 | 25 | 100% |
| Regression cached-result workbooks | 9 | 9 | 100% |
| Local-private workbook rows | 0 | 0 | Skipped; files absent |

| Feature bucket | Evidence | Pass rate |
|---|---|---:|
| Basic grid data | Generated supported-pass round-trip and summary comparison | 100% |
| Formulas, cached values, cross-sheet references, and named ranges | Generated semantic assertions plus regression cached-result rows | 100% |
| Formatting, styles, style-only blank cells, document metadata, and workbook structure | Generated semantic assertions plus metadata retention checks | 100% |
| Data validation and conditional formatting metadata | Generated semantic assertions plus dxf/unknown-cf retention smoke tests | 100% |
| Tables, AutoFilter metadata, and structured references | Generated semantic assertions plus table metadata smoke tests | 100% |
| Charts, pictures, sparklines, text boxes, and drawing shapes | Generated semantic assertions plus native drawing/package retention smoke tests | 100% |
| PivotTables, pivot caches, and PivotChart binding | Generated semantic assertions plus PivotTable/PivotChart command, cache metadata, and native package smoke tests | 100% |
| Protection, page setup, printer settings, views, and worksheet/workbook edge metadata | Generated semantic assertions plus native metadata retention smoke tests | 100% |
| Slicers, timelines, external links, printer settings, custom XML | Metadata-pass manifest rows plus package retention smoke tests | 100% |
| Known unsupported/excluded XLSX surfaces | Generated known-gap rows produce expected warnings and retain critical package parts | 100% |
| Public real-world workbook structures | 25 Tealeg workbooks open, save, reload, retain model-visible workbook summaries, and pass package-health checks | 100% |

Verification commands:

```powershell
dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj
dotnet test tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj
dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj
dotnet build Freexcel.slnx
```

Results: IO tests 360/360 pass, Model tests 858/858 pass, App Host tests 781/781 pass, focused ChartRenderer tests 48/48 pass, and full solution build succeeds with 0 warnings and 0 errors.

## Feature Buckets Exercised

| Bucket | Generated fixture |
|---|---|
| Basic grid data | `generated-grid-basic-001` |
| Formulas | `generated-formulas-001` |
| Cross-sheet formulas and named ranges | `generated-cross-sheet-001`, `generated-named-ranges-formulas-002`, plus unsupported `definedName` retention smoke test |
| Formatting, style-only blank cells, and document metadata | `generated-formatting-001`, `generated-style-only-cells-002`, plus stylesheet native metadata and document-property smoke tests |
| Structure | `generated-structure-001`, `generated-merged-freeze-002` |
| Data validation | `generated-validation-001`, `generated-validation-custom-002` |
| Conditional formatting | `generated-conditional-formatting-001` |
| Color scale conditional formatting | `generated-color-scales-001` |
| Data bar conditional formatting | `generated-data-bars-001` |
| Conditional formatting long-tail metadata and `dxf` styling | `generated-conditional-formatting-001` plus smoke tests |
| Icon set conditional formatting | `generated-icon-sets-001` |
| Objects, comments, and links | `generated-objects-001`, `generated-comments-hyperlinks-002` |
| Images and sparklines | `generated-images-sparklines-001`, `generated-images-sparklines-002`, plus unknown worksheet `extLst` merge smoke test |
| Text boxes and basic drawing shapes | `generated-text-boxes-shapes-001` |
| Charts, including radar and stock | `generated-charts-001`, `generated-charts-combo-002` with date-category volume stock coverage |
| PivotTables, pivot caches, and PivotChart binding | `generated-pivots-001`, `generated-pivots-filters-002`, plus PivotTable/PivotChart command, refresh, field layout command, aggregation, nested column fields, page filters, label/value filters, grouping, sorting, layout/style options, custom PivotStyle definitions, calculated-field/item, Show Details, pivot cache shared-item edge metadata, external/OLAP cache source metadata, PivotChart `pivotFmts`, external-data pointer plus relationship type/target/target-mode metadata, plot-area and legend manual layout metadata, date-system/language, color-map, print-settings, style-id, protection-flag, rounded-corner, auto-title-deleted, hidden-row-data visibility, blank-display, and data-label-over-maximum metadata, native same-sheet/cross-sheet PivotChart graph/cache binding, and OOXML smoke tests |
| Structured tables | `generated-structured-tables-001`, `generated-structured-table-totals-002`, plus totals-row and AutoFilter metadata smoke tests |
| Protection, calculation, page setup, and worksheet/workbook view/error/what-if metadata | `generated-protection-page-setup-001`, `generated-print-titles-breaks-001`, plus advanced sheet/workbook-protection metadata, protected-range native attributes, primary/additional worksheet sheet views, header/footer legacy drawing references, worksheet custom-properties/smart-tags, sheet-level AutoFilter, workbook file-version/sharing/recovery/smart-tag/function-group/property, workbook calculation-property/native metadata, worksheet calculation-property, primary/additional workbook-view, custom-workbook-view, worksheet `sheetPr`, worksheet `sheetFormatPr`, worksheet dimension/formula/merged-cell metadata, worksheet row/cell/column metadata, worksheet page-break metadata, worksheet print-option/page-setup/header-footer metadata, phonetic-property, sort-state, data-consolidation, ignored-errors, cell-watch, `customSheetViews`, scenario, and workbook `extLst` smoke tests |
| Slicers, timelines, external links, printer settings, custom XML | Metadata-pass manifest rows plus package retention smoke tests |
| Public real-world workbook structures | 25 Tealeg XLSX workbooks covering hyperlinks, merged cells, inline/shared strings, styles, chartsheets, empty rows/cells, WPS/Google/Numbers/Excel variants, and workbook relationship edge cases |

## Gaps Before 95% Fidelity Claim

- Add local-private workbook rows for user-approved samples; keep files ignored.
- Continue expanding the 100-row corpus beyond the current baseline, with deeper per-feature semantic comparisons for package-only public samples and richer private workbooks.
- Continue adding issue-specific regression workbooks when a failing XLSX round-trip is fixed.
- Complete manual desktop Excel interop review: open native samples in Freexcel, save, reopen in desktop Excel, and verify no repair dialog or feature loss for the sampled features.
- Continue PivotTable fidelity past the current functional core only in the remaining native-fidelity gaps: exact PivotStyle gallery UI/rendering semantics, richer PivotChart layout/design editing beyond chart-space design metadata, and external/OLAP/data-model refresh or execution.
- Keep excluded Microsoft/Office integration features as warning-only/out-of-scope: VBA projects, OLE/embedded objects, Power Query, Data Model/Power Pivot, linked data types, threaded comments, track changes/revision history, ActiveX/form controls, digital signatures, custom Ribbon UI, Office add-ins/web extensions, live web queries/web publish items, and sensitivity labels.
