# Freexcel Project Status Report

Generated: 2026-05-19  
Baseline branch: `main` at `a73111ae` (`merge: formula time serial parity`)  
Repository position: `main` is ahead of `origin/main` by 114 commits.

## Executive Summary

Freexcel is in late parity-expansion mode. The core spreadsheet model, command layer, formula engine, XLSX round-trip path, and WPF host are all active, with the largest recent gains in Excel compatibility: paste-special behavior, keyboard parity, formula date/time serial edge cases, workbook/worksheet metadata retention, and host UI planner extraction.

Overall completion estimate: **78%**

This is a working estimate based on implemented surface area, test coverage, active unfinished branches, and remaining integration risk. The project is broadly functional, but not yet release-clean because several workstreams remain active and one agent branch is blocked in unresolved merge conflicts.

## Current Mainline State

| Item | Status |
| --- | --- |
| Mainline branch | `main` |
| Current main commit | `a73111ae` |
| Ahead of origin | 114 commits |
| Latest verified focused suite | Formula tests: 1,390 passed, 0 failed |
| Latest broad suite evidence | Previous broad run after major merges: 3,290 passed, 0 failed |
| Current root checkout | `codex/menutoolbar-responsive-qa`, dirty WIP |

Note: the current working checkout is not `main`; `main` is available in the temporary worktree `E:/Users/anton/AppData/Local/Temp/Freexcel-main-final`.

## Source Code Metrics

Tracked Freexcel files on `main`:

| Metric | Count |
| --- | ---: |
| Total tracked Freexcel files | 547 |
| Total tracked lines | 134,631 |
| C# files | 413 |
| C# lines | 107,433 |
| XAML files | 18 |
| XAML lines | 4,803 |
| Markdown docs | 45 |
| Markdown lines | 13,497 |
| Test method attributes | 2,691 |
| Source C# files | 218 |
| Source C# lines | 63,051 |
| Test C# files | 195 |
| Test C# lines | 44,382 |

Area breakdown:

| Area | Files | Lines |
| --- | ---: | ---: |
| `src/Freexcel.App.Host` | 98 | 22,157 |
| `src/Freexcel.App.UI` | 4 | 4,566 |
| `src/Freexcel.Core.Model` | 28 | 2,628 |
| `src/Freexcel.Core.Commands` | 84 | 14,316 |
| `src/Freexcel.Core.Formula` | 9 | 10,135 |
| `src/Freexcel.Core.Calc` | 5 | 1,577 |
| `src/Freexcel.Core.IO` | 8 | 12,475 |
| `tests` | 195 | 44,389 |

## Active Workstreams

| Workstream | Branch / Worktree | Status | Completion | Notes |
| --- | --- | --- | ---: | --- |
| Mainline consolidation | `main` | Integrated | 92% | Recent merges brought in paste special, host refactors, keyboard parity, XLSX metadata retention, and formula serial parity. Needs push/release hygiene. |
| Menu/toolbar responsive QA | `codex/menutoolbar-responsive-qa` | Active dirty WIP | 75% | Current checkout has edits in ribbon adaptive layout plus screenshot artifacts under `Freexcel/artifacts`. Needs screenshot review, cleanup, targeted host tests, then commit. |
| Command parity autofit | `codex/commands-parity-autofit-fix` | Clean branch, not merged | 90% | Contains `fix: plan autofit sizes per row and column`. Likely ready for targeted verification and merge if not superseded by responsive QA work. |
| XLSX parity loop | `codex/xlsx-parity-loop-2` | Active WIP | 82% | Clean unique commits exist for advanced protection/custom XML metadata; worktree also has a dirty `FileAdapterSmokeTests.cs`. Needs IO test pass after final edits. |
| Host refactor loop | `codex-host-refactor-loop` | Active dirty WIP | 68% | Has planner extraction work plus untracked `ExcelTextEditorPlanner` files. Needs compile/test cleanup before merge. |
| Formula serial parity | `codex/formula-datedif-relative-serials` | Clean / likely patch-equivalent to main | 90% | Worktree is clean; branch no longer appears as unmerged against `main`. Treat as closed unless more DATEDIF cases are planned. |
| Keyboard cross-sheet audit | `codex/keyboard-cross-sheet-audit` | Clean / likely patch-equivalent to main | 90% | Worktree is clean; no unique cherry-pick delta against `main`. Treat as merged or dormant. |
| Home screen UX | `claude/inspiring-hoover-1e0ea7` | Clean dormant worktree | 80% | Older UX branch, not currently showing as an active unmerged blocker. Needs product review before any revival. |
| Agent XLSX/pivot phase | `agents/decent-aphid` | Blocked | 20% | Heavy unresolved merge state: 37 status lines, 20 unresolved conflict entries, plus untracked pivot dialog files. Do not merge until conflict recovery is explicit. |
| Branch topology leftovers | `codex/menutoolbar-alignment`, `codex/menutoolbar-layout-polish`, `codex/commands-parity-closeout-2` | Needs pruning/reconciliation | 95% | These are still listed as not merged by topology, but their useful patches appear largely represented on `main`. Review before deletion. |

## Completion by Area

| Area | Estimated Completion | Current Read |
| --- | ---: | --- |
| Workbook/model fundamentals | 90% | Stable object model with broad command and IO integration. |
| Formula engine | 84% | Strong test volume and active Excel serial parity work; edge cases still being closed. |
| Command parity | 82% | Paste, autofit, formatting, layout, keyboard, and selection commands are moving quickly; a few branch leftovers remain. |
| XLSX fidelity | 78% | Metadata retention and round-trip behavior are much improved; remaining parity loop is still active. |
| WPF host / ribbon UX | 72% | Feature-rich but still in active responsive QA and refactor extraction. |
| Keyboard parity | 78% | Recent active-cell, corner cycling, formula-audit selection work merged; cross-sheet audit appears clean. |
| Documentation / project tracking | 70% | Many parity docs exist, but status consolidation and branch pruning need recurring upkeep. |
| Release readiness | 62% | Test coverage is high, but active dirty worktrees and unresolved conflict branches prevent a clean release posture. |

## Risks and Blockers

1. `agents/decent-aphid` is unsafe to merge until conflicts are resolved or abandoned.
2. Current root checkout is dirty on `codex/menutoolbar-responsive-qa`; do not treat the workspace as clean.
3. Several old branches are not merged by topology even though their work appears superseded. This can confuse status tracking.
4. WPF test/build runs can leave locked processes and screenshot artifacts; cleanup should be part of the QA workflow.
5. `main` is significantly ahead of `origin/main`; remote sync has not happened.

## Recommended Next Steps

1. Finish `codex/menutoolbar-responsive-qa`: review screenshots, remove artifacts, run host tests, commit.
2. Verify and merge `codex/commands-parity-autofit-fix` if its autofit behavior is not already covered by mainline.
3. Finish the dirty XLSX parity loop edits and run `Freexcel.Core.IO.Tests`.
4. Decide whether to recover or abandon `agents/decent-aphid`.
5. Prune or label topology-only stale branches after confirming their patches are on `main`.
6. Push `main` once the active branch cleanup decision is made.
