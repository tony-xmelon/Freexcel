# Project Build History Metrics

Generated: 2026-05-30 00:32 +03:00
Repository: https://github.com/tony-xmelon/FreeX.git
Baseline ref: local main at 94ea32573; origin/main at 94ea32573
History window: 2026-05-12 through 2026-05-29

## Scope And Caveats

- Daily build rows are Git numstat churn on the current local main integration branch for src, tests, and docs. They answer how much code changed per day.
- Current LOC counts are exact for the checkout at the baseline ref. Historical cumulative LOC requires a longer offline ETL pass over each snapshot and is intentionally not estimated here.
- Token/provider rows were reprocessed from local Codex and Claude JSONL logs on 2026-05-30 for activity through 2026-05-29 inclusive. Bytes are attributed log-file bytes reported by those extraction passes; raw token counts are observed local usage, not provider invoices.
- Provider-style billable-equivalent tokens apply cache weighting to make the local logs easier to compare with provider dashboards: OpenAI cached input is weighted at 0.5x, Anthropic cache write at 1.25x, Anthropic cache read at 0.1x, and output/reasoning at 1x. Exact billed cost still requires provider exports, model-level rates, and invoice-side normalization.
- Daily build churn `Bytes +/-`, `OpenAI Tokens`, and `Anthropic Tokens` are the per-date raw provider-log totals from the token extraction table. Byte removals are reported as `-0` because logs are attributed by observed usage, not deleted usage.

## Current Repository Footprint

- Registered worktrees: 1
- Local branches: 159
- Remote branches: 210
- Tracked files: 2,080
- Current C# source LOC: 177,816
- Current C# test LOC: 177,742
- Current XAML LOC: 8,024
- Current docs LOC: 49,645
- Observed Codex JSONL sessions/logs: 2,077
- Observed Claude FreeX JSONL sessions/logs: 246
- Provider log bytes attributed: 16,661,053,932
- Observed raw provider tokens: 92,932,144,336
- Provider-style billable-equivalent tokens: 47,069,741,107

## Daily Build Churn

| Date | Commits | Files Changed | LoC +/- | Source C# +/- | Test C# +/- | Docs +/- | Bytes +/- | OpenAI Tokens | Anthropic Tokens | Git Authors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | 21 | 46 | +6,520 / -121 | +4,349 / -113 | +1,672 / -1 | +180 / -0 | +58,308,841 / -0 | 0 | 46,952,042 | 1 |
| 2026-05-13 | 27 | 444 | +56,420 / -40,844 | +8,579 / -2,151 | +2,847 / -418 | +4,633 / -1 | +53,525,808 / -0 | 0 | 89,096,112 | 1 |
| 2026-05-14 | 24 | 57 | +10,239 / -736 | +4,244 / -451 | +1,330 / -0 | +2,432 / -14 | +430,120,353 / -0 | 230,175,315 | 72,028,574 | 1 |
| 2026-05-15 | 26 | 173 | +30,205 / -848 | +15,827 / -788 | +7,135 / -10 | +2,927 / -1 | +339,350,510 / -0 | 675,028,848 | 70,356,959 | 1 |
| 2026-05-16 | 39 | 215 | +42,607 / -4,580 | +17,290 / -2,854 | +20,324 / -1,390 | +20 / -18 | +343,989,780 / -0 | 788,413,672 | 165,410,741 | 1 |
| 2026-05-17 | 33 | 2,901 | +649,481 / -637,975 | +7,727 / -786 | +3,859 / -246 | +2,375 / -64 | +659,020,523 / -0 | 273,797,872 | 179,734,396 | 1 |
| 2026-05-18 | 20 | 88 | +28,420 / -4,156 | +15,762 / -1,342 | +8,712 / -191 | +3,277 / -617 | +430,511,763 / -0 | 285,434,755 | 87,615,455 | 1 |
| 2026-05-19 | 811 | 386 | +59,611 / -9,849 | +30,126 / -7,573 | +23,019 / -578 | +4,747 / -1,159 | +1,240,391,550 / -0 | 1,946,649,860 | 0 | 1 |
| 2026-05-20 | 690 | 286 | +43,742 / -16,298 | +26,569 / -14,637 | +11,309 / -219 | +2,088 / -792 | +1,279,127,455 / -0 | 1,648,668,689 | 382,576 | 1 |
| 2026-05-21 | 762 | 1,056 | +52,377 / -25,258 | +31,489 / -21,341 | +7,537 / -1,083 | +3,098 / -978 | +1,161,100,892 / -0 | 1,122,427,892 | 76,187,087 | 1 |
| 2026-05-22 | 366 | 908 | +51,799 / -26,753 | +27,219 / -20,610 | +4,381 / -158 | +662 / -117 | +1,229,071,998 / -0 | 588,664,932 | 26,472,688 | 1 |
| 2026-05-23 | 1,201 | 1,053 | +53,515 / -43,284 | +26,861 / -20,090 | +11,026 / -322 | +1,076 / -308 | +1,306,964,850 / -0 | 2,854,848,393 | 76,777,952 | 2 |
| 2026-05-24 | 1,374 | 1,017 | +54,493 / -24,365 | +29,530 / -14,883 | +12,078 / -279 | +1,797 / -385 | +1,314,446,360 / -0 | 1,820,600,791 | 68,471,261 | 1 |
| 2026-05-25 | 717 | 866 | +31,975 / -10,339 | +17,767 / -4,299 | +11,403 / -237 | +1,707 / -247 | +1,426,927,077 / -0 | 2,329,328,343 | 86,546,349 | 2 |
| 2026-05-26 | 1,464 | 616 | +53,755 / -24,739 | +31,313 / -21,459 | +20,407 / -1,819 | +1,262 / -978 | +1,616,999,475 / -0 | 5,974,647,607 | 38,435,538 | 2 |
| 2026-05-27 | 1,366 | 433 | +35,110 / -10,101 | +16,893 / -8,337 | +16,184 / -447 | +980 / -683 | +1,481,783,267 / -0 | 4,649,815,155 | 0 | 1 |
| 2026-05-28 | 928 | 467 | +27,119 / -6,542 | +10,969 / -5,024 | +13,788 / -765 | +1,698 / -596 | +1,025,588,295 / -0 | 24,060,030,258 | 178,994,747 | 2 |
| 2026-05-29 | 1,113 | 2,374 | +30,142 / -13,112 | +8,609 / -4,446 | +15,373 / -4,018 | +4,214 / -3,756 | +1,263,825,135 / -0 | 42,404,907,390 | 15,242,087 | 2 |
| TOTAL | 10,982 | 13,386 | +1,317,530 / -899,900 | +331,123 / -151,184 | +192,384 / -12,181 | +39,173 / -10,714 | +16,661,053,932 / -0 | 91,653,439,772 | 1,278,704,564 | 2 |

