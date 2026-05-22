# Command Priorities 1-5 Fidelity Loop

## Scope

Advance the five user-prioritized Commands parity areas with one bounded, test-backed fidelity slice each:

1. Export to PDF/XPS
2. Custom Number Format / locale fidelity
3. PivotTable
4. PivotChart
5. Tables / Format as Table

Each slice must be developed on an isolated `codex/` branch, verified with focused tests, merged to `main`, pushed, and documented before the next slice starts.

## Slice Plan

### 1. Export to PDF/XPS

- [x] Target the remaining publish-options gap without replacing the existing WPF print-renderer pipeline.
- [x] Prefer planner/exporter behavior that is easy to test without UI automation.
- [x] Update architecture and parity docs to distinguish supported options from still-raster PDF limitations.

### 2. Custom Number Format / Locale Fidelity

- [x] Continue the table-driven locale catalog rather than adding formatter branches.
- [x] Add deterministic coverage for a common LCID or accounting/custom-format behavior that currently falls back to invariant output.
- [x] Keep OS culture independence as an architectural constraint.

### 3. PivotTable

- [x] Improve model-first PivotTable fidelity in command/refresh code rather than adding UI-only state.
- [x] Prefer a slice that affects materialized output or persisted metadata and can be covered by Core.Model/Core.IO tests.
- [x] Keep external/OLAP/data-model pivot execution out of scope.

### 4. PivotChart

- [x] Improve bound PivotChart behavior while preserving the PivotTable connection.
- [x] Prefer modeled chart metadata or field-button/tooling state over decorative UI work.
- [x] Keep full Excel PivotChart Tools layout/design parity out of scope.

### 5. Tables / Format as Table

- [x] Improve structured table behavior through `StructuredTableModel` and commands.
- [x] Prefer totals-row or structured-reference behavior because docs identify it as the most visible remaining gap.
- [x] Keep full Excel table-style theme semantics out of scope for this loop.

## Verification Log

