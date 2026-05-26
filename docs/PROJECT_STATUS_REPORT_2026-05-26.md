# Freexcel Project Status Report

Generated: 2026-05-26  
Mainline observed: `origin/main` at `4a627a598`
Report branch: `codex/docs-status-refresh`

## Executive Summary

Freexcel remains in late-stage parity hardening. The core product surfaces are broad and functional: formula coverage is documented at **345/345 in-scope functions**, command coverage remains **100% for in-scope commands**, and XLSX fidelity work is focused on deeper retention, corpus regression coverage, and package-health proof rather than first-pass support.

Overall completion estimate: **91-92%**. The remaining work is mostly verification depth, Excel-edge fidelity, release packaging, accessibility review, and coordination across active parallel branches.

The tester-release workflow dispatch API recovered after the GitHub Actions incident, but the latest validation run failed before publish because `Freexcel.Core.IO.Tests.XlsxCorpusRunnerTests` found two corpus regressions on `main`: hidden-row drift in `generated-structured-tables-001` and relationship-target normalization differences for `public-tealeg-chartsheet`. No release artifact was created from that failed run.

## Current Repository Metrics

| Metric | Count |
| --- | ---: |
| Tracked files | 1,771 |
| C# source files under `src/` | 819 |
| C# test files under `tests/` | 347 |
| Markdown docs under `docs/` | 195 |
| Workflow files | 1 |
| Release metadata files | 1 |
| Source lines under `src/` | 134,197 |
| Test lines under `tests/` | 109,167 |
| Documentation lines under `docs/` | 14,734 |
| Test methods marked `[Fact]` / `[Theory]` | 5,585 |
| XLSX corpus manifest rows | 119 |

## Current Parity Snapshot

| Surface | Status |
| --- | --- |
| Formula engine | 345/345 in-scope functions implemented and tested; current work is edge-case parity, cached-result fixtures, array coercion, and spill/volatility hardening. |
| Command surface | 100% of in-scope commands covered; partial rows are depth or polish gaps rather than absent command entry points. |
| Keyboard shortcuts | 84% parity (71/85), 16% partial (14/85), 0 missing. |
| XLSX fidelity | 119-row manifest baseline; generated, public, local-private, and regression rows drive package retention and semantic comparison. The most recent tester-release validation before this refresh exposed Core.IO corpus regressions; rerun after the active corpus fixes land. |
| UI/dialog parity | Broad coverage with ongoing polish in dialog focus/access keys, range pickers, ribbon overflow, print preview, filter menus, and advanced chart/dialog surfaces. |
| Release readiness | User guide and troubleshooting docs exist; tester release workflow is automated and JSON-versioned; MSIX automation, release notes workflow, accessibility pass, and green tester-release validation remain open. |

## Active Workstream Picture

Parallel work is active by design. Current worktrees show formula hardening, dialog parity, command parity, XLSX/open-format fidelity, performance, refactor refresh, user-feedback retest, and ribbon/layout polish branches. Treat `origin/main` plus the current docs listed in [README.md](README.md) as the integration baseline; active worktree changes should be considered in-flight until merged and verified.

Operational risk is mostly coordination:

- Keep session branches synced from `main` before editing shared files.
- Merge small verified slices frequently.
- Avoid claiming release readiness while tester-release fails in the Core.IO corpus test step.
- Keep docs, `release/progress.json`, and release workflow naming aligned whenever the completion band changes.

## Recent Consolidated Updates

| Area | Current state |
| --- | --- |
| Release versioning | `release/progress.json` drives default tester versions. `overallCompletion: 92` maps to the `v0.6.<run>` band; manual `release_version` override remains available. |
| Tester release naming | Releases use `Freexcel (Test Release) vX.Y.Z (yyyy-MM-dd-HH-mm-ss) Run N Attempt M (shortSha)`. |
| XLSX corpus | Manifest baseline is 119 rows. Recent failures are now tracked as release blockers rather than documentation drift. |
| Planning docs | [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md), [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md), [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md), and this report are the current status set. Older status reports are historical snapshots only. |

## Remaining Outstanding Work

See [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md) for the source-of-truth backlog. Key open items:

1. **XLSX corpus and fidelity proof**
2. **Package-preserving XLSX save path**
3. **Release documentation and packaging**
4. **Shortcut and keytip verification**
5. **XLSX warning coverage as new gaps are found**

Product parity remaining is tracked in [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md). Current planning and parity sources: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), and [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md).

Product parity notes from the next-phase plan include Phase 7C advanced chart families and Phase 7D: Deeper color-scale XLSX edge semantics as new gaps are found.
