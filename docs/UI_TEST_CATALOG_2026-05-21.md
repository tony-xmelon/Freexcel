# Freexcel UI Test Catalog

Generated: 2026-05-21
Branch: `codex/ui-test-catalog`
Baseline source: freshly fetched `origin/main` at worktree creation.

## Purpose

This is the comprehensive and append-only UI test catalog for Freexcel. It translates the command parity, shortcut parity, and WPF surface into an execution plan for mouse, keyboard, keytip, context-menu, dialog, and UI Automation testing, and it is also the single chronological place to record coverage status, findings, smoke checks, blocked attempts, and session notes.

Do not append new UI testing work to a separate coverage log. Every pass should update this catalog with which rows were exercised, what target was used, which command was expected, and which model/UI state proved the action worked.

## Coverage Contract

Every supported command should eventually have evidence for each applicable layer:

| Layer | Required proof |
|---|---|
| Visible surface | Button/menu/control is visible in the correct ribbon, backstage page, dialog, context menu, status bar, or grid state. |
| Mouse activation | Click, double-click, drag, wheel, resize, or menu selection triggers the expected command path. |
| Keyboard activation | Shortcut, access key, keytip sequence, tab traversal, Enter/Space, Escape, and accelerator behavior trigger or cancel correctly. |
| Command routing | The UI path reaches the intended host handler and command bus/model command where one exists. |
| State mutation | Workbook, sheet, selection, style, drawing, chart, pivot, table, view, file, or dialog state changes exactly as expected. |
| Undo/repeat | Undo/redo and F4 repeat are verified for commands that are meant to be undoable or repeatable. |
| Target breadth | The command is tested against every supported target class listed in the target matrix below. |
| Accessibility | Automation name/id, Invoke/Toggle/Selection/ExpandCollapse pattern, focus return, and disabled-state behavior are verified where applicable. |
| Persistence | Save/load or export output is checked when the command changes persisted workbook state. |

## Current Verification Baseline

| Check | Command | Result |
|---|---|---|
| Git state | `git status --short --branch` | Historical UI testing branch: `codex/testing`; existing modified `docs/PROJECT_STATUS_REPORT_2026-05-19.md` left untouched. Current catalog branch: `codex/ui-test-catalog`. |
| Worktrees | `git worktree list --porcelain` | Current checkout is an active session branch; no nested worktree created. |
| Build | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors. |
| Rebuild after worktree changed | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors. |
| Focused finding regression tests | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests\|FullyQualifiedName~KeyboardShortcutMatcherTests\|FullyQualifiedName~WorksheetContextMenuPlannerTests"` | Passed, 194 tests, 0 failures. |
| UIA dialog entry regression tests | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests"` | Passed, 68 tests, 0 failures. |
| UIA dialog entry regression recheck | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FullyQualifiedName~MainWindowXamlKeyTipTests" -m:1 /nodeReuse:false -p:UseSharedCompilation=false` | Passed, 74 tests, 0 failures. |
| Host regression suite | `dotnet test tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj` | Passed, 847 tests, 0 failures. |
| Current build | `dotnet build Freexcel.slnx -m:1` | Passed, 0 warnings, 0 errors. |
| Continuation UIA/mouse dialog pass | Fresh Debug build launched via `src\Freexcel.App.Host\bin\Debug\net10.0-windows10.0.19041.0\Freexcel.App.Host.exe`; UIA activation plus guarded mouse clicks where foreground was verified. | Account and About opened by foreground-confirmed mouse clicks. UIA `InvokePattern` still returned success for Insert Function/About without opening a dialog before the fix. |
| Catalog branch build baseline | `dotnet build Freexcel.slnx -m:1 /nodeReuse:false -p:UseSharedCompilation=false` | Passed on 2026-05-21 from latest fetched `origin/main`. |

## Coverage Model

Each surface is tracked with these states:

| State | Meaning |
|---|---|
| Not Started | No current manual pass in this session. |
| In Progress | One or more paths tested, more expected. |
| Passed | Smoke path passed with no issue observed. |
| Finding | One or more issues recorded below. |
| Blocked | Could not test because of environment, missing data, modal/system dependency, focus safety, or crash. |
| Excluded | Intentionally out of scope for Freexcel or delegated to operating-system/native UI. |

