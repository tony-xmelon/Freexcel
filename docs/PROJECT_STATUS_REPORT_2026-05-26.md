# Freexcel Project Status Report

Generated: 2026-05-26  
Branch observed: `main`  
Mainline observed: `origin/main` at `a0ba0e4ac`

## Executive Summary

Freexcel continues in late-stage parity hardening. Formula coverage is documented at **345/345 in-scope functions**, command surface coverage remains at **100% of in-scope commands**, and XLSX/corpus work continues fidelity proof and edge-case hardening.

Recent session work (2026-05-26):
- **PR #25** – Release documentation: `docs/USER_GUIDE.md` and `docs/TROUBLESHOOTING.md` written and merged.
- **PR #26** – Advanced data bar options exposed in `ConditionalFormatDialog`: five previously model-only properties (`DataBarBorder`, `DataBarAxisPosition`, `DataBarAxisColor`, `DataBarNegativeFillColor`, `DataBarNegativeBorderColor`) are now editable with optional color pickers and axis-position selector. Fixed pre-existing `CommandParityStatusTests` mismatch on the Paste Special row name.
- **PR #27** – CF rule manager UX: `MouseDoubleClick` and `Enter`/`Delete` keyboard shortcuts added to the rules `ListView`, matching Excel's rule manager keyboard behavior.
- **Settings** – Project `.claude/settings.json` created with `PowerShell(*)`, `Bash(dotnet test *)`, `Bash(dotnet build *)`, `Bash(git worktree *)` allowlist entries to reduce permission prompts.

Overall completion estimate: **91–92%**. Most in-scope surfaces are solid; remaining work is advanced fidelity, polish, verification, packaging, and release readiness.

---

## Current Repository State

| Item | Status |
| --- | --- |
| Mainline | `origin/main` at `a0ba0e4ac` |
| App.Host test count | 2,786 passing |
| Core.Model test count | 1,181 passing |

---

## Current Parity Snapshot

| Surface | Status |
| --- | --- |
| Formula engine | 345/345 in-scope functions implemented and tested; current work is edge-case parity proof. |
| Command surface | 100% of in-scope commands covered; partial items are depth/polish gaps. |
| Keyboard shortcuts | **84% parity** (71/85), **16% partial** (14/85), **0 missing**. |
| XLSX fidelity | 71 in-scope feature categories with support; package-preserving save, corpus expansion, and deeper comparisons remain active. |
| UI/dialog parity | Broad coverage; recent additions: advanced data bar options, CF rule manager keyboard UX. |
| Release readiness | `USER_GUIDE.md` and `TROUBLESHOOTING.md` written; MSIX release automation and accessibility pass remain open. |

---

## Recent Merges (since 2026-05-25 report)

| PR | Summary |
| --- | --- |
| #25 | Release documentation: USER_GUIDE.md and TROUBLESHOOTING.md |
| #26 | Expose advanced data bar options in ConditionalFormatDialog (5 new controls, optional color pickers) |
| #27 | Add double-click and Enter/Delete keyboard shortcuts to CF rule manager list |

---

## Remaining Outstanding Work

See [OUTSTANDING_BUILD.md](OUTSTANDING_BUILD.md) for the current backlog. Parity source references: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md). Key open items:

1. **XLSX corpus and fidelity proof** – Expand the 101-row corpus baseline; publish pass/fail rate by feature bucket.
2. **Package-preserving XLSX save** – Broader retention coverage and manual desktop Excel validation.
3. **Release packaging** – MSIX release automation; real accessibility pass with keyboard-only and screen-reader validation.
4. **Shortcut and keytip verification** – Pixel-perfect keytip overlay placement; future nested submenu keytips beyond Conditional Formatting.
5. **XLSX warning coverage** – Keep unsupported-feature detection aligned with newly discovered OOXML package parts.

Product parity remaining (see [NEXT_PHASES_PLAN.md](NEXT_PHASES_PLAN.md)):
- Phase 7C: Advanced chart families (treemap, sunburst, histogram, waterfall, funnel, etc.)
- Phase 7D: Remaining CF hardening beyond data bar/color scale advanced options
- Data workflow polish (sort/filter dialog UX, forecast chart UX)
- View/window management (multi-window, split pane polish)

Current planning and parity sources: [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md), [MENU_TOOLBAR_PARITY.md](MENU_TOOLBAR_PARITY.md), [SHORTCUT_PARITY_MATRIX.md](SHORTCUT_PARITY_MATRIX.md), [FIDELITY_CONTRACT.md](FIDELITY_CONTRACT.md), and [XLSX_CORPUS_REPORT.md](XLSX_CORPUS_REPORT.md).
