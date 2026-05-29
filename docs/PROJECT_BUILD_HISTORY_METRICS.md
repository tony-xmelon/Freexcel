# Project Build History Metrics

Generated: 2026-05-29 00:42 +03:00
Repository: https://github.com/tony-xmelon/FreeX.git
Baseline ref: local main at 1039a4c0c; origin/main at e6eb94234
History window: 2026-05-12 through 2026-05-28

## Scope And Caveats

- Daily build rows are Git numstat churn on the current local main integration branch for src, tests, and docs. They answer how much code changed per day.
- Current LOC counts are exact for the checkout at the baseline ref. Historical cumulative LOC requires a longer offline ETL pass over each snapshot and is intentionally not estimated here.
- Token/provider rows were reprocessed from local Codex and Claude JSONL logs on 2026-05-29 for activity through 2026-05-28 inclusive. Bytes are attributed log-file bytes reported by those extraction passes; token counts are observed local usage, not provider invoices.
- Daily build churn `Bytes +/-`, `OpenAI Tokens`, and `Anthropic Tokens` are the per-date provider-log totals from the token extraction table. Byte removals are reported as `-0` because logs are attributed by observed usage, not deleted usage.

## Current Repository Footprint

- Registered worktrees: 42
- Local branches: 63
- Remote branches: 84
- Tracked files: 2,021
- Current C# source LOC: 174,065
- Current C# test LOC: 167,136
- Current XAML LOC: 7,815
- Current docs LOC: 49,267
- Observed Codex JSONL sessions/logs: 1,854
- Observed Claude FreeX JSONL sessions/logs: 243
- Provider log bytes attributed: 14,824,420,535
- Observed provider tokens: 50,510,111,955

## Daily Build Churn