## Inventory Snapshot

| Source | Current count | Notes |
|---|---:|---|
| Command surface in-scope rows | 182 | From `COMMAND_INVENTORY.json`: Implemented + Partial command-surface rows. |
| Menu/toolbar in-scope rows | 183 | Includes the current Draw tab menu/toolbar delta. |
| Top-level ribbon/backstage tabs | 10 | File, Home, Insert, Draw, Page Layout, Formulas, Data, Review, View, Help. |
| XAML click handlers | 495 | Unique `Click="..."` handlers in `MainWindow.xaml`. |
| Keyboard command shortcut usages | 68 matcher rules / 67 dispatcher targets | Matcher includes non-dispatcher surfaces such as insert/delete, number formats, font toggles, borders, and grid selection paths. |
| Documented shortcut rows | 81 | From `SHORTCUT_PARITY_MATRIX.md`: 69 parity, 12 partial. |
| Worksheet context menu commands | 46 | From `WorksheetContextMenuPlanner.BuildCommands()`. |
| Existing UI evidence screenshots | 55 | Current `docs/ui-test-artifacts` images from prior passes. |

## Target Matrix

Each command should be tested against every applicable target. Mark non-applicable targets explicitly instead of leaving them ambiguous.

| Target class | Required variants |
|---|---|
| Cell | blank, value, formula, error, date/time, formatted, protected locked/unlocked. |
| Range | single cell, contiguous range, multi-area selection, whole row, whole column, whole sheet, current region, visible-cells-only filtered range. |
| Sheet | first/middle/last sheet, hidden/very hidden where supported, grouped sheets, chart sheet, renamed sheet, colored tab. |
| Table | plain range, structured table with headers, totals row, filtered table, styled table. |
| PivotTable | row fields, column fields, value fields, page filters, empty intersections, contextual Analyze/Design tabs, field list. |
| Chart | embedded chart, chart sheet, PivotChart, selected series/point/axis/title/legend/plot area/chart area. |
| Drawing object | picture, shape, text box, selected object, multi-object selection where supported, cropped/rotated/resized object. |
| Sparkline | line/column/win-loss groups, selected sparkline range, hidden row/column interactions. |
| Slicer/timeline | active slicer, active timeline, connected PivotTable, selected/cleared items. |
| Workbook/file | unsaved workbook, saved XLSX, CSV, unsupported-feature XLSX, read/write path, missing file, print/export output. |
| View state | normal/page layout/page break, frozen panes, split panes, zoom levels, hidden headings/gridlines/formula bar. |
| Dialog state | default values, changed values, invalid input, OK, Cancel, Escape, access keys, focus order. |

## Interaction Channels

| Channel | Scope |
|---|---|
| Mouse | Ribbon buttons, dropdown arrows, menu items, grid click/drag, fill handle, column/row resize, sheet tabs, status zoom, dialogs, backstage navigation. |
| Keyboard shortcut | All rows in `SHORTCUT_PARITY_MATRIX.md`, with exact-modifier rejection where documented. |
| Ribbon keytips | Alt/F10 top-level badges, tab badges, QAT badges, command badges, dropdown menu keytips, nested Conditional Formatting menu keytips, Escape cancellation. |
| Access keys | Dialog mnemonic labels, menu headers, backstage commands, context menus, OK/Cancel/Apply-style button rows. |
| Context menu | Worksheet right-click, Shift+F10, Menu key, sheet-tab context menu, pivot field context menu, chart/PivotChart field menus, object-aware variants. |
| UI Automation | Stable AutomationId/Name, Invoke/Toggle/Selection/ExpandCollapse patterns, focus movement, top-level owned dialog detection. |
| Direct model verification | Use command bus state, workbook model assertions, saved file inspection, or existing unit tests to confirm non-visual effects. |

## Inspected Surface Inventory

