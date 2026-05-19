# Shortcut Parity Matrix

**Last updated:** 2026-05-19

This matrix tracks Excel-for-Windows shortcut fidelity for the visible Freexcel command surface. Status values use the command-surface contract: Parity, Partial, Excluded, or Missing.

## Coverage Summary

| Status | Count | % of in-scope |
|---|---:|---:|
| Parity | 62 | **81%** |
| Partial | 15 | **19%** |
| Not Implemented | 0 | **0%** |
| Excluded | 0 | — |
| **Total in-scope** | **77** | — |


| Area | Excel Shortcut | Freexcel Status | Notes |
|---|---:|---|---|
| File | Ctrl+N | Parity | Creates a blank workbook. |
| File | Ctrl+O | Parity | Opens the file picker. |
| File | Ctrl+S | Parity | Saves to the current workbook path; new/unsupported paths use Save As. |
| File | F12 | Parity | Opens Save As. |
| File | Ctrl+P | Partial | Opens File backstage on the Print command instead of immediately launching print preview; native print dialog parity remains partial. |
| Edit | Ctrl+Z | Parity | Undo command bus action. |
| Edit | Ctrl+Y | Parity | Redo command bus action. |
| Clipboard | Ctrl+C | Parity | Copies selection. |
| Clipboard | Ctrl+X | Parity | Defers source clearing until a non-overlapping paste, preserves an internal cut clipboard, and shows the cut outline while pending. |
| Clipboard | Ctrl+V | Partial | Paste and basic paste-special modes exist, including F4 repeat for internal cell paste, values/formulas/formats, transpose/arithmetic Paste Special, paste link, pasted range pictures, external text paste, and keep-column-widths composite paste. Full Excel paste matrix remains partial. |
| Clipboard | Ctrl+Alt+V | Partial | Opens Paste Special; implemented modes include values, formulas, formats, arithmetic operations, transpose, paste link, picture paste, and keep column widths. Full Excel Paste Special option matrix remains partial. |
| Formatting | Ctrl+B / Ctrl+2 | Parity | Toggle bold. |
| Formatting | Ctrl+I / Ctrl+3 | Parity | Toggle italic. |
| Formatting | Ctrl+U / Ctrl+4 | Parity | Toggle underline. |
| Formatting | Ctrl+1 | Partial | Opens Format Cells for number, alignment, font, fill, border, and protection fields supported by the current style model, including custom number formats, shrink-to-fit, indent, rotation, double underline, superscript/subscript, clear fill, per-edge border style/color, and locked-cell protection. Excel's full multi-page dialog remains broader. |
| Formatting | Ctrl+Shift+F / Ctrl+Shift+P | Partial | Opens Format Cells on the Font tab with font family, size, bold, italic, underline, double underline, strikethrough, superscript/subscript, and font color. Excel's full font effects surface remains partial. |
| Formatting | Ctrl+Shift+~ / ! / @ / # / $ / % / ^ | Parity | Applies General, Number, Time, Date, Currency, Percentage, and Scientific number formats. |
| Formatting | Ctrl+Shift+& / Ctrl+Shift+_ | Parity | Applies outline border / removes borders from the selection. |
| Navigation | Arrow keys | Parity | Move active cell. |
| Navigation | Shift+Arrow | Parity | Extend selection. |
| Navigation | Ctrl+Arrow | Parity | Jump to data boundary. |
| Navigation | Home | Parity | Move to first column in row. |
| Navigation | Ctrl+Home | Parity | Move to A1. |
| Navigation | Ctrl+End | Parity | Move to used-range end. |
| Navigation | Ctrl+Backspace | Parity | Scrolls the active cell back into view without changing the selection. |
| Navigation | Page Up / Page Down | Parity | Move by viewport page. |
| Navigation | Alt+Page Up / Alt+Page Down | Parity | Moves one viewport page left/right. |
| Navigation | End, then Arrow | Parity | Enters End Mode and uses the next arrow key to jump to the data boundary, matching Ctrl+Arrow behavior. |
| Navigation | Enter / Tab | Parity | Move down/right from active cell. |
| Navigation | Shift+Enter / Shift+Tab | Parity | Completes entry and moves up/left. |
| Selection | Ctrl+A | Parity | Selects the current region first when active cell is in data; a second press or blank active cell selects the whole sheet. |
| Selection | Ctrl+Shift+Space | Parity | Selects all, matching Excel's whole-sheet selection shortcut. |
| Selection | Ctrl+Shift+* | Parity | Selects the current region around the active cell. |
| Selection | Ctrl+Space / Shift+Space | Parity | Selects current column(s) / row(s). |
| Selection | F8 / Shift+F8 | Parity | Toggles Extend Selection and Add to Selection modes for keyboard range expansion. |
| Selection | Ctrl+. | Parity | Cycles the active corner of the current selection clockwise. |
| Editing | F2 | Parity | Enters cell edit mode. |
| Editing | Ctrl+F2 | Parity | Moves editing focus to the formula bar for the active cell. |
| Editing | Delete | Parity | Clears selection contents. |
| Editing | Ctrl++ / Ctrl+- | Partial | Inserts/deletes full selected rows or columns, including main-keyboard Ctrl+Shift+= for Ctrl++; normal cell ranges now prompt for shift cells right/down or entire row/column on insert and shift cells left/up or entire row/column on delete. A native Excel-style modal insert/delete dialog remains partial. |
| Row/Column | Ctrl+9 / Ctrl+Shift+9 | Parity | Hides / unhides selected rows. |
| Row/Column | Ctrl+0 / Ctrl+Shift+0 | Parity | Hides / unhides selected columns. |
| Editing | Escape | Parity | Cancels inline edit. |
| Editing | Alt+Enter | Parity | Inserts a new line in the same cell while editing. |
| Editing | Ctrl+Enter | Parity | Fills the selected range with the current entry. |
| Editing | Ctrl+' | Parity | Copies the formula or content from the cell above into the active cell. |
| Editing | Ctrl+Shift+" | Parity | Copies the calculated value from the cell above into the active cell. |
| Find | Ctrl+F | Parity | Opens Find. |
| Find | Ctrl+H | Parity | Opens Replace. |
| Formulas | Ctrl+` | Parity | Toggles Show Formulas. |
| Formulas | Shift+F3 | Parity | Opens Insert Function. |
| Formulas | F9 / Shift+F9 / Ctrl+Alt+F9 / Ctrl+Alt+Shift+F9 | Parity | Calculates workbook/sheet and routes Ctrl+Alt+Shift+F9 through an explicit dependency rebuild plus full workbook recalculation path. |
| Formulas | Ctrl+Shift+U | Parity | Expands/collapses the formula bar. |
| Formulas | Ctrl+[ / Ctrl+] / Ctrl+Shift+[ / Ctrl+Shift+] | Parity | Selects direct or all traceable precedents / dependents for the active cell, switching sheets when the first matched reference is on another worksheet. |
| Review | F7 | Parity | Runs worksheet spelling check. |
| Review | Shift+F2 / Ctrl+Shift+F2 | Partial | Shift+F2 opens Freexcel's simple note workflow and preloads existing selected-cell note text for editing; Ctrl+Shift+F2 maps to the same simple note flow because Excel's separate threaded-comment model is not yet represented. |
| View | Ctrl+Mouse Wheel | Parity | Zooms in/out. |
| View | Ctrl+Alt+= / Ctrl+Alt+- | Parity | Zooms in/out with keyboard shortcuts. |
| Data | Ctrl+Shift+L | Parity | Toggles/reapplies the current filter command. |
| Data | Alt+Down | Partial | Opens the active cell's data-validation list dropdown, including quoted inline list items with commas, or a searchable value checklist for the active AutoFilter header's current-region column. Full Excel AutoFilter sort/filter command menu remains pending. |
| Data | Alt+Shift+Right / Alt+Shift+Left | Parity | Groups / ungroups selected rows, or whole selected columns. |
| Sheet Tabs | Ctrl+Page Up / Ctrl+Page Down | Parity | Moves to previous/next visible worksheet. |
| Sheet Tabs | Ctrl+Shift+Page Up / Ctrl+Shift+Page Down | Parity | Selects the current and previous/next visible worksheet as a grouped sheet range. |
| Sheet Tabs | Shift+F11 / Alt+Shift+F1 | Parity | Inserts a worksheet. |
| Insert | Alt+= | Parity | Inserts SUM through AutoSum. |
| Insert | Ctrl+L / Ctrl+T | Parity | Opens Create Table. |
| Insert | Ctrl+K | Parity | Opens Insert Hyperlink for the active cell. |
| Insert | Alt+F1 / F11 | Partial | Creates a chart from the current range; Freexcel uses its chart command surface rather than a distinct native embedded-vs-chart-sheet flow. |
| Analysis | Ctrl+Q | Partial | Opens a grouped Quick Analysis menu for formatting, charts, totals, tables, and sparklines using existing Freexcel commands, including conditional-format data bars, color scales, icon sets, greater-than, top-10, clear-formatting choices, Column/Line/Pie/Bar/Area/Scatter charts, and Sum/Average/Count/Max/Min totals. Excel's hover-preview gallery and full option matrix remain partial. |
| Workbook | Ctrl+Shift+G | Parity | Opens Workbook Statistics. |
| UI | F10 | Partial | Enters Freexcel ribbon keytip mode; pixel-perfect Excel keytip overlay placement remains partial under the broader ribbon keytip row. |
| UI | Shift+F10 / Menu key | Partial | Opens the worksheet context menu with clipboard, Paste Special, cell insert/delete prompts, row/column insert/delete, sort, filter, hide/unhide rows and columns, new/delete note, hyperlink, format-cells, clear-formats, clear-hyperlinks, and clear-content actions. Full Excel context-menu contents remain partial. |
| Editing | Ctrl+; / Ctrl+Shift+; | Parity | Inserts current date / current time, with F4 repeat using the inserted value. |
| Editing | Ctrl+D / Ctrl+R | Parity | Fill Down / Fill Right with undoable formula-reference adjustment. |
| Formatting | Ctrl+5 | Parity | Toggle strikethrough. |
| Formulas | F4 while editing a formula reference | Partial | Cycles local, local range, repeated-sheet-qualified range, full-column/full-row, lowercase-normalized, sheet-qualified, escaped quoted-sheet, 3D sheet-range, and external-workbook A1 references through relative/absolute modes, while preserving structured-reference column names and string literals. |
| Editing | F4 outside formula editing | Partial | Repeats the last repeatable formatting, Merge & Center, paste/paste-special/picture paste, AutoSum, Fill Down/Right/Up/Left, Fill Series, Flash Fill, current date/time insertion, symbol insertion, comments, Clear All/Formats/Contents/Comments/Hyperlinks, sort/filter, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Subtotal, Data Table, Insert Sheet/Chart/Sparkline/Hyperlink, common chart layout/label/axis/trendline formatting, drawing object insertion/size/rotation/color/reorder/Alt Text, outline group/ungroup/collapse/expand, insert/delete row-column/cell, or hide/unhide row-column command against the current selection with a fresh undoable command instance. Dialog-driven workflows such as Goal Seek, Scenario Manager, import, protection, and sheet-tab context operations remain intentionally non-repeatable. |
| Ribbon | Alt, then F/H/N/J/P/M/A/R/W/Y; Alt+F/H/N/J/P/M/A/R/W/Y | Partial | Opens File backstage or selects the File/Home/Insert/Draw/Page Layout/Formulas/Data/Review/View/Help ribbon tabs through direct Alt combinations or two-step Alt keytip mode. QAT, tab, formula-bar, sheet-tab, and broad visible command keytip metadata render as visible badges for the current visual tree with measured in-window placement; command-scope overlay measurement refreshes layout after tab switches, QAT badges invoke only from top-level mode, off-tab ribbon controls are filtered out, and visible button/toggle/combo command sequences invoke their controls from command scope with toggle state changes, exact command keytips winning over unrelated longer prefixes, duplicate keytip metadata and deterministic resolver behavior guarded by tests. All direct ribbon dropdown menu items and nested Conditional Formatting menu choices have staged keytip metadata/routing, recursive nested leaf/prefix resolution coverage, menu keytips are displayed in the menu gesture-text slot, keyed parent menu choices open their submenu layer, Escape closes menu keytip mode, and real-window host coverage now exercises Home command, dropdown routing, and top-level/command overlay badges. Pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting are not complete. |

## Next Shortcut Work

1. Build the full Excel Print backstage / native print dialog flow for `Ctrl+P`; the current path opens Freexcel's print preview/export flow.
2. Expand `Ctrl+V` and `Ctrl+Alt+V` to the remaining Excel paste and Paste Special modes beyond the currently supported values/formulas/formats/arithmetic/transpose/link/picture/column-width paths.
3. Continue broadening Format Cells for `Ctrl+1` and `Ctrl+Shift+F/P` beyond the supported style model toward Excel's full multi-page dialog.
4. Replace the text-based `Ctrl++` / `Ctrl+-` insert/delete prompt with a native Excel-style modal dialog, preserving the supported shift cells and entire row/column choices.
5. Add a real threaded-comment model for `Ctrl+Shift+F2`; `Shift+F2` currently edits Freexcel simple notes.
6. Expand the `Alt+Down` AutoFilter checklist into a full dropdown UI with sort/filter commands and Excel-style in-place anchoring.
7. Distinguish `Alt+F1` embedded charts from `F11` chart-sheet behavior instead of routing both through Freexcel's chart command surface.
8. Add Quick Analysis hover previews and the remaining Excel gallery options for `Ctrl+Q`.
9. Continue ribbon keytips into pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting.
10. Expand `Shift+F10` / Menu key toward the full Excel worksheet context menu.
11. Extend F4 formula reference cycling to additional advanced reference forms not yet modeled by the current A1/range/full-row/full-column parser.
12. Decide which dialog-driven workflows should become repeatable through F4 and add explicit repeat command objects for them.

