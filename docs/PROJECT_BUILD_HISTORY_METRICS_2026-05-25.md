# Project Build History Metrics

Generated: 2026-05-26 09:43 +03:00
Repository: https://github.com/tony-xmelon/Freexcel.git
Baseline ref: origin/main at 19cbfe3b1
History window: 2026-05-12 through 2026-05-26

## Scope And Caveats

- Daily build rows are Git numstat churn on origin/main for src, tests, and docs. They answer how much code changed per day.
- Current LOC counts are exact for the checkout at the baseline ref. Historical cumulative LOC requires a longer offline ETL pass over each snapshot and is intentionally not estimated here.
- Token/provider rows were processed asynchronously by subagents from local Codex and Claude JSONL logs. Bytes are attributed log-file bytes reported by those extraction passes; token counts are observed local usage, not provider invoices.

## Current Repository Footprint

- Registered worktrees: 32
- Local branches: 209
- Remote branches: 62
- Tracked files: 1,711
- Current C# source LOC: 149,160
- Current C# test LOC: 119,395
- Current XAML LOC: 7,330
- Current docs LOC: 25,947
- Observed Codex JSONL sessions/logs: 711
- Observed Claude Freexcel JSONL sessions/logs: 217
- Provider log bytes attributed: 9,994,848,060
- Observed provider tokens: 15,710,023,110

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
| 2026-05-25 | 555 | 820 | +28,219 / -8,009 | +14,874 / -2,030 | +10,719 / -203 | +1,585 / -241 | 2 |
| 2026-05-26 | 20 | 28 | +1,279 / -73 | +572 / -42 | +682 / -11 | +25 / -20 | 1 |
| TOTAL | 5,169 | 11,884 | +526,479 / -202,891 | +260,749 / -109,422 | +126,630 / -5,109 | +30,446 / -4,341 | 2 |

## Daily Provider Token Usage

| Date | Provider | Sessions | Events | Bytes | Input | Cached Input | Cache Create | Cache Read | Output | Reasoning | Total Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | anthropic | 3 | 825 | 58,815,510 | 5,620 | 0 | 2,140,167 | 47,961,493 | 311,298 | 0 | 50,418,578 |
| 2026-05-13 | anthropic | 2 | 913 | 53,106,715 | 7,910 | 0 | 2,643,687 | 82,409,107 | 568,872 | 0 | 85,629,576 |
| 2026-05-14 | anthropic | 1 | 1,252 | 55,316,387 | 2,221 | 0 | 3,319,694 | 79,705,419 | 649,395 | 0 | 83,676,729 |
| 2026-05-14 | openai | 5 | 2,455 | 333,686,363 | 350,359,915 | 342,572,416 | 0 | 0 | 723,590 | 103,002 | 351,969,217 |
| 2026-05-15 | anthropic | 1 | 1,015 | 53,067,454 | 7,258 | 0 | 2,519,006 | 77,512,578 | 490,807 | 0 | 80,529,649 |
| 2026-05-15 | openai | 1 | 4,634 | 253,765,745 | 677,855,226 | 664,721,024 | 0 | 0 | 1,528,147 | 189,092 | 680,000,428 |
| 2026-05-16 | anthropic | 1 | 1,917 | 62,974,756 | 35,764 | 0 | 5,928,091 | 165,546,623 | 620,539 | 0 | 172,131,017 |
| 2026-05-16 | openai | 1 | 5,210 | 253,765,745 | 745,787,637 | 729,714,176 | 0 | 0 | 1,795,045 | 195,447 | 748,470,731 |
| 2026-05-17 | anthropic | 1 | 1,896 | 62,243,799 | 24,974 | 0 | 4,819,538 | 169,114,482 | 387,446 | 0 | 174,346,440 |
| 2026-05-17 | openai | 3 | 1,527 | 506,039,662 | 211,506,691 | 203,821,312 | 0 | 0 | 478,997 | 82,227 | 212,234,814 |
| 2026-05-18 | anthropic | 1 | 632 | 52,732,128 | 797 | 0 | 1,707,637 | 62,530,805 | 222,563 | 0 | 64,461,802 |
| 2026-05-18 | openai | 2 | 2,290 | 331,774,344 | 332,264,534 | 323,709,440 | 0 | 0 | 776,001 | 120,695 | 333,542,369 |
| 2026-05-19 | openai | 232 | 16,885 | 1,009,773,653 | 2,029,998,455 | 1,955,995,648 | 0 | 0 | 5,291,441 | 1,097,021 | 2,037,165,415 |
| 2026-05-20 | anthropic | 1 | 288 | 78,931,870 | 318 | 0 | 607,434 | 30,833,430 | 246,268 | 0 | 31,687,450 |
| 2026-05-20 | openai | 66 | 11,413 | 902,975,142 | 1,558,217,251 | 1,512,642,688 | 0 | 0 | 3,292,058 | 609,622 | 1,563,040,464 |
| 2026-05-21 | anthropic | 1 | 498 | 79,181,886 | 3,335 | 0 | 1,710,588 | 42,555,886 | 612,404 | 0 | 44,882,213 |
| 2026-05-21 | openai | 84 | 8,591 | 873,453,465 | 1,073,459,207 | 1,041,576,704 | 0 | 0 | 2,629,146 | 449,246 | 1,077,130,124 |
| 2026-05-22 | anthropic | 1 | 355 | 78,931,870 | 5,919 | 0 | 2,254,631 | 29,535,973 | 475,066 | 0 | 32,271,589 |
| 2026-05-22 | openai | 41 | 4,614 | 929,940,935 | 612,749,280 | 592,425,216 | 0 | 0 | 1,314,394 | 241,141 | 614,852,091 |
| 2026-05-23 | anthropic | 1 | 893 | 78,931,870 | 2,802 | 0 | 1,650,663 | 95,440,901 | 559,218 | 0 | 97,653,584 |
| 2026-05-23 | openai | 85 | 21,638 | 1,000,405,458 | 2,984,327,421 | 2,908,088,704 | 0 | 0 | 6,057,343 | 954,942 | 2,993,521,981 |
| 2026-05-24 | anthropic | 1 | 404 | 78,931,870 | 1,300 | 0 | 866,763 | 40,775,863 | 152,802 | 0 | 41,796,728 |
| 2026-05-24 | openai | 51 | 12,244 | 971,646,809 | 1,672,496,727 | 1,627,801,216 | 0 | 0 | 3,264,823 | 521,366 | 1,677,567,033 |
| 2026-05-25 | anthropic | 1 | 777 | 78,931,870 | 1,527 | 0 | 1,183,214 | 85,074,172 | 287,436 | 0 | 86,546,349 |
| 2026-05-25 | openai | 209 | 18,198 | 1,055,321,351 | 2,350,480,496 | 2,281,068,928 | 0 | 0 | 5,257,735 | 940,364 | 2,358,236,227 |
| 2026-05-26 | openai | 15 | 163 | 700,201,403 | 16,159,831 | 13,874,432 | 0 | 0 | 55,855 | 6,844 | 16,260,512 |
| TOTAL | all | 811 | 121,527 | 9,994,848,060 | 14,615,762,416 | 14,198,011,904 | 31,351,113 | 1,008,996,732 | 38,048,689 | 5,511,009 | 15,710,023,110 |