| Surface | Catalog notes |
|---|---|
| Shortcut/keytip routing | 81 documented shortcut rows; 68 matcher rules; 67 dispatcher targets; broad XAML keytip metadata including top-level `F/H/N/J/P/M/A/R/W/Y` plus contextual PivotTable `JA/JD`; representative nested menu keytip coverage exists, but all partial shortcut rows still need hands-on UI passes. |
| Mouse/grid interaction | Grid click, Shift+click, drag selection, double-click edit/pivot detail, row/column/top-left header selection, autofill handle, row/column resize, page-layout margin guide drag, split divider drag, split-pane mini-scrollbars, pivot chart field buttons, wheel/Shift+wheel/Ctrl+wheel, and sheet-tab click/group/drag/double-click/right-click all need live WPF hit-test evidence. |
| Context menus | Worksheet context menu has 46 planner commands and should be tested through right-click, Shift+F10, Menu key, access-key traversal, target-specific disabled states, and command state mutation. Sheet-tab, pivot field, ribbon dropdown, backstage recent/pinned, and object-aware context menus need separate rows. |
| Ribbon/backstage/dialogs | Backstage, QAT, Home, Insert, Draw, Page Layout, Formulas, Data, Review, View, contextual PivotTable Analyze/Design, and Help are fully inventoried in parity docs. Dialog coverage is strong at parser/planner level but needs real focus order, access keys, Escape/Enter/default/cancel, high-DPI layout, and UIA pattern checks. |
| System-dependent flows | Open/Save file dialogs, picture/background import, CSV Get Data, PDF/XPS export save dialogs, Windows Share, browser Help/Feedback links, and print dialogs require guarded environment-aware manual testing. |

## Live Input Safety Rule

Before any global keyboard or mouse input, verify that the foreground window belongs to the launched Freexcel process and that the window title matches the expected workbook. Re-check this before every click, drag, wheel, or key sequence. If any other application owns foreground focus, mark the attempt Blocked and discard any screenshots from that attempt.

## Command Families

