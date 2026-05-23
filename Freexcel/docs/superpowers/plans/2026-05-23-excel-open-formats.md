# Excel Open Formats Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add open support for common Excel-compatible workbook formats beyond `.xlsx`, harden Excel parity for the implemented formats, and keep `.ods` parked until explicitly resumed.

**Architecture:** Extend the current `IFileAdapter` model with optional open aliases and save capability metadata, keeping existing adapters compatible. Reuse the XLSX load path for Open XML workbook/template formats, add a delimited text adapter for `.txt/.tsv/.tab`, and add a legacy `.xls` adapter backed by a read-only parser dependency.

**Tech Stack:** .NET 10, WPF, ClosedXML, ExcelDataReader for legacy binary `.xls`, xUnit/FluentAssertions.

---

### Task 1: Format Registry And Dialog Planning

**Files:**
- Create: `Freexcel/src/Freexcel.Core.IO/FileFormatDescriptor.cs`
- Create: `Freexcel/src/Freexcel.Core.IO/FileDialogFilterBuilder.cs`
- Modify: `Freexcel/src/Freexcel.Core.IO/IFileAdapter.cs`
- Modify: `Freexcel/src/Freexcel.Core.IO/FileSavePlanner.cs`
- Test: `Freexcel/tests/Freexcel.Core.IO.Tests/FileDialogFilterBuilderTests.cs`
- Test: `Freexcel/tests/Freexcel.Core.IO.Tests/FileSavePlannerTests.cs`

- [x] Write failing tests for open aliases, save-only filtering, and adapter resolution.
- [x] Run `dotnet test Freexcel\tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "FileDialogFilterBuilderTests|FileSavePlannerTests" -p:UseSharedCompilation=false -p:NodeReuse=false` and verify failure.
- [x] Add `FileFormatDescriptor` and default `IFileAdapter.Formats`.
- [x] Add filter builders and update save resolution to use save-capable descriptors.
- [x] Rerun the filtered tests and commit `Add workbook file format registry`.

### Task 2: Modern Open XML Aliases And Template Open Behavior

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.IO/XlsxFileAdapter.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/OpenWorkbookLoader.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.Backstage.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.xaml.cs`
- Test: `Freexcel/tests/Freexcel.App.Host.Tests/OpenWorkbookLoaderTests.cs`
- Test: `Freexcel/tests/Freexcel.App.Host.Tests/MainWindowSourceHygieneTests.cs`

- [x] Write failing tests for `.xlsm/.xltx/.xltm` descriptors and template open metadata.
- [x] Run the focused host tests and verify failure.
- [x] Add `.xlsx/.xlsm/.xltx/.xltm` open descriptors to `XlsxFileAdapter`; keep save limited to `.xlsx`.
- [x] Make template opens clear the current path so Save routes to Save As.
- [x] Update Open/Save dialogs to use `FileDialogFilterBuilder`.
- [x] Rerun focused tests and commit `Open modern Excel workbook variants`.

### Task 3: Delimited Text Open Support

**Files:**
- Create: `Freexcel/src/Freexcel.Core.IO/DelimitedTextFileAdapter.cs`
- Modify: `Freexcel/src/Freexcel.Core.IO/CsvFileAdapter.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/App.xaml.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.DataCommands.cs`
- Test: `Freexcel/tests/Freexcel.Core.IO.Tests/DelimitedTextFileAdapterTests.cs`
- Test: `Freexcel/tests/Freexcel.Integration.Tests/IoRoundTripTests.cs`

- [x] Write failing tests for `.txt/.tsv/.tab` tab-delimited opens and quoted fields.
- [x] Run focused tests and verify failure.
- [x] Extract reusable delimited text parsing and keep CSV behavior unchanged.
- [x] Register tab-delimited text adapters and include them in Get Data.
- [x] Rerun focused tests and commit `Add delimited text workbook open support`.

### Task 4: Legacy `.xls` Read Support

**Files:**
- Modify: `Freexcel/src/Freexcel.Core.IO/Freexcel.Core.IO.csproj`
- Create: `Freexcel/src/Freexcel.Core.IO/LegacyXlsFileAdapter.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/App.xaml.cs`
- Test: `Freexcel/tests/Freexcel.Core.IO.Tests/LegacyXlsFileAdapterTests.cs`

- [x] Write failing tests proving `.xls` is open-only and maps workbook sheets plus basic scalar values.
- [x] Run focused tests and verify failure.
- [x] Add `ExcelDataReader` and `System.Text.Encoding.CodePages`.
- [x] Implement read-only `.xls` mapping and register the adapter.
- [x] Rerun focused tests and solution build, then commit `Add legacy XLS open support`.

### Task 5: Phase 3 `.ods` Research Note

Status: parked by user request while parity/hardening continues for the implemented formats.

**Files:**
- Create: `Freexcel/docs/OPEN_FORMAT_PHASE3_ODS_RESEARCH.md`

- [ ] Research maintained .NET ODS options from primary sources.
- [ ] Document license, maintenance status, read fidelity, deployment impact, and recommendation.
- [ ] Commit `Research ODS open support options`.

### Task 5a: Implemented Format Parity And Hardening

- [x] Name single-sheet text workbooks after the opened source file using Excel-compatible sheet-name rules.
- [x] Honor Excel CSV `sep=` delimiter directives.
- [x] Inspect unsupported package features for `.xlsx/.xlsm/.xltx/.xltm`.
- [x] Coerce imported booleans, numbers, percentages, formulas, error literals, ISO dates, and times in delimited text formats.
- [x] Preserve `DateTimeValue` when saving CSV.
- [x] Preserve legacy `.xls` date cells as `DateTimeValue`.
- [x] Respect Excel's column limit during delimited text import.
- [ ] Continue corpus-driven hardening for Open XML package features and implemented text/legacy formats.

### Task 6: Final Verification And Integration

- [ ] Run focused IO, host, and integration tests.
- [ ] Run `dotnet build Freexcel\Freexcel.slnx -m:1 -p:UseSharedCompilation=false -p:NodeReuse=false`.
- [ ] Merge verified branch into `main`, push `main`, and sync this branch from updated `main`.
