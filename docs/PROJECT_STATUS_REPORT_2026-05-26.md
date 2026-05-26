# Freexcel Project Status Report

Generated: 2026-05-26  
Branch observed: `codex/next-phases-build` merged with latest `origin/main`
Mainline observed: `origin/main` at `a0185a7a3`

## Executive Summary

Freexcel continues in late-stage parity hardening. Formula coverage is documented at **345/345 in-scope functions**, command surface coverage remains at **100% of in-scope commands**, and XLSX/corpus work continues fidelity proof and edge-case hardening.

Recent session work (2026-05-26):
- **PR #25** - Release documentation: `docs/USER_GUIDE.md` and `docs/TROUBLESHOOTING.md` written and merged.
- **PR #26** - Advanced data bar options exposed in `ConditionalFormatDialog`: five previously model-only properties (`DataBarBorder`, `DataBarAxisPosition`, `DataBarAxisColor`, `DataBarNegativeFillColor`, `DataBarNegativeBorderColor`) are now editable with optional color pickers and axis-position selector. Fixed pre-existing `CommandParityStatusTests` mismatch on the Paste Special row name.
- **PR #27** - CF rule manager UX: `MouseDoubleClick` and `Enter`/`Delete` keyboard shortcuts added to the rules `ListView`, matching Excel's rule manager keyboard behavior.
- **Current mainline hardening** - Dialog/range-picker access-key coverage expanded across data, pivot, page setup, sort/filter, find/replace, and named-range workflows; formula/recalculation range handling continued; XLSX corpus metadata and warning coverage expanded to 124 manifest rows.
- **Backlog guard closeout** - Current planning docs now have automated guards for source links, status-report shortcut/backlog snapshots, conditional-formatting remaining scope, UI catalog counts, worksheet context-menu counts, and corpus manifest baselines.
- **Current session** - Preserved color-scale `cfvo/@gte` thresholds through XLSX load/save/copy paths; added Scenario Summary result-cell reports with list/range parsing; added unsigned local MSIX packaging to the tester-release workflow; and added a process-scoped UI Automation catalog snapshot harness for visible controls.
- **Settings** - Project `.claude/settings.json` created with `PowerShell(*)`, `Bash(dotnet test *)`, `Bash(dotnet build *)`, `Bash(git worktree *)` allowlist entries to reduce permission prompts.

Overall completion estimate: **91-92%**. Most in-scope surfaces are solid; remaining work is advanced fidelity, polish, verification, packaging, and release readiness.

---

## Current Repository State

| Item | Status |
| --- | --- |
| Mainline | `origin/main` at `a0185a7a3` |
| Session branch | `codex/next-phases-build` clean after merging latest `origin/main`; local integrations are ahead pending push |
| Last full build | `dotnet build Freexcel.slnx --no-restore --disable-build-servers -p:UseSharedCompilation=false -p:NodeReuse=false /nr:false -m:1` passed with 0 warnings and 0 errors |
| Focused doc/corpus/UI guards | Current-doc guard slice passed 35/35; `XlsxCorpusScaffoldTests` passed 5/5 during backlog closeout; UI Automation catalog snapshot slice passed 45/45 |

---

## Current Parity Snapshot

| Surface | Status |
| --- | --- |
| Formula engine | 345/345 in-scope functions implemented and tested; current work is edge-case parity proof. |
| Command surface | 100% of in-scope commands covered; partial items are depth/polish gaps. |
| Keyboard shortcuts | **84% parity** (71/85), **16% partial** (14/85), **0 missing**. |
| XLSX fidelity | 71 in-scope feature categories with support; 124 workbook manifest rows; package-preserving save, corpus expansion, and deeper comparisons remain active. |
| UI/dialog parity | Broad coverage; recent additions: advanced data bar options, CF rule manager keyboard UX, broader dialog range-picker/access-key wiring, Scenario Summary result-cell UX, and process-scoped UIA snapshot coverage. |
| Release readiness | `USER_GUIDE.md` and `TROUBLESHOOTING.md` written; tester-release workflow now builds unsigned local MSIX packages when Windows SDK tooling is available; signing, installer trust validation, accessibility pass, and release-note polish remain open. |

---

## Recent Merges (since 2026-05-25 report)

| PR | Summary |
| --- | --- |
| #25 | Release documentation: USER_GUIDE.md and TROUBLESHOOTING.md |
| #26 | Expose advanced data bar options in ConditionalFormatDialog (5 new controls, optional color pickers) |
| #27 | Add double-click and Enter/Delete keyboard shortcuts to CF rule manager list |
| Current mainline | Expanded range-picker/access-key dialog parity, formula/recalc hardening, and XLSX corpus metadata/warning coverage |
| Current session | Preserved color-scale `gte` thresholds, added Scenario Summary result cells and list parsing, added unsigned MSIX release packaging, added UIA catalog snapshot coverage, and synced/merged through `main` |

---

## Remaining Outstanding Work

See [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md) for the current backlog. Parity source references: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md). Key open items:

1. **XLSX corpus and fidelity proof** - Expand the 124-row corpus baseline; publish pass/fail rate by feature bucket.
2. **Package-preserving XLSX save path** - Broader retention coverage and manual desktop Excel validation.
3. **Release documentation and packaging** - Signing, installer trust validation, release-note workflow polish, and real accessibility pass with keyboard-only and screen-reader validation.
4. **Shortcut and keytip verification** - Continue UI automation coverage beyond the first process-scoped visible-control snapshot, including pixel-perfect keytip overlay placement and future nested submenu keytips beyond Conditional Formatting.
5. **XLSX warning coverage as new gaps are found** - Keep unsupported-feature detection aligned with newly discovered OOXML package parts.

Product parity remaining (see [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md)):
- Phase 7C: Advanced chart families (treemap, sunburst, histogram, waterfall, funnel, etc.)
- Phase 7D: Deeper color-scale XLSX edge semantics as new gaps are found
- Data workflow polish (sort/filter dialog UX, forecast chart UX)
- View/window management (multi-window, split pane polish)

Current planning and parity sources: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), and [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md).