| Area | Surfaces to exercise | Required target breadth | Existing automated coverage | Manual/UI gaps |
|---|---|---|---|---|
| App shell and title bar | Launch, QAT Save/Undo/Redo, custom title buttons, window focus/activation. | Unsaved workbook, saved workbook, maximized/restored window. | App host source hygiene and QAT/keytip tests. | Real window chrome clicks, Alt+Space/system behavior, focus after modal closure. |
| File/backstage | New, Open, Save, Save As, Print, Export, Info, Share, Account, Options, Recent/Pinned, Close, Back. | Unsaved/saved file, missing recent file, unsupported XLSX, print/export scopes. | Backstage automation/keytip/source tests; print/export planner tests. | Native file dialogs, guarded mouse clicks, UIA Invoke on every backstage command, output file inspection for PDF/XPS. |
| Formula bar/name box | Name box navigation, formula entry, `fx`, expand/collapse, formula edit references. | Named range, A1/R1C1, cross-sheet refs, long formula, invalid reference. | Cell entry/parser, formula reference and edit planner tests. | Mouse focus into name box/formula bar, F2/Ctrl+F2 parity, visual reference highlight confirmation. |
| Worksheet grid | Selection, navigation, entry, edit, autofill, fill handle, resize, scroll, split/freeze, page layout margins. | Target matrix cell/range/view variants. | Selection/navigation/edit/viewport/grid planner tests. | Real drag selection, fill handle drag, resize mouse hit testing, wheel/trackpad scroll, page layout visual checks. |
| Home clipboard | Cut, Copy, Paste, Paste Special, Format Painter. | Internal/external text, formulas, styles, comments, validation, images, overlapping/non-overlapping cut paste. | Clipboard/paste planner and command tests. | Real clipboard formats, mouse paste dropdown, persistent Format Painter double-click and Escape cancel. |
| Home font/alignment/number/styles | Font, size, bold/italic/underline, colors, borders, alignment, merge, number formats, CF, Format as Table, Cell Styles. | Blank/value/formula/range/table/protected cells, themed workbook. | Style model, dialogs, planners, source hygiene tests. | Dropdown galleries by mouse/keytip, visual swatches, applied rendering across grid and saved XLSX. |
| Home cells/editing | Insert/delete cells/rows/cols/sheets, row/column size, hide/unhide, AutoSum, fill, Flash Fill, clear, sort/filter, find/replace/go-to. | Rows, columns, tables, filtered ranges, notes/comments, formulas. | Planner/command/filter/find tests. | Modal prompts through keyboard/mouse, F4 repeat, focus return, visible row/column state. |
| Insert | PivotTable, Table, charts, sparklines, pictures, shapes, text box, symbol, hyperlink, comment/note. | Range/table/pivot/chart/object targets. | Dialog parser/planner and chart/pivot tests. | End-to-end insert workflows, object selection handles, chart sheet activation, symbol picker mouse/keyboard. |
| Draw/object formatting | Shapes, ordering, size/rotate, fill/outline/effects, crop/reset crop, alt text. | Picture, shape, text box, selected chart/drawing object. | Drawing target/input parser and object dialog tests. | Mouse selection/drag handles, object context states, visual rendering after changes. |
| Page Layout | Themes, margins, orientation, size, print area, breaks, background, print titles, scale, sheet options, arrange. | Normal/page layout/page break views, saved print settings, exported output. | Page layout parser/dialog and print model tests. | Dialog tab traversal, live page layout visuals, print/export smoke. |
| Formulas | Insert Function, AutoSum categories, names, auditing, show formulas, error checking, evaluate, watch window, calculation. | Formula/value/error/cross-sheet refs, named ranges, watched cells. | Formula planner/dialog/error-checking tests. | Real Formula Auditing arrows, Watch Window add/delete/refresh, Evaluate Formula modal flow. |
| Data | Get data/import, refresh, sort/filter, Advanced Filter, Text to Columns, Remove Duplicates, Validation, Consolidate, What-If, Outline. | Tables, filtered ranges, grouped rows/columns, validation lists, scenario/data-table targets. | Data dialog parsers/planners and command tests. | Real dropdown filter UI, drag selected ranges into dialogs, grouped outline buttons, import/native file dialogs. |
| Review | Spelling, Accessibility, comments/notes, protect sheet/workbook/ranges, workbook statistics, share messages. | Notes/threaded comments, locked cells, protected sheet/workbook, issue-bearing workbook. | Spell check, accessibility/protection/workbook stats tests. | Dialog workflows by mouse/keyboard, protected-state disabled commands, UIA names. |
| View | Workbook views, show toggles, freeze/split panes, zoom, arrange/window commands, custom views. | View-state matrix, hidden gridlines/headings/formula bar, multiple sheets. | View command and arrangement planner tests. | Real status zoom slider/buttons, split-pane drag, frozen pane visuals, custom view round trip. |
| Help | Help Online, Send Feedback, About. | Online launch blocked/allowed environment, About dialog. | Help/about UIA and source tests. | Guarded external process checks, About dialog focus/accessibility. |
| Contextual PivotTable/PivotChart | Analyze/Design tabs, field list, filters, value settings, PivotChart buttons. | Pivot target matrix, slicer/timeline, chart field buttons. | Pivot planner/dialog/slicer/timeline tests. | Contextual tab visibility, field-list drag/drop, field button mouse menus. |
| Worksheet context menu | 46 planner commands via right-click, Shift+F10, Menu key. | Cell/range/row/column/table/filter/comment targets. | Worksheet context menu planner and source routing tests. | Every menu item by mouse and keyboard access key, disabled/hidden states by target. |
| Sheet tab strip | Add, rename, duplicate, delete, move, hide/unhide, color, group/ungroup, navigation arrows. | First/middle/last/hidden/grouped sheets. | Sheet tab service/planner tests where present. | Real tab drag/reorder, right-click menu, overflow arrows, grouped sheet commands. |
| Status bar | Ready text, selection stats, zoom out/in/slider, view hints. | Single/range numeric/text selection, formula/error cells, zoom min/max. | Status/stat planner tests. | Mouse click/drag slider, live stat update, accessibility names. |
| Dialog catalog | All modal and modeless dialogs from ribbon/context/backstage. | Valid/default/invalid/cancel states for every input field. | Parser/planner tests for most dialogs. | End-to-end keyboard tab order, access keys, UIA patterns, layout screenshots. |

## Full UI Surface Coverage

