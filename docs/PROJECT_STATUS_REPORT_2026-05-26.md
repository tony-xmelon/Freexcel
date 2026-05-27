# Freexcel Project Status Report

Generated: 2026-05-27  
Mainline observed: `origin/main` at `6adfb7482`  
Report scope: consolidated mainline documentation/status refresh

## Executive Summary

Freexcel remains in late-stage parity hardening. The core product surfaces are broad and functional: formula coverage is documented at **345/345 in-scope functions**, command coverage remains **100% for in-scope commands**, and XLSX fidelity work is focused on deeper retention, corpus regression coverage, and package-health proof rather than first-pass support.

Overall completion estimate: **91-92%**. The remaining work is mostly verification depth, Excel-edge fidelity, release packaging/signing, accessibility review, and coordination across active parallel branches.

Recent May 26 integration work expanded to 144 manifest rows in the XLSX corpus, preserved color-scale `cfvo/@gte` thresholds through XLSX load/save/copy paths, added Scenario Summary result-cell reports with list/range parsing, added unsigned local MSIX packaging to the tester-release workflow, and added a process-scoped UI Automation catalog snapshot harness for visible controls.

## Current Repository Metrics

| Metric | Count |
| --- | ---: |
| Tracked files | 1,885 |
| C# source files under `src/` | 910 |
| C# test files under `tests/` | 371 |
| Markdown docs under `docs/` | 224 |
| Source lines under `src/` | 161,178 |
| Test lines under `tests/` | 141,325 |
| Documentation lines under `docs/` | 26,361 |
| Test methods marked `[Fact]` / `[Theory]` | 6,055 |
| XLSX corpus manifest rows | 144 |

## Current Repository State

| Item | Status |
| --- | --- |
| Mainline | `origin/main` at `6adfb7482` before this docs-branch consolidation merge |
| Branch posture | Parallel feature branches remain active; merge small verified slices into `main` and sync workstreams from `main` frequently |
| Last full build | `dotnet build Freexcel.slnx --no-restore --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false /nr:false -m:1` passed with 0 warnings and 0 errors in the latest captured hardening report |
| Focused doc/corpus/UI guards | Current-doc guard slice passed 35/35; `XlsxCorpusScaffoldTests` passed 5/5 during backlog closeout; UI Automation catalog snapshot slice passed 45/45 |

## Current Parity Snapshot

| Surface | Status |
| --- | --- |
| Formula engine | 345/345 in-scope functions implemented and tested; current work is edge-case parity proof, cached-result fixtures, array coercion, and spill/volatility hardening. |
| Command surface | 100% of in-scope commands covered; partial items are depth/polish gaps. |
| Keyboard shortcuts | **84% parity** (71/85), **16% partial** (14/85), **0 missing**. |
| XLSX fidelity | 71 in-scope feature categories with support; 144 workbook manifest rows; package-preserving save, corpus expansion, and deeper comparisons remain active. |
| UI/dialog parity | Broad coverage; recent additions include advanced data bar options, CF rule manager keyboard UX, broader dialog range-picker/access-key wiring, Scenario Summary result-cell UX, and process-scoped UIA snapshot coverage. |
| Release readiness | `USER_GUIDE.md` and `TROUBLESHOOTING.md` are written; tester-release workflow is JSON-versioned and now builds unsigned local MSIX packages when Windows SDK tooling is available; signing, installer trust validation, accessibility pass, and release-note polish remain open. |

## Active Workstream Picture

Parallel work is active by design. Current worktrees show formula hardening, dialog parity, command parity, XLSX/open-format fidelity, performance, refactor refresh, user-feedback retest, and ribbon/layout polish branches. Treat `origin/main` plus the current docs listed in [README.md](README.md) as the integration baseline; active worktree changes should be considered in-flight until merged and verified.

Operational risk is mostly coordination:

- Keep session branches synced from `main` before editing shared files.
- Merge small verified slices frequently.
- Do not treat a new tester release as available until the workflow completes successfully through restore, build, test, release metadata, artifact upload, and GitHub release publication.
- Keep docs, `release/progress.json`, and release workflow naming aligned whenever the completion band changes.

## Recent Consolidated Updates

| Area | Current state |
| --- | --- |
| Release documentation | `docs/USER_GUIDE.md` and `docs/TROUBLESHOOTING.md` are present and linked from the docs index. |
| Release versioning | `release/progress.json` drives default tester versions. `overallCompletion: 92` maps to the `v0.6.<run>` band; manual `release_version` override remains available. |
| Tester release naming | Releases use `Freexcel (Test Release) vX.Y.Z (yyyy-MM-dd-HH-mm-ss) Run N Attempt M (shortSha)`. |
| XLSX corpus | Manifest baseline is 144 rows, with generated, public, local-private, and regression rows driving package retention and semantic comparison. |
| Current mainline | Expanded range-picker/access-key dialog parity, Quick Analysis keyboard coverage, formula/recalc hardening, XLSX corpus/theme/table metadata/warning coverage, unsigned MSIX release packaging, and UIA catalog snapshot coverage. |
| Planning docs | [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md), [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md), [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md), and this report are the current status set. Older status reports are historical snapshots only. |

## Remaining Outstanding Work

See [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md) for the source-of-truth backlog. Key open items:

1. **XLSX corpus and fidelity proof** - Expand the 144-row corpus baseline; publish pass/fail rate by feature bucket.
2. **Package-preserving XLSX save path** - Broader retention coverage and manual desktop Excel validation.
3. **Release documentation and packaging** - Signing, installer trust validation, release-note workflow polish, and real accessibility pass with keyboard-only and screen-reader validation.
4. **Shortcut and keytip verification** - Continue UI automation coverage beyond the first process-scoped visible-control snapshot, including pixel-perfect keytip overlay placement and future nested submenu keytips beyond Conditional Formatting.
5. **XLSX warning coverage as new gaps are found** - Keep unsupported-feature detection aligned with newly discovered OOXML package parts.

Product parity remaining is tracked in [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md). Current planning and parity sources: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), and [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md).

Product parity notes from the next-phase plan include Phase 7C advanced chart families and Phase 7D: Deeper color-scale XLSX edge semantics as new gaps are found.
