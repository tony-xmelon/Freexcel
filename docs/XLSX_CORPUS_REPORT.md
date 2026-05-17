# Freexcel XLSX Corpus Report

**Last updated:** 2026-05-17  
**Status:** Executable parity harness with model-first XLSX retention slices  

## Current Corpus

| Source type | Count | Status |
|---|---:|---|
| Generated deterministic supported-pass fixtures | 15 | Passing through in-memory XLSX save/load with stronger per-feature summary comparison |
| Generated deterministic model-first PivotTable fixture | 1 | Pivot cache/table metadata loads and package references are retained |
| Generated deterministic known-gap fixtures | 21 | Declared with expected warnings and notes; warning detector covers unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, printer settings, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, slicers, timelines, external links, embedded objects, and custom XML |
| Public redistributed workbooks | 0 | Pending source/license review |
| Local private workbooks | 0 | Supported by runner; missing files are skipped |
| Regression workbooks | 0 | Pending first issue-specific binary fixture |

Total manifest rows: 37.

## Current Result

| Check | Result |
|---|---|
| Manifest schema and policy tests | Pass |
| Generated fixture factory coverage | 15/15 supported-pass manifest rows |
| Generated XLSX save/load round-trip with supported-feature summary comparison | 15/15 pass |
| Generated known-gap warning/notes coverage | 21/21 pass |
| Generated known-gap package warning execution | 21/21 pass |
| Generated known-gap package retention after model edit | 21/21 pass for critical package parts |
| Unsupported feature detector known-gap coverage | Unsupported chart package parts, threaded comments, track changes/revision history, unsupported sheet types, form controls/ActiveX controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publishing, sensitivity labels/IRM metadata, SmartArt diagrams, printer settings, VBA macros, Power Query, Data Model/Power Pivot, Microsoft linked data types, slicers, timelines, external links, embedded objects, and custom XML detected, including multiple unsupported worksheet/package feature families |
| Missing local-private files | Skipped without failure |
| Workbook structure protection XLSX round-trip | Pass; `workbookPassword` is written as legacy hash text, not raw password text |
| Structured table XLSX retention | Pass; table metadata loads, authored table parts save, and native table references are preserved after edits |
| Advanced conditional formatting metadata | Pass; color scales, data bars, and icon set metadata load/save through worksheet XML |
| Conditional formatting long-tail metadata | Pass; top/bottom, text, date-occurring, duplicate/unique, blank/nonblank, and error/no-error rule metadata load/save through worksheet XML |
| Unsupported chart drawing retention | Pass; unsupported chart package parts and worksheet drawing relationships stay attached after model edits |
| Picture/image XLSX fidelity | Pass for PNG image drawing metadata/bytes load, authored image save, and native picture package retention after model edits |
| Sparkline XLSX fidelity | Pass for worksheet extension sparkline group load/save |
| Text box and shape XLSX fidelity | Pass for native/authored text boxes and basic rectangle/ellipse/line drawing shapes |

Focused command:

```powershell
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --no-restore --filter XlsxCorpusRunnerTests
```

Result: 5/5 corpus runner tests passing over 37 manifest rows.

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
| Conditional formatting long-tail metadata | `generated-conditional-formatting-001` |
| Objects and links | `generated-objects-001` |
| Images and sparklines | `generated-images-sparklines-001` |
| Text boxes and basic drawing shapes | `generated-text-boxes-shapes-001` |
| Charts | `generated-charts-001` |
| Structured tables | `generated-structured-tables-001` |
| Protection and page setup | `generated-protection-page-setup-001` |

## Gaps Before 95% Fidelity Claim

- Add real public/open-license XLSX workbooks and record source URLs, retrieval dates, and licenses.
- Add local-private workbook rows for user-approved samples; keep files ignored.
- Continue expanding the runner from structural save/load smoke checks into deeper per-feature semantic comparisons.
- Add explicit known-gap rows for other modeled-but-not-yet-round-tripped package features as they are discovered.
- Promote issue-specific regression workbooks when a failing XLSX round-trip is fixed.

