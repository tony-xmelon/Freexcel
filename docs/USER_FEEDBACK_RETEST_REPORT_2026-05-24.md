# Freexcel User Feedback Retest Report - 2026-05-24

## Summary

Retest timestamp: 2026-05-24T23:00:57+03:00

Branch/worktree: `codex/user-feedback-retest` at `0b2c998af`, after merging latest `origin/main` before the final verification pass.

Scope: all 14 issues in `docs/USER_TESTING_REPORT_2026-05-24.md`.

Result: all 14 user feedback issues are verified resolved by fresh build plus focused automated regression tests. No retest failures were observed.

Important limitation: most fixes are verified by planner/model/rendering regression tests, not by full WPF end-to-end interaction tests. The checked-in WPF `Category=UIE2E` suite was also run and passed, but it covers formula/cell editing smoke behavior rather than every feedback issue. The two large-workbook reports still need the original 12 MB/100+ sheet workbook for exact timing and hang benchmarking.

## Latest Build Verification

| Check | Command | Result |
| --- | --- | --- |
| Solution build | `dotnet build Freexcel.slnx -m:1 /nodeReuse:false -p:UseSharedCompilation=false -v:minimal` | Passed: 0 warnings, 0 errors. |
| Core Calc feedback regressions | `dotnet test .\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --configuration Debug --no-build --no-restore --filter ViewportStyleTests -v:minimal` | Passed: 5/5. |
| Host feedback regressions | `dotnet test .\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --configuration Debug --no-build --no-restore --filter "ClipboardPastePlannerTests\|WorkbookDropPlannerTests\|MainWindowSourceHygieneTests.FormulaBarTextChanged_SkipsFormulaHighlightWorkForSelectionDisplayUpdates\|ViewportScrollCalculatorTests\|SaveWorkbookWriterTests\|OpenWorkbookLoaderTests\|ToolbarVisualStateTests\|ObjectDialogTests.Hyperlink\|ObjectDialogTests.HyperlinkDialogPrefill" -v:minimal` | Passed: 54/54. |
| App UI feedback regressions | `dotnet test .\tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj --configuration Debug --no-build --no-restore --filter "GridViewTextDecorationTests\|GridViewDrawingObjectThemeTests" -v:minimal` | Passed: 27/27. |
| Integration undo/redo regressions | `dotnet test .\tests\Freexcel.Integration.Tests\Freexcel.Integration.Tests.csproj --configuration Debug --no-build --no-restore --filter UndoRedoTests -v:minimal` | Passed: 7/7. |
| Chart/comment/link model regressions | `dotnet test .\tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --configuration Debug --no-build --no-restore --filter "ChartCommandTests\|CommentCommandTests\|HyperlinkCommandTests" -v:minimal` | Passed: 145/145. |
| Chart host regressions | `dotnet test .\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --configuration Debug --no-build --no-restore --filter ChartDialogTests -v:minimal` | Passed: 47/47. |
| WPF UI smoke suite | `dotnet test .\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --configuration Debug --filter Category=UIE2E -v:minimal` | Passed: 2/2; screenshots saved under `tests\Freexcel.App.Host.Tests\bin\Debug\net10.0-windows10.0.19041.0\FormulaEditingUiE2E\20260524-*`. |

## Issue-by-Issue Retest

