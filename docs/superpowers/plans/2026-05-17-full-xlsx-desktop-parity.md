# Full XLSX Desktop Excel Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring Freexcel XLSX open/edit/save behavior as close as practical to desktop Microsoft Excel, while retaining excluded/unsupported package features intact.

**Architecture:** Treat the OOXML package as the source of truth for features Freexcel cannot fully render yet, and add model-first implementations one feature family at a time. Every slice starts with a failing corpus or smoke test, then adds model/IO/command/UI behavior only as needed; package-preservation tests remain mandatory so native Excel workbooks do not lose unsupported content after ordinary edits.

**Tech Stack:** C#/.NET 10, ClosedXML where it is reliable, direct `ZipArchive` + `XDocument` OOXML patching for package fidelity, xUnit/FluentAssertions, WPF.

---

## Scope Rules

**Must retain even when not implemented:** VBA/macros, OLE/embedded objects, Power Query, Data Model/Power Pivot internals, linked/rich data, threaded comments, track changes, ActiveX/form controls, digital signatures, custom ribbon UI, Office add-ins/web extensions, live web queries/web publish, sensitivity labels.

**Must implement or model-first preserve:** worksheet data/styles/formulas, tables, PivotTables, slicers/timelines metadata, charts, drawings/images/text boxes/shapes, sparklines, conditional formatting variants, data validation, comments/hyperlinks, page setup/print options, protection, custom views/scenarios/watch/error-checking, worksheet views, named ranges, external links metadata, workbook calc/theme/window metadata.

**Definition of done per feature family:** native Excel-created XLSX opens, model metadata is available where appropriate, ordinary Freexcel edits save without losing the feature, authored Freexcel models save as valid XLSX where in-scope, and corpus/tests prove the behavior.

---

### Task 1: Package Fidelity Harness v2

**Files:**
- Modify: `tests/Freexcel.Core.IO.Tests/XlsxCorpusRunnerTests.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/XlsxCorpusFixtureFactory.cs`
- Modify: `test-corpus/manifest.csv`
- Modify: `docs/XLSX_CORPUS_REPORT.md`

- [ ] Add package-level assertions to compare critical package relationships before/after save.

```csharp
private static PackagePartSummary CapturePackageSummary(Stream stream)
{
    using var archive = new ZipArchive(stream, ZipArchiveMode.Read, leaveOpen: true);
    return new PackagePartSummary(
        archive.Entries
            .Select(entry => entry.FullName.Replace('\\', '/'))
            .Where(path => IsFidelityCriticalPart(path))
            .Order(StringComparer.OrdinalIgnoreCase)
            .ToArray());
}

private static bool IsFidelityCriticalPart(string path) =>
    path.StartsWith("xl/drawings/", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/charts/", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/media/", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/tables/", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/pivot", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/slicer", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/timeline", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("xl/externalLinks/", StringComparison.OrdinalIgnoreCase) ||
    path.StartsWith("customXml/", StringComparison.OrdinalIgnoreCase) ||
    path.EndsWith(".rels", StringComparison.OrdinalIgnoreCase);

private sealed record PackagePartSummary(IReadOnlyList<string> CriticalParts);
```

- [ ] Add a failing test that loads a known-gap package, performs a simple cell edit, saves, and verifies all critical package parts still exist.

Run: `dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter XlsxCorpusRunnerTests`

Expected first failure: at least one package family loses a relationship or worksheet pointer.

- [ ] Implement generic retention helpers only for package links that are safe to preserve without semantic edits.

Use existing `PreserveSourcePackageParts`, `MergeContentTypes`, `MergeRelationshipParts`, `PreserveWorksheetDrawingReferences`, `PreserveStructuredTableXmlReferences`, and `PreservePivotXmlReferences` as the pattern.

- [ ] Update `docs/XLSX_CORPUS_REPORT.md` with the package-fidelity check.

---

### Task 2: Images and Picture Fidelity

