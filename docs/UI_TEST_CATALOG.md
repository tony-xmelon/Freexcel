# Freexcel UI Test Catalog

Last updated: 2026-05-22
Canonical path: `docs/UI_TEST_CATALOG.md`
Branch: `codex/ui-test-catalog`
Baseline source: synced from latest `origin/main` before each catalog update.

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
| XAML click-wired controls | 586 | `Click="..."` occurrences in `MainWindow.xaml` on latest synced `origin/main`. |
| Keyboard command shortcut usages | 68 matcher rules / 67 dispatcher targets | Matcher includes non-dispatcher surfaces such as insert/delete, number formats, font toggles, borders, and grid selection paths. |
| Documented shortcut rows | 81 | From `SHORTCUT_PARITY_MATRIX.md`: 69 parity, 12 partial. |
| Worksheet context menu commands | 46 | From `WorksheetContextMenuPlanner.BuildCommands()`. |
| Existing UI evidence screenshots | 55 | Current `docs/ui-test-artifacts` images from prior passes; append new evidence paths to the relevant row. |

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
| Draw/object formatting | Shapes, ordering, size/rotate with default numeric-input focus, fill/outline/effects, crop/reset crop with left-crop focus, alt text. | Picture, shape, text box, selected chart/drawing object. | Drawing target/input parser and object dialog tests. | Mouse selection/drag handles, object context states, visual rendering after changes. |
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
| Insert ribbon | In Progress | PivotTable, Table, charts, sparklines, pictures, shapes, text box, symbols, hyperlink with address-box default focus, comments. |
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

## Catalog Row Index

Append test results against these row IDs. A row is not complete until mouse, keyboard/keytip/access-key, UI Automation where applicable, target breadth, command route, visible result, and persistence proof are either passed or explicitly marked not applicable.