| Area | Status | Manual Scope |
|---|---|---|
| App launch and shell | In Progress | Process launch, main window render, custom title bar, QAT Save/Undo/Redo, minimize/maximize/close. |
| File/backstage/start overlay | In Progress | File tab, Home/Info/New/Open/Save/Save As/Print/Export/Account/Options/Close, recent/pinned list. |
| Formula bar and name box | In Progress | Name box navigation, formula entry, `fx` Insert Function, expand/collapse formula bar. |
| Worksheet grid core | In Progress | Cell selection, drag selection, data entry, inline edit, formula edit, navigation, undo/redo. |
| Home ribbon | In Progress | Clipboard, Paste Special, Format Painter, font, fill, border, alignment, number formats, styles, cells, editing. |
| Insert ribbon | In Progress | PivotTable, Table, charts, sparklines, pictures, shapes, text box, symbols, hyperlink, comments. |
| Draw ribbon | In Progress | Shapes, ordering, size/rotation, fill/outline, alt text, crop/effects prompts. |
| Page Layout ribbon | In Progress | Margins, orientation, paper, print area, breaks, background, print titles, scale, themes, page setup. |
| Formulas ribbon | In Progress | Insert Function, AutoSum/categories, names, auditing, error checking, evaluate, watch window, calculation. |
| Data ribbon | In Progress | Import, refresh, sort/filter, Advanced Filter, Text to Columns, Remove Duplicates, Validation, What-If, outline. |
| Review ribbon | In Progress | Spell Check, Accessibility, comments/notes, protections, sharing messages, workbook statistics. |
| View ribbon | In Progress | Workbook views, show toggles, freeze/split panes, zoom, arrange/window commands. |
| Help ribbon | In Progress | Help, feedback, About and excluded/help messaging. |
| Contextual PivotTable tabs | Not Started | Analyze/Design visibility, field list, filters, value settings, contextual commands. |
| Worksheet context menu | In Progress | Shift+F10/Menu key/right-click, clipboard, insert/delete, sort/filter, notes, hyperlink, Format Cells, clear commands. |
| Sheet tab strip/context menu | In Progress | Add, rename, duplicate, delete, move, color, hide/unhide, grouping, tab navigation. |
| Status bar and zoom | In Progress | Ready/status text, selection stats, zoom buttons, slider, keyboard/mouse-wheel zoom. |
| Dialog catalog | In Progress | Format Cells, Find/Replace, Data Validation, Page Setup, Options, Names, CF manager, Goal Seek, Custom Views, pivot filters, Evaluate Formula, Watch Window, Theme, Symbol picker. |
| Keyboard shortcuts | In Progress | Shortcut matrix high-risk paths: Ctrl+P, Ctrl+V/Ctrl+Alt+V, Ctrl+1, Ctrl++/Ctrl+-, Alt+Down, Ctrl+Q, Shift+F10, F4 repeat. |
| Ribbon keytips | In Progress | Alt/F10 overlay, tab keytips, QAT keytips, visible command keytips, menu/nested menu keytips, Escape cancellation. |
| Accessibility and focus | In Progress | Keyboard-only traversal, focus return after dialogs, visible focus indicators, screen-reader naming smoke. |
| Visual fidelity | In Progress | Ribbon density, overlay placement, dialog layout, grid rendering, chart/drawing rendering, split/freeze visual behavior. |
| File IO and interop smoke | Not Started | Open/save round trip with representative XLSX/CSV, unsupported feature warnings, export output behavior. |

## First-Pass Test Queue

1. Launch latest Debug build and capture process/window state.
2. Exercise File/backstage: create blank workbook, Options, Account, Print/Export messages, return to workbook.
3. Exercise worksheet grid: type values/formulas, edit with F2/formula bar, navigate with Enter/Tab/arrows, undo/redo.
4. Exercise Home ribbon: bold/italic/underline, fill/font color prompts, borders menu, number format, merge, Find/Replace, Format Cells.
5. Exercise keyboard/keytips: Alt/F10 top-level tabs, Home command keytips, Escape, Shift+F10 worksheet menu, Ctrl+1.
6. Exercise sheet tabs/status: add/rename/duplicate/move/color/hide/unhide sheets, zoom controls.
7. Record findings immediately with reproduction, expected behavior, actual behavior, severity, and evidence.

## Execution Waves

