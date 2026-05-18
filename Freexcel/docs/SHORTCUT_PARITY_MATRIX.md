# Shortcut Parity Matrix

**Last updated:** 2026-05-18

This matrix tracks Excel-for-Windows shortcut fidelity for the visible Freexcel command surface. Status values use the command-surface contract: Parity, Partial, Excluded, or Missing.

## Coverage Summary

| Status | Count | % of in-scope |
|---|---:|---:|
| Parity | 50 | **88%** |
| Partial | 7 | **12%** |
| Not Implemented | 0 | **0%** |
| Excluded | 0 | — |
| **Total in-scope** | **57** | — |


| Area | Excel Shortcut | Freexcel Status | Notes |
|---|---:|---|---|
| File | Ctrl+N | Parity | Creates a blank workbook. |
| File | Ctrl+O | Parity | Opens the file picker. |
| File | Ctrl+S | Parity | Saves to the current workbook path; new/unsupported paths use Save As. |
| File | Ctrl+P | Partial | Opens the current print/export flow; native print dialog parity is partial. |
| Edit | Ctrl+Z | Parity | Undo command bus action. |
| Edit | Ctrl+Y | Parity | Redo command bus action. |
| Clipboard | Ctrl+C | Parity | Copies selection. |
| Clipboard | Ctrl+X | Partial | Cuts by copy plus clear; marching-ants cut state is partial. |
| Clipboard | Ctrl+V | Partial | Paste and basic paste-special modes exist, including F4 repeat for internal cell paste, values/formulas/formats, transpose/arithmetic Paste Special, paste link, pasted range pictures, external text paste, and keep-column-widths composite paste. Full Excel paste matrix remains partial. |
| Formatting | Ctrl+B / Ctrl+2 | Parity | Toggle bold. |
| Formatting | Ctrl+I / Ctrl+3 | Parity | Toggle italic. |
| Formatting | Ctrl+U / Ctrl+4 | Parity | Toggle underline. |
| Formatting | Ctrl+1 | Partial | Opens Format Cells; dialog coverage is narrower than Excel. |
| Formatting | Ctrl+Shift+~ / ! / @ / # / $ / % / ^ | Parity | Applies General, Number, Time, Date, Currency, Percentage, and Scientific number formats. |
| Formatting | Ctrl+Shift+& / Ctrl+Shift+_ | Parity | Applies outline border / removes borders from the selection. |
| Navigation | Arrow keys | Parity | Move active cell. |
| Navigation | Shift+Arrow | Parity | Extend selection. |
| Navigation | Ctrl+Arrow | Parity | Jump to data boundary. |
| Navigation | Home | Parity | Move to first column in row. |
| Navigation | Ctrl+Home | Parity | Move to A1. |
| Navigation | Ctrl+End | Parity | Move to used-range end. |
| Navigation | Page Up / Page Down | Parity | Move by viewport page. |
| Navigation | Enter / Tab | Parity | Move down/right from active cell. |
| Selection | Ctrl+A | Parity | Selects the current region first when active cell is in data; a second press or blank active cell selects the whole sheet. |
| Selection | Ctrl+Space / Shift+Space | Parity | Selects current column(s) / row(s). |
| Editing | F2 | Parity | Enters cell edit mode. |
| Editing | Delete | Parity | Clears selection contents. |
| Editing | Ctrl++ / Ctrl+- | Partial | Inserts/deletes full selected rows or columns; normal cell ranges use shift down/up. Excel's insert/delete dialog choice matrix is not complete. |
| Row/Column | Ctrl+9 / Ctrl+Shift+9 | Parity | Hides / unhides selected rows. |
| Row/Column | Ctrl+0 / Ctrl+Shift+0 | Parity | Hides / unhides selected columns. |
| Editing | Escape | Parity | Cancels inline edit. |
| Find | Ctrl+F | Parity | Opens Find. |
| Find | Ctrl+H | Parity | Opens Replace. |
| Formulas | Ctrl+` | Parity | Toggles Show Formulas. |
| View | Ctrl+Mouse Wheel | Parity | Zooms in/out. |
| Data | Ctrl+Shift+L | Parity | Toggles/reapplies the current filter command. |
| Data | Alt+Shift+Right / Alt+Shift+Left | Parity | Groups / ungroups selected rows, or whole selected columns. |
| Sheet Tabs | Ctrl+Page Up / Ctrl+Page Down | Parity | Moves to previous/next visible worksheet. |
| Sheet Tabs | Shift+F11 | Parity | Inserts a worksheet. |
| Insert | Alt+= | Parity | Inserts SUM through AutoSum. |
| Insert | Ctrl+K | Parity | Opens Insert Hyperlink for the active cell. |
| Editing | Ctrl+; / Ctrl+Shift+; | Parity | Inserts current date / current time, with F4 repeat using the inserted value. |
| Editing | Ctrl+D / Ctrl+R | Parity | Fill Down / Fill Right with undoable formula-reference adjustment. |
| Formatting | Ctrl+5 | Parity | Toggle strikethrough. |
| Formulas | F4 while editing a formula reference | Partial | Cycles local, sheet-qualified, escaped quoted-sheet, 3D sheet-range, and external-workbook A1 references through relative/absolute modes, while preserving structured-reference column names and string literals. |
| Editing | F4 outside formula editing | Partial | Repeats the last repeatable formatting, Merge & Center, paste/paste-special/picture paste, AutoSum, Fill Down/Right/Up/Left, Fill Series, Flash Fill, current date/time insertion, symbol insertion, comments, Clear All/Formats/Contents/Comments/Hyperlinks, sort/filter, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Subtotal, Data Table, Insert Sheet/Chart/Sparkline/Hyperlink, common chart layout/label/axis/trendline formatting, drawing object insertion/size/rotation/color/reorder/Alt Text, outline group/ungroup/collapse/expand, insert/delete row-column/cell, or hide/unhide row-column command against the current selection with a fresh undoable command instance. Dialog-driven workflows such as Goal Seek, Scenario Manager, import, protection, and sheet-tab context operations remain intentionally non-repeatable. |
| Ribbon | Alt, then F/H/N/J/P/M/A/R/W/Y; Alt+F/H/N/J/P/M/A/R/W/Y | Partial | Opens File backstage or selects the File/Home/Insert/Draw/Page Layout/Formulas/Data/Review/View/Help ribbon tabs through direct Alt combinations or two-step Alt keytip mode. QAT, tab, formula-bar, sheet-tab, and broad visible command keytip metadata render as visible badges for the current visual tree with measured in-window placement; command-scope overlay measurement refreshes layout after tab switches, QAT badges invoke only from top-level mode, off-tab ribbon controls are filtered out, and visible button/toggle/combo command sequences invoke their controls from command scope with toggle state changes, exact command keytips winning over unrelated longer prefixes, duplicate keytip metadata and deterministic resolver behavior guarded by tests. All direct ribbon dropdown menu items and nested Conditional Formatting menu choices have staged keytip metadata/routing, recursive nested leaf/prefix resolution coverage, menu keytips are displayed in the menu gesture-text slot, keyed parent menu choices open their submenu layer, Escape closes menu keytip mode, and real-window host coverage now exercises Home command, dropdown routing, and top-level/command overlay badges. Pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting are not complete. |

## Next Shortcut Work

1. Add UI automation coverage for WPF key routing.
2. Extend repeat-last-command F4 beyond formatting into additional repeatable Excel commands.
3. Extend ribbon keytips into pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting.