| Catalog ID | Area | Commands / controls | Required interaction paths | Targets / states | Required proof | Status |
|---|---|---|---|---|---|---|
| UI-CAT-SHELL-001 | Launch/title/QAT | Process launch, workbook title, Save, Undo, Redo, custom minimize/maximize/close. | Mouse, Alt+Space/system menu, QAT keytips, UIA invoke. | Unsaved workbook, saved workbook, maximized/restored window, dirty/clean undo stack. | Shell renders, focus lands in grid, QAT Undo/Redo enabled states are command-stack backed, title updates after save/rename. | In Progress |
| UI-CAT-SHELL-002 | Ribbon chrome | Tab selection, collapsed group overflow, keyboard focus, high-DPI/resize behavior. | Mouse tab click, F6/Shift+F6 shell focus cycling, Ctrl+F6 where supported, Alt/F10 keytips, Tab/Shift+Tab traversal, focused-ribbon arrow and Home/End traversal. | Narrow width, normal width, maximized, active contextual tab. | Correct tab/group visible, overflow menu preserves checked/input-gesture state, F6 skips regions that reject focus, focus indicator remains visible. | In Progress |
| UI-CAT-FILE-001 | Backstage navigation | File Home/Info/New/Open/Save/Save As/Print/Export/Share/Account/Options/Close/Back. | Mouse, Alt+F keytips, Tab/Ctrl+Tab containment, F6/Shift+F6 containment, access keys, Escape, sidebar Up/Down/Home/End traversal, Shift+F10 recent/pinned row menus with first-item focus, UIA invoke. | Unsaved, saved local path, missing recent file, unsupported-feature workbook. | Correct page/dialog opens, File/Backstage focus lands on Home navigation for keyboard continuation, disabled/excluded commands explain state, Escape/Back returns focus to workbook, F6 does not move focus behind the overlay. | In Progress |
| UI-CAT-FILE-002 | Print/export | Print Preview, PDF/XPS export options, page ranges, open-after-publish, document properties. | Backstage mouse/keytip/access keys, dialog Tab/Enter/Escape, guarded native save dialog. | Active sheet, selected range, entire visible workbook, extensionless `.pdf`, explicit `.xps`, invalid path/page range. | Output file exists, metadata embedded, invalid input blocked, preview toolbar and close return focus. | Not Started |
| UI-CAT-GRID-001 | Grid selection/navigation | Cell/range/row/column/sheet selection, arrows, Tab, Enter, Home/End, Ctrl variants. | Mouse click/drag, Shift+click, keyboard shortcuts, name box navigation. | Blank/value/formula/error cells, whole row/column, multi-area where supported, filtered visible rows. | Selection model, name box, formula bar, status stats, and visual highlight all agree. | In Progress |
| UI-CAT-GRID-002 | Editing/formula entry | Type values/formulas, F2 edit, formula bar edit, reference highlighting, cancel/commit. | Mouse into grid/formula bar, keyboard, Enter/Tab/Escape, Ctrl+Enter where supported. | Long text, formula, cross-sheet reference, invalid formula, date/time, protected locked/unlocked cell. | Value/formula stored correctly, undo/redo works, invalid input messaging/focus recovery matches expectation. | In Progress |
| UI-CAT-GRID-003 | Pointer mechanics | Autofill handle, row/column resize, page-layout margins, split dividers, wheel/Shift+wheel/Ctrl+wheel. | Drag, double-click, wheel, keyboard fallback. | Normal/page layout/page break views, frozen panes, split panes, zoom min/max. | Hit targets respond only at correct edges, layout persists, scroll/zoom/status update correctly. | Not Started |
| UI-CAT-HOME-001 | Clipboard | Cut, Copy, Paste, Paste dropdown, Paste Special, Format Painter single/double-click. | Mouse, Ctrl+X/C/V, Ctrl+Alt+V, initial Paste Special focus, menu keytips, dialog access keys. | Values, formulas, formats, comments/notes, validation, tables, overlapping cut/paste, external text. | Clipboard effects, undo stack, cut marquee, persistent Format Painter, dialog choices, and target mutation verified. | In Progress |
| UI-CAT-HOME-002 | Font/alignment/number | Font family/size, grow/shrink, bold/italic/underline, borders, fill/font color, alignment, merge, number formats. | Ribbon mouse, dropdown galleries, keytips, Ctrl+B/I/U/5, Ctrl+1 dialog. | Blank/value/formula/range/table/protected cells, custom number LCIDs, theme color variants. | Rendered grid style, model style, saved/reloaded XLSX/native JSON state, undo/redo. | In Progress |
| UI-CAT-HOME-003 | Styles/conditional/table | Conditional Formatting, Format as Table, Cell Styles, table totals/filter styling. | Mouse galleries, nested menu keytips, dialogs, context menu where present. | Plain range, structured table with headers/totals, filtered table, themed workbook. | Gallery preview/selection, rule/table metadata, visible rendering, saved/reloaded package state. | In Progress |
| UI-CAT-HOME-004 | Cells/editing | Insert/delete cells/rows/columns/sheets, hide/unhide, row height/column width with default input focus, AutoFit, Clear, Fill, Flash Fill, Sort/Filter, Find/Replace/Go To. | Mouse, shortcuts, keytips, dialog access keys, context menu. | Rows, columns, formulas, notes, hyperlinks, filtered ranges, contact-pattern Flash Fill data. | Correct command route, visible sheet mutation, undo/redo/F4 repeat, dialog focus return. | In Progress |
| UI-CAT-INSERT-001 | Tables/pivots | PivotTable, Table, Pivot field list, value settings, pivot filters. | Mouse, keytips, dialog access keys, UIA invoke. | Source range/table, new sheet/current sheet placement, empty intersections, value formats, label/value filters. | Pivot/table created, contextual tabs visible, field list/action buttons work, saved/reloaded model state. | Not Started |
| UI-CAT-INSERT-002 | Charts/sparklines | Supported chart families, Select Data, Move Chart, chart formatting, line/column/win-loss sparklines. | Mouse, keytips, dialog access keys, chart selection handles. | Embedded chart, chart sheet, selected series/axis/title/legend/plot area, sparkline group. | Chart/sparkline renders, dialogs mutate model, unsupported chart families are disabled or clearly blocked. | Not Started |
| UI-CAT-INSERT-003 | Objects/links/text | Picture, shapes, text box, symbol, hyperlink, header/footer, comment/note. | Mouse, keytips, Ctrl+K, dialogs, object selection. | Picture/shape/text box, selected object, hyperlink cell, threaded comment/note cell. | Object appears and can be selected, dialog choices persist, saved/reloaded drawing/comment/hyperlink state. | In Progress |
| UI-CAT-DRAW-001 | Drawing commands | Rectangle, ellipse, line, bring/send, size/rotation, fill/outline, alt text, crop/reset, gradients/effects, Selection Pane. | Mouse, keytips, dialogs, list keyboard traversal, UIA patterns. | Picture, shape, text box, chart/drawing object, multiple objects where supported. | Object z-order/size/fill/name/visibility mutates, Selection Pane rename/visibility persists to native JSON/XLSX. | Not Started |
| UI-CAT-PAGE-001 | Page layout | Margins, orientation, paper size, print area, breaks, background, print titles, scale, gridlines/headings, themes, header/footer, page setup. | Mouse/keytips, dialogs, access keys, page-layout drag. | Normal/page layout/page break, saved print settings, themed workbook, export output. | Visual page setup changes, dialog state round trips, print/export output reflects settings. | In Progress |
| UI-CAT-FORMULAS-001 | Formula authoring/audit | Insert Function, AutoSum variants, function menus, names, Use in Formula, Create from Selection. | Mouse, keytips, shortcuts, dialog access keys, UIA invoke. | Named ranges, formula/value/error cells, cross-sheet refs. | Dialog results insert correct formula/name state, undo/redo, saved/reloaded defined names. | In Progress |
| UI-CAT-FORMULAS-002 | Formula diagnostics | Trace precedents/dependents, Remove Arrows, Show Formulas, Error Checking, Evaluate Formula, Watch Window, calculation options. | Mouse/keytips, Ctrl+`, dialog access keys, modal/modeless focus. | Error cells, inconsistent formulas, formulas referring to blanks, watched cells, manual/auto calc. | Arrows/rendering/status/dialog steps update correctly, Watch Window opens on the watch list with the first row selected when present, add/delete/refresh works. | In Progress |
| UI-CAT-DATA-001 | Import/sort/filter | Get Data CSV, Refresh All, Sort, Filter dropdowns, Advanced Filter, AutoFilter search/select all. | Mouse, keytips, native file dialog guard, dropdown keyboard, access keys. | Tables/plain ranges, blanks, numeric/text/date filters, filtered rows, invalid CSV/path. | Rows hidden/shown correctly, sort/filter criteria persist where modeled, focus returns after dropdown/dialog. | In Progress |
| UI-CAT-DATA-002 | Data tools | Text to Columns, Remove Duplicates, Data Validation, Consolidate, Goal Seek, Scenario Manager, Data Table, Forecast Sheet. | Mouse/keytips, wizard/dialog access keys, range picker, Enter/Escape. | Delimited/fixed-width text, validation list/input/error, scenario variables, one/two-variable table. | Dialog choices mutate workbook correctly, invalid input blocked, Goal Seek status lands on the default action button, undo/redo. | In Progress |
| UI-CAT-DATA-003 | Outline | Subtotal, Group, Ungroup, Show/Hide Detail, outline buttons. | Ribbon mouse/keytips, grid outline buttons, keyboard where applicable. | Rows/columns grouped, nested groups, filtered ranges. | Outline levels render, buttons work, hidden/detail state persists through save/load. | Not Started |
| UI-CAT-REVIEW-001 | Proofing/accessibility | Spell Check, Accessibility Checker, Statistics. | Mouse/keytips, dialogs, list selection, access keys. | Text cells with known corrections, hyperlinks/emails/files skipped, inaccessible workbook issues. | Replace/replace-all/ignore works, Accessibility Checker issue text receives default focus, stats dialog OK is focused by default, stats match workbook state. | In Progress |
| UI-CAT-REVIEW-002 | Comments/protection/share | New/Edit/Delete Note, threaded comment, previous/next/show notes, Protect Sheet/Workbook, Allow Edit Ranges, Share. | Mouse/keytips, Ctrl+Shift+F2, dialogs/access keys, protected-state command checks. | Note/comment cells, locked/unlocked cells, allowed ranges, saved/unsaved local file. | Comment/note/protection state mutates and persists, password dialogs focus password entry, Allow Edit Ranges focuses/selects the range box, disabled commands respect protection, share routes save when needed. | In Progress |
| UI-CAT-VIEW-001 | Workbook views/show toggles | Normal/Page Break/Page Layout, Custom Views, gridlines/headings/ruler/formula bar. | Mouse/keytips, dialog access keys, status/view buttons. | Multiple sheets, saved custom view, hidden UI toggles. | View state and UI visibility update, custom views save/show/delete correctly, persistence where supported. | In Progress |
| UI-CAT-VIEW-002 | Panes/window/zoom | Freeze Panes, Split, Zoom, Zoom to Selection, 100%, Arrange All. | Mouse/keytips, split drag, wheel zoom, status slider/buttons. | Frozen/split panes, selected range, narrow/wide viewport, multiple zoom levels. | Pane geometry, active pane scrolling, zoom value/status, Arrange All partial state all behave as documented. | In Progress |
| UI-CAT-HELP-001 | Help/about/feedback | Help, Send Feedback, About. | Mouse/keytips, UIA invoke, guarded external process check. | Online allowed/blocked environment, modal About dialog. | External launches are guarded and documented, About dialog focus/accessibility and close paths work. | In Progress |
| UI-CAT-CONTEXT-001 | Worksheet context menu | 46 worksheet context-menu planner commands. | Right-click, Shift+F10, Menu key, initial menu-item focus, access keys, UIA menu items. | Cell/range/row/column/table/filter/comment/hyperlink/protected targets. | Menu opens at active target, focus lands on the first enabled command, comment/note/hyperlink enabled state is model-backed, every item routes to expected command. | In Progress |
| UI-CAT-CONTEXT-002 | Sheet tab/contextual menus | Add, rename, duplicate, delete, move, color, hide/unhide, select all, ungroup, overflow arrows. | Mouse click/double-click/drag/right-click, F6 focus, tab-strip arrow keys, Shift+F10/Menu key, keyboard access keys. | First/middle/last sheet, hidden sheet, grouped sheets, colored tab. | Tab state/order/name/color/visibility mutates, grouping commands target correct sheets. | In Progress |
| UI-CAT-CONTEXT-003 | Contextual object tabs/menus | PivotTable Analyze/Design, PivotChart field buttons, chart/object/table/sparkline surfaces. | Mouse, keytips, field-button dropdowns, object context menus. | Active pivot/chart/table/sparkline/drawing object, selected chart subpart. | Correct contextual tab appears/disappears, commands route to active object, disabled states match target. | Not Started |
| UI-CAT-DIALOG-001 | Dialog behavior contract | All modal/modeless Freexcel dialogs. | Tab/Shift+Tab, access keys, Enter default, Escape cancel, mouse OK/Cancel/Apply, UIA patterns. | Default, changed, invalid, canceled, high-DPI/narrow-window cases. | Focus order, automation names/ids, validation, result/cancel semantics, focus return, screenshot evidence. | In Progress |

## Expanded Child Rows

Use these child rows when a broad `UI-CAT-*` row is too large for a single pass. Add result/evidence notes to the parent row and the child row.

| Child ID | Parent | Surface | Required test focus | Status |
|---|---|---|---|---|
| UI-CAT-FILE-001A | UI-CAT-FILE-001 | Open/Save As native dialogs | Guarded OpenFileDialog/SaveFileDialog focus, cancel, invalid path, recent list update, workbook title/path state. | Not Started |
| UI-CAT-FILE-001B | UI-CAT-FILE-001 | Recent/Pinned backstage items | Open recent, pin/unpin, remove/missing file handling, context-menu access keys, UIA names. | Not Started |
| UI-CAT-FILE-001C | UI-CAT-FILE-001 | Open progress/unsupported warnings | Loading overlay, unsupported-feature message, focus recovery after dismiss, file state after failure. | Not Started |
| UI-CAT-FILE-002A | UI-CAT-FILE-002 | Print Preview | Toolbar buttons with Print as the default keyboard focus target, page navigation, zoom, close, keyboard traversal, output scope. | In Progress |
| UI-CAT-FILE-002B | UI-CAT-FILE-002 | Export Options dialog | Active sheet/selection/workbook scope, page range validation, standard/minimum quality, open-after-publish, access keys. | Not Started |
| UI-CAT-FILE-002C | UI-CAT-FILE-002 | PDF/XPS publish save dialog | Extensionless `.pdf`, explicit `.xps`, existing file overwrite/cancel, metadata/output inspection. | Not Started |
| UI-CAT-DATA-001A | UI-CAT-DATA-001 | CSV import | Data > Get Data CSV native dialog, delimiter/encoding assumptions, cancel/error paths, resulting sheet data. | Not Started |
| UI-CAT-INSERT-003A | UI-CAT-INSERT-003 | Picture import | Insert Picture native dialog, supported/unsupported image files, placement, selection, persistence. | Not Started |
| UI-CAT-PAGE-001A | UI-CAT-PAGE-001 | Sheet background import | Page Layout background dialog, tiling display, replacement/clear path, persistence expectations. | Not Started |
| UI-CAT-CONTEXT-001A | UI-CAT-CONTEXT-001 | Worksheet context entry paths | Right-click, Shift+F10, Menu key, Escape, access-key traversal, foreground guard. | In Progress |
| UI-CAT-CONTEXT-001B | UI-CAT-CONTEXT-001 | Worksheet context targets | Cell, range, row, column, table, filter, comment/note, hyperlink, protected cell enabled/disabled matrix. | Not Started |
| UI-CAT-CONTEXT-001C | UI-CAT-CONTEXT-001 | Worksheet context command mutation | Clipboard, insert/delete, clear, sort/filter, note/comment, hyperlink, Format Cells, row/column size. | Not Started |
| UI-CAT-CONTEXT-002A | UI-CAT-CONTEXT-002 | Sheet-tab pointer actions | Click select, double-click rename, drag reorder, overflow arrows, right-click menu. | Not Started |
| UI-CAT-CONTEXT-002B | UI-CAT-CONTEXT-002 | Sheet-tab commands | Add, rename, duplicate, delete, move, tab color, hide/unhide, select all, ungroup, active-tab F6 focus, tab-strip Left/Right/Home/End navigation, and Shift+F10/Menu-key context entry. | In Progress |
| UI-CAT-CONTEXT-003A | UI-CAT-CONTEXT-003 | Pivot contextual tabs | PivotTable Analyze/Design visibility, `JA`/`JD` keytips, active pivot target changes. | Not Started |
| UI-CAT-CONTEXT-003B | UI-CAT-CONTEXT-003 | Pivot Field List | Show/close, search, action buttons, defer/update, drag/drop row/column/value/filter areas. | Not Started |
| UI-CAT-CONTEXT-003C | UI-CAT-CONTEXT-003 | Pivot field menus | Field context menus, checked-item filter, label filter, value filter, grouping, calculated field/item. | Not Started |
| UI-CAT-INSERT-001A | UI-CAT-INSERT-001 | Pivot create/source dialogs | Source range picker, new/current worksheet placement, invalid source, OK/Cancel/Escape. | Not Started |
| UI-CAT-INSERT-001B | UI-CAT-INSERT-001 | Pivot options/settings dialogs | PivotTable Options, PivotChart Options, Value Field Settings tabs, number format, empty-cell text. | Not Started |
| UI-CAT-INSERT-001C | UI-CAT-INSERT-001 | Slicer/timeline | Insert slicer/timeline dialogs, connection to pivot, select/clear items, contextual disabled states. | Not Started |
| UI-CAT-INSERT-001D | UI-CAT-INSERT-001 | Table creation and Format as Table | Ctrl+T/Create Table dialog with initial focus on the range box, header checkbox, gallery sections/swatches, totals row materialization. | In Progress |
| UI-CAT-DATA-001B | UI-CAT-DATA-001 | Table/AutoFilter dropdown | Header dropdown, Alt+Down initial focus on first sort command, search/select all, blank item, number/text/date filters, clear/reapply behavior. | In Progress |
| UI-CAT-INSERT-002A | UI-CAT-INSERT-002 | Insert/change chart | Chart family menus, supported/deferred/excluded families, render and selected chart target. | Not Started |
| UI-CAT-INSERT-002B | UI-CAT-INSERT-002 | Chart data/layout dialogs | Select Data, Move Chart, labels, trendlines, error bars, axis and series formatting. | Not Started |
| UI-CAT-INSERT-002C | UI-CAT-INSERT-002 | Chart contextual behavior | Chart area/plot/series/axis/title/legend selection, context commands, persistence. | Not Started |
| UI-CAT-DRAW-001A | UI-CAT-DRAW-001 | Object selection and disabled states | No-object messages, selected picture/shape/text box/chart object enabled-state matrix. | Not Started |
| UI-CAT-DRAW-001B | UI-CAT-DRAW-001 | Object geometry/appearance | Size dialogs with height-box default focus/select-all, rotate, crop/reset crop, fill, outline, gradient with first RGB stop focus/select-all, effects, z-order. | In Progress |
| UI-CAT-DRAW-001C | UI-CAT-DRAW-001 | Selection Pane | Search/filter, visibility checkboxes, rename, show all/hide all, bring/send reorder. | Not Started |
| UI-CAT-DIALOG-001A | UI-CAT-DIALOG-001 | Data dialogs | Sort and Sort Options with default focus targets, Advanced Filter, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Goal Seek, Scenario Manager, Data Table. | In Progress |
| UI-CAT-DIALOG-001B | UI-CAT-DIALOG-001 | Formatting/page dialogs | Format Cells with active-tab first-control default focus, colors, Conditional Formatting manager/rules with manager focus landing on the scope selector and threshold dialogs focusing the threshold input, Theme, Page Setup, Header/Footer. | In Progress |
| UI-CAT-DIALOG-001C | UI-CAT-DIALOG-001 | Formula/review dialogs | Insert Function, Name Manager, Create from Selection, Error Checking, Evaluate Formula, Watch Window, Spell Check, Accessibility, Protection. | In Progress |
| UI-CAT-RIBBON-001A | UI-CAT-SHELL-002 | Top-level tab render/select | Home, Insert, Draw, Page Layout, Formulas, Data, Review, View, Help render after mouse click, Alt keytip, and UIA SelectionItem. | In Progress |
| UI-CAT-RIBBON-001B | UI-CAT-SHELL-002 | File/backstage tab keytip | File tab opens via mouse and `Alt+F`, shows Back/Home/Info/New/Open/Save/Save As/Print/Export/Share/Account/Options/Close keytips. | In Progress |
| UI-CAT-RIBBON-001C | UI-CAT-SHELL-002 | Contextual ribbon visibility | PivotTable Analyze and Design tabs are hidden without pivot selection, visible after pivot selection, and expose `JA`/`JD` keytips. Automated planner/source coverage now requires contextual tabs and Field List to use strict PivotTable selection instead of workbook fallback; live screenshot evidence remains. | In Progress |
| UI-CAT-RIBBON-002A | UI-CAT-SHELL-002 | Collapsed group overflow | Narrow-window collapsed Home Editing, Insert Charts, and View Window groups open menus with live checked/enabled state and input gesture text. | In Progress |
| UI-CAT-RIBBON-002B | UI-CAT-SHELL-002 | Overflow command routing | Collapsed group child commands invoke the same command route as their expanded ribbon controls and direct overflow commands return focus to the visible collapsed group button. Automated coverage now verifies cloned nested menu clicks route only to the matching source item without invoking parent menu commands. | In Progress |
| UI-CAT-RIBBON-003A | UI-CAT-SHELL-002 | Inventory reconciliation | Draw tab inventory treats Bring Forward and Send Backward as separate menu rows while command-surface inventory may count one arrangement command family. | Not Started |
| UI-CAT-QAT-001A | UI-CAT-SHELL-001 | QAT Save | Save button/keytip `1` on unsaved workbook routes to Save As; on saved workbook writes without unexpected dialog and updates dirty state. | Not Started |
| UI-CAT-QAT-001B | UI-CAT-SHELL-001 | QAT Undo | Undo button/keytip `2` disabled initially, enabled after edit, mutates workbook and selection/status correctly. | Not Started |
| UI-CAT-QAT-001C | UI-CAT-SHELL-001 | QAT Redo | Redo button/keytip `3` disabled initially, enabled after undo, reapplies mutation and updates disabled/enabled state. | Not Started |
| UI-CAT-SHEETTAB-001A | UI-CAT-CONTEXT-002 | Sheet-tab selection/grouping | Tab click selects, Ctrl/Shift click groups, grouped styling appears, Ungroup restores single-sheet targeting. | Not Started |
| UI-CAT-SHEETTAB-001B | UI-CAT-CONTEXT-002 | Sheet-tab reorder/navigation | Drag reorder, Move Left, Move Right, scroll left/right arrows, first/middle/last sheet edge behavior. | Not Started |
| UI-CAT-SHEETTAB-001C | UI-CAT-CONTEXT-002 | Sheet-tab creation/rename/delete | Add button, double-click rename, context Rename/Duplicate/Delete, protected/last-sheet disabled states. | In Progress |
| UI-CAT-SHEETTAB-001D | UI-CAT-CONTEXT-002 | Sheet-tab visibility/color | Tab Color, Hide, Unhide dialog, Select All Sheets, color persistence, hidden-sheet edge cases. | Not Started |
| UI-CAT-STATUS-001A | UI-CAT-VIEW-002 | Status mode text | Ready/input/editing status text updates during selection, entry, formula edit, modal dialog return. | Not Started |
| UI-CAT-STATUS-001B | UI-CAT-VIEW-002 | Selection statistics | Average, Count, Sum, Min, Max update for numeric, text, mixed, blank, filtered, and multi-cell selections. | Not Started |
| UI-CAT-STATUS-001C | UI-CAT-VIEW-002 | Zoom buttons/text | Zoom out/in buttons and 100% text update model, status text, and rendered grid scale with min/max clamping. | In Progress |
| UI-CAT-STATUS-001D | UI-CAT-VIEW-002 | Zoom slider/wheel | Slider drag, UIA range value, Ctrl+wheel zoom, and keyboard focus leave no stale status text. | Not Started |

## Command-Level Coverage Backlog

This backlog is the next layer below `Catalog Row Index`: each row should eventually become one or more executed records using the `Per-Command Record Template`. Keep these rows compact, but do not remove a command from the backlog until it has passed or has an explicit Excluded/Deferred rationale.

### Backstage, QAT, Shell, Status

| Backlog ID | Parent | Commands / surface | Required targets and proof | Status |
|---|---|---|---|---|
| UI-CMD-FILE-001 | UI-CAT-FILE-001 | New, Open, Save, Save As, Close | Unsaved/saved workbook, dirty prompt behavior, shortcut/keytip/mouse/UIA, focus return. | Not Started |
| UI-CMD-FILE-002 | UI-CAT-FILE-001 | Info panel and unsupported-feature warnings | Clean workbook, workbook with formulas/accessibility issues, unsupported XLSX warnings, properties/stat summaries. | Not Started |
| UI-CMD-FILE-003 | UI-CAT-FILE-001 | Recent Files and pinned items | Open existing recent, missing file, pin/unpin, remove, keyboard access and UIA names. | Not Started |
| UI-CMD-FILE-004 | UI-CAT-FILE-001 | Share | Unsaved file routes through Save As, saved local file opens Windows Share, cloud exclusions are visibly scoped. | Not Started |
| UI-CMD-FILE-005 | UI-CAT-FILE-001 | Options and Account | Mouse/keytip/UIA invoke, Options category-list default focus, category navigation, OK/Cancel/Escape, focus return, excluded account messaging. | In Progress |
| UI-CMD-FILE-006 | UI-CAT-FILE-002 | Print Preview and native Print | Ctrl+P, File > Print, preview toolbar, native print dialog guard, page settings summary. | Not Started |
| UI-CMD-FILE-007 | UI-CAT-FILE-002 | Export to PDF/XPS | Scope with active-sheet default focus, page range, quality, extension inference, metadata, overwrite/cancel, open-after-publish. | In Progress |
| UI-CMD-QAT-001 | UI-CAT-SHELL-001 | Save, Undo, Redo | Enabled/disabled states, keytips `1/2/3`, dirty stack, saved file and grid mutation proof. | Not Started |
| UI-CMD-SHELL-001 | UI-CAT-SHELL-001 | Window chrome and title bar | Minimize/maximize/restore/close, Alt+Space, drag window, title dirty/saved path update. | Not Started |
| UI-CMD-STATUS-001 | UI-CAT-VIEW-002 | Ready/edit/input status | Mode text changes during selection, edit, formula edit, dialogs, and errors. | Not Started |
| UI-CMD-STATUS-002 | UI-CAT-VIEW-002 | Selection stats | Average, Count, Numerical Count, Min, Max, Sum for numeric/text/mixed/filtered selections. | Not Started |
| UI-CMD-STATUS-003 | UI-CAT-VIEW-002 | Zoom out/in/slider/text | Button, slider, Ctrl+wheel, Ctrl+Alt+=/-, min/max clamp, status and grid scale proof. | In Progress |

### Home Tab

| Backlog ID | Parent | Commands / surface | Required targets and proof | Status |
|---|---|---|---|---|
| UI-CMD-HOME-CLIP-001 | UI-CAT-HOME-001 | Cut, Copy, Paste | Values, formulas, formats, notes/comments, validation, overlapping cut/paste, external text. | In Progress |
| UI-CMD-HOME-CLIP-002 | UI-CAT-HOME-001 | Paste dropdown and Paste Special | All supported paste modes, arithmetic options, skip blanks, transpose, paste link, pictures, access keys. | Not Started |
| UI-CMD-HOME-CLIP-003 | UI-CAT-HOME-001 | Format Painter | Single-use, persistent double-click, Escape cancel, style-only mutation, undo behavior. | Not Started |
| UI-CMD-HOME-FONT-001 | UI-CAT-HOME-002 | Font family/size/grow/shrink | Mouse dropdowns, keyboard traversal, grid render, style model, saved reload. | Not Started |
| UI-CMD-HOME-FONT-002 | UI-CAT-HOME-002 | Bold, Italic, Underline, Double Underline, Strikethrough | Ribbon, shortcuts, mixed selection, undo/redo, saved reload. | In Progress |
| UI-CMD-HOME-FONT-003 | UI-CAT-HOME-002 | Font Color, Fill Color, Theme Colors | Standard/custom color picker, theme slots, cancel/apply, render and persistence. | Not Started |
| UI-CMD-HOME-FONT-004 | UI-CAT-HOME-002 | Borders gallery | Outline/no border, full preset gallery, remembered line color/style, edge-specific render. | Not Started |
| UI-CMD-HOME-ALIGN-001 | UI-CAT-HOME-002 | Horizontal/vertical align, indent, rotation | Blank/value/formula/range targets, Format Cells parity, render and persistence. | Not Started |
| UI-CMD-HOME-ALIGN-002 | UI-CAT-HOME-002 | Wrap Text, Merge & Center, Distributed/Justify, Shrink to Fit | Single/range/table/protected targets, disabled states, undo/repeat, save/load. | In Progress |
| UI-CMD-HOME-NUM-001 | UI-CAT-HOME-002 | Number format dropdown and common styles | General, Number, Currency, Accounting, Date, Time, Percent, Fraction, Scientific, Text. | In Progress |
| UI-CMD-HOME-NUM-002 | UI-CAT-HOME-002 | Custom/locale number formats | LCID catalog, color sections, elapsed time, date/time tokens, accounting partials, save/load. | Not Started |
| UI-CMD-HOME-NUM-003 | UI-CAT-HOME-002 | Increase/Decrease Decimal, Comma, Currency, Percent | Value/formula/date/error cells, repeated F4, visual rounding and stored value proof. | Not Started |
| UI-CMD-HOME-STYLE-001 | UI-CAT-HOME-003 | Conditional Formatting menus | Highlight rules, top/bottom, data bars, color scales, icon sets, More Rules, rule dialogs with first-editor default focus/select-all, manager with scope-selector default focus. | In Progress |
| UI-CMD-HOME-STYLE-002 | UI-CAT-HOME-003 | Format as Table and table styles | Gallery swatches, create table dialog, header/totals, undo, filter behavior, persistence. | In Progress |
| UI-CMD-HOME-STYLE-003 | UI-CAT-HOME-003 | Cell Styles | Normal, Good/Bad/Neutral, calculation/check/cell/link styles, accent variants, theme dependency. | Not Started |
| UI-CMD-HOME-CELLS-001 | UI-CAT-HOME-004 | Insert cells/rows/columns/sheets | Ribbon, shortcut, context menu, modal shift choices with default keyboard focus, row/column/table targets. | In Progress |
| UI-CMD-HOME-CELLS-002 | UI-CAT-HOME-004 | Delete cells/rows/columns/sheets | Ribbon, shortcut, context menu, modal shift choices with default keyboard focus, notes/comments preserved or removed correctly, undo. | In Progress |
| UI-CMD-HOME-CELLS-003 | UI-CAT-HOME-004 | Row Height, Column Width, AutoFit | Dialog prompts, double-click headers, hidden/protected targets, render measurement. | Not Started |
| UI-CMD-HOME-CELLS-004 | UI-CAT-HOME-004 | Hide/Unhide rows, columns, sheets | Ribbon/shortcut/context/sheet-tab paths, grouped sheets, protected-state disabled behavior; sheet-tab keyboard context menus now open with initial focus on the first enabled item. | In Progress |
| UI-CMD-HOME-EDIT-001 | UI-CAT-HOME-004 | AutoSum and Fill Down/Right/Up/Left/Series | Formula adjustment, selected range variants, Series dialog direction default focus, F4 repeat, undo/redo. | In Progress |
| UI-CMD-HOME-EDIT-002 | UI-CAT-HOME-004 | Flash Fill | Contact-name/email inference variants, partial limitations, undo/repeat, blocked ambiguous cases. | Not Started |
| UI-CMD-HOME-EDIT-003 | UI-CAT-HOME-004 | Clear All/Formats/Contents/Comments/Hyperlinks | Notes/threaded comments, hyperlinks, formats, tables, undo and context-menu parity. | Not Started |
| UI-CMD-HOME-EDIT-004 | UI-CAT-HOME-004 | Sort, Filter, Find, Replace, Go To, Go To Special | Dialog options, access keys, Find/Replace search-box default focus/select-all, filtered data, hidden rows, selection targets. | In Progress |

### Insert, Draw, Contextual Objects

| Backlog ID | Parent | Commands / surface | Required targets and proof | Status |
|---|---|---|---|---|
| UI-CMD-INSERT-001 | UI-CAT-INSERT-001 | PivotTable create | Source picker, placement, invalid source, new/current worksheet, undo, contextual tabs. | Not Started |
| UI-CMD-INSERT-002 | UI-CAT-INSERT-001 | Pivot Field List and settings | Search, drag areas, action buttons, defer/update, Value Field Settings tabs, number formats. | Not Started |
| UI-CMD-INSERT-003 | UI-CAT-INSERT-001 | Pivot filters/grouping/options | Checked-item, label/value filters, grouping, calculated field/item with name-box default focus/select-all, PivotTable Options, empty display. | In Progress |
| UI-CMD-INSERT-004 | UI-CAT-INSERT-001 | Table creation | Ctrl+T, Insert > Table, Format as Table shared flow, range-box default focus, header checkbox, totals, AutoFilter. | In Progress |
| UI-CMD-INSERT-005 | UI-CAT-INSERT-002 | Charts | Embedded/chart sheet, supported families, Insert Chart recommended-gallery default focus, Change Chart Type subtype-gallery default focus, Chart Titles title-box default focus, Chart Styles gallery default focus, Move Chart target-choice default focus, Select Data range-box default focus, Chart Area fill-box default focus/select-all, Data Labels show-choice default focus, Series selector default focus, Trendline show-choice default focus, Error Bars show-choice default focus, Axis minimum-box default focus/select-all, axes, series, trendlines, error bars. | In Progress |
| UI-CMD-INSERT-006 | UI-CAT-INSERT-002 | Deferred/excluded chart families | Surface/treemap/sunburst/histogram/waterfall/funnel/map/3D disabled or blocked with clear rationale. | Not Started |
| UI-CMD-INSERT-007 | UI-CAT-INSERT-002 | Sparklines | Line/column/win-loss, Insert Sparkline default data-range focus/select-all, group selection, hidden row/column interactions, persistence. | In Progress |
| UI-CMD-INSERT-008 | UI-CAT-INSERT-003 | Picture, shapes, text box | File import, shape insertion, text editing, selection handles, save/load. | In Progress |
| UI-CMD-INSERT-009 | UI-CAT-INSERT-003 | Header & Footer, Symbol, Hyperlink | Dialog access keys, token buttons, Ctrl+K, cancel/apply, persistence. | In Progress |
| UI-CMD-INSERT-010 | UI-CAT-INSERT-003 | Comment/Note | Insert tab comment/note paths, Review parity, threaded-comment limitation, navigation. | In Progress |
| UI-CMD-DRAW-001 | UI-CAT-DRAW-001 | Rectangle, Ellipse, Line | Insert, select, move, resize where supported, z-order, save/load. | Not Started |
| UI-CMD-DRAW-002 | UI-CAT-DRAW-001 | Bring Forward, Send Backward | Multiple objects, Selection Pane order, grid overlap visual proof, undo. | Not Started |
| UI-CMD-DRAW-003 | UI-CAT-DRAW-001 | Object size/rotation, fill, outline, alt text | Shape/picture/text box targets, dialogs, render and persistence. | Not Started |
| UI-CMD-DRAW-004 | UI-CAT-DRAW-001 | Crop, gradients, effects | Picture crop/reset, shape gradient/shadow, no-object disabled state, persistence. | Not Started |
| UI-CMD-DRAW-005 | UI-CAT-DRAW-001 | Selection Pane | Search/filter with search-box default focus, rename, visibility, show all/hide all, reorder buttons, keyboard traversal. | In Progress |
| UI-CMD-CTXOBJ-001 | UI-CAT-CONTEXT-003 | Pivot/PivotChart field buttons and menus | Field button visibility, dropdowns, checked/filter state, active chart/pivot targets. | Not Started |
| UI-CMD-CTXOBJ-002 | UI-CAT-CONTEXT-003 | Chart/object/table/sparkline contextual states | Correct contextual commands appear, target-specific disabled states, focus return. | Not Started |

### Page Layout, Formulas, Data

| Backlog ID | Parent | Commands / surface | Required targets and proof | Status |
|---|---|---|---|---|
| UI-CMD-PAGE-001 | UI-CAT-PAGE-001 | Margins, Orientation, Size, Print Area, Breaks | Page views, print preview/export output, save/load, invalid ranges. | Not Started |
| UI-CMD-PAGE-002 | UI-CAT-PAGE-001 | Background, Print Titles, Scale to Fit | Native image dialog guard, range picker, page-layout render, persistence expectations. | Not Started |
| UI-CMD-PAGE-003 | UI-CAT-PAGE-001 | Gridlines/Headings print/show, Center on page, Page Order | Sheet options, page setup dialog, preview/export proof. | Not Started |
| UI-CMD-PAGE-004 | UI-CAT-PAGE-001 | Themes, Colors, Fonts, Effects | Preset menus, custom theme dialog, access keys, theme-dependent style render. | In Progress |
| UI-CMD-PAGE-005 | UI-CAT-PAGE-001 | Header/Footer and Page Setup dialog | Presets, section fields with center-header default focus/select-all, picture format size dialog with width focus/select-all, token buttons, tabs, OK/Cancel/Escape, output proof. | In Progress |
| UI-CMD-FORM-001 | UI-CAT-FORMULAS-001 | Insert Function and function category menus | Search-box default focus/select-all, category/list/help/OK/cancel, formula insertion, shortcut Shift+F3. | In Progress |
| UI-CMD-FORM-002 | UI-CAT-FORMULAS-001 | Names | Name Manager, Define Name, Use in Formula, Create from Selection with default focus on Top row, invalid ranges, save/load. | In Progress |
| UI-CMD-FORM-003 | UI-CAT-FORMULAS-002 | Formula auditing | Trace precedents/dependents, remove arrows, direct/all refs across sheets, visual arrows. | Not Started |
| UI-CMD-FORM-004 | UI-CAT-FORMULAS-002 | Show Formulas and calculation | Ctrl+`, R1C1, Manual/Auto, Calculate Now, Calculate Sheet, formula/value render. | In Progress |
| UI-CMD-FORM-005 | UI-CAT-FORMULAS-002 | Error Checking with issue-list default focus, Evaluate Formula with Evaluate-button default focus, Watch Window | Issue taxonomy, step controls, add/delete/refresh watch, modeless focus. | In Progress |
| UI-CMD-DATA-001 | UI-CAT-DATA-001 | Get Data CSV and Refresh All | Native file dialog guard, invalid/cancel, imported data, recalculation proof. | Not Started |
| UI-CMD-DATA-002 | UI-CAT-DATA-001 | Sort and Filter | Single/multi-key sort with Custom Sort focus landing on the first sort level, AutoFilter dropdown, Alt+Down, color/text/number/date filters, clear/reapply. | In Progress |
| UI-CMD-DATA-003 | UI-CAT-DATA-001 | Advanced Filter | Action/options/reference controls with initial focus on the in-place action choice, range picker, criteria/copy targets, invalid input. | In Progress |
| UI-CMD-DATA-004 | UI-CAT-DATA-002 | Text to Columns | Wizard modes with initial focus on the source type choice, delimiter/qualifier, destination picker, fixed-width, cancel/finish, undo. | In Progress |
| UI-CMD-DATA-005 | UI-CAT-DATA-002 | Remove Duplicates and Data Validation | Header choice with default focus, column selection, validation allow-type default focus, validation list/input/error tabs, dropdown behavior. | In Progress |
| UI-CMD-DATA-006 | UI-CAT-DATA-002 | Consolidate, Goal Seek, Scenario Manager, Data Table, Forecast Sheet | Dialog access keys, status dialogs, default focus including Consolidate function, Goal Seek set-cell entry, Scenario Manager list/name-field, and Data Table row-input entry, results, invalid input, undo where supported. | In Progress |
| UI-CMD-DATA-007 | UI-CAT-DATA-003 | Subtotal, Group, Ungroup, Show/Hide Detail | Subtotal dialog initial focus on the group-column choice, rows/columns, nested groups, outline buttons, filtered ranges, persistence. | In Progress |