| Wave | Goal | Exit criteria |
|---|---|---|
| 0. Inventory guard | Keep catalog in sync with code. | Counts for XAML click handlers, shortcuts, context menu commands, command inventory, and docs are updated. |
| 1. Launch/shell/backstage | Prove app starts and global surfaces work. | Latest build launches, shell renders, File/QAT/title/status basics pass by mouse and keyboard. |
| 2. Keyboard/keytips | Prove command access without mouse. | All shortcut matrix rows and top-level/keyed ribbon paths are either passed, partial with finding, or explicitly blocked. |
| 3. Home/grid/core editing | Prove common spreadsheet work. | Cell/range/row/column/sheet targets pass for selection, editing, formatting, clipboard, insert/delete, undo/redo, F4. |
| 4. Ribbon tab sweep | Exercise every visible command by tab. | Every in-scope command row has at least one mouse activation, one keyboard/keytip/access-key path where applicable, and state proof. |
| 5. Contextual/object surfaces | Cover targets that appear only after selection. | PivotTable, chart, drawing, table, slicer/timeline, sparkline, and sheet-tab contextual surfaces are covered. |
| 6. Dialog catalog | Cover every modal/modeless dialog. | Each dialog has default, changed, invalid, OK, Cancel/Escape, access-key, focus-order, and UIA evidence. |
| 7. Persistence/output | Prove command effects survive IO. | Relevant actions are verified through save/load, CSV/XLSX/native JSON, PDF/XPS, print preview, or screenshot evidence. |
| 8. Regression closure | Convert findings into automated guards. | Each fixed bug has a focused unit/source/UIA test and a retest entry in the coverage log. |

## Per-Command Record Template

Use this table shape in follow-up passes when recording detailed rows:

| Field | Value |
|---|---|
| Catalog ID | `UI-CAT-AREA-NNN` |
| Command | Visible command name and source doc row. |
| Surfaces | Mouse, shortcut, keytip, access key, context menu, UIA. |
| Targets | Applicable target-matrix entries. |
| Expected command route | Host handler and model command/planner where known. |
| Expected result | State mutation, visual change, dialog, output, or persisted package change. |
| Evidence | Screenshot, test command, model assertion, saved file path, or finding ID. |
| Status | Not Started, In Progress, Passed, Partial, Finding, Blocked, Excluded. |

## Findings Log

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

Expected: Backstage returns to the workbook, matching the normal keyboard escape route from a temporary full-window command surface.

Actual: The keytip badges clear after the first Escape, but the File backstage remains visible after a second Escape. The only observed visual route back is the back arrow.

### UI-2026-05-19-002: F10 does not visibly enter ribbon keytip mode from the worksheet

Severity: P2
Status: Fixed
Evidence: `docs/ui-test-artifacts/keytips-f10.png`
Fix: `MainWindow` handles `F10` during `PreviewKeyDown`, before worksheet focus can consume it, and enters top-level ribbon keytip mode.
Verification: `MainWindowXamlKeyTipTests.MainWindowPreviewKeys_HandleWorksheetKeytipAndContextMenuEntryPoints` plus existing shortcut/keytip tests.

Repro:

1. Launch Freexcel and keep focus on the worksheet.
2. Press `F10`.

Expected: Ribbon keytip badges appear for the top-level tabs and QAT, as documented in `docs/SHORTCUT_PARITY_MATRIX.md`.

Actual: No keytip badges appeared in the captured worksheet view. `Alt+F` did open File backstage with keytip badges, so the keytip system was present but this entry path needed a focused retest/fix.

### UI-2026-05-19-003: Shift+F10 did not open the worksheet context menu in the initial pass

Severity: P2
Status: Fixed after recheck
Evidence: `docs/ui-test-artifacts/worksheet-context-menu.png`
Fix: `MainWindow` handles `Shift+F10` during `PreviewKeyDown` and routes it through the existing worksheet context menu command path.
Verification: `MainWindowXamlKeyTipTests.MainWindowPreviewKeys_HandleWorksheetKeytipAndContextMenuEntryPoints`, `KeyboardShortcutMatcherTests`, and `WorksheetContextMenuPlannerTests`.

Repro:

1. Select a worksheet cell.
2. Press `Shift+F10`.

Expected: Worksheet context menu opens from the active cell.

Actual: No context menu appeared in the captured worksheet view. This needed a focused recheck using a verified foreground Freexcel window before filing as a product bug.

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

