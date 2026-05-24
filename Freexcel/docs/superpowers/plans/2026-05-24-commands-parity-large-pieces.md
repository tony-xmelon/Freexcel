# Commands Parity Large Pieces Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the remaining large command-parity gaps through testable waves that keep `main` buildable.

**Architecture:** Preserve the current layered boundaries: PDF export and dialogs in `App.Host`, formatting in `Core.Calc`, PivotTable materialization in `Core.Commands`, durable model state in `Core.Model`, and XLSX/package fidelity in `Core.IO`. Each wave narrows one documented parity gap and updates architecture/parity docs before merge.

**Tech Stack:** C# 12, .NET 10, WPF, PDFsharp-WPF, ClosedXML, xUnit, FluentAssertions.

---

### Task 1: PDF Publish Options And Bookmark Modes

**Files:**
- Modify: `Freexcel/src/Freexcel.App.Host/ExportPlanner.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/ExportOptionsDialog.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.PrintExport.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/PdfDocumentExporter.cs`
- Modify: `Freexcel/tests/Freexcel.App.Host.Tests/ExportPlannerTests.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`
- Modify: `Freexcel/docs/COMMAND_SURFACE_PARITY.md`

- [x] **Step 1: Add failing tests for bookmark modes**

Add tests that construct `ExportOptions` with `PdfBookmarkMode.SheetNames`, `PdfBookmarkMode.PrintTitles`, and `PdfBookmarkMode.PageNumbers`, then assert `ExportPlanner.DescribeOptions` names each mode.

- [x] **Step 2: Add the model**

Add `PdfBookmarkMode { None, SheetNames, PrintTitles, PageNumbers }` and replace `bool CreateBookmarks` with `PdfBookmarkMode BookmarkMode`. Preserve compatibility through `ExportOptionsDialog.CreateResult(..., bool createBookmarks)` by mapping `true` to `SheetNames`.

- [x] **Step 3: Generate bookmark captions**

Update `MainWindow.CreatePdfBookmarks` so sheet mode keeps current sheet names, print-title mode uses a sheet print-title summary when available and falls back to sheet name, and page-number mode writes `Page 1`, `Page 2`, etc. after page-range filtering.

- [x] **Step 4: Verify and commit**

Run:

```powershell
dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~ExportPlannerTests" -v minimal
dotnet build Freexcel\Freexcel.slnx --no-restore --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false /nr:false -m:1 -v minimal
```

Commit:

```powershell
git add Freexcel\src\Freexcel.App.Host\ExportPlanner.cs Freexcel\src\Freexcel.App.Host\ExportOptionsDialog.cs Freexcel\src\Freexcel.App.Host\MainWindow.PrintExport.cs Freexcel\src\Freexcel.App.Host\PdfDocumentExporter.cs Freexcel\tests\Freexcel.App.Host.Tests\ExportPlannerTests.cs Freexcel\docs\ARCHITECTURE.md Freexcel\docs\COMMAND_SURFACE_PARITY.md
git commit -m "Expand PDF bookmark publish options"
```

### Task 2: PDF Viewer Publish Options

**Files:**
- Modify: `Freexcel/src/Freexcel.App.Host/ExportPlanner.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/ExportOptionsDialog.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/PdfDocumentExporter.cs`
- Modify: `Freexcel/tests/Freexcel.App.Host.Tests/ExportPlannerTests.cs`

- [x] **Step 1: Add tests for page layout and page mode**

Assert default PDF export uses single-page layout, outline bookmarks set outline mode, and new options can request one-column continuous layout and full-screen mode.

- [x] **Step 2: Add option enums**

Add `PdfInitialView { SinglePage, OneColumn, TwoColumnLeft, TwoColumnRight }` and `PdfOpenMode { Normal, Outlines, FullScreen }` to `ExportPlanner.cs`. Store them on `ExportOptions`.

- [x] **Step 3: Apply viewer preferences**

Update `PdfDocumentExporter` to map initial view to `/PageLayout` and open mode to `/PageMode`, while preserving outline mode when bookmarks are present unless the user explicitly requests full screen.

- [x] **Step 4: Verify and commit**

Run App.Host tests filtered to `PdfDocumentExporter` plus full build, then commit `Add PDF initial view options`.

### Task 3: Selectable PDF Text Overlay Foundation

**Files:**
- Modify: `Freexcel/src/Freexcel.App.Host/PdfDocumentExporter.cs`
- Create: `Freexcel/src/Freexcel.App.Host/PdfTextOverlayExtractor.cs`
- Modify: `Freexcel/tests/Freexcel.App.Host.Tests/ExportPlannerTests.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`

- [ ] **Step 1: Add a test document with a `TextBlock`**

Export a one-page `FixedDocument` with a `TextBlock` and assert the PDF content stream contains the text when vector text overlay is enabled.

- [ ] **Step 2: Add overlay extraction**

Create `PdfTextOverlayExtractor` that walks `FixedPage.Children`, extracts simple `TextBlock` text, margin, font size, and foreground brush, and returns page-relative overlay records.