### Review, View, Help, Context Menus

| Backlog ID | Parent | Commands / surface | Required targets and proof | Status |
|---|---|---|---|---|
| UI-CMD-REVIEW-001 | UI-CAT-REVIEW-001 | Spell Check | Corrections, default suggestion-list focus with replacement fallback, replace/replace-all/ignore, skipped URLs/emails/files, casing preservation. | In Progress |
| UI-CMD-REVIEW-002 | UI-CAT-REVIEW-001 | Accessibility Checker and Statistics | Issue list, focus target action, chart alt/title issues, hidden content, comment counts. | In Progress |
| UI-CMD-REVIEW-003 | UI-CAT-REVIEW-002 | Notes and threaded comments | New/edit/delete/previous/next/show, Shift+F2/Ctrl+Shift+F2, persistence limits. | In Progress |
| UI-CMD-REVIEW-004 | UI-CAT-REVIEW-002 | Protection and Allow Edit Ranges | Protect sheet/workbook, allowed ranges, locked/unlocked cells, disabled command matrix. | Not Started |
| UI-CMD-REVIEW-005 | UI-CAT-REVIEW-002 | Share | Saved and unsaved file paths, Windows Share guard, cloud exclusions. | Not Started |
| UI-CMD-VIEW-001 | UI-CAT-VIEW-001 | Workbook views and show toggles | Normal/Page Break/Page Layout, gridlines/headings/ruler/formula bar, persistence. | In Progress |
| UI-CMD-VIEW-002 | UI-CAT-VIEW-001 | Custom Views | Add/show/delete, list default focus, Add View name-box focus/select-all, invalid names, hidden UI state, OK/Cancel/Escape. | In Progress |
| UI-CMD-VIEW-003 | UI-CAT-VIEW-002 | Freeze Panes and Split | Toggle, drag dividers, pane scrollbars, active pane, frozen/split interactions. | Not Started |
| UI-CMD-VIEW-004 | UI-CAT-VIEW-002 | Zoom, Zoom to Selection, 100%, Arrange All | Ribbon/status/shortcut paths, Zoom dialog custom percent selected on open, partial Arrange All checked state, focus return. | In Progress |
| UI-CMD-HELP-001 | UI-CAT-HELP-001 | Help, Send Feedback, About | External process guard, About modal, UIA invoke, keyboard close, excluded Microsoft services. | In Progress |
| UI-CMD-WCM-001 | UI-CAT-CONTEXT-001 | Worksheet context clipboard group | Cut, Copy, Paste, Paste Special through right-click, Shift+F10, Menu key, access headers. | In Progress |
| UI-CMD-WCM-002 | UI-CAT-CONTEXT-001 | Worksheet context insert/delete group | Insert/Delete cells, rows, columns, shift dialogs, row/column targets. | Not Started |
| UI-CMD-WCM-003 | UI-CAT-CONTEXT-001 | Worksheet context sort/filter/data group | Sort, Custom Sort, Filter, Clear/Reapply, Pick From Drop-down, Quick Analysis, including Ctrl+Q menu anchoring at the visible selection edge and initial keyboard focus. | In Progress |
| UI-CMD-WCM-004 | UI-CAT-CONTEXT-001 | Worksheet context row/column group | Hide/Unhide, Row Height, Column Width, AutoFit, target-specific disabled states. | Not Started |
| UI-CMD-WCM-005 | UI-CAT-CONTEXT-001 | Worksheet context comment/link/format/clear group | New Comment/Note, Edit/Delete/Show Notes, Hyperlink, Format Cells, clear commands. | Not Started |
| UI-CMD-SHEET-001 | UI-CAT-CONTEXT-002 | Sheet-tab context commands | Add, rename, duplicate, delete, move left/right, color, hide/unhide, select all, ungroup. | In Progress |
| UI-CMD-SHEET-002 | UI-CAT-CONTEXT-002 | Sheet-tab pointer/keyboard operations | Click, Ctrl/Shift group, drag reorder, double-click rename, scroll arrows, Ctrl+PageUp/PageDown, F6 active-tab focus, tab-strip Left/Right/Home/End, Shift+F10/Menu key. | In Progress |
| UI-CMD-SHORTCUT-001 | UI-CAT-SHELL-002 | All shortcut parity rows | Each shortcut row gets exact-modifier, target-state, visible result, undo/repeat evidence including Scenario Manager Show through F4, and focus evidence. | In Progress |
| UI-CMD-KEYTIP-001 | UI-CAT-SHELL-002 | Ribbon keytips | Top-level, QAT, command-scope, dropdown, nested Conditional Formatting, Escape cancellation, pixel placement; narrow collapsed-group routing now ignores hidden source controls so visible overflow group keytips win. | In Progress |

