# Freexcel XLSX Corpus Report

**Last updated:** 2026-05-17  
**Status:** Initial executable scaffold  

## Current Corpus

| Source type | Count | Status |
|---|---:|---|
| Generated deterministic supported-pass fixtures | 10 | Passing through in-memory XLSX save/load with summary comparison |
| Generated deterministic known-gap fixtures | 18 | Declared with expected warnings and notes; warning detector covers unsupported chart package parts, conditional formats, drawing objects, sparklines, threaded comments, track changes/revision history, form controls/ActiveX controls, VBA macros, PivotTables/pivot caches, Power Query, Data Model/Power Pivot, Microsoft linked data types, slicers, timelines, external links, embedded objects, and custom XML |
| Public redistributed workbooks | 0 | Pending source/license review |
| Local private workbooks | 0 | Supported by runner; missing files are skipped |
| Regression workbooks | 0 | Pending first issue-specific binary fixture |

Total manifest rows: 28.

## Current Result

| Check | Result |
|---|---|
| Manifest schema and policy tests | Pass |
| Generated fixture factory coverage | 10/10 manifest rows |
| Generated XLSX save/load round-trip with supported-feature summary comparison | 10/10 pass |
| Generated known-gap warning/notes coverage | 18/18 pass |
| Generated known-gap package warning execution | 18/18 pass |
| Unsupported feature detector known-gap coverage | Unsupported chart package parts, conditional formats, drawing objects, sparklines, threaded comments, track changes/revision history, form controls/ActiveX controls, VBA macros, PivotTables/pivot caches, Power Query, Data Model/Power Pivot, Microsoft linked data types, slicers, timelines, external links, embedded objects, and custom XML detected, including multiple unsupported worksheet/package feature families |
| Missing local-private files | Skipped without failure |
| Workbook structure protection XLSX round-trip | Pass; `workbookPassword` is written as legacy hash text, not raw password text |

Focused command:

```powershell
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --no-restore --filter XlsxCorpusRunnerTests
```

Result: 4/4 corpus runner tests passing over 28 manifest rows. Full solution verification is 2047/2047 tests passing with 0 build warnings.

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
| Objects and links | `generated-objects-001` |
| Charts | `generated-charts-001` |
| Protection and page setup | `generated-protection-page-setup-001` |

## Gaps Before 95% Fidelity Claim

- Add real public/open-license XLSX workbooks and record source URLs, retrieval dates, and licenses.
- Add local-private workbook rows for user-approved samples; keep files ignored.
- Expand the runner from structural save/load smoke checks into per-feature comparisons.
- Add explicit known-gap rows for other modeled-but-not-yet-round-tripped package features as they are discovered.
- Promote issue-specific regression workbooks when a failing XLSX round-trip is fixed.
