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

- Continue the table-driven locale catalog rather than adding formatter branches.
- Add deterministic coverage for a common LCID or accounting/custom-format behavior that currently falls back to invariant output.
- Keep OS culture independence as an architectural constraint.

### 3. PivotTable

- Improve model-first PivotTable fidelity in command/refresh code rather than adding UI-only state.
- Prefer a slice that affects materialized output or persisted metadata and can be covered by Core.Model/Core.IO tests.
- Keep external/OLAP/data-model pivot execution out of scope.

### 4. PivotChart

- Improve bound PivotChart behavior while preserving the PivotTable connection.
- Prefer modeled chart metadata or field-button/tooling state over decorative UI work.
- Keep full Excel PivotChart Tools layout/design parity out of scope.

### 5. Tables / Format as Table

- Improve structured table behavior through `StructuredTableModel` and commands.
- Prefer totals-row or structured-reference behavior because docs identify it as the most visible remaining gap.
- Keep full Excel table-style theme semantics out of scope for this loop.

## Verification Log

- PDF/XPS quality slice:
  - Red: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` failed because `ExportQuality` did not exist.
  - Green: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter "FullyQualifiedName~ExportPlannerTests" -v minimal` passed 47 tests.