## Leaf Row Split Queue

These are the next exact leaf IDs to materialize as testing reaches each area. The `Commands to split` column is intentionally explicit: every named command needs its own evidence row or an explicit Excluded/Deferred row.

| Leaf ID range | Parent | Commands to split | Status |
|---|---|---|---|
| UI-CAT-FILE-001D-L | UI-CAT-FILE-001 | New; Save; Close; Backstage Back/Escape return; Info panel; Share; Account; Options; visible excluded/unsupported backstage entries such as Check In/Out and Online Templates. | Not Started |
| UI-CAT-QAT-001D | UI-CAT-SHELL-001 | Customize QAT excluded/disabled affordance if visible. | Not Started |
| UI-CAT-SHELL-001A-C | UI-CAT-SHELL-001 | Minimize; maximize/restore; close window. | Not Started |
| UI-CAT-HOME-001A-E | UI-CAT-HOME-001 | Cut; Copy; Paste; Paste Special; Format Painter. | In Progress |
| UI-CAT-HOME-002A-M | UI-CAT-HOME-002 | Font family; font size; grow/shrink font; bold; italic; underline; double underline; strikethrough; font color; fill color; border presets; full border gallery; theme colors. | Not Started |
| UI-CAT-HOME-002N-V | UI-CAT-HOME-002 | Horizontal align; vertical align; wrap text; merge and center; indent increase/decrease; text rotation; justify/distributed; shrink to fit; Format Cells alignment. | Not Started |
| UI-CAT-HOME-002W-AF | UI-CAT-HOME-002 | Number format dropdown; built-in formats; custom format; decimal increase/decrease; comma; currency; percentage; locale/accounting partials. | Not Started |
| UI-CAT-HOME-003A-C | UI-CAT-HOME-003 | Conditional Formatting; Format as Table; Cell Styles. | In Progress |
| UI-CAT-HOME-004A-M | UI-CAT-HOME-004 | Insert cells/rows/columns/sheets; Delete cells/rows/columns/sheets; Row Height; Column Width; AutoFit; Hide/Unhide rows/columns/sheets; Format Cells; AutoSum; Fill; Fill Series; Flash Fill; Clear variants; Sort; Filter; Find; Replace; Go To; Go To Special. | In Progress |
| UI-CAT-INSERT-001E-H | UI-CAT-INSERT-001 | PivotTable refresh/layout/options; PivotChart; Recommended PivotTables excluded; Table distinct from Format as Table. | Not Started |
| UI-CAT-INSERT-002D-H | UI-CAT-INSERT-002 | Supported chart families; stock/radar; deferred advanced chart families; Recommended Charts excluded; sparklines. | Not Started |
| UI-CAT-INSERT-003B-K | UI-CAT-INSERT-003 | Shapes; Text Box; Header/Footer; Symbols; Hyperlink; Comment/Note; Online Pictures excluded; Icons excluded; 3D Models excluded; SmartArt excluded; Screenshot excluded; WordArt excluded; Equation excluded. | Not Started |
| UI-CAT-DRAW-001D-Q | UI-CAT-DRAW-001 | Rectangle; Ellipse; Line; Bring Forward; Send Backward; Size/Rotation; Fill Color; Outline Color; Alt Text; Crop; Gradients/Effects; Selection Pane; Freehand Ink excluded; interactive drag handles deferred. | Not Started |
| UI-CAT-PAGE-001B-R | UI-CAT-PAGE-001 | Margins; Orientation; Paper Size; Print Area set/clear; Breaks; Background; Print Titles; Scale to Fit; Print Gridlines; Print Headings; Sheet Options display toggles; Themes with name-box default focus, Colors; Fonts; Effects; Header/Footer editing; Page Setup; Center on Page; Page Order. | In Progress |
| UI-CAT-FORMULAS-001A-H | UI-CAT-FORMULAS-001 | Insert Function; AutoSum variants; Logical; Text; Date & Time; Lookup & Reference; Math & Trig; Name Manager; Define Name; Use in Formula; Create from Selection. | In Progress |
| UI-CAT-FORMULAS-002A-I | UI-CAT-FORMULAS-002 | Trace Precedents; Trace Dependents; Remove Arrows; Show Formulas; Error Checking; Evaluate Formula; Watch Window; R1C1 Reference Style; Calculation Options; Calculate Now; Calculate Sheet. | In Progress |
| UI-CAT-DATA-001C-H | UI-CAT-DATA-001 | Refresh All; Sort; Filter; Advanced Filter; AutoFilter dropdown; Power Query connectors excluded. | In Progress |
| UI-CAT-DATA-002A-I | UI-CAT-DATA-002 | Text to Columns; Remove Duplicates; Data Validation; Consolidate; Goal Seek; Scenario Manager; Data Table; Forecast Sheet; Flash Fill. | In Progress |
| UI-CAT-DATA-003A-E | UI-CAT-DATA-003 | Subtotal; Group/Outline; Ungroup; Show Detail; Hide Detail; Data Model/Power Pivot excluded. | Not Started |
| UI-CAT-REVIEW-001A-C | UI-CAT-REVIEW-001 | Spell Check; Accessibility Checker; Statistics. | In Progress |
| UI-CAT-REVIEW-002A-Q | UI-CAT-REVIEW-002 | New Comment; threaded comment workflow; New Note; Edit Note; Delete Note; Previous Note; Next Note; Show Notes; Protect Sheet; Allow Edit Ranges; Protect Workbook; Share; Thesaurus excluded; Smart Lookup excluded; Translate excluded; Share Workbook legacy excluded; Track Changes excluded. | In Progress |
| UI-CAT-VIEW-001A-H | UI-CAT-VIEW-001 | Normal; Page Break Preview; Page Layout; Custom Views; Show Gridlines; Show Headings; Show Ruler; Show Formula Bar. | In Progress |
| UI-CAT-VIEW-002A-H | UI-CAT-VIEW-002 | Freeze Panes; Split; Zoom; Zoom to Selection; 100% Zoom; Arrange All; New Window excluded; View Side by Side excluded; Synchronous Scrolling excluded; Switch Windows excluded. | In Progress |
| UI-CAT-SHEETTAB-002A-J | UI-CAT-CONTEXT-002 | Add Sheet; Rename with default name-box focus/select-all; Delete; Duplicate; Move Left; Move Right; Tab Color; Hide Sheet; Unhide Sheet; Select All Sheets; Ungroup Sheets. | In Progress |
| UI-CAT-SHEETTAB-003A-C | UI-CAT-CONTEXT-002 | Tab click selection; double-click rename; drag reorder and overflow arrows. | Not Started |
| UI-CAT-STATUS-002A-F | UI-CAT-VIEW-002 | Ready/Edit/Input mode text; Average; Count; Sum; Min; Max. | Not Started |
| UI-CAT-STATUS-003A-E | UI-CAT-VIEW-002 | Normal view button; Page Layout view button; Page Break Preview button; Zoom Out; Zoom In; Zoom percentage/dialog; Zoom slider; F6 status-bar focus starts at the first zoom control with slider fallback, and Tab/Shift+Tab stay within status controls instead of moving worksheet cells. | In Progress |

