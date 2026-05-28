# Freexcel Project Status Report

Generated: 2026-05-28
Observed at: 2026-05-28T09:22:13+03:00
Report scope: status/completion refresh plus build/docs/test-health verification after project history metrics were updated through 2026-05-27 inclusive
Mainline observed: branch-neutral `origin/main` snapshot; worker-specific branch and worktree names are intentionally omitted from this status report

## Executive Summary

Freexcel remains in late-stage parity hardening. Core product surfaces are broad and functional: formula coverage remains **345/345 in-scope functions**, command coverage remains **100% for in-scope commands**, and XLSX fidelity work is focused on deeper corpus proof, package-retention validation, and Excel-edge semantics rather than first-pass support.

Overall completion estimate is now **93%**. The remaining work is verification depth, Excel-edge XLSX fidelity, release signing/trust validation, accessibility review, and coordination across many parallel branches and worktrees.

The project history metrics report now covers Git and provider-log activity from 2026-05-12 through 2026-05-27 inclusive. Through May 27, the Git churn table records **8,941 commits**, **10,545 distinct changed files**, **+1,260,269 / -880,246 LoC**, and local provider logs attribute **26,271,086,950 observed tokens** across OpenAI/Codex and Anthropic/Claude rows.

## Current Repository Metrics

| Metric | Count |
| --- | ---: |
| Tracked files | 1,980 |
| C# source files under `src/` | 948 |
| C# test files under `tests/` | 424 |
| Markdown docs under `docs/` | 228 |
| XLSX corpus manifest rows | 144 |

## Current Repository State

| Item | Status |
| --- | --- |
| Mainline | Current status is anchored to `origin/main`; local session branches and checkouts are treated as worker-owned implementation detail |
| Completion tracking | `release/progress.json` is updated to `overallCompletion: 93`, mapping tester builds to the `v0.7.<run>` stream |
| History metrics | [PROJECT_BUILD_HISTORY_METRICS.md](PROJECT_BUILD_HISTORY_METRICS.md) is refreshed through 2026-05-27 inclusive |
| Branch posture | Parallel feature branches remain active; sync and merge frequently because branch and worktree counts are intentionally fluid |
| Worktree posture | Active worktrees are session-owned; dirty active-session work is intentionally not treated as cleanup material |
| Release posture | Tester-release automation is JSON-versioned and can produce unsigned local MSIX packages; signing, trust validation, accessibility validation, and release-note polish remain open |

## Current Parity Snapshot

| Surface | Status |
| --- | --- |
| Formula engine | 345/345 in-scope functions implemented and tested; active work is edge-case parity proof, cached-result fixtures, array coercion, volatility, and spill semantics. |
| Command surface | 100% of in-scope commands covered; remaining items are depth/polish gaps rather than absent command entry points. |
| Keyboard shortcuts | **84% parity** (71/85), **16% partial** (14/85), **0 missing**. |
| XLSX fidelity | 71 in-scope feature categories with support; 144 workbook manifest rows; package-preserving save, corpus expansion, and deeper comparisons remain active. |
| UI/dialog parity | Broad coverage with continuing polish in dialog access keys, focus/default states, chart/dialog surfaces, range pickers, ribbon/keytips, and context-menu keyboard behavior. |
| Release readiness | User guide and troubleshooting docs are present; unsigned MSIX workflow exists; signing, installer trust, accessibility pass, and release-note workflow remain. |

## Active Workstream Picture

Parallel work is active by design. Current workstreams still include chart-family work, dialog parity, command parity, XLSX/open-format fidelity, performance, refactor refresh, ribbon/layout polish, UIA/keytip guards, and feedback retest slices.

Operational risk remains mostly coordination:

- Keep session branches synced from `main` before editing shared files.
- Merge small verified slices frequently.
- Treat dirty worktrees as active session-owned work.
- Keep docs, `release/progress.json`, and tester-release naming aligned whenever the completion band changes.
- Keep the build-history token table bounded to completed local-date windows; this report intentionally summarizes through 2026-05-27 inclusive.

## Code Review Hardening — 2026-05-28

A comprehensive architectural review of the full 1,166-file source completed today, resolving 17 prioritised findings across 12 PRs (#33–#44). All items are merged to `main`.

| Priority | Item | PR |
|---|---|---|
| P0 | `CellStyle` equality includes all `NativeDifferential*` fields (registry collision fix) | #33 |
| P0 | `NativeJsonAdapter` static options, compact JSON, SHA-256 password hashing | #34 |
| P0 | `XlsxFileAdapter` load failures surface as warnings instead of silent `Debug.WriteLine` | #35 |
| P1 | GridView brush/pen/typeface caches promoted to class-level fields (no per-frame alloc) | #36 |
| P1 | `CommandBus.Undo`/`Redo` guard `Revert`/`Apply` with try/catch + rollback | #37 |
| P1 | `FormulaEvaluator` 256-depth limit returns `#NUM!` instead of stack overflow | #38 |
| P1 | `GetStyle` returns registered `CellStyle` directly (no defensive clone) | #39 |
| P2 | Hyperlink URI scheme whitelist blocks `javascript:`, `data:`, `vbscript:` | #40 |
| P2 | `IUserMessageService` replaces ~55 `MessageBox.Show` calls in `MainWindow` | #41 |
| P3 | `OpenWorkbookLoader` passes `FileStream` directly — halves peak XLSX load memory | #42 |
| P3 | Undo stack gains 50 MB byte-budget eviction via `IEstimatesMemory` | #43 |
| P3 | 12 `WorksheetXxxMetadataModel` classes consolidated into `NativeXmlPreserveBag` | #44 |

See [CODE_REVIEW_COMPREHENSIVE_2026-05-28.md](CODE_REVIEW_COMPREHENSIVE_2026-05-28.md) for the full findings document and [DECISIONS/008-code-review-hardening-2026-05-28.md](DECISIONS/008-code-review-hardening-2026-05-28.md) for the ADR.

---

## Remaining Outstanding Work

See [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md) for the source-of-truth backlog. Key open items:

1. **XLSX corpus and fidelity proof** - Expand the 144-row corpus baseline; publish pass/fail rate by feature bucket.
2. **Package-preserving XLSX save path** - Broader retention coverage and manual desktop Excel validation.
3. **Release documentation and packaging** - Signing, installer trust validation, release-note workflow polish, and real accessibility pass with keyboard-only and screen-reader validation.
4. **Shortcut and keytip verification** - Continue UI automation coverage beyond the first process-scoped visible-control snapshot, including pixel-perfect keytip overlay placement and future nested submenu keytips beyond Conditional Formatting.
5. **XLSX warning coverage as new gaps are found** - Keep unsupported-feature detection aligned with newly discovered OOXML package parts.

Product parity remaining is tracked in [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md), including Phase 7D: Deeper color-scale XLSX edge semantics as new gaps are found. Current planning, parity, and release-readiness sources: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md), and [TEST_DISTRIBUTION_PLAN.md](TEST_DISTRIBUTION_PLAN.md).
