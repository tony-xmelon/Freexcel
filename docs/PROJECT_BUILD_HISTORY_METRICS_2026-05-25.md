# Project Build History Metrics

Generated: 2026-05-25 23:28 +03:00
Repository: https://github.com/tony-xmelon/Freexcel.git
Baseline ref: origin/main at 3d7cd4527
History window: 2026-05-12 through 2026-05-25

## Scope And Caveats

- Daily build rows are Git numstat churn on origin/main for src, tests, and docs. They answer how much code changed per day.
- Current LOC counts are exact for the checkout at the baseline ref. Historical cumulative LOC requires a longer offline ETL pass over each snapshot and is intentionally not estimated here.
- Token/provider logs exist locally under C:/Users/anton/.codex and C:/Users/anton/.claude/projects/*Freexcel*, but the full token ETL over multi-GB logs did not complete within an interactive run. The report records the source locations and observed session volume rather than inventing incomplete totals.

## Current Repository Footprint

- Registered worktrees: 31
- Local branches: 207
- Remote branches: 61
- Tracked files: 1,710
- Current C# source LOC: 148,320
- Current C# test LOC: 118,465
- Current XAML LOC: 7,330
- Current docs LOC: 25,868
- Observed Codex JSONL sessions/logs: 668
- Observed Claude Freexcel JSONL sessions/logs: 217

## Daily Build Churn

| Date | Commits | Files Changed | Total +/- | Source C# +/- | Test C# +/- | Docs +/- | Git Authors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | 20 | 45 | +6,483 / -121 | +4,349 / -113 | +1,672 / -1 | +180 / -0 | 1 |
| 2026-05-13 | 25 | 1,686 | +55,744 / -40,812 | +8,579 / -2,151 | +2,847 / -418 | +4,633 / -1 | 1 |
| 2026-05-14 | 24 | 50 | +9,000 / -718 | +4,244 / -451 | +1,330 / -0 | +2,432 / -14 | 1 |
| 2026-05-15 | 26 | 169 | +30,180 / -833 | +15,827 / -788 | +7,135 / -10 | +2,927 / -1 | 1 |
| 2026-05-16 | 39 | 195 | +39,767 / -4,570 | +17,290 / -2,854 | +20,324 / -1,390 | +20 / -18 | 1 |
| 2026-05-17 | 32 | 91 | +14,825 / -1,349 | +7,727 / -786 | +3,859 / -246 | +2,375 / -64 | 1 |
| 2026-05-18 | 20 | 74 | +28,356 / -2,154 | +15,762 / -1,342 | +8,712 / -191 | +3,277 / -617 | 1 |
| 2026-05-19 | 675 | 436 | +59,188 / -9,825 | +30,126 / -7,573 | +23,019 / -578 | +4,747 / -1,159 | 1 |
| 2026-05-20 | 528 | 285 | +43,595 / -16,296 | +26,569 / -14,637 | +11,309 / -219 | +2,088 / -792 | 1 |
| 2026-05-21 | 660 | 3,990 | +51,391 / -24,837 | +31,489 / -21,341 | +7,537 / -1,083 | +2,622 / -604 | 1 |
| 2026-05-22 | 339 | 907 | +51,789 / -26,753 | +27,219 / -20,610 | +4,381 / -158 | +662 / -117 | 1 |
| 2026-05-23 | 1,017 | 1,052 | +53,308 / -43,283 | +26,861 / -20,090 | +11,026 / -322 | +1,076 / -308 | 2 |
| 2026-05-24 | 1,189 | 2,056 | +53,355 / -23,258 | +29,261 / -14,614 | +12,078 / -279 | +1,797 / -385 | 1 |
| 2026-05-25 | 534 | 813 | +27,596 / -7,955 | +14,519 / -1,985 | +10,458 / -201 | +1,579 / -235 | 2 |

## Provider Token Usage

| Provider | Local source | Status |
| --- | --- | --- |
| OpenAI / Codex | C:/Users/anton/.codex/sessions and archived_sessions | Source located; full per-day token ETL deferred because logs are multi-GB and timed out interactively. |
| Anthropic / Claude | C:/Users/anton/.claude/projects/*Freexcel* | Source located; full per-day token ETL deferred because logs are multi-GB and timed out interactively. |

## Git Authors Observed

- 2026-05-12: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-13: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-14: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-15: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-16: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-17: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-18: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-19: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-20: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-21: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-22: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-23: Antoni Ivanov <tony.xmelon@gmail.com>; tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-24: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-25: Antoni Ivanov <tony.xmelon@gmail.com>; tony-xmelon <tony.xmelon@gmail.com>

## Reading The Trend

- The project started in Git on 2026-05-12 and has consolidated work through 2026-05-25.
- The daily churn table highlights where implementation volume, tests, and documentation moved together.
- A follow-up offline ETL can turn the located provider logs into exact provider/day token totals without blocking interactive development.