**Files:**
- Modify: `src/Freexcel.Core.Model/PictureModel.cs` or existing picture model file
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/XlsxCorpusFixtureFactory.cs`
- Modify: `test-corpus/manifest.csv`

- [ ] Write failing tests for loading an Excel drawing with `xdr:pic`, media relationship, alt text, anchor, dimensions, and content type.

Test names:
`XlsxAdapter_LoadsPictureMetadataAndBytes`
`XlsxAdapter_LoadedWorkbookSave_PreservesPictureDrawingAndMediaReferencesAlongsideModelEdits`

- [ ] Implement picture reader from worksheet drawing parts.

Required behavior:
read `xl/worksheets/sheetN.xml` drawing rel, read `xl/drawings/drawingN.xml`, find `xdr:pic`, resolve `a:blip r:embed`, load media bytes, map one-cell/two-cell/absolute anchors, map `cNvPr descr` to alt text.

- [ ] Implement picture writer for modeled pictures using existing media content-type helpers.

- [ ] Promote `generated-images-sparklines-001` image portion only after picture package load/save passes; keep sparkline warning until Task 3.

---

### Task 3: Sparkline Model and XLSX Fidelity

**Files:**
- Modify/Create: `src/Freexcel.Core.Model/SparklineModel.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/SparklineCommandTests.cs`

- [ ] Write failing test for loading `x14:sparklineGroups` from worksheet `extLst`.

Expected assertions:
`Kind`, `DataRange`, `Location`, group color/style fields where present.

- [ ] Write failing test for saving modeled sparkline groups back to worksheet XML.

- [ ] Implement XML reader/writer for Excel 2010 sparkline extension markup.

- [ ] Promote `generated-images-sparklines-001` once both image and sparkline checks pass.

---

### Task 4: Text Boxes and Shape Fidelity

**Files:**
- Modify: `src/Freexcel.Core.Model/TextBoxModel.cs`
- Modify: `src/Freexcel.Core.Model/DrawingShapeModel.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/TextBoxCommandTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/ShapeCommandTests.cs`

- [ ] Write failing tests for `xdr:sp` text box load/save with text body, fill, outline, alt text, rotation, and anchor.

- [ ] Write failing tests for basic AutoShapes: rectangle, ellipse, line, connector.

- [ ] Implement model mapping from DrawingML shape preset geometry.

- [ ] Implement writer for modeled text boxes and basic shapes.

- [ ] Preserve unknown DrawingML shape properties if a source package exists and Freexcel does not edit that object.

- [ ] Promote `generated-text-boxes-shapes-001` when modeled and preservation tests pass.

---

### Task 5: Chart Family Expansion

**Files:**
- Modify: `src/Freexcel.Core.Model/ChartModel.cs`
- Modify: `src/Freexcel.Core.IO/XlsxChartPartReader.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/ChartCommandTests.cs`

- [ ] Add failing tests for radar, stock, surface, combo, histogram, waterfall, treemap, sunburst, box-whisker, funnel, and map chart package metadata.

- [ ] Implement model-first preservation for chart families Freexcel cannot render yet.

- [ ] Implement full read/write for the next three high-value families: combo, radar, stock.

- [ ] Keep unsupported chart XML retained and worksheet-linked even when semantic model support is partial.

- [ ] Split chart tests into family-specific files if `ChartCommandTests.cs` becomes too large.

---

### Task 6: PivotTable Functional Parity

**Files:**
- Modify: `src/Freexcel.Core.Model/PivotTableModel.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableCommands.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Create: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Create: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [ ] Add tests for row, column, page/filter, value fields, number formats, subtotal function, grand totals, compact/tabular layout, and style names.

- [ ] Implement in-memory PivotTable refresh that materializes a static grid from worksheet source data.

- [ ] Add command tests for add/remove fields, refresh, and undo/redo.

- [ ] Save authored PivotTables as valid pivot cache + pivot table OOXML.