## Daily Provider Token Usage

| Date | Provider | Files | Sessions | Events | Bytes +/- | Input | Cached Input | Cache Write | Cache Read | Output | Reasoning | Raw Tokens | Billable Eq Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | anthropic | 37 | 37 | 768 | 58,308,841 | 5,546 | 0 | 2,002,836 | 44,641,519 | 302,141 | 0 | 46,952,042 | 7,275,384 |
| 2026-05-13 | anthropic | 16 | 16 | 979 | 53,525,808 | 7,984 | 0 | 2,781,018 | 85,729,081 | 578,029 | 0 | 89,096,112 | 12,635,194 |
| 2026-05-14 | anthropic | 36 | 36 | 937 | 53,252,443 | 1,876 | 0 | 2,752,526 | 68,695,779 | 578,393 | 0 | 72,028,574 | 10,890,504 |
| 2026-05-14 | openai | 5 | 5 | 1,621 | 376,867,910 | 228,903,051 | 223,460,352 | 0 | 0 | 485,175 | 70,202 | 230,175,315 | 117,728,252 |
| 2026-05-15 | anthropic | 41 | 41 | 1,138 | 55,131,398 | 7,384 | 0 | 2,734,629 | 67,169,686 | 445,260 | 0 | 70,356,959 | 10,587,899 |
| 2026-05-15 | openai | 1 | 1 | 4,560 | 284,219,112 | 672,998,247 | 660,068,096 | 0 | 0 | 1,467,643 | 170,945 | 675,028,848 | 344,602,787 |
| 2026-05-16 | anthropic | 45 | 45 | 1,871 | 59,770,668 | 24,710 | 0 | 4,992,743 | 159,782,011 | 611,277 | 0 | 165,410,741 | 22,855,117 |
| 2026-05-16 | openai | 1 | 1 | 5,503 | 284,219,112 | 785,631,408 | 768,870,528 | 0 | 0 | 1,854,098 | 228,326 | 788,413,672 | 403,278,568 |
| 2026-05-17 | anthropic | 35 | 35 | 1,985 | 64,012,476 | 36,051 | 0 | 5,351,357 | 173,871,772 | 475,216 | 0 | 179,734,396 | 24,587,640 |
| 2026-05-17 | openai | 3 | 3 | 1,960 | 595,008,047 | 272,786,866 | 263,650,304 | 0 | 0 | 663,945 | 93,284 | 273,797,872 | 141,718,943 |
| 2026-05-18 | anthropic | 12 | 12 | 813 | 53,559,540 | 993 | 0 | 2,462,711 | 84,890,659 | 261,092 | 0 | 87,615,455 | 11,829,540 |
| 2026-05-18 | openai | 2 | 2 | 1,968 | 376,952,223 | 284,433,721 | 277,189,376 | 0 | 0 | 654,054 | 92,778 | 285,434,755 | 146,585,865 |
| 2026-05-19 | openai | 217 | 217 | 16,091 | 1,240,391,550 | 1,939,736,608 | 1,870,288,640 | 0 | 0 | 5,045,311 | 1,030,415 | 1,946,649,860 | 1,010,668,014 |
| 2026-05-20 | anthropic | 1 | 1 | 11 | 86,136,729 | 13 | 0 | 34,469 | 345,627 | 2,467 | 0 | 382,576 | 80,129 |
| 2026-05-20 | openai | 82 | 82 | 12,133 | 1,192,990,726 | 1,643,667,766 | 1,594,734,080 | 0 | 0 | 3,493,967 | 668,083 | 1,648,668,689 | 850,462,776 |
| 2026-05-21 | anthropic | 2 | 2 | 794 | 86,386,745 | 3,640 | 0 | 2,283,553 | 73,043,689 | 856,205 | 0 | 76,187,087 | 11,018,655 |
| 2026-05-21 | openai | 87 | 87 | 9,007 | 1,074,714,147 | 1,118,380,109 | 1,084,102,144 | 0 | 0 | 2,804,713 | 484,236 | 1,122,427,892 | 579,617,986 |
| 2026-05-22 | anthropic | 1 | 1 | 301 | 86,136,729 | 5,841 | 0 | 2,002,779 | 24,078,649 | 385,419 | 0 | 26,472,688 | 5,302,599 |
| 2026-05-22 | openai | 38 | 38 | 4,267 | 1,142,935,269 | 586,840,256 | 568,882,176 | 0 | 0 | 1,189,575 | 212,172 | 588,664,932 | 303,800,915 |
| 2026-05-23 | anthropic | 1 | 1 | 707 | 86,136,729 | 2,620 | 0 | 1,548,615 | 74,668,986 | 557,731 | 0 | 76,777,952 | 9,963,018 |
| 2026-05-23 | openai | 77 | 77 | 20,634 | 1,220,828,121 | 2,845,976,246 | 2,772,940,544 | 0 | 0 | 5,792,856 | 920,648 | 2,854,848,393 | 1,466,219,478 |
| 2026-05-24 | anthropic | 1 | 1 | 659 | 86,136,729 | 1,560 | 0 | 1,220,663 | 67,005,102 | 243,936 | 0 | 68,471,261 | 8,471,835 |
| 2026-05-24 | openai | 57 | 57 | 13,343 | 1,228,309,631 | 1,815,015,023 | 1,766,173,056 | 0 | 0 | 3,588,009 | 577,885 | 1,820,600,791 | 936,094,389 |
| 2026-05-25 | anthropic | 1 | 1 | 778 | 86,136,729 | 1,527 | 0 | 1,183,214 | 85,074,172 | 287,436 | 0 | 86,546,349 | 10,275,398 |
| 2026-05-25 | openai | 188 | 188 | 17,860 | 1,340,790,348 | 2,321,739,339 | 2,252,745,088 | 0 | 0 | 5,143,919 | 903,840 | 2,329,328,343 | 1,201,414,554 |
| 2026-05-26 | anthropic | 3 | 3 | 383 | 86,594,989 | 549 | 0 | 649,782 | 37,632,606 | 152,601 | 0 | 38,435,538 | 4,728,638 |
| 2026-05-26 | openai | 548 | 548 | 46,296 | 1,530,404,486 | 5,952,654,969 | 5,766,743,040 | 0 | 0 | 15,047,907 | 2,418,450 | 5,974,647,607 | 3,086,749,806 |
| 2026-05-27 | openai | 294 | 294 | 36,627 | 1,481,783,267 | 4,637,115,732 | 4,468,712,448 | 0 | 0 | 9,470,811 | 1,749,663 | 4,649,815,155 | 2,413,979,982 |
| 2026-05-28 | anthropic | 25 | 25 | 2,050 | 98,458,174 | 13,970 | 0 | 4,058,604 | 174,648,047 | 274,126 | 0 | 178,994,747 | 22,826,156 |
| 2026-05-28 | openai | 386 | 386 | 186,507 | 927,130,121 | 24,014,231,896 | 23,567,933,440 | 0 | 0 | 38,313,607 | 4,146,165 | 24,060,030,258 | 12,272,724,948 |
| 2026-05-29 | anthropic | 4 | 4 | 164 | 87,231,544 | 180 | 0 | 330,494 | 14,886,976 | 24,437 | 0 | 15,242,087 | 1,926,432 |
| 2026-05-29 | openai | 244 | 244 | 316,657 | 1,176,593,591 | 42,315,429,592 | 41,551,918,848 | 0 | 0 | 73,046,880 | 6,322,658 | 42,404,907,390 | 21,618,839,706 |
| TOTAL | all | 2,491 | 2,491 | 709,372 | 16,661,053,932 | 91,435,655,273 | 89,458,412,160 | 36,389,993 | 1,236,164,361 | 174,098,236 | 20,089,750 | 92,932,144,336 | 47,069,741,107 |