| Date | Commits | Files Changed | LoC +/- | Source C# +/- | Test C# +/- | Docs +/- | Bytes +/- | OpenAI Tokens | Anthropic Tokens | Git Authors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | 21 | 46 | +6,520 / -121 | +4,349 / -113 | +1,672 / -1 | +180 / -0 | +58,296,722 / -0 | 0 | 46,952,042 | 1 |
| 2026-05-13 | 27 | 444 | +56,420 / -40,844 | +8,579 / -2,151 | +2,847 / -418 | +4,633 / -1 | +52,138,320 / -0 | 0 | 87,213,208 | 1 |
| 2026-05-14 | 24 | 57 | +10,239 / -736 | +4,244 / -451 | +1,330 / -0 | +2,432 / -14 | +430,120,353 / -0 | 230,175,315 | 72,028,574 | 1 |
| 2026-05-15 | 26 | 173 | +30,205 / -848 | +15,827 / -788 | +7,135 / -10 | +2,927 / -1 | +339,350,510 / -0 | 675,028,848 | 70,356,959 | 1 |
| 2026-05-16 | 39 | 215 | +42,607 / -4,580 | +17,290 / -2,854 | +20,324 / -1,390 | +20 / -18 | +343,989,780 / -0 | 788,413,672 | 165,410,741 | 1 |
| 2026-05-17 | 33 | 2,901 | +649,481 / -637,975 | +7,727 / -786 | +3,859 / -246 | +2,375 / -64 | +659,020,523 / -0 | 273,797,872 | 179,734,396 | 1 |
| 2026-05-18 | 20 | 88 | +28,420 / -4,156 | +15,762 / -1,342 | +8,712 / -191 | +3,277 / -617 | +430,511,763 / -0 | 285,434,755 | 87,615,455 | 1 |
| 2026-05-19 | 811 | 386 | +59,611 / -9,849 | +30,126 / -7,573 | +23,019 / -578 | +4,747 / -1,159 | +1,184,939,883 / -0 | 1,946,649,860 | 0 | 1 |
| 2026-05-20 | 690 | 286 | +43,742 / -16,298 | +26,569 / -14,637 | +11,309 / -219 | +2,088 / -792 | +1,220,542,466 / -0 | 1,648,668,689 | 382,576 | 1 |
| 2026-05-21 | 762 | 1,056 | +52,377 / -25,258 | +31,489 / -21,341 | +7,537 / -1,083 | +3,098 / -978 | +1,115,504,535 / -0 | 1,122,427,892 | 76,187,087 | 1 |
| 2026-05-22 | 366 | 908 | +51,799 / -26,753 | +27,219 / -20,610 | +4,381 / -158 | +662 / -117 | +1,183,475,641 / -0 | 588,664,932 | 26,472,688 | 1 |
| 2026-05-23 | 1,201 | 1,053 | +53,515 / -43,284 | +26,861 / -20,090 | +11,026 / -322 | +1,076 / -308 | +1,237,673,629 / -0 | 2,854,848,393 | 76,777,952 | 2 |
| 2026-05-24 | 1,374 | 1,017 | +54,493 / -24,365 | +29,530 / -14,883 | +12,078 / -279 | +1,797 / -385 | +1,243,536,774 / -0 | 1,820,600,791 | 68,471,261 | 1 |
| 2026-05-25 | 717 | 866 | +31,975 / -10,339 | +17,767 / -4,299 | +11,403 / -237 | +1,707 / -247 | +1,334,699,743 / -0 | 2,329,328,343 | 86,546,349 | 2 |
| 2026-05-26 | 1,464 | 616 | +53,755 / -24,739 | +31,313 / -21,459 | +20,407 / -1,819 | +1,262 / -978 | +1,557,117,120 / -0 | 5,974,647,607 | 38,435,538 | 2 |
| 2026-05-27 | 1,366 | 433 | +35,110 / -10,101 | +16,893 / -8,337 | +16,184 / -447 | +980 / -683 | +1,378,122,105 / -0 | 4,649,815,155 | 0 | 1 |
| 2026-05-28 | 928 | 467 | +27,119 / -6,542 | +10,969 / -5,024 | +13,788 / -765 | +1,698 / -596 | +932,710,081 / -0 | 24,060,030,258 | 178,994,747 | 2 |
| TOTAL | 9,869 | 11,012 | +1,287,388 / -886,788 | +322,514 / -146,738 | +177,011 / -8,163 | +34,959 / -6,958 | +14,824,420,535 / -0 | 49,149,934,782 | 1,360,580,574 | 2 |

## Daily Provider Token Usage

