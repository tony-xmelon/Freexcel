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

- Improve structured table behavior through `StructuredTableModel` and commands.
- Prefer totals-row or structured-reference behavior because docs identify it as the most visible remaining gap.
- Keep full Excel table-style theme semantics out of scope for this loop.

## Verification Log

- PDF/XPS quality slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` failed because `ExportQuality` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` passed 47 tests.
- Custom-number East Asian LCID slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcid" --logger "console;verbosity=detailed"` failed for Korean `412` date separators before catalog support.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcid" -v minimal` passed 39 tests.
- PivotTable empty-value display slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests.Refresh_MatrixUsesEmptyValueTextForMissingIntersections" -v minimal` failed because `PivotTableModel.EmptyValueText` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~PivotTableRefreshServiceTests|FullyQualifiedName~PivotTableCommandTests" -v minimal` passed 99 tests.
- PivotChart field-button visibility slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ChartRendererTests.PivotChartRenderer_HidesIndividualFieldButtonAnnotations|FullyQualifiedName~ChartRendererTests.GridView_DoesNotHitTestIndividuallyHiddenPivotChartFieldButtons" -v minimal` failed because `ChartModel.ShowPivotChartValueFieldButtons` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ChartRendererTests" -v minimal` passed 62 tests.