- [ ] Retain native PivotTable XML when source workbook exists and Freexcel only edits unrelated cells.

---

### Task 7: Slicers and Timelines

**Files:**
- Create: `src/Freexcel.Core.Model/SlicerModel.cs`
- Create: `src/Freexcel.Core.Model/TimelineModel.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFeatureInspector.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [ ] Write failing tests that slicer/timeline package parts and drawing relationships survive ordinary edits.

- [ ] Implement model-first metadata loader: name, cache name, source PivotTable, field, selected items/date range, package part.

- [ ] Keep UI/filter interaction out of the first pass unless the model tests require it.

- [ ] Remove slicers/timelines from unsupported warning list after retention and metadata tests pass.

---

### Task 8: Conditional Formatting Long Tail

**Files:**
- Modify: `src/Freexcel.Core.Model/ConditionalFormat.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/ConditionalFormatCommandTests.cs`

- [ ] Add tests for top/bottom, unique/duplicate, contains text, date occurring, blanks/no-blanks, errors/no-errors.

- [ ] Add differential style (`dxf`) fidelity tests for font, fill, border, and number format.

- [ ] Implement OOXML load/save for each rule type.

- [ ] Keep unknown future CF rules retained as raw XML when source package exists.

---

### Task 9: Workbook and Worksheet Edge Cases

**Files:**
- Modify: `src/Freexcel.Core.Model/Workbook.cs`
- Modify: `src/Freexcel.Core.Model/Sheet.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `tests/Freexcel.Core.Model.Tests/*`

- [ ] Add tests for hidden/veryHidden sheets, chartsheets metadata, dialog/macro sheet retention, custom sheet views, workbook views, calculation chain, calc properties, sheet code names.

- [ ] Implement model fields for safe metadata.

- [ ] Preserve unsupported sheet type parts and workbook relationships, while warning if Freexcel cannot render them.

- [ ] Add regression tests for named ranges scoped to sheets, 3D references, print titles, page breaks, page layout, and pane states.

---

### Task 10: External Links and Connections Metadata

**Files:**
- Create: `src/Freexcel.Core.Model/ExternalLinkModel.cs`
- Modify: `src/Freexcel.Core.Model/Workbook.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [ ] Add tests for preserving `xl/externalLinks/*`, workbook references, and relationship files.

- [ ] Add metadata model for external workbook links: target, sheet names, defined names, package part.

- [ ] Retain link metadata and formulas without recalculating external references.

---

### Task 11: Real Workbook Corpus

**Files:**
- Modify: `test-corpus/manifest.csv`
- Create: `test-corpus/public/README.md`
- Modify: `tests/Freexcel.Core.IO.Tests/XlsxCorpusRunnerTests.cs`
- Modify: `docs/XLSX_TEST_CORPUS_PLAN.md`
- Modify: `docs/XLSX_CORPUS_REPORT.md`

- [ ] Add at least 25 public/open-license XLSX files with source URLs, retrieval dates, and licenses.

- [ ] Add local-private manifest rows for user-supplied Excel torture workbooks.

- [ ] Add per-file expected feature assertions so a workbook cannot silently stop exercising a feature.

- [ ] Add regression bucket for fixed real-world bugs.

---

### Task 12: Final Parity Gate

**Files:**
- Modify: `docs/XLSX_CORPUS_REPORT.md`
- Modify: `docs/FIDELITY_CONTRACT.md`
- Modify: `docs/DECISIONS/003-xlsx-fidelity.md`

- [ ] Run full focused verification:

```powershell
dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj
dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj
dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj
dotnet build Freexcel.slnx
```

- [ ] Launch the WPF app and review native Excel sample open/save flows manually.

- [ ] Report parity as three numbers:
  - generated corpus supported-pass percentage
  - in-scope feature-family percentage
  - real workbook corpus pass percentage

- [ ] Do not claim 95% parity unless real workbook corpus pass rate is at least 95%, generated corpus supported-pass is at least 95%, and all excluded features are retained or warned.