Expected: The visible `Options` command exposes an activation pattern, such as `InvokePattern`, matching its role as a clickable command and supporting accessibility/test automation.

Actual: The visible `Options` element was found by name, but it exposed no Invoke, Select, or ExpandCollapse pattern. A UIA activation attempt failed with `No invoke/select/expand pattern for Options`.

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

Expected: The visible `Account` command exposes an activation pattern, such as `InvokePattern`, matching its role as a clickable backstage navigation command.

Actual: The visible `Account` element exposed only `SynchronizedInputPattern` and no Invoke, Select, or ExpandCollapse pattern in the UIA pass. A guarded foreground mouse click did open the Account informational dialog, so this was scoped to accessibility/test automation rather than the visual click path.

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

Expected: Each dialog entry point opens its corresponding dialog, and the dialog appears as a top-level owned window in the Freexcel process.

Actual: `Insert Function` and `About Freexcel` both exposed activation patterns and returned from UIA activation, but no additional Freexcel top-level dialog appeared. Later mouse checks proved the visual click path worked, while UI Automation activation needed the fix above.

## Passed Smoke Checks

| Check | Evidence | Notes |
|---|---|---|
| App launch renders main shell | `docs/ui-test-artifacts/launch-shell.png` | Title bar, QAT, Home ribbon, formula bar, grid, sheet tab strip, and status bar visible. |
| Grid accepts typed numeric input | `docs/ui-test-artifacts/grid-entry.png` | Initial coordinate calibration clicked B7 instead of A1, but keyboard data entry and Enter navigation worked. |
| `Ctrl+1` opens Format Cells | `docs/ui-test-artifacts/format-cells-dialog.png` | Dialog opens on Number tab and shows tab strip through Protection. |
| File backstage opens via `Alt+F` | `docs/ui-test-artifacts/file-backstage.png` | Backstage displays Home/New/Recent/Pinned and keytip badges. |
| File backstage Back returns to workbook | `docs/ui-test-artifacts/pass2-file-back-uia.png` | UIA found and invoked the `Back` control successfully. |
| Sheet insertion works from UIA | `docs/ui-test-artifacts/pass2-add-sheet.png` | Invoking `Insert Sheet` created and selected `Sheet2`. |
| Zoom buttons work from UIA | `docs/ui-test-artifacts/pass2-zoom-in.png`, `docs/ui-test-artifacts/pass2-zoom-out.png` | Zoom changed through the status bar controls and returned near baseline. |
| Data ribbon renders | `docs/ui-test-artifacts/pass5-data-tab.png` | Top-level Data commands visible; several detailed commands are under collapsed dropdown groups at this width. |
| Insert ribbon renders | `docs/ui-test-artifacts/pass5-insert-tab.png` | PivotTable, Table, Pivot refresh, Charts, Sparklines, Links & Objects visible. |
| View ribbon renders | `docs/ui-test-artifacts/pass5-view-tab.png` | View controls captured for follow-up interaction testing. |
| Review ribbon renders | `docs/ui-test-artifacts/pass5-review-tab.png` | Review controls captured for follow-up interaction testing. |
| Backstage Account opens by mouse | `docs/ui-test-artifacts/pass10-account-mouse.png` | Foreground-confirmed mouse click opened the Account informational dialog. |
| Help tab renders and About opens by mouse | `docs/ui-test-artifacts/pass10-help-tab-mouse.png`, `docs/ui-test-artifacts/pass10-about-mouse.png` | Foreground-confirmed mouse click opened the About Freexcel dialog. |
| Help tab selects by UI Automation | `docs/ui-test-artifacts/pass11b-help-activation.png` | `SelectionItemPattern.Select` switched to the Help tab on the latest clean build. |
| Draw ribbon renders on latest build | `docs/ui-test-artifacts/pass12-draw-tab-uia.png` | UIA selected the Draw tab and captured the command surface. |
| Page Layout ribbon renders on latest build | `docs/ui-test-artifacts/pass12-page-layout-tab-uia.png` | UIA selected the Page Layout tab and captured the command surface. |
| Formulas ribbon renders on latest build | `docs/ui-test-artifacts/pass12-formulas-tab-uia.png` | UIA selected the Formulas tab and captured the command surface. |
| Data/Review/View ribbons render on latest build | `docs/ui-test-artifacts/pass12-data-tab-uia.png`, `docs/ui-test-artifacts/pass12-review-tab-uia.png`, `docs/ui-test-artifacts/pass12-view-tab-uia.png` | UIA selected each tab and captured the command surface. |
| Help ribbon renders on latest build | `docs/ui-test-artifacts/pass12-help-tab-uia.png` | UIA selected the Help tab and captured the command surface. |
| Catalog branch build baseline | No screenshot | `codex/ui-test-catalog` built successfully on 2026-05-21 from latest fetched `origin/main` with `dotnet build Freexcel.slnx -m:1 /nodeReuse:false -p:UseSharedCompilation=false`. |