| ID | User feedback | Fresh retest result | Evidence | Remaining gap |
| --- | --- | --- | --- | --- |
| UT-2026-05-24-001 | Cell comment display does not identify assigned cell clearly. | Verified resolved. | `ViewportStyleTests` passed 5/5; `CommentCommandTests` included in Core.Model run passed. | No dedicated WPF visual assertion for the red corner marker. |
| UT-2026-05-24-002 | Selection changes between empty and non-empty cells cause short lag. | Verified resolved by source-level regression. | Host regression run passed 54/54 including `FormulaBarTextChanged_SkipsFormulaHighlightWorkForSelectionDisplayUpdates`. | No direct UI latency/performance test for selection changes. |
| UT-2026-05-24-003 | Initial paste from external text into selected cell fails until edit mode. | Verified resolved. | Host regression run passed 54/54 including `ClipboardPastePlannerTests`. | No real OS clipboard WPF test from another app. |
| UT-2026-05-24-004 | Initial paste from external Excel cells fails until edit mode. | Verified resolved. | Same clipboard planner coverage as UT-003; tab/newline external text path remains covered. | No real Excel clipboard-format WPF test. |
| UT-2026-05-24-005 | Dragging and dropping an Excel file does not open it. | Verified resolved by planner/drop routing tests. | Host regression run passed 54/54 including `WorkbookDropPlannerTests`. | No full WPF drag-drop event test opening a real dropped file. |
| UT-2026-05-24-006 | Opening a 12 MB workbook with 100+ sheets takes about nine minutes. | Verified resolved for the identified no-formula recalculation path. | Host regression run passed 54/54 including `OpenWorkbookLoaderTests`. | Original workbook is unavailable, so exact 12 MB timing is not benchmarked. |
| UT-2026-05-24-007 | Touchpad vertical scrolling stops working sporadically. | Verified resolved. | Host regression run passed 54/54 including `ViewportScrollCalculatorTests`. | No physical touchpad/WPF wheel interaction test. |
| UT-2026-05-24-008 | Insert > Charts commands do nothing. | Verified resolved. | `ChartDialogTests` passed 47/47; Core.Model chart command coverage passed inside 145/145 run. | No ribbon-click WPF test proving visible chart insertion. |
| UT-2026-05-24-009 | Added comment is acknowledged but not displayed. | Verified resolved. | Same comment viewport/model coverage as UT-001. | No end-to-end add-comment-and-see-marker UI test. |
| UT-2026-05-24-010 | Inserted picture cannot be selected or manipulated. | Verified resolved for selection affordance rendering. | App.UI regression run passed 27/27 including `GridViewDrawingObjectThemeTests`. | No WPF insert-picture/select/manipulate workflow test. |
| UT-2026-05-24-011 | Inserting a link requires replacing cell text and resulting link does not work. | Verified resolved. | Host regression run passed 54/54 including hyperlink dialog/navigation planner tests; Core.Model hyperlink command coverage passed. | No WPF dialog/Ctrl+click launch test. |
| UT-2026-05-24-012 | Undo and redo are slow and freeze the app for simple edits. | Verified resolved for incremental recalculation path. | Integration `UndoRedoTests` passed 7/7. | No direct WPF undo/redo latency measurement. |
| UT-2026-05-24-013 | Font family and size dropdowns are disconnected from displayed cell formatting. | Verified resolved. | App.UI run passed 27/27 including `GridViewTextDecorationTests`; Host run passed 54/54 including `ToolbarVisualStateTests`. | No WPF dropdown-to-rendered-cell synchronization test. |
| UT-2026-05-24-014 | Saving the large 12 MB/100+ sheet workbook crashes or hangs indefinitely. | Verified resolved for atomic-save failure protection. | Host regression run passed 54/54 including `SaveWorkbookWriterTests`. | Original workbook is unavailable, so exact large-save timing/hang behavior is not benchmarked. |

## E2E Evidence Notes

The real WPF UI smoke suite launched the Debug app and produced screenshots in:

`tests\Freexcel.App.Host.Tests\bin\Debug\net10.0-windows10.0.19041.0\FormulaEditingUiE2E\20260524-224939`

`tests\Freexcel.App.Host.Tests\bin\Debug\net10.0-windows10.0.19041.0\FormulaEditingUiE2E\20260524-224952`

These screenshots are useful as broad latest-build UI smoke evidence, especially for formula editing and grid interaction, but they are not comprehensive user-feedback workflow coverage.

## Recommendation

Keep the 14 issues in `Verified` status for the latest build. The next quality step is to add dedicated WPF E2E tests for the gaps above: external paste, file drag/drop, comment marker visibility, chart insertion, hyperlink dialog/navigation, picture selection, touchpad wheel deltas, toolbar font synchronization, and large-file open/save timing with the original workbook.