## Token Extraction Notes

- OpenAI / Codex source: `C:/Users/anton/.codex/sessions/2026/05` and `C:/Users/anton/.codex/archived_sessions`.
- Anthropic / Claude source: `C:/Users/anton/.claude/projects/*FreeX*`.
- Codex rows use `payload.info.last_token_usage` from `token_count` events to avoid re-summing cumulative totals.
- Claude rows use assistant `message.usage` fields and request-id deduplication when available.
- Files is the row-attributed log/session file count from the extractor outputs; for these local logs it tracks the distinct session/transcript files represented by the row.
- freex_openai_daily_tokens.json: Scoped to C:/Users/anton/.codex/sessions/2026/05 and C:/Users/anton/.codex/archived_sessions.
- freex_openai_daily_tokens.json: Included only JSONL session files whose session_meta cwd/initial_cwd contained FreeX or an earlier local project folder name, or whose first 250 lines / 256 KiB mentioned the project.
- freex_openai_daily_tokens.json: Aggregated event timestamps into local +03 dates from payload.info.last_token_usage on token_count events.
- freex_openai_daily_tokens.json: bytes is the sum of distinct matching session file sizes attributed to each date/provider row; cacheCreate and cacheRead are fixed at 0 because Codex logs expose cached_input_tokens, not create/read split.
- freex_openai_daily_tokens.json: Reprocessed `C:/Users/anton/.codex/sessions/2026/05` and `C:/Users/anton/.codex/archived_sessions`; row-attributed OpenAI file/date bytes total 15,474,137,661 through 2026-05-29.
- freex_anthropic_daily_tokens.json: Scanned only local Claude project directories under C:/Users/anton/.claude/projects whose directory names contain FreeX or an earlier local project folder name.
- freex_anthropic_daily_tokens.json: Reprocessed local Claude FreeX project transcripts using line streaming; skipped non-jsonl tool-result side files.
- freex_anthropic_daily_tokens.json: Deduplicated assistant usage events by requestId when present, otherwise by file path plus uuid/timestamp.
- freex_anthropic_daily_tokens.json: Bytes are attributed per date as the sum of each matching .jsonl file's full size, counted once for every date on which that file had at least one attributed assistant usage event.
- freex_anthropic_daily_tokens.json: Row-attributed Anthropic file/date bytes total 1,186,916,271 through 2026-05-29; attributed assistant usage events: 14,338.

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
- 2026-05-26: Antoni Ivanov <tony.xmelon@gmail.com>; tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-27: tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-28: Antoni Ivanov <tony.xmelon@gmail.com>; tony-xmelon <tony.xmelon@gmail.com>
- 2026-05-29: Antoni Ivanov <tony.xmelon@gmail.com>; tony-xmelon <tony.xmelon@gmail.com>

## Reading The Trend

- The project started in Git on 2026-05-12 and has consolidated work through 2026-05-29.
- The daily churn table highlights where implementation volume, tests, and documentation moved together.
- The refreshed token pass attributed 16,661,053,932 bytes of local provider logs, 92,932,144,336 observed raw tokens, and 47,069,741,107 provider-style billable-equivalent tokens across OpenAI/Codex and Anthropic/Claude rows through 2026-05-29.
