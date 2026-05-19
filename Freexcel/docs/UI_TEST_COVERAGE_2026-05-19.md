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
| Formula bar and name box | Not Started | Name box navigation, formula entry, `fx` Insert Function, expand/collapse formula bar |
| Worksheet grid core | In Progress | Cell selection, drag selection, data entry, inline edit, formula edit, navigation, undo/redo |
| Home ribbon | In Progress | Clipboard, Paste Special, Format Painter, font, fill, border, alignment, number formats, styles, cells, editing |
| Insert ribbon | In Progress | PivotTable, Table, charts, sparklines, pictures, shapes, text box, symbols, hyperlink, comments |
| Draw ribbon | Not Started | Shapes, ordering, size/rotation, fill/outline, alt text, crop/effects prompts |
| Page Layout ribbon | Not Started | Margins, orientation, paper, print area, breaks, background, print titles, scale, themes, page setup |
| Formulas ribbon | Not Started | Insert Function, AutoSum/categories, names, auditing, error checking, evaluate, watch window, calculation |
| Data ribbon | In Progress | Import, refresh, sort/filter, Advanced Filter, Text to Columns, Remove Duplicates, Validation, What-If, outline |
| Review ribbon | In Progress | Spell Check, Accessibility, comments/notes, protections, sharing messages, workbook statistics |
| View ribbon | In Progress | Workbook views, show toggles, freeze/split panes, zoom, arrange/window commands |
| Help ribbon | Not Started | Help, feedback, About and excluded/help messaging |
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
Fix: `MainWindow` now handles bare Escape while Backstage is visible and returns focus to the workbook before running normal transient-mode cancellation.
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
Fix: `MainWindow` now handles `F10` during `PreviewKeyDown`, before the focused worksheet grid can consume it, and enters top-level ribbon keytip mode.
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
Fix: `MainWindow` now handles `Shift+F10` during `PreviewKeyDown` and routes it through the existing worksheet context menu command path.
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
Fix: The Backstage Options command now has an explicit `x:Name`, `AutomationProperties.Name`, help text, and tab-stop contract while retaining the normal button `Click` handler.
Verification: `MainWindowXamlKeyTipTests.BackstageOptionsEntryPoint_IsNamedCommandForUiAutomation`.

Repro:
1. Launch Freexcel.
2. Open File backstage.
3. Inspect or activate the visible `Options` item through UI Automation.

Expected:
The visible `Options` command exposes an activation pattern, such as `InvokePattern`, matching its role as a clickable command and supporting accessibility/test automation.

Actual:
The visible `Options` element was found by name, but it exposed no Invoke, Select, or ExpandCollapse pattern. A UIA activation attempt failed with `No invoke/select/expand pattern for Options`.

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

## Session Notes

- Subagent coverage inventory found strong planner, parser, formatter, XAML, and command-status tests, but limited end-to-end WPF workflow coverage.
- High-risk manual gaps: keytip placement/routing, real WPF focus transitions, partial shortcut paths, dialog workflows, file picker/print/export flows, pivot UI, and visual fidelity.
- Test harness incident: a later automation pass failed to bring Freexcel above OneNote before sending input. Accidental OneNote input was immediately undone, and invalid OneNote screenshots were deleted from `docs/ui-test-artifacts`. Future passes must verify the foreground window title is `Book1 - Freexcel` before sending global keyboard input.
- Harness adjustment: subsequent passes use UI Automation invocation plus `PrintWindow` screenshots so Freexcel can be tested without stealing foreground focus. This works well for normal buttons/tabs, but popup/dropdown flyouts need a separate foreground-safe mouse-input strategy because they are not reliably captured through the owner window.