## 2026-05-22 Expansion Rows

These rows were appended after syncing from latest `origin/main` so newly merged or heavily refreshed UI surfaces are not lost while the catalog is expanded into executable leaf cases. Each row must eventually record mouse, keyboard/keytip/access-key, UIA, command-route, target-matrix, undo/focus, and persistence/output proof where applicable.

| Row ID | Parent | Current surface to cover | Required UI proof | Status |
|---|---|---|---|---|
| UI-CMD-FILE-008 | UI-CAT-FILE-002 | PDF/XPS publish options depth | Export active sheet, selection, and visible workbook to `.pdf`, explicit `.xps`, and extensionless paths; cover page range, standard/minimum quality, ignore print areas, open-after-publish on/off, overwrite/cancel, PDF sheet-name bookmarks with page filtering, XPS core properties, and visible option summaries. | Not Started |
| UI-CMD-FILE-009 | UI-CAT-FILE-002 | Print Preview toolbar and navigation | Open from Ctrl+P and File > Print; verify next/previous/first/last page controls, page-count labels, zoom controls, margins/orientation/paper summary, disabled states at boundaries, Escape/back return, and foreground-safe screenshot evidence. | Not Started |
| UI-CMD-IO-001 | UI-CAT-FILE-001 | XLSX/native persistence warnings tied to UI actions | From UI-created workbook content, save/reopen and verify visible warnings or preserved state for pivot XML refs, drawing refs, sheet refs, external links, unsupported sheet refs, advanced conditional formatting, comments, shared strings, printer settings, chart design metadata, and unsupported feature messaging. | Not Started |
| UI-CMD-GRID-004 | UI-CAT-GRID-002 | Inline formula editing and formula bar parity | Edit with F2, double-click, formula bar, Ctrl+F2, Enter/Tab/Escape; verify reference coloring, overlay text, absolute/relative F4 conversion, range selection while editing, structured-reference insertion, caret movement, and focus return. | Not Started |
| UI-CMD-HOME-EDIT-005 | UI-CAT-HOME-004 | Go To dialog history and navigation targets | Cover Ctrl+G/F5, Home > Find & Select > Go To, reference-box default focus/select-all, named ranges, sheet-qualified refs, invalid refs, Go To Special first-choice focus, history persistence in-session, OK/Cancel/Escape, and active selection/focus proof. | In Progress |
| UI-CMD-HOME-EDIT-006 | UI-CAT-HOME-004 | Find/Replace with format criteria | Cover find-only and replace flows with text, formulas, values, workbook/sheet scope, match case, entire cell, direction, format picker/clear format, all results list, no-match state, access keys, search-box default focus/select-all, and focus restoration. | In Progress |
| UI-CMD-HOME-STYLE-004 | UI-CAT-HOME-003 | Structured-reference formula UI in tables | Create a table, use table headers/totals, and verify data-body column refs, `#Headers`, `#Data`, `#All`, `#Totals`, current-row, `#This Row`, unqualified row refs, multi-column ranges, dependency tracking, recalculation, formula edit coloring, and save/load. | Not Started |
| UI-CMD-INSERT-011 | UI-CAT-INSERT-001 | PivotTable style gallery and style options | Activate a PivotTable and cover built-in Light/Medium/Dark styles, explicit `PivotStyleMedium2`, custom/authored style preservation, row/column stripes, header/subtotal/grand-total rendering, undo, style persistence, and contextual Design tab keytips. | Not Started |
| UI-CMD-INSERT-012 | UI-CAT-INSERT-001 | PivotTable Show Details drill-down | Trigger Show Details by double-click and ribbon for item, subtotal, grand total, matrix, column-only, empty, and filtered cells; verify created sheet naming, extracted source rows, disabled states, undo/focus, and save/load behavior. | Not Started |
| UI-CMD-INSERT-013 | UI-CAT-INSERT-001 | Pivot slicer and timeline authoring | Insert slicers/timelines for connected worksheet-range PivotTables, use pane controls and keyboard selection, verify filter state, clear/filter buttons, cross-sheet source data, cache relationships, persistence, and partial/excluded native floating-object fidelity notes. | Not Started |
| UI-CMD-INSERT-014 | UI-CAT-INSERT-001 | PivotChart field buttons and options | Insert bound PivotChart, toggle master/report-filter/axis-field/value-field buttons, open field-button menus, verify sort/filter/value-settings routes, native JSON persistence, binding refresh after PivotTable layout changes, and chart selection focus. | Not Started |
| UI-CMD-INSERT-015 | UI-CAT-INSERT-001 | GETPIVOTDATA UI/formula behavior | With PivotTable selection active, create `GETPIVOTDATA` formulas by cell selection and manual edit; verify lookup results, invalid field/item handling, recalculation after pivot filters/layout changes, formula bar display, and save/load. | Not Started |
| UI-CMD-INSERT-016 | UI-CAT-INSERT-002 | Chart design metadata and Select Data deferred controls | Create chart, change type/style/title/legend/data source through visible dialogs, verify design metadata persisted to native JSON, Select Data helper/deferred controls are labeled honestly, and chart commands enable only for chart targets. | Not Started |
| UI-CMD-PAGE-006 | UI-CAT-PAGE-001 | Page Setup and Header/Footer dialog fidelity | Cover Page Setup tabs, first/odd/even header/footer variants, presets, section fields, token buttons, print titles, center on page, page order, OK/Cancel/Escape, access keys, print preview reflection, and persistence. | Not Started |
| UI-CMD-FORM-006 | UI-CAT-FORMULAS-001 | Insert Function category breadth | Through Insert Function and formula bar, cover recently surfaced function families including dynamic arrays, database, engineering, financial, statistical, lookup/reference, text, date/time, logical, math/trig, higher-order/lambda-adjacent, and pivot functions; verify search, MRU, argument help, invalid arguments, and formula insertion. | Not Started |
| UI-CMD-DATA-008 | UI-CAT-DATA-001 | AutoFilter typed criteria and ribbon/keytip routes | Create filters from table/range headers, open dropdown by mouse and Alt keytips, cover typed criteria area, search, select all, blanks, text/number/date filters, clear/reapply, keyboard navigation, and row visibility proof. | Not Started |
| UI-CMD-DATA-009 | UI-CAT-DATA-001 | Advanced Filter dialog safety and criteria defaults | Cover list range, criteria range, copy-to range, unique records, invalid/missing criteria, no-risk defaults, OK/Cancel/Escape, range picker focus, and resulting filtered/copied output. | Not Started |
| UI-CMD-DATA-010 | UI-CAT-DATA-003 | Subtotal dialog Excel-like flow | Cover At each change in, Use function, Add subtotal to, Replace current, Page break, Summary below, Remove All, grouped outline levels, invalid source, access keys, undo, and save/load. | Not Started |
| UI-CMD-REVIEW-006 | UI-CAT-REVIEW-002 | Protection permissions and command disabled-state matrix | Protect sheet/workbook with selected permissions, Allow Edit Ranges, locked/unlocked cells, password/cancel/invalid flows, ribbon/context/menu disabled states, edit attempts by target type, unprotect, undo limits, and persistence. | Not Started |
| UI-CMD-RIBBON-004 | UI-CAT-SHELL-001 | Ribbon SVG icon visual coverage | Sweep all visible large/small generated icons across File/QAT/ribbon/contextual tabs; verify no missing keys, correct icon-only/icon+label layout, high-DPI scaling, disabled state tint, tooltip/name parity, and no clipping across tabs. Automated coverage now asserts visible main ribbon tooltip titles resolve to semantic icons instead of the generic fallback; File/QAT/contextual visual screenshot breadth remains. | In Progress |
| UI-CMD-HARNESS-001 | UI-CAT-SHELL-001 | Screenshot and visual evidence harness | Use `tools/screenshot_excel.ps1` and `tools/screenshot_ribbon.ps1` against latest build; verify foreground guard, captured window bounds, ribbon-tab screenshots, popup/dropdown limitations, output naming, and catalog evidence attachment. | Not Started |
| UI-CMD-CONTEXT-006 | UI-CAT-CONTEXT-001 | Target-specific worksheet context coverage | For cell, range, row, column, table, filtered range, chart, drawing, PivotTable, protected sheet, and edit-mode targets, verify right-click/Menu/Shift+F10 commands route to the intended planner rows with correct enabled states. | Not Started |
| UI-CMD-DIALOG-001 | UI-CAT-SHELL-002 | Dialog keyboard/accessibility sweep | For every modal/modeless dialog reached from command rows, record default focus, Tab order, access-key collisions, Enter/Space/Escape behavior, OK/Cancel equivalence, validation messages, UIA names/patterns, and focus return target; Advanced Filter, Consolidate, Go To Special, Scenario Manager, Subtotal, and Data Table now record default-focus coverage. | In Progress |
| UI-CMD-TARGET-001 | UI-CAT-GRID-001 | Cross-target command matrix execution | Re-run each command class against single cell, multi-cell range, whole row, whole column, non-contiguous selection, table body/header/totals, filtered selection, chart, drawing, PivotTable, protected sheet, hidden row/column, and multi-sheet group targets; record unsupported targets explicitly. | Not Started |

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
| 8. Regression closure | Convert findings into automated guards. | Each fixed bug has a focused unit/source/UIA test and a retest entry in this catalog. |

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

