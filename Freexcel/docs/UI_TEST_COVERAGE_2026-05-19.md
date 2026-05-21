# Freexcel UI Test Coverage Log

Generated: 2026-05-19
Branch: `codex/testing`
Worktree: `Freexcel/`
Test target: `src\Freexcel.App.Host\bin\Debug\net10.0-windows10.0.19041.0\Freexcel.App.Host.exe`

## Purpose

This is the living manual UI test plan and findings log for Freexcel. It complements the command, shortcut, and unit-test parity docs by tracking real end-to-end WPF behavior with mouse and keyboard input.

## Current Verification Baseline

| Check | Command | Result |
| --- | --- | --- |
| Git state | `git status --short --branch` | `codex/testing`; existing modified `docs/PROJECT_STATUS_REPORT_2026-05-19.md` left untouched |
| Worktrees | `git worktree list --porcelain` | Current checkout is already an active session branch; no nested worktree created |
| Build | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors |
| Rebuild after worktree changed | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors |
| Focused finding regression tests | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests\|FullyQualifiedName~KeyboardShortcutMatcherTests\|FullyQualifiedName~WorksheetContextMenuPlannerTests"` | Passed, 194 tests, 0 failures |
| UIA dialog entry regression tests | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests"` | Passed, 68 tests, 0 failures |
| UIA dialog entry regression recheck | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests" -m:1 /nodeReuse:false -p:UseSharedCompilation=false` | Passed, 74 tests, 0 failures |
| Host regression suite | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj` | Passed, 847 tests, 0 failures |
| Current build | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors |
| Continuation UIA/mouse dialog pass | Fresh Debug build launched via `src\Freexcel.App.Host\bin\Debug\net10.0-windows10.0.19041.0\Freexcel.App.Host.exe`; UIA activation plus guarded mouse clicks where foreground was verified | Account and About opened by foreground-confirmed mouse clicks. UIA `InvokePattern` still returned success for Insert Function/About without opening a dialog. |

## Coverage Model

Each surface is tracked with these states:

| State | Meaning |
| --- | --- |
| Not Started | No current manual pass in this session |
| In Progress | One or more paths tested, more expected |
| Passed | Smoke path passed with no issue observed |
| Finding | One or more issues recorded below |
| Blocked | Could not test because of environment, missing data, modal/system dependency, or crash |

## Full UI Surface Coverage

| Area | Status | Manual Scope |
| --- | --- | --- |
| App launch and shell | In Progress | Process launch, main window render, custom title bar, QAT Save/Undo/Redo, minimize/maximize/close |
| File/backstage/start overlay | In Progress | File tab, Home/Info/New/Open/Save/Save As/Print/Export/Account/Options/Close, recent/pinned list |
| Formula bar and name box | In Progress | Name box navigation, formula entry, `fx` Insert Function, expand/collapse formula bar |
| Worksheet grid core | In Progress | Cell selection, drag selection, data entry, inline edit, formula edit, navigation, undo/redo |
| Home ribbon | In Progress | Clipboard, Paste Special, Format Painter, font, fill, border, alignment, number formats, styles, cells, editing |
| Insert ribbon | In Progress | PivotTable, Table, charts, sparklines, pictures, shapes, text box, symbols, hyperlink, comments |
| Draw ribbon | In Progress | Shapes, ordering, size/rotation, fill/outline, alt text, crop/effects prompts |
| Page Layout ribbon | In Progress | Margins, orientation, paper, print area, breaks, background, print titles, scale, themes, page setup |
| Formulas ribbon | In Progress | Insert Function, AutoSum/categories, names, auditing, error checking, evaluate, watch window, calculation |
| Data ribbon | In Progress | Import, refresh, sort/filter, Advanced Filter, Text to Columns, Remove Duplicates, Validation, What-If, outline |
| Review ribbon | In Progress | Spell Check, Accessibility, comments/notes, protections, sharing messages, workbook statistics |
| View ribbon | In Progress | Workbook views, show toggles, freeze/split panes, zoom, arrange/window commands |
| Help ribbon | In Progress | Help, feedback, About and excluded/help messaging |
| Contextual PivotTable tabs | Not Started | Analyze/Design visibility, field list, filters, value settings, contextual commands |
| Worksheet context menu | In Progress | Shift+F10/Menu key/right-click, clipboard, insert/delete, sort/filter, notes, hyperlink, Format Cells, clear commands |
| Sheet tab strip/context menu | In Progress | Add, rename, duplicate, delete, move, color, hide/unhide, grouping, tab navigation |
| Status bar and zoom | In Progress | Ready/status text, selection stats, zoom buttons, slider, keyboard/mouse-wheel zoom |
| Dialog catalog | In Progress | Format Cells, Find/Replace, Data Validation, Page Setup, Options, Names, CF manager, Goal Seek, Custom Views, pivot filters, Evaluate Formula, Watch Window, Theme, Symbol picker |
| Keyboard shortcuts | In Progress | Shortcut matrix high-risk paths: Ctrl+P, Ctrl+V/Ctrl+Alt+V, Ctrl+1, Ctrl++/Ctrl+-, Alt+Down, Ctrl+Q, Shift+F10, F4 repeat |
| Ribbon keytips | In Progress | Alt/F10 overlay, tab keytips, QAT keytips, visible command keytips, menu/nested menu keytips, Escape cancellation |
| Accessibility and focus | In Progress | Keyboard-only traversal, focus return after dialogs, visible focus indicators, screen-reader naming smoke |
| Visual fidelity | In Progress | Ribbon density, overlay placement, dialog layout, grid rendering, chart/drawing rendering, split/freeze visual behavior |
| File IO and interop smoke | Not Started | Open/save round trip with representative XLSX/CSV, unsupported feature warnings, export output behavior |

## First-Pass Test Queue

1. Launch latest Debug build and capture process/window state.
2. Exercise File/backstage: create blank workbook, Options, Account, Print/Export messages, return to workbook.
3. Exercise worksheet grid: type values/formulas, edit with F2/formula bar, navigate with Enter/Tab/arrows, undo/redo.
4. Exercise Home ribbon: bold/italic/underline, fill/font color prompts, borders menu, number format, merge, Find/Replace, Format Cells.
5. Exercise keyboard/keytips: Alt/F10 top-level tabs, Home command keytips, Escape, Shift+F10 worksheet menu, Ctrl+1.
6. Exercise sheet tabs/status: add/rename/duplicate/move/color/hide/unhide sheets, zoom controls.
7. Record findings immediately with reproduction, expected behavior, actual behavior, severity, and evidence.

## Findings

### UI-2026-05-19-001: File backstage does not close with Escape

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/file-backstage.png`, `docs/ui-test-artifacts/backstage-after-second-escape.png`
Fix: `MainWindow` handles bare Escape while Backstage is visible and returns focus to the workbook before normal transient-mode cancellation.
Verification: `MainWindowXamlKeyTipTests.EscapeFromVisibleBackstage_ReturnsToWorkbookBeforeTransientCancellation`.