| Date | Provider | Files | Sessions | Events | Bytes +/- | Input | Cached Input | Cache Create | Cache Read | Output | Reasoning | Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-05-12 | anthropic | 37 | 3 | 768 | 58,308,841 | 5,546 | 0 | 2,002,836 | 44,641,519 | 302,141 | 0 | 46,952,042 |
| 2026-05-13 | anthropic | 15 | 1 | 936 | 52,138,320 | 7,933 | 0 | 2,719,527 | 83,920,592 | 565,156 | 0 | 87,213,208 |
| 2026-05-14 | anthropic | 36 | 1 | 937 | 53,252,443 | 1,876 | 0 | 2,752,526 | 68,695,779 | 578,393 | 0 | 72,028,574 |
| 2026-05-14 | openai | 5 | 5 | 1,621 | 376,867,910 | 228,903,051 | 223,460,352 | 0 | 0 | 485,175 | 70,202 | 230,175,315 |
| 2026-05-15 | anthropic | 41 | 1 | 1,138 | 55,131,398 | 7,384 | 0 | 2,734,629 | 67,169,686 | 445,260 | 0 | 70,356,959 |
| 2026-05-15 | openai | 1 | 1 | 4,560 | 284,219,112 | 672,998,247 | 660,068,096 | 0 | 0 | 1,467,643 | 170,945 | 675,028,848 |
| 2026-05-16 | anthropic | 45 | 1 | 1,871 | 59,770,668 | 24,710 | 0 | 4,992,743 | 159,782,011 | 611,277 | 0 | 165,410,741 |
| 2026-05-16 | openai | 1 | 1 | 5,503 | 284,219,112 | 785,631,408 | 768,870,528 | 0 | 0 | 1,854,098 | 228,326 | 788,413,672 |
| 2026-05-17 | anthropic | 35 | 1 | 1,985 | 64,012,476 | 36,051 | 0 | 5,351,357 | 173,871,772 | 475,216 | 0 | 179,734,396 |
| 2026-05-17 | openai | 3 | 3 | 1,960 | 595,008,047 | 272,786,866 | 263,650,304 | 0 | 0 | 663,945 | 93,284 | 273,797,872 |
| 2026-05-18 | anthropic | 12 | 1 | 813 | 53,559,540 | 993 | 0 | 2,462,711 | 84,890,659 | 261,092 | 0 | 87,615,455 |
| 2026-05-18 | openai | 2 | 2 | 1,968 | 376,952,223 | 284,433,721 | 277,189,376 | 0 | 0 | 654,054 | 92,778 | 285,434,755 |
| 2026-05-19 | openai | 217 | 217 | 16,091 | 1,199,351,448 | 1,939,736,608 | 1,870,288,640 | 0 | 0 | 5,045,311 | 1,030,415 | 1,946,649,860 |
| 2026-05-20 | anthropic | 1 | 1 | 11 | 83,003,751 | 13 | 0 | 34,469 | 345,627 | 2,467 | 0 | 382,576 |
| 2026-05-20 | openai | 82 | 82 | 12,133 | 1,151,950,624 | 1,643,667,766 | 1,594,734,080 | 0 | 0 | 3,493,967 | 668,083 | 1,648,668,689 |
| 2026-05-21 | anthropic | 2 | 1 | 794 | 83,253,767 | 3,640 | 0 | 2,283,553 | 73,043,689 | 856,205 | 0 | 76,187,087 |
| 2026-05-21 | openai | 87 | 87 | 9,007 | 1,045,141,232 | 1,118,380,109 | 1,084,102,144 | 0 | 0 | 2,804,713 | 484,236 | 1,122,427,892 |
| 2026-05-22 | anthropic | 1 | 1 | 301 | 83,003,751 | 5,841 | 0 | 2,002,779 | 24,078,649 | 385,419 | 0 | 26,472,688 |
| 2026-05-22 | openai | 38 | 38 | 4,267 | 1,113,362,354 | 586,840,256 | 568,882,176 | 0 | 0 | 1,189,575 | 212,172 | 588,664,932 |
| 2026-05-23 | anthropic | 1 | 1 | 707 | 83,003,751 | 2,620 | 0 | 1,548,615 | 74,668,986 | 557,731 | 0 | 76,777,952 |
| 2026-05-23 | openai | 77 | 77 | 20,634 | 1,171,715,239 | 2,845,976,246 | 2,772,940,544 | 0 | 0 | 5,792,856 | 920,648 | 2,854,848,393 |
| 2026-05-24 | anthropic | 1 | 1 | 659 | 83,003,751 | 1,560 | 0 | 1,220,663 | 67,005,102 | 243,936 | 0 | 68,471,261 |
| 2026-05-24 | openai | 57 | 57 | 13,343 | 1,179,196,749 | 1,815,015,023 | 1,766,173,056 | 0 | 0 | 3,588,009 | 577,885 | 1,820,600,791 |
| 2026-05-25 | anthropic | 1 | 1 | 778 | 83,003,751 | 1,527 | 0 | 1,183,214 | 85,074,172 | 287,436 | 0 | 86,546,349 |
| 2026-05-25 | openai | 188 | 188 | 17,860 | 1,284,040,971 | 2,321,739,339 | 2,252,745,088 | 0 | 0 | 5,143,919 | 903,840 | 2,329,328,343 |
| 2026-05-26 | anthropic | 3 | 1 | 383 | 83,462,011 | 549 | 0 | 649,782 | 37,632,606 | 152,601 | 0 | 38,435,538 |
| 2026-05-26 | openai | 548 | 548 | 46,296 | 1,473,655,109 | 5,952,654,969 | 5,766,743,040 | 0 | 0 | 15,047,907 | 2,418,450 | 5,974,647,607 |
| 2026-05-27 | openai | 294 | 294 | 36,627 | 1,378,122,105 | 4,637,115,732 | 4,468,712,448 | 0 | 0 | 9,470,811 | 1,749,663 | 4,649,815,155 |
| 2026-05-28 | anthropic | 25 | 25 | 2,050 | 98,458,174 | 13,970 | 0 | 4,058,604 | 174,648,047 | 274,126 | 0 | 178,994,747 |
| 2026-05-28 | openai | 386 | 386 | 186,507 | 834,251,907 | 24,014,231,896 | 23,567,933,440 | 0 | 0 | 38,313,607 | 4,146,165 | 24,060,030,258 |
| TOTAL | all | 2,242 | 2,027 | 392,508 | 14,824,420,535 | 49,120,225,450 | 47,906,493,312 | 35,998,008 | 1,219,468,896 | 101,014,046 | 13,767,092 | 50,510,111,955 |