## Catalog Maintenance Rules

- Keep this file date-free and canonical at `docs/UI_TEST_CATALOG.md`.
- Append new coverage rows, finding IDs, smoke checks, and session notes here only.
- Update the row status in `Catalog Row Index` whenever evidence changes a row from Not Started to In Progress, Passed, Finding, Blocked, or Excluded.
- Preserve historical findings; add retest notes instead of rewriting old observations away.
- After each sync from `main`, refresh inventory counts when command docs or `MainWindow.xaml` changed.

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

1. Generate a machine-readable row list from `COMMAND_SURFACE_PARITY.md`, `MENU_TOOLBAR_PARITY.md`, `SHORTCUT_PARITY_MATRIX.md`, `WorksheetContextMenuPlanner.cs`, `MainWindow.xaml`, dialog classes, contextual tab declarations, and the screenshot tools so future passes can diff current UI against this catalog.
2. Add a UI automation harness that launches the latest Debug build, snapshots visible controls by AutomationId/Name/control type, and compares them against this catalog.
3. Attach `tools/screenshot_excel.ps1` and `tools/screenshot_ribbon.ps1` visual evidence to catalog rows, with a foreground-window guard before any global input.
4. Continue Wave 1 and Wave 2 on the latest build, recording every pass/finding in this catalog.
5. Expand each `UI-CAT-*` row into per-command child rows as live testing reaches that area.
6. For each finding, add a focused automated guard when the bugfixing session closes it.