## Blocked / Invalidated Smoke Attempts

| Attempt | Status | Notes |
|---|---|---|
| 2026-05-21 catalog Wave 1 guarded live input | Blocked | Freexcel launched, but global keyboard/mouse focus was captured by an unrelated Microsoft Excel window. The generated screenshots were invalid and deleted. Future live input passes must verify foreground process/window title immediately before every global mouse or keyboard action, or use process-scoped UI Automation patterns only. |

## Session Notes

- Subagent coverage inventory found strong planner, parser, formatter, XAML, and command-status tests, but limited end-to-end WPF workflow coverage.
- High-risk manual gaps: keytip placement/routing, real WPF focus transitions, partial shortcut paths, dialog workflows, file picker/print/export flows, pivot UI, and visual fidelity.
- Test harness incident: a later automation pass failed to bring Freexcel above OneNote before sending input. Accidental OneNote input was immediately undone, and invalid OneNote screenshots were deleted from `docs/ui-test-artifacts`. Future passes must verify the foreground window title is `Book1 - Freexcel` before sending global keyboard input.
- Harness adjustment: subsequent passes use UI Automation invocation plus `PrintWindow` screenshots so Freexcel can be tested without stealing foreground focus. This works well for normal buttons/tabs, but popup/dropdown flyouts need a separate foreground-safe mouse-input strategy because they are not reliably captured through the owner window.
- Foreground-safe mouse limitation: Windows foreground locking later kept Codex in front, and the harness correctly aborted before sending mouse input. Further visual click testing should be done only when the foreground guard confirms a Freexcel-owned window title, or through a dedicated interactive runner.
- Harness targeting note: a name-only UIA lookup for `Insert` can hit the Home-ribbon Insert button before the top-level Insert tab. Future tab sweeps should filter for `ControlType.TabItem` plus name.

## Current High-Risk Gaps

| Gap | Why it matters |
|---|---|
| Real WPF end-to-end coverage is still thinner than planner/parser coverage. | Unit tests prove command planning, but mouse/focus/menu automation can still fail in the real window. |
| Dropdown galleries and nested menus need systematic mouse/keytip passes. | The XAML contains hundreds of click handlers; grouped menus are where command routing commonly drifts. |
| Target-specific command behavior needs explicit coverage. | A command that works on a single cell can still fail on rows, columns, filtered ranges, tables, pivots, charts, or protected sheets. |
| Modal dialogs need access-key/focus/UIA sweeps. | Many dialog parser tests exist, but keyboard users and UI automation depend on WPF wiring and focus return. |
| Object and contextual surfaces need selection-state coverage. | Chart, PivotTable, table, drawing, slicer/timeline, and sparkline commands are invisible until the correct object is active. |
| Persistence checks should be attached to UI actions. | Formatting, page setup, charts, pivots, tables, and protection need save/load proof, not just visual proof. |

## Next Catalog Tasks

1. Generate a machine-readable row list from `COMMAND_SURFACE_PARITY.md`, `MENU_TOOLBAR_PARITY.md`, `SHORTCUT_PARITY_MATRIX.md`, `WorksheetContextMenuPlanner.cs`, and `MainWindow.xaml` so future passes can mark row-level status.
2. Add a UI automation harness that launches the latest Debug build, snapshots visible controls by AutomationId/Name/control type, and compares them against this catalog.
3. Start Wave 1 and Wave 2 on the latest build, recording every pass/finding in this catalog.
4. For each finding, add a focused automated guard when the bugfixing session closes it.
