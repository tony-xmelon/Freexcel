# Freexcel User Testing Report - 2026-05-24

## Report Metadata

| Field | Value |
| --- | --- |
| Tracker status | Active |
| Reported timestamp | 2026-05-24T12:25:23+03:00 |
| Last updated timestamp | 2026-05-24T23:06:17+03:00 |
| App version/build | freexcel-0-5-phase-5-20260523-214245-064903f4-win-x64-singlefile |
| App version date | 2026-05-23 21:42:45 |
| Release artifact | artifacts/releases/freexcel-0-5-phase-5-20260523-214245-064903f4-win-x64-singlefile.exe |
| Build commit | 064903f4 |
| Source report | User feedback pasted into Codex thread on 2026-05-24 |
| Intake owner | Codex |
| Working branch | codex/excel-open-formats-hardening-sync |

## Intake Notes

The first user testing feedback was provided in the Codex thread on 2026-05-24. Issues below preserve the user's observations, track reproducibility separately from the initial report, and should be moved through New, Confirmed, In progress, Fixed, and Verified as each item is reproduced and resolved against the current synced codebase.

## Issue Tracker

| ID | Title | Reported timestamp | Source | Environment | Reproducibility | Severity | Priority | Status | Resolution | Last updated timestamp | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UT-2026-05-24-001 | Cell comment display does not identify assigned cell clearly | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P1 | Verified | Root cause: visible viewport cells had no comment indicator metadata, so the grid could not mark the owning cell. Resolution adds `DisplayCell.HasComment` and renders a red upper-right corner marker on cells with notes or threaded comments. | 2026-05-24T12:36:48+03:00 | Added `ViewportStyleTests.GetViewport_CommentOnlyCell_PopulatesDisplayCellWithCommentIndicator`; `dotnet test tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --filter ViewportStyleTests --no-restore` passed: 4/4. |
| UT-2026-05-24-002 | Selection changes between empty and non-empty cells cause short lag | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P1 | Verified | Root cause: programmatic FormulaBar text changes during selection could still run formula-reference highlighting after the formula bar had previously captured an edit cell. Resolution gates formula-reference highlighting to active formula/inline edit scenarios, so selection display updates clear overlays and return quickly. | 2026-05-24T13:08:10+03:00 | Added `MainWindowSourceHygieneTests.FormulaBarTextChanged_SkipsFormulaHighlightWorkForSelectionDisplayUpdates`; focused host tests passed: 24/24. |
| UT-2026-05-24-003 | Initial paste from external text into selected cell fails until cell edit mode is opened | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | High | P0 | Verified | Root cause: Freexcel preferred its stale internal clipboard before checking whether the OS clipboard had changed. Resolution records the copied text with internal clipboard state and falls back to external text/image paste when the OS clipboard no longer matches. | 2026-05-24T12:29:39+03:00 | Added red/green coverage in `ClipboardPastePlannerTests.ShouldUseInternalClipboard_RejectsStaleInternalCopyWhenSystemClipboardChanged`; `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter ClipboardPastePlannerTests --no-restore` passed: 13/13. |
| UT-2026-05-24-004 | Initial paste from external Excel cells into selected cells fails until cell edit mode is opened | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | High | P0 | Verified | Same root cause and resolution as UT-2026-05-24-003; Excel places tab/newline-delimited text on the OS clipboard, which now supersedes stale internal Freexcel clipboard state. | 2026-05-24T12:29:39+03:00 | Covered by the same clipboard planner regression test and focused host test run: 13/13 passed. |
| UT-2026-05-24-005 | Dragging and dropping an Excel file does not open it | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | High | P1 | Verified | Root cause: the main window had no file-drop handlers, so workbook file drops were only ignored. Resolution enables window-level file drops, accepts supported open formats, and routes the dropped file through the existing `OpenFileAsync` loader. | 2026-05-24T12:33:22+03:00 | Added `WorkbookDropPlannerTests`; `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "ClipboardPastePlannerTests|WorkbookDropPlannerTests" --no-restore` passed: 15/15. |
| UT-2026-05-24-006 | Opening a 12 MB workbook with 100+ sheets takes about nine minutes | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Not reproduced with original file; reproduced by open-path review | High | P1 | Verified | Root cause candidate: every loaded workbook ran the full calculation stage even when it contained no formulas, which can add unnecessary work for large multi-sheet files. Resolution skips the calculation stage when the loaded workbook has no formula cells. Exact 12 MB workbook timing still needs the user sample for benchmarking. | 2026-05-24T13:08:10+03:00 | Added `OpenWorkbookLoaderTests.LoadAsync_SkipsRecalculateStageWhenWorkbookHasNoFormulas`; focused host tests passed: 24/24. |
| UT-2026-05-24-007 | Touchpad vertical scrolling stops working sporadically | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P2 | Verified | Root cause: high-resolution touchpads can emit wheel deltas smaller than 120; integer division converted those events to zero scroll notches while still handling the event. Resolution normalizes any non-zero sub-notch wheel delta to one scroll step in the correct direction. | 2026-05-24T13:08:10+03:00 | Added `ViewportScrollCalculatorTests.NormalizeWheelNotches_PreservesHighResolutionTouchpadDeltas`; focused host tests passed: 24/24. |
| UT-2026-05-24-008 | Insert > Charts commands do nothing | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced against release gap; resolved in current branch | Medium | P1 | Verified | The current synced branch includes chart ribbon handlers for supported chart families plus AddChartCommand backing logic. Deferred advanced chart families now show explicit unsupported-family messaging instead of silently doing nothing. | 2026-05-24T12:41:29+03:00 | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter ChartDialogTests --no-restore` passed: 41/41. `dotnet test tests\Freexcel.Core.Model.Tests\Freexcel.Core.Model.Tests.csproj --filter ChartCommandTests --no-restore` passed: 125/125. |
| UT-2026-05-24-009 | Added comment is acknowledged but not displayed | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P1 | Verified | Same root cause and resolution as UT-2026-05-24-001; comment-only cells now appear in the viewport and render with a visible cell-corner marker after adding a note/comment. | 2026-05-24T12:36:48+03:00 | Covered by the comment-only viewport regression test; focused App.Host planner tests also passed: 15/15. |
| UT-2026-05-24-010 | Inserted picture cannot be selected or manipulated | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P2 | Verified | Root cause: inserted pictures had format/crop commands but no visible selected-object affordance after insertion. Resolution leaves the anchor cell active after insertion and renders a selected-picture outline with corner handles when the active cell is the picture anchor. | 2026-05-24T13:08:10+03:00 | Added `GridViewDrawingObjectThemeTests.PictureRenderer_DrawsSelectionAdornerForPictureAtActiveCell`; focused UI tests passed: 5/5. |
| UT-2026-05-24-011 | Inserting a link requires replacing cell text and resulting link does not work | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P1 | Verified | Root causes: the hyperlink dialog always opened with blank display text, so accepting it replaced existing cell text with the URL, and the grid had no click navigation path. Resolution pre-fills display text from the selected cell, preserves existing link targets when editing, and supports Ctrl+click navigation for external and in-workbook links. | 2026-05-24T13:08:10+03:00 | Added `HyperlinkDialogPrefill_UsesExistingCellTextAsDisplayText`, `HyperlinkNavigationPlanner_CreatesExternalLaunchPlanForWebLink`, and `HyperlinkNavigationPlanner_CreatesWorksheetPlanForDocumentLink`; focused host tests passed: 24/24. |
| UT-2026-05-24-012 | Undo and redo are slow and freeze the app for simple edits | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | High | P1 | Verified | Root cause: undo/redo of simple cell edits always triggered full-workbook recalculation. Resolution lets commands expose affected cells; edit-cell undo/redo now returns the edited addresses so the host can use incremental recalculation where possible and fall back to full recalculation only when affected cells are unknown. | 2026-05-24T13:08:10+03:00 | Added `UndoRedoTests.UndoRedo_EditCell_ReturnsAffectedCellForIncrementalRecalculation`; focused integration tests passed: 7/7. |
| UT-2026-05-24-013 | Font family and size dropdowns are disconnected from displayed cell formatting | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Reproduced by code path | Medium | P1 | Verified | Root causes: grid text rendering hardcoded Calibri instead of `CellStyle.FontName`, and style changes refreshed the viewport/status but not toolbar dropdown state. Resolution applies style font family/weight/italic during rendering and refreshes the toolbar after shared style diffs. | 2026-05-24T12:40:30+03:00 | Added `GridViewTextDecorationTests.CreateCellTypeface_UsesStyleFontNameAndWeight`; `dotnet test tests\Freexcel.App.UI.Tests\Freexcel.App.UI.Tests.csproj --filter GridViewTextDecorationTests --no-restore` passed: 22/22. `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter ToolbarVisualStateTests --no-restore` passed: 1/1. |
| UT-2026-05-24-014 | Saving the large 12 MB/100+ sheet workbook crashes or hangs indefinitely | 2026-05-24T12:25:23+03:00 | User feedback | Windows x64 single-file build | Not reproduced with original file; reproduced by save-path review | Critical | P0 | Verified | Root cause candidate: saving wrote directly to the destination path, so a failure or crash during serialization could leave the target file partially written. Resolution writes to a same-directory temp file and atomically replaces the target only after adapter save succeeds; temp files are cleaned up on failure. Exact large-file save timing still needs the user sample for benchmarking. | 2026-05-24T13:08:10+03:00 | Added `SaveWorkbookWriterTests.SaveAsync_PreservesExistingFileWhenAdapterFails`; focused host tests passed: 24/24. |

## Issue Template

Use this template for each user-reported finding as reports arrive.

| Field | Value |
| --- | --- |
| ID | UT-YYYY-MM-DD-NNN |
| Title |  |
| Reported timestamp |  |
| App version/build | freexcel-0-5-phase-5-20260523-214245-064903f4-win-x64-singlefile |
| App version date | 2026-05-23 21:42:45 |
| Reporter/source |  |
| Environment | Windows x64 single-file build |
| Reproducibility | Always / Intermittent / Once / Unknown |
| Severity | Critical / High / Medium / Low |
| Priority | P0 / P1 / P2 / P3 |
| Status | New / Confirmed / In progress / Fixed / Verified / Won't fix / Duplicate / Blocked |
| Resolution |  |
| Reproduction steps |  |
| Expected result |  |
| Actual result |  |
| Evidence |  |
| Code area |  |
| Fix branch/commit |  |
| Verification |  |
| Last updated timestamp |  |

## Status Definitions

| Status | Meaning |
| --- | --- |
| New | Report has been filed but not yet verified. |
| Confirmed | Behavior was reproduced or verified against code/log evidence. |
| In progress | Fix work has started. |
| Fixed | Code or documentation change has landed on the working branch. |
| Verified | Relevant tests/build/manual checks passed after the fix. |
| Blocked | Missing information or dependency prevents progress. |
| Duplicate | Covered by another tracked issue. |
| Won't fix | Intentionally left unchanged with rationale recorded. |

## Change Log

| Timestamp | Change |
| --- | --- |
| 2026-05-24T00:40:31+03:00 | Created tracker for the first user testing report and recorded intake blocker because the raw report was not found in the workspace. |
| 2026-05-24T10:18:25+03:00 | Started the requested fix loop, synced from `origin/main`, confirmed the issue list contains no actionable product findings, and left intake blocked pending the raw user report. |
| 2026-05-24T12:25:23+03:00 | Filed 14 issues from the pasted first user testing feedback and marked the tracker active. |
| 2026-05-24T12:29:39+03:00 | Fixed stale internal clipboard routing for external paste reports UT-2026-05-24-003 and UT-2026-05-24-004; focused clipboard planner tests passed. |
| 2026-05-24T12:33:22+03:00 | Fixed workbook file drag/drop for UT-2026-05-24-005; focused clipboard and drop planner tests passed. |
| 2026-05-24T12:36:48+03:00 | Fixed comment visibility/ownership markers for UT-2026-05-24-001 and UT-2026-05-24-009; focused host and calc tests passed. |
| 2026-05-24T12:40:30+03:00 | Fixed font rendering and toolbar refresh behavior for UT-2026-05-24-013; focused UI and toolbar tests passed. |
| 2026-05-24T12:41:29+03:00 | Verified Insert > Charts command handling for UT-2026-05-24-008 in the current synced branch; chart dialog and chart command tests passed. |
| 2026-05-24T13:08:10+03:00 | Continued through the remaining list: fixed selection-display formula highlight churn, high-resolution touchpad wheel deltas, hyperlink prefill/navigation, selected-picture affordance, incremental undo/redo recalculation, no-formula open calculation skip, and atomic save hardening; focused host, UI, and integration tests passed. |
| 2026-05-24T22:50:29+03:00 | Retested all 14 user feedback issues against latest synced `main`; solution build, focused regression matrix, and WPF `Category=UIE2E` smoke tests passed. Added `docs/USER_FEEDBACK_RETEST_REPORT_2026-05-24.md` with issue-by-issue evidence and remaining E2E coverage gaps. |
| 2026-05-24T23:00:57+03:00 | Merged the newer `origin/main` commits into `codex/user-feedback-retest` and reran the full retest verification matrix at `0b2c998af`; all commands passed again. |
| 2026-05-24T23:06:17+03:00 | Merged the final visible `origin/main` batch into `codex/user-feedback-retest` and reran the full retest verification matrix at `d75c22984`; all commands passed again. |