## Token Extraction Notes

- OpenAI / Codex source: `C:/Users/anton/.codex/sessions/2026/05` and `C:/Users/anton/.codex/archived_sessions`.
- Anthropic / Claude source: `C:/Users/anton/.claude/projects/*Freexcel*`.
- Codex rows use `payload.info.last_token_usage` from `token_count` events to avoid re-summing cumulative totals.
- Claude rows use assistant `message.usage` fields and request-id deduplication when available.
- freexcel_openai_daily_tokens.json: Scoped to C:/Users/anton/.codex/sessions/2026/05 and C:/Users/anton/.codex/archived_sessions.
- freexcel_openai_daily_tokens.json: Included only JSONL session files whose session_meta cwd/initial_cwd contained Freexcel or whose first 250 lines / 256 KiB mentioned Freexcel.
- freexcel_openai_daily_tokens.json: Aggregated event timestamp UTC dates from payload.info.last_token_usage on token_count events with model_provider/provider openai.
- freexcel_openai_daily_tokens.json: bytes is the sum of distinct matching session file sizes attributed to each date/provider row; cacheCreate and cacheRead are fixed at 0 because Codex logs expose cached_input_tokens, not create/read split.
- freexcel_openai_daily_tokens.json: Scanned 703 JSONL files (1291868254 bytes); matched 703 Freexcel OpenAI session files (1291868254 bytes); matched files without token_count events: 0.
- freexcel_anthropic_daily_tokens.json: Scanned only local Claude project directories under C:/Users/anton/.claude/projects whose directory names contain Freexcel.
- freexcel_anthropic_daily_tokens.json: Scanned 217 .jsonl transcript files using line streaming and regex field extraction; skipped non-jsonl tool-result side files.
- freexcel_anthropic_daily_tokens.json: Deduplicated assistant usage events by requestId when present, otherwise by file path plus line number; skipped 9805 duplicate event(s).
- freexcel_anthropic_daily_tokens.json: Bytes are attributed per date as the sum of each matching .jsonl file's full size, counted once for every date on which that file had at least one attributed assistant usage event.
- freexcel_anthropic_daily_tokens.json: Total .jsonl bytes scanned: 181252576; total lines scanned: 42249; attributed assistant usage events: 11665.

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
- 2026-05-26: tony-xmelon <tony.xmelon@gmail.com>

## Reading The Trend

- The project started in Git on 2026-05-12 and has consolidated work through 2026-05-26.
- The daily churn table highlights where implementation volume, tests, and documentation moved together.
- The async token pass attributed 9,994,848,060 bytes of local provider logs and 15,710,023,110 observed tokens across OpenAI/Codex and Anthropic/Claude rows.