Repro:
1. Launch Freexcel.
2. Open File backstage with `Alt+F`.
3. Press `Escape`.
4. Press `Escape` again.

Expected:
Backstage returns to the workbook, matching the normal keyboard escape route from a temporary full-window command surface.

Actual:
The keytip badges clear after the first Escape, but the File backstage remains visible after a second Escape. The only observed visual route back is the back arrow.

### UI-2026-05-19-002: F10 does not visibly enter ribbon keytip mode from the worksheet

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/keytips-f10.png`
Fix: `MainWindow` handles `F10` during `PreviewKeyDown`, before worksheet focus can consume it, and enters top-level ribbon keytip mode.
Verification: `MainWindowXamlKeyTipTests.MainWindowPreviewKeys_HandleWorksheetKeytipAndContextMenuEntryPoints` plus existing shortcut/keytip tests.

Repro:
1. Launch Freexcel and keep focus on the worksheet.
2. Press `F10`.

Expected:
Ribbon keytip badges appear for the top-level tabs and QAT, as documented in `docs/SHORTCUT_PARITY_MATRIX.md`.

Actual:
No keytip badges appeared in the captured worksheet view. `Alt+F` did open File backstage with keytip badges, so the keytip system is present but this entry path needs a focused retest/fix.

### UI-2026-05-19-003: Shift+F10 did not open the worksheet context menu in the initial pass

Severity: P2
Status: Fixed after recheck
Evidence: `docs/ui-test-artifacts/worksheet-context-menu.png`
Fix: `MainWindow` handles `Shift+F10` during `PreviewKeyDown` and routes it through the existing worksheet context menu command path.
Verification: `MainWindowXamlKeyTipTests.MainWindowPreviewKeys_HandleWorksheetKeytipAndContextMenuEntryPoints`, `KeyboardShortcutMatcherTests`, and `WorksheetContextMenuPlannerTests`.

Repro:
1. Select a worksheet cell.
2. Press `Shift+F10`.

Expected:
Worksheet context menu opens from the active cell.

Actual:
No context menu appeared in the captured worksheet view. This needs a focused recheck using a verified foreground Freexcel window before filing as a product bug.

### UI-2026-05-19-004: Backstage Options is visible but not UI Automation invokable

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/pass4-file-open.png`, `docs/ui-test-artifacts/pass3-after-options.png`
Fix: The Backstage Options command has explicit `x:Name`, `AutomationProperties.Name`, `AutomationProperties.AutomationId`, help text, and tab-stop metadata while retaining the normal button `Click` handler.
Verification: `MainWindowXamlKeyTipTests.BackstageOptionsEntryPoint_IsNamedCommandForUiAutomation`.