## Token Extraction Notes

- OpenAI / Codex source: `C:/Users/anton/.codex/sessions/2026/05` and `C:/Users/anton/.codex/archived_sessions`.
- Anthropic / Claude source: `C:/Users/anton/.claude/projects/*FreeX*`.
- Codex rows use `payload.info.last_token_usage` from `token_count` events to avoid re-summing cumulative totals.
- Claude rows use assistant `message.usage` fields and request-id deduplication when available.
- Files is the row-attributed log/session file count from the extractor outputs; for these local logs it tracks the distinct session/transcript files represented by the row.
- freex_openai_daily_tokens.json: Scoped to C:/Users/anton/.codex/sessions/2026/05 and C:/Users/anton/.codex/archived_sessions.
- freex_openai_daily_tokens.json: Included only JSONL session files whose session_meta cwd/initial_cwd contained FreeX or whose first 250 lines / 256 KiB mentioned FreeX.
- freex_openai_daily_tokens.json: Aggregated event timestamps into local +03 dates from payload.info.last_token_usage on token_count events.
- freex_openai_daily_tokens.json: bytes is the sum of distinct matching session file sizes attributed to each date/provider row; cacheCreate and cacheRead are fixed at 0 because Codex logs expose cached_input_tokens, not create/read split.
- freex_openai_daily_tokens.json: Reprocessed `C:/Users/anton/.codex/sessions/2026/05` and `C:/Users/anton/.codex/archived_sessions`; row-attributed OpenAI file/date bytes total 13,261,304,123 through 2026-05-28.
- freex_anthropic_daily_tokens.json: Scanned only local Claude project directories under C:/Users/anton/.claude/projects whose directory names contain FreeX.
- freex_anthropic_daily_tokens.json: Reprocessed local Claude FreeX project transcripts using line streaming; skipped non-jsonl tool-result side files.
- freex_anthropic_daily_tokens.json: Deduplicated assistant usage events by requestId when present, otherwise by file path plus uuid/timestamp.
- freex_anthropic_daily_tokens.json: Bytes are attributed per date as the sum of each matching .jsonl file's full size, counted once for every date on which that file had at least one attributed assistant usage event.
- freex_anthropic_daily_tokens.json: Row-attributed Anthropic file/date bytes total 1,563,116,412 through 2026-05-28; attributed assistant usage events: 19,931.

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

## Reading The Trend

- The project started in Git on 2026-05-12 and has consolidated work through 2026-05-28.
- The daily churn table highlights where implementation volume, tests, and documentation moved together.
- The refreshed token pass attributed 14,824,420,535 bytes of local provider logs and 50,510,111,955 observed tokens across OpenAI/Codex and Anthropic/Claude rows through 2026-05-28.