- [ ] **Step 3: Draw invisible or visible text overlay**

Use PDFsharp text drawing at matching point coordinates after raster draw. Keep raster as visual truth; overlay text should not change page dimensions.

- [ ] **Step 4: Verify and commit**

Run `PdfDocumentExporter` tests and full build, then commit `Add selectable PDF text overlay`.

### Task 4: Accounting Width Formatting

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.Calc/NumberFormatter.cs`
- Modify: `Freexcel/tests/Freexcel.Core.Calc.Tests/NumberFormatterTests.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`
- Modify: `Freexcel/docs/COMMAND_SURFACE_PARITY.md`

- [ ] **Step 1: Add tests for accounting fill alignment**

Add cases for `_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)` that assert positive, negative, and zero outputs keep deterministic symbol, sign, and trailing placeholder spacing.

- [ ] **Step 2: Implement accounting section token interpretation**

Teach `PreserveAccountingFillSpace` to account for `_` skip directives and `*` fill directives as deterministic spaces around currency symbols and zero dashes.

- [ ] **Step 3: Verify and commit**

Run `NumberFormatterTests` and full build, then commit `Improve accounting layout spacing`.

### Task 5: OS-Localized Date/Time Pattern Provider

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.Calc/NumberFormatter.DateTime.cs`
- Create: `Freexcel/src/Freexcel.Core.Calc/DateTimePatternProvider.cs`
- Modify: `Freexcel/tests/Freexcel.Core.Calc.Tests/NumberFormatterTests.cs`

- [ ] **Step 1: Add deterministic provider tests**

Add tests that set a test provider for long date/time patterns and assert `[$-F800]` and `[$-F400]` use the provider rather than hardcoded invariant strings.

- [ ] **Step 2: Add provider seam**

Implement an internal provider with default invariant patterns and a test-only setter guarded by `InternalsVisibleTo`.

- [ ] **Step 3: Verify and commit**

Run `NumberFormatterTests` and full build, then commit `Add date time pattern provider`.

### Task 6: PivotTable Compact/Subtotal Merge Fidelity

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.Commands/PivotTableRefreshService.Writers.cs`
- Modify: `Freexcel/tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`

- [ ] **Step 1: Add compact merge regression**

Test a compact two-row-field PivotTable with `MergeAndCenterLabels = true` and `ShowSubtotals = true`; assert subtotal rows do not break valid outer-label spans and stale merges are cleared on refresh.

- [ ] **Step 2: Refine merge span detection**

Extend `ApplyMergedRowLabels` to treat compact label cells and subtotal captions as explicit span boundaries, using existing `IsPivotSubtotalCaption` and `IsPivotGrandTotalCaption` helpers.

- [ ] **Step 3: Verify and commit**

Run `PivotTableRefreshServiceTests` and full build, then commit `Refine PivotTable compact merges`.

### Task 7: PivotStyle Theme Semantics

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.Commands/PivotStylePaletteResolver.cs`
- Modify: `Freexcel/tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Modify: `Freexcel/src/Freexcel.Core.Model/PivotTableStyleModel.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`

- [ ] **Step 1: Add tests for theme-driven built-in style colors**

Create a workbook theme with changed accent slots and assert a supported PivotStyle resolves header/stripe colors from the theme instead of fixed RGB.

- [ ] **Step 2: Add theme-aware resolver**

Pass `WorkbookTheme` into the resolver and map supported style families to theme slots plus tint values.

- [ ] **Step 3: Verify and commit**

Run PivotTable style tests and full build, then commit `Resolve PivotStyles from workbook theme`.

### Task 8: Native Slicer/Timeline Drawing Fidelity

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.Model/SlicerModel.cs`
- Modify: `Freexcel/src/Freexcel.Core.Model/TimelineModel.cs`
- Modify: `Freexcel/src/Freexcel.Core.IO/XlsxFileAdapter*.cs`
- Modify: `Freexcel/tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Modify: `Freexcel/docs/ARCHITECTURE.md`

- [ ] **Step 1: Add package round-trip tests for anchors**

Extend existing slicer/timeline package fixture tests to assert loaded anchor coordinates and nonvisual shape names are available on `SlicerModel` and `TimelineModel`.

- [ ] **Step 2: Model drawing anchors**

Add nullable anchor records with from/to row/column and EMU offsets. Keep missing anchor data null for authored pane-only slicers/timelines.

- [ ] **Step 3: Load/save modeled anchors**

Update XLSX slicer/timeline drawing readers/writers to populate and preserve modeled anchors. Source-package merge remains best-effort for unsupported drawing children.

- [ ] **Step 4: Verify and commit**

Run the slicer/timeline smoke tests and full build, then commit `Model slicer timeline drawing anchors`.

## Merge Discipline

After each task:

```powershell
git fetch origin
git merge origin/main --no-edit
dotnet build Freexcel\Freexcel.slnx --no-restore --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false /nr:false -m:1 -v minimal
git push origin HEAD:main
git fetch origin
git merge origin/main --no-edit
```

If `main` moves during push, merge `origin/main`, rerun the focused tests for the task, and push again.