- PDF/XPS quality slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` failed because `ExportQuality` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` passed 47 tests.
- XPS extensionless explicit-format slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "PlanExport_AppendsXpsExtensionForExplicitExtensionlessXpsRequests" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because no explicit-format overload existed.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "ExportPlannerTests" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 49 tests.
- PDF/XPS ignore-print-areas slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "RenderWorksheet_CanIgnoreConfiguredPrintAreaForExport|ExportOptions_DefaultsToActiveSheetWithoutDocumentProperties|ExportOptions_DescribeSelectionAndOpenAfterPublish|ExportOptionsDialog_CreateResult_NormalizesExcelOptions|ExportOptionsDialog_ExposesKeyboardAccessKeys|ExportOptionsDialog_ExposesOnlyHonoredPdfXpsChoices" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v normal` failed because `IgnorePrintAreas` and `ignorePrintArea` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "RenderWorksheet_CanIgnoreConfiguredPrintAreaForExport|ExportOptions_DefaultsToActiveSheetWithoutDocumentProperties|ExportOptions_DescribeSelectionAndOpenAfterPublish|ExportOptionsDialog_CreateResult_NormalizesExcelOptions|ExportOptionsDialog_ExposesKeyboardAccessKeys|ExportOptionsDialog_ExposesOnlyHonoredPdfXpsChoices" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 6 tests.
- PDF sheet-name bookmarks slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "ExportOptions_DescribeSelectionAndOpenAfterPublish|ExportOptionsDialog_CreateResult_NormalizesExcelOptions|ExportOptionsDialog_ExposesKeyboardAccessKeys|PdfDocumentExporter_WritesRequestedBookmarksAndFiltersThemToPageRange" -v minimal` failed because `CreateBookmarks`, `PdfBookmark`, and the PDF exporter bookmark overload did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "ExportOptions_DescribeSelectionAndOpenAfterPublish|ExportOptionsDialog_CreateResult_NormalizesExcelOptions|ExportOptionsDialog_ExposesKeyboardAccessKeys|PdfDocumentExporter_WritesRequestedBookmarksAndFiltersThemToPageRange" -v minimal` passed 4 tests.
- Custom-number East Asian LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcid" --logger "console;verbosity=detailed"` failed for Korean `412` date separators before catalog support.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcid" -v minimal` passed 39 tests.
- Custom-number Latin American Spanish LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed for Latin American Spanish LCIDs that still used invariant separators.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 55 tests.
- Custom-number Indian grouping slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `[$₹-4009]#,##0.00` rendered Western grouping as `₹1,234,567.89`.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 45 tests.
- Custom-number French Canada / Commonwealth LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` failed because `C0C` and `1C09` still rendered with invariant separators.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 63 tests.
- Custom-number native Indian LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` failed because `439`, `445`, `449`, `44A`, and `44E` used Western grouping and invariant date separators.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 71 tests.
- Custom-number Middle East / Southeast Asia LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` reported failing Vietnam `42A` and Indonesia `421` separator expectations before timing out.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 81 tests.
- Custom-number Balkan/Baltic LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` failed 19 cases for missing `402`, `408`, `418`, `41A`, `41B`, `424`, `425`, `426`, `427`, and `241A` separator mappings.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 101 tests.
- Custom-number Arabic/Persian LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` failed for Persian `429` decimal slash, Pashto `463` separators, and Moroccan Arabic `1801` date hyphen.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 117 tests.
- Custom-number African LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` failed for Afrikaans/Xhosa grouping, French Morocco/Senegal separators, and Afrikaans date hyphen.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators|CustomNumberSubset_UsesKnownLcidDateSeparatorsForDateValues" -v minimal` passed 137 tests.
- PivotTable empty-value display slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests.Refresh_MatrixUsesEmptyValueTextForMissingIntersections" -v minimal` failed because `PivotTableModel.EmptyValueText` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests|FullyQualifiedName~PivotTableCommandTests" -v minimal` passed 99 tests.
- PivotTable style gallery fidelity slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableOptionsDialog_ExposesBroaderPivotStyleGalleryAndPreservesCurrentStyle" -v normal` failed because only four style names were available and `PivotStyleMedium10`/`PivotStyleDark7` were missing.
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests.Refresh_MapsAdditionalBuiltInPivotStyleFamilies" -v minimal` failed because `PivotStyleMedium2` rendered as the generic medium fallback.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableOptionsDialog_ExposesBroaderPivotStyleGalleryAndPreservesCurrentStyle" -v minimal` passed 1 test.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests.Refresh_MapsAdditionalBuiltInPivotStyleFamilies" -v minimal` passed 5 tests.
- PivotChart field-button visibility slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ChartRendererTests.PivotChartRenderer_HidesIndividualFieldButtonAnnotations|FullyQualifiedName~ChartRendererTests.GridView_DoesNotHitTestIndividuallyHiddenPivotChartFieldButtons" -v minimal` failed because `ChartModel.ShowPivotChartValueFieldButtons` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ChartRendererTests" -v minimal` passed 62 tests.
- PivotChart Native JSON option persistence slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "NativeJsonAdapter_RoundTrip_PivotChartOptions" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because PivotChart flags loaded as default non-PivotChart values.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "NativeJsonAdapter_RoundTrip_PivotChartOptions" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
- Native JSON chart design metadata slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "NativeJsonAdapter_RoundTrip_ChartDesignMetadata" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `PivotFormatsXml` and related design metadata were not loaded.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.IO.Tests\Freexcel.Core.IO.Tests.csproj --filter "NativeJsonAdapter_RoundTrip_ChartDesignMetadata" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
- Table totals-row refresh slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~StructuredTableCommandTests.RefreshStructuredTableTotalsCommand_MaterializesLabelsAndCommonFunctionsWithUndo" -v minimal` failed because `RefreshStructuredTableTotalsCommand` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~StructuredTableCommandTests" -v minimal` passed 10 tests.
- Structured-reference formula evaluation slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter StructuredReferenceFormulaTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `Sales[Amount]` stopped at an unexpected `[` token.
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter StructuredReferenceDependencyTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` also initially hit a compiler output-file lock when run concurrently with the formula red test; subsequent verification is run sequentially.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter StructuredReferenceFormulaTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 2 tests.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter StructuredReferenceDependencyTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
- Structured-reference selector slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter StructuredReferenceFormulaTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `#Headers`, `#Data`, and `#All` selectors resolved as unknown column names.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter StructuredReferenceFormulaTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 5 tests after a transient `csc.exe -1` rerun with build servers shut down.
- Combined structured-reference selector slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter StructuredReferenceFormulaTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because nested `[[#Section],[Column]]` references stopped at the first inner closing bracket.
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter Serialize_CombinedStructuredReference --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because serialization over-escaped nested structured-reference brackets.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter "StructuredReferenceFormulaTests|Serialize_CombinedStructuredReference" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 10 tests after clearing a transient blank compiler-server failure.
- Current-row structured-reference slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter StructuredReferenceCurrentRowTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `[@Amount]` evaluated as `#VALUE!`.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter StructuredReferenceCurrentRowTests --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter "Serialize_CurrentRowStructuredReference|Serialize_TableQualifiedCurrentRowStructuredReference" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 2 tests.
- Multi-column structured-reference slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter MultiColumnStructuredReference_ResolvesColumnRange --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v normal` failed because multi-column selectors returned `#NAME?`.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Formula.Tests\Freexcel.Core.Formula.Tests.csproj --filter "MultiColumnStructuredReference_ResolvesColumnRange|Serialize_MultiColumnStructuredReference" --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 4 tests.
- `#This Row` structured-reference slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter Recalculate_ThisRowStructuredReference_UsesFormulaCellTableRow --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because `Sales[[#This Row],[Amount]:[Tax]]` returned `#NAME?`.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter Recalculate_ThisRowStructuredReference_UsesFormulaCellTableRow --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
- Unqualified `#This Row` structured-reference slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter Recalculate_UnqualifiedThisRowStructuredReference_UsesContainingTableRow --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` failed because standalone `[[#This Row],[Amount]:[Tax]]` parsed to `#VALUE!`.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter Recalculate_UnqualifiedThisRowStructuredReference_UsesContainingTableRow --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 -v minimal` passed 1 test.
