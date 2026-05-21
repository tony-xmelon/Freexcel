# Freexcel UI Test Catalog

Generated: 2026-05-21
Branch: `codex/ui-test-catalog`
Baseline source: freshly fetched `origin/main` at worktree creation.

## Purpose

This is the comprehensive UI test catalog for Freexcel. It translates the command parity, shortcut parity, and WPF surface into an execution plan for mouse, keyboard, keytip, context-menu, dialog, and UI Automation testing.

The existing `UI_TEST_COVERAGE_2026-05-19.md` remains the chronological findings log. This file is the coverage contract: every pass should mark which catalog rows were exercised, what target was used, which command was expected, and which model/UI state proved the action worked.

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
3. Start Wave 1 and Wave 2 on the latest build, recording every pass/finding in `UI_TEST_COVERAGE_2026-05-19.md`.
4. For each finding, add a focused automated guard when the bugfixing session closes it.