Repro:
1. Launch Freexcel.
2. Open File backstage.
3. Inspect or activate the visible `Options` item through UI Automation.

Expected:
The visible `Options` command exposes an activation pattern, such as `InvokePattern`, matching its role as a clickable command and supporting accessibility/test automation.

Actual:
The visible `Options` element was found by name, but it exposed no Invoke, Select, or ExpandCollapse pattern. A UIA activation attempt failed with `No invoke/select/expand pattern for Options`.

### UI-2026-05-19-005: Backstage Account is visible but not UI Automation invokable

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/pass7-after-account-attempt.png`, `docs/ui-test-artifacts/pass10-account-mouse.png`
Fix: Backstage Account now uses `AutomationInvokeButton` with stable `AutomationProperties.Name`, `AutomationProperties.AutomationId`, help text, tab-stop metadata, and an owned activated message route.
Verification: `MainWindowXamlKeyTipTests.BackstageAccountEntryPoint_DisclosesLocalAccountDecision` and `MainWindowXamlKeyTipTests.DialogEntryPointButtons_HaveStableAutomationIds`.

Repro:
1. Launch Freexcel.
2. Open File backstage.
3. Inspect or activate the visible `Account` item through UI Automation.

Expected:
The visible `Account` command exposes an activation pattern, such as `InvokePattern`, matching its role as a clickable backstage navigation command.

Actual:
The visible `Account` element exposed only `SynchronizedInputPattern` and no Invoke, Select, or ExpandCollapse pattern in the UIA pass. A guarded foreground mouse click did open the Account informational dialog, so this is currently scoped to accessibility/test automation rather than the visual click path.

### UI-2026-05-19-006: UIA Invoke on dialog entry points returns without opening dialogs

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/pass8-after-fx-invoke.png`, `docs/ui-test-artifacts/pass8-after-options-invoke.png`, `docs/ui-test-artifacts/pass9-help-tab.png`, `docs/ui-test-artifacts/pass11b-insert-function-activation.png`, `docs/ui-test-artifacts/pass11b-about-activation.png`
Fix: Insert Function, About Freexcel, Account, and Options now use an explicit `IInvokeProvider` button peer that dispatches the click to the WPF dispatcher; dialog/message entry points are shown as owned, activated windows/messages.
Verification: `MainWindowXamlKeyTipTests.DialogEntryPointButtons_HaveStableAutomationIds`, `MainWindowXamlKeyTipTests.DialogEntryPointHandlers_UseOwnedActivatedDialogs`, and focused `MainWindowXamlKeyTipTests` run passed 74 tests.

Repro:
1. Launch Freexcel.
2. Invoke `Insert Function` through UI Automation.
3. Select Help through UI Automation and invoke `About Freexcel`.
4. Inspect top-level windows for the Freexcel process after each invocation.

Expected:
Each dialog entry point opens its corresponding dialog, and the dialog appears as a top-level owned window in the Freexcel process.

Actual:
`Insert Function` and `About Freexcel` both expose activation patterns and return from UIA activation, but no additional Freexcel top-level dialog appears. Latest screenshots show the app remains on the workbook or Help tab after activation. A guarded foreground mouse click did open About Freexcel, so the current failure is the UI Automation activation path.

## Passed Smoke Checks

