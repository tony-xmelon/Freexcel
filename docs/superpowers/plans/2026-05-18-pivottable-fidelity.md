# PivotTable Fidelity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move PivotTables from a basic single-value sum slice toward Excel-like functional fidelity for existing and authored PivotTables.

**Architecture:** Keep `PivotTableModel` as the source of truth and expand the refresh engine rather than adding a parallel pivot subsystem. Refresh reads source rows, applies page-field filters, groups by all row fields plus the first column field, evaluates all data fields with Excel-style summary functions, writes a static materialized grid, and keeps bound PivotCharts synchronized.

**Tech Stack:** C#/.NET 10, Freexcel.Core.Model, Freexcel.Core.Commands, Freexcel.Core.IO OOXML, xUnit/FluentAssertions.

---

### Task 1: Aggregation Semantics

**Files:**
- Modify: `src/Freexcel.Core.Model/PivotTableModel.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`

- [x] Add failing tests for multiple row fields, multiple data fields, and non-sum summaries (`count`, `average`, `min`, `max`, `product`, `countNums`).
- [x] Add optional selected-item filtering to `PivotFieldModel`.
- [x] Rewrite refresh around reusable grouping and aggregation helpers.
- [x] Keep existing row-only and row/column matrix tests green.

### Task 2: Page Field Filtering

**Files:**
- Modify: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`

- [x] Add failing test for a page field that filters source rows before aggregation.
- [x] Apply all selected page-field filters before grouping.
- [x] Verify PivotChart output-range sync still follows filtered materialized output.

### Task 3: XLSX Metadata For Expanded Fields

**Files:**
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Test: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [x] Add failing save/load smoke test for multiple row fields, page fields, and summary functions.
- [x] Preserve optional page-field selected item metadata when Freexcel authors PivotTables.
- [x] Keep native PivotTable package preservation unchanged for unrelated edits.

### Task 4: App Command Surface

**Files:**
- Modify: `src/Freexcel.App.Host/MainWindow.xaml`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`
- Test: `tests/Freexcel.App.Host.Tests/MainWindowXamlKeyTipTests.cs`

- [x] Replace the deferred PivotTable Insert button with a working creation path for the selected range.
- [x] Add visible Refresh PivotTable command for the active sheet/selection.
- [x] Keep field-list drag/drop and drill-down explicitly deferred in docs.

### Task 5: Docs And Verification

**Files:**
- Modify: `docs/FIDELITY_CONTRACT.md`
- Modify: `docs/XLSX_CORPUS_REPORT.md`
- Modify: `docs/COMMAND_SURFACE_PARITY.md`
- Modify: `docs/NEXT_PHASES_PLAN.md`

- [x] Mark PivotTables as functional for creation, refresh, multiple data fields, common summaries, page filters, and PivotChart sync.
- [x] Run `dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --filter "PivotTableRefresh|PivotTableCommand|PivotChart"`.
- [x] Run `dotnet test tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "PivotTable|PivotChart"`.
- [x] Run full model, IO, host tests and `dotnet build Freexcel.slnx`.

### Task 6: Subtotals, Calculated Fields, And Drill-Down

**Files:**
- Modify: `src/Freexcel.Core.Model/PivotTableModel.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableCommands.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableCommandTests.cs`
- Test: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`
- Test: `tests/Freexcel.App.Host.Tests/MainWindowXamlKeyTipTests.cs`

- [x] Add failing tests for outer row-field subtotals, calculated-field aggregation, and source-row drill-down extraction.
- [x] Add PivotTable model support for subtotal flags and calculated fields.
- [x] Evaluate calculated fields during pivot refresh with arithmetic field-reference formulas.
- [x] Add command-backed Show Details drill-down sheet creation with undo.
- [x] Round-trip authored subtotal and calculated-field pivot metadata through XLSX.
- [x] Add Insert ribbon Show Details entry point.
- [x] Add double-click Show Details gesture before cell edit fallback.
- [x] Run host tests and `dotnet build Freexcel.slnx` after double-click gesture wiring.

### Task 7: Grouping, Filters, And Calculated Items

**Files:**
- Modify: `src/Freexcel.Core.Model/PivotTableModel.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Test: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [x] Add failing tests for multi-select page filters, date grouping, top-N value filters, and calculated items.
- [x] Add model primitives for field grouping, value filters, and calculated items.
- [x] Apply grouping/filter semantics during PivotTable refresh.
- [x] Persist grouping/filter/calculated-item metadata through authored PivotTable XML.
- [x] Run full model, IO, formula, host tests and `dotnet build Freexcel.slnx`.

### Task 8: Number Grouping, Advanced Filters, Sorting, And Layout Command

**Files:**
- Modify: `src/Freexcel.Core.Model/PivotTableModel.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableRefreshService.cs`
- Modify: `src/Freexcel.Core.Commands/PivotTableCommands.cs`
- Modify: `src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableRefreshServiceTests.cs`
- Test: `tests/Freexcel.Core.Model.Tests/PivotTableCommandTests.cs`
- Test: `tests/Freexcel.Core.IO.Tests/FileAdapterSmokeTests.cs`

- [x] Add failing tests for number grouping, label filters, threshold value filters, value sorting, and layout editing.
- [x] Add model primitives for number grouping, label filters, threshold value filters, and sort settings.
- [x] Apply number grouping, label/value filtering, and sort semantics during refresh.
- [x] Add undoable command-level PivotTable field layout editing.
- [x] Persist number grouping, label filters, value thresholds, and sort metadata through authored PivotTable XML.
- [x] Run pivot-focused model/IO tests, full model/IO/host tests, and `dotnet build Freexcel.slnx`.
- [ ] Full formula suite is blocked by unrelated Phase B distribution failures (`KURT`, `GAMMA.DIST`, `BETA.DIST`, `SKEW`, `T.TEST`).