| Check | Evidence | Notes |
| --- | --- | --- |
| App launch renders main shell | `docs/ui-test-artifacts/launch-shell.png` | Title bar, QAT, Home ribbon, formula bar, grid, sheet tab strip, and status bar visible |
| Grid accepts typed numeric input | `docs/ui-test-artifacts/grid-entry.png` | Initial coordinate calibration clicked B7 instead of A1, but keyboard data entry and Enter navigation worked |
| `Ctrl+1` opens Format Cells | `docs/ui-test-artifacts/format-cells-dialog.png` | Dialog opens on Number tab and shows tab strip through Protection |
| File backstage opens via `Alt+F` | `docs/ui-test-artifacts/file-backstage.png` | Backstage displays Home/New/Recent/Pinned and keytip badges |
| File backstage Back returns to workbook | `docs/ui-test-artifacts/pass2-file-back-uia.png` | UIA found and invoked the `Back` control successfully |
| Sheet insertion works from UIA | `docs/ui-test-artifacts/pass2-add-sheet.png` | Invoking `Insert Sheet` created and selected `Sheet2` |
| Zoom buttons work from UIA | `docs/ui-test-artifacts/pass2-zoom-in.png`, `docs/ui-test-artifacts/pass2-zoom-out.png` | Zoom changed through the status bar controls and returned near baseline |
| Data ribbon renders | `docs/ui-test-artifacts/pass5-data-tab.png` | Top-level Data commands visible; several detailed commands are under collapsed dropdown groups at this width |
| Insert ribbon renders | `docs/ui-test-artifacts/pass5-insert-tab.png` | PivotTable, Table, Pivot refresh, Charts, Sparklines, Links & Objects visible |
| View ribbon renders | `docs/ui-test-artifacts/pass5-view-tab.png` | View controls captured for follow-up interaction testing |
| Review ribbon renders | `docs/ui-test-artifacts/pass5-review-tab.png` | Review controls captured for follow-up interaction testing |
| Backstage Account opens by mouse | `docs/ui-test-artifacts/pass10-account-mouse.png` | Foreground-confirmed mouse click opened the Account informational dialog |
| Help tab renders and About opens by mouse | `docs/ui-test-artifacts/pass10-help-tab-mouse.png`, `docs/ui-test-artifacts/pass10-about-mouse.png` | Foreground-confirmed mouse click opened the About Freexcel dialog |
| Help tab selects by UI Automation | `docs/ui-test-artifacts/pass11b-help-activation.png` | `SelectionItemPattern.Select` switched to the Help tab on the latest clean build |
| Draw ribbon renders on latest build | `docs/ui-test-artifacts/pass12-draw-tab-uia.png` | UIA selected the Draw tab and captured the command surface |
| Page Layout ribbon renders on latest build | `docs/ui-test-artifacts/pass12-page-layout-tab-uia.png` | UIA selected the Page Layout tab and captured the command surface |
| Formulas ribbon renders on latest build | `docs/ui-test-artifacts/pass12-formulas-tab-uia.png` | UIA selected the Formulas tab and captured the command surface |
| Data/Review/View ribbons render on latest build | `docs/ui-test-artifacts/pass12-data-tab-uia.png`, `docs/ui-test-artifacts/pass12-review-tab-uia.png`, `docs/ui-test-artifacts/pass12-view-tab-uia.png` | UIA selected each tab and captured the command surface |
| Help ribbon renders on latest build | `docs/ui-test-artifacts/pass12-help-tab-uia.png` | UIA selected the Help tab and captured the command surface |
| Catalog branch build baseline | No screenshot | `codex/ui-test-catalog` built successfully on 2026-05-21 from latest fetched `origin/main` with `dotnet build Freexcel.slnx -m:1 /nodeReuse:false -p:UseSharedCompilation=false`. |

## Blocked / Invalidated Smoke Attempts

| Attempt | Status | Notes |
| --- | --- | --- |
| 2026-05-21 catalog Wave 1 guarded live input | Blocked | Freexcel launched, but global keyboard/mouse focus was captured by an unrelated Microsoft Excel window. The generated screenshots were invalid and deleted. Future live input passes must verify foreground process/window title immediately before every global mouse or keyboard action, or use process-scoped UI Automation patterns only. |

## Session Notes

- Subagent coverage inventory found strong planner, parser, formatter, XAML, and command-status tests, but limited end-to-end WPF workflow coverage.
- High-risk manual gaps: keytip placement/routing, real WPF focus transitions, partial shortcut paths, dialog workflows, file picker/print/export flows, pivot UI, and visual fidelity.
- Test harness incident: a later automation pass failed to bring Freexcel above OneNote before sending input. Accidental OneNote input was immediately undone, and invalid OneNote screenshots were deleted from `docs/ui-test-artifacts`. Future passes must verify the foreground window title is `Book1 - Freexcel` before sending global keyboard input.
- Harness adjustment: subsequent passes use UI Automation invocation plus `PrintWindow` screenshots so Freexcel can be tested without stealing foreground focus. This works well for normal buttons/tabs, but popup/dropdown flyouts need a separate foreground-safe mouse-input strategy because they are not reliably captured through the owner window.
- Foreground-safe mouse limitation: Windows foreground locking later kept Codex in front, and the harness correctly aborted before sending mouse input. Further visual click testing should be done only when the foreground guard confirms a Freexcel-owned window title, or through a dedicated interactive runner.
- Harness targeting note: a name-only UIA lookup for `Insert` can hit the Home-ribbon Insert button before the top-level Insert tab. Future tab sweeps should filter for `ControlType.TabItem` plus name.
