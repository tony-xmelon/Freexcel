# Shortcut Parity Matrix

**Last updated:** 2026-05-20

This matrix tracks Excel-for-Windows shortcut fidelity for the visible Freexcel command surface. Status values use the command-surface contract: Parity, Partial, Excluded, or Missing. Exact command shortcuts reject unrelated extra modifiers so combinations such as Ctrl+Alt+C or Ctrl+Shift+Z do not steal AltGr/non-US input or future shortcut space.

## Coverage Summary

| Status | Count | % of in-scope |
|---|---:|---:|
| Parity | 69 | **85%** |
| Partial | 12 | **15%** |
| Not Implemented | 0 | **0%** |
| Excluded | 0 | — |
| **Total in-scope** | **81** | — |


| Area | Excel Shortcut | Freexcel Status | Notes |
|---|---:|---|---|
| File | Ctrl+N | Parity | Creates a blank workbook. |
| File | Ctrl+O | Parity | Opens the file picker. |
| File | Ctrl+S | Parity | Saves to the current workbook path; new/unsupported paths use Save As. |
| File | F12 | Parity | Opens Save As. |
| File | Ctrl+W / Ctrl+F4 | Parity | Closes the current workbook window. |
| File | Ctrl+P | Partial | Routes through the File/Backstage Print entry point before opening Freexcel's print preview, with an access-keyed Print button that opens the native WPF print dialog for the rendered document and an active-sheet print-settings summary for orientation, paper size, scaling, gridlines, headings, and print-area scope. Page Setup exposes tab, option, OK, and Cancel access keys for the modeled print settings. Printed comment output includes notes and local threaded comments for as-displayed overlays and at-end summary pages. Full Excel-style print backstage/settings editing parity remains partial. |
| Edit | Ctrl+Z | Parity | Undo command bus action. |
| Edit | Ctrl+Y | Parity | Redo command bus action. |
| Clipboard | Ctrl+C / Ctrl+Insert | Parity | Copies selection. |
| Clipboard | Ctrl+X / Shift+Delete | Parity | Defers source clearing until a non-overlapping paste, preserves an internal cut clipboard, and shows the cut outline while pending. |
| Clipboard | Ctrl+V / Shift+Insert / Ctrl+Shift+V | Partial | Paste and paste-values exist, including F4 repeat for internal cell paste, values/formulas/formats, transposed format-only paste, values-and-source-formatting, transpose/arithmetic Paste Special, skip blanks, paste link, pasted range pictures, linked range-picture source metadata, external text paste, keep-column-widths composite paste, validation paste, comments/notes/threaded-comments paste, all-using-source-theme, all-except-borders, all-merging-conditional-formats, formulas-and-number-formats, and values-and-number-formats. Full Excel paste matrix remains partial. |
| Clipboard | Ctrl+Alt+V | Partial | Opens Paste Special with keyboard access keys for dialog choices and OK/Cancel; implemented modes include values, formulas, formats including transposed format-only paste, values-and-source-formatting, all using source theme, arithmetic operations, skip blanks, transpose, paste link, picture and linked-picture paste with source-range metadata, comments/notes/threaded-comments, validation, all-except-borders, all-merging-conditional-formats, formulas-and-number-formats, values-and-number-formats, and keep column widths. Full Excel Paste Special option matrix remains partial. |
| Formatting | Ctrl+B / Ctrl+2 | Parity | Toggle bold; exact matching rejects unrelated extra modifiers. |
| Formatting | Ctrl+I / Ctrl+3 | Parity | Toggle italic; exact matching rejects unrelated extra modifiers. |
| Formatting | Ctrl+U / Ctrl+4 | Parity | Toggle underline; exact matching rejects unrelated extra modifiers. |
| Formatting | Ctrl+1 | Partial | Opens Format Cells with keyboard access keys for tabs, OK/Cancel, supported option checkboxes, color picker buttons, border presets/preview/details controls, and Pivot Value Field Settings tabs when reached from pivot value formatting; covers number, alignment, font, fill, border, and protection fields supported by the current style model, including custom number formats, number/currency/accounting/percentage decimal-place and symbol controls, negative-number variants, shrink-to-fit, indent, rotation, double underline, superscript/subscript, clear fill, per-edge border style/color, and locked-cell protection. Excel's full multi-page dialog remains broader. |
| Formatting | Ctrl+Shift+F / Ctrl+Shift+P | Partial | Opens Format Cells on the Font tab with keyboard access keys plus font family, size, bold, italic, underline, double underline, strikethrough, superscript/subscript, and font color picker access. Excel's full font effects surface remains partial. |
| Formatting | Ctrl+Shift+~ / ! / @ / # / $ / % / ^ | Parity | Applies General, Number, Time, Date, Currency, Percentage, and Scientific number formats. |
| Formatting | Ctrl+Shift+& / Ctrl+Shift+_ | Parity | Applies outline border / removes borders from the selection. |
| Navigation | Arrow keys | Parity | Move active cell. |
| Navigation | Shift+Arrow | Parity | Extend selection. |
| Navigation | Ctrl+Arrow | Parity | Jump to data boundary. |
| Navigation | Home | Parity | Move to first column in row. |
| Navigation | Ctrl+Home | Parity | Move to A1. |
| Navigation | Ctrl+End | Parity | Move to used-range end. |
| Navigation | F5 / Ctrl+G | Parity | Opens Go To for jumping to a cell reference, with access keys for the reference field, OK, and Cancel; Go To Special exposes access keys for core selection targets and OK/Cancel. |
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
| Selection | Alt+; | Parity | Selects visible cells only in the current selection, matching Go To Special > Visible cells only. |
| Selection | Ctrl+Shift+O | Parity | Selects cells with notes/comments in the current selection. |
| Selection | F8 / Shift+F8 | Parity | Toggles Extend Selection and Add to Selection modes for keyboard range expansion. |
| Selection | Ctrl+. | Parity | Cycles the active corner of the current selection clockwise. |
| Editing | F2 | Parity | Enters cell edit mode. |
| Editing | Ctrl+F2 | Parity | Moves editing focus to the formula bar for the active cell. |
| Editing | Delete | Parity | Clears selection contents. |
| Editing | Ctrl++ / Ctrl+- | Parity | Inserts/deletes full selected rows or columns, including main-keyboard Ctrl+Shift+= for Ctrl++; normal cell ranges use a native modal with access keys for shift cells right/down or entire row/column on insert and shift cells left/up or entire row/column on delete. |
| Row/Column | Ctrl+9 / Ctrl+Shift+9 | Parity | Hides / unhides selected rows. |
| Row/Column | Ctrl+0 / Ctrl+Shift+0 | Parity | Hides / unhides selected columns. |
| Editing | Escape | Parity | Cancels inline edit. |
| Editing | Alt+Enter | Parity | Inserts a new line in the same cell while editing. |
| Editing | Ctrl+Enter | Parity | Fills the selected range with the current entry. |
| Editing | Ctrl+' | Parity | Copies the formula or content from the cell above into the active cell. |
| Editing | Ctrl+Shift+" | Parity | Copies the calculated value from the cell above into the active cell. |
| Find | Ctrl+F | Parity | Opens Find with access keys for the find field, options expander, Find Next, and Close. |
| Find | Ctrl+H | Parity | Opens Replace with access keys for find/replace fields, options expander, Replace All, and Close. |
| Formulas | Ctrl+` | Parity | Toggles Show Formulas. |
| Formulas | Shift+F3 | Parity | Opens Insert Function with access keys for category, search, OK, and Cancel. |
| Formulas | F9 / Shift+F9 / Ctrl+Alt+F9 / Ctrl+Alt+Shift+F9 | Parity | Calculates workbook/sheet and routes Ctrl+Alt+Shift+F9 through an explicit dependency rebuild plus full workbook recalculation path. |
| Formulas | Ctrl+Shift+U | Parity | Expands/collapses the formula bar. |
| Formulas | Ctrl+[ / Ctrl+] / Ctrl+Shift+[ / Ctrl+Shift+] | Parity | Selects direct or all traceable precedents / dependents for the active cell, switching sheets when the first matched reference is on another worksheet. |
| Review | F7 | Parity | Runs worksheet spelling check. |
| Review | Shift+F2 / Ctrl+Shift+F2 | Partial | Shift+F2 opens Freexcel's simple note workflow and preloads existing selected-cell note text for editing; Ctrl+Shift+F2 opens a distinct model-backed threaded-comment workflow with undo support, and Ctrl+Shift+O plus Review previous/next/show navigation treat notes and threaded comments as comment-bearing cells. Full Excel threaded conversation/reply UI and XLSX threaded-comment package fidelity remain partial. |
| View | Ctrl+Mouse Wheel | Parity | Zooms in/out. |
| View | Ctrl+Alt+= / Ctrl+Alt+- | Parity | Zooms in/out with keyboard shortcuts. |
| Data | Ctrl+Shift+L | Parity | Toggles/reapplies the current filter command. |
| Data | Alt+Down | Partial | Opens the active cell's data-validation list dropdown, including quoted inline list items with commas, or an active-header-anchored AutoFilter dialog backed by an Excel-style menu plan: sort A-Z/Z-A, clear filter from the active header, filter by color with the shared color picker, explicit Excel-style section separators, keyboard-selectable text/number/date filter-family criteria suggestions including executable text equals, above/below average, and blank/nonblank aliases, access keys for search, select-all, clear-all, sort choices, OK/Cancel, searchable value checklist, top/bottom item and percent filters, text, number, date equality/inequality/range, blank, nonblank, and Excel-style two-condition And/Or custom criteria for the current-region column. Full Excel visual menu layout and richer nested command UI remain pending. |
| Data | Alt+Shift+Right / Alt+Shift+Left | Parity | Groups / ungroups selected rows, or whole selected columns. |
| Sheet Tabs | Ctrl+Page Up / Ctrl+Page Down | Parity | Moves to previous/next visible worksheet. |
| Sheet Tabs | Ctrl+Shift+Page Up / Ctrl+Shift+Page Down | Parity | Selects the current and previous/next visible worksheet as a grouped sheet range. |
| Sheet Tabs | Shift+F11 / Alt+Shift+F1 | Parity | Inserts a worksheet. |
| Insert | Alt+= | Parity | Inserts SUM through AutoSum. |
| Insert | Ctrl+L / Ctrl+T | Parity | Opens Create Table. |
| Insert | Ctrl+K | Parity | Opens Insert Hyperlink for the active cell. |
| Insert | Alt+F1 / F11 | Parity | Alt+F1 inserts a default embedded column chart on the active worksheet; F11 creates a new `Chart1`/`Chart2`-style chart sheet from the current range and activates it. |
| Analysis | Ctrl+Q | Partial | Opens a grouped Quick Analysis menu for formatting, charts, totals, tables, and sparklines using existing Freexcel commands, including conditional-format data bars, color scales, icon sets, greater-than/less-than/between/equal-to/text/date-occurring/duplicate-values, top/bottom item and percent, above/below-average, clear-formatting choices, Column/Stacked Column/100% Stacked Column/Line/Pie/Doughnut/Bar/Stacked Bar/100% Stacked Bar/Area/Scatter/Bubble/Radar/Stock charts plus More Charts to the full Insert Chart dialog, Sum/Average/Count/% Total/Running Total/Max/Min adjacent-row totals, hover preview tooltips, icon-sized visual preview swatches, live hover status previews, and an in-grid hover preview overlay that targets either the selection or the adjacent totals/sparkline column. Excel's full rendered worksheet gallery and full option matrix remain partial. |
| Workbook | Ctrl+Shift+G | Parity | Opens Workbook Statistics, with comment totals including notes and threaded comments. |
| UI | F10 | Partial | Enters Freexcel ribbon keytip mode; pixel-perfect Excel keytip overlay placement remains partial under the broader ribbon keytip row. |
| UI | Shift+F10 / Menu key | Partial | Opens the active-cell-anchored worksheet context menu with keyboard access keys plus clipboard, Paste Special, Insert Copied Cells with shift direction prompt, cell insert/delete prompts, row/column insert/delete and sort commands that preserve notes and threaded comments, custom-sort dialog access keys, filter, clear/reapply filter, pick-from-drop-down-list, Quick Analysis, Define Name, Create Table, Format as Table, Text to Columns, Remove Duplicates, Data Validation dialog option/button access keys, hide/unhide rows and columns, row-height/column-width prompts, AutoFit row height/column width, New/Edit/Delete Comment routed to the threaded-comment workflow, new/edit/delete/show note actions, hyperlink, format-cells, clear-all, clear-formats, clear-comments for notes and threaded comments, clear-hyperlinks, clear-content actions, active-cell object-aware menus for picture format/crop/reset-crop, Alt Text, plus shape/text-box size, rotation, fill, outline, and shape reorder commands, and row/column-selection menus that prune irrelevant column/row layout commands. Full Excel context-menu contents remain partial. |
| Editing | Ctrl+; / Ctrl+Shift+; | Parity | Inserts current date / current time, with F4 repeat using the inserted value. |
| Editing | Ctrl+D / Ctrl+R | Parity | Fill Down / Fill Right with undoable formula-reference adjustment. |
| Formatting | Ctrl+5 | Parity | Toggle strikethrough. |
| Formulas | F4 while editing a formula reference | Parity | Cycles local, local range, repeated-sheet-qualified range, full-column/full-row, lowercase-normalized, sheet-qualified, escaped quoted-sheet, 3D sheet-range, external-workbook A1 references, and R1C1-mode references through relative/absolute modes, while preserving structured-reference column names and string literals. |
| Editing | F4 outside formula editing | Partial | Repeats the last repeatable formatting, Merge & Center, paste/paste-special/picture paste, AutoSum, Fill Down/Right/Up/Left, Fill Series, Flash Fill, current date/time insertion, symbol insertion, comments, Clear All/Formats/Contents/Comments/Hyperlinks, sort/filter with notes/threaded-comments preserved, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Subtotal with dialog option access keys, Data Table, Insert Sheet/Chart/Sparkline/Hyperlink, common chart layout/label/axis/trendline formatting, drawing object insertion/size/rotation/color/reorder/Alt Text, outline group/ungroup/collapse/expand, insert/delete row-column/cell with notes/threaded-comments preserved, or hide/unhide row-column command against the current selection with a fresh undoable command instance. Dialog-driven workflows such as Goal Seek, Scenario Manager, import, protection, and sheet-tab context operations remain intentionally non-repeatable. |
| Ribbon | Alt, then F/H/N/J/P/M/A/R/W/Y; Alt+F/H/N/J/P/M/A/R/W/Y | Partial | Opens File backstage or selects the File/Home/Insert/Draw/Page Layout/Formulas/Data/Review/View/Help ribbon tabs through direct Alt combinations or two-step Alt keytip mode. QAT, tab, formula-bar, sheet-tab, and broad visible command keytip metadata render as visible badges for the current visual tree with measured in-window placement; command-scope overlay measurement refreshes layout after tab switches, QAT badges invoke only from top-level mode, off-tab ribbon controls are filtered out, and visible button/toggle/combo command sequences invoke their controls from command scope with toggle state changes, exact command keytips winning over unrelated longer prefixes, duplicate keytip metadata and deterministic resolver behavior guarded by tests. All direct ribbon dropdown menu items and nested Conditional Formatting menu choices have staged keytip metadata/routing, recursive nested leaf/prefix resolution coverage, menu keytips are displayed in the menu gesture-text slot, keyed parent menu choices open their submenu layer, Escape closes menu keytip mode, and real-window host coverage now exercises Home command, dropdown routing, top-level/command overlay badges, plus access-keyed Error Checking and Conditional Formatting manager dialog commands. Pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting are not complete. |

## Next Shortcut Work

1. Build the full Excel Print backstage/settings editing flow for `Ctrl+P`; the current path routes through File/Backstage Print, then opens Freexcel's print preview with a native print-dialog button and active-sheet settings summary.
2. Expand `Ctrl+V` and `Ctrl+Alt+V` to the remaining Excel paste and Paste Special modes beyond the currently supported values/formulas/formats/values-and-source-formatting/all-using-source-theme/all-except-borders/all-merging-conditional-formats/arithmetic/skip-blanks/transpose/link/picture/linked-picture/column-width/comments/validation/number-format paths.
3. Continue broadening Format Cells for `Ctrl+1` and `Ctrl+Shift+F/P` beyond the supported style model and current number-control composition toward Excel's full multi-page dialog.
4. Expand `Ctrl+Shift+F2` from the current model-backed threaded-comment entry point into full Excel threaded conversation/reply UI and XLSX threaded-comment package fidelity.
5. Complete the remaining `Alt+Down` Excel visual menu layout and richer nested command UI beyond the current Excel-style filter menu plan with two-condition custom criteria.
6. Add full in-grid visual Quick Analysis hover-preview rendering and the remaining Excel gallery options for `Ctrl+Q`; current live preview coverage includes icon-sized menu swatches plus status/target metadata, More Charts, and percent/running-total formulas rather than Excel's full rendered worksheet gallery.
7. Continue ribbon keytips into pixel-perfect Excel overlay placement and any future nested submenu keytips beyond Conditional Formatting.
8. Expand `Shift+F10` / Menu key toward the remaining full Excel worksheet context menu entries beyond the current command-backed worksheet, row/column-selection, and active-cell object menus.
9. Decide which dialog-driven workflows should become repeatable through F4 and add explicit repeat command objects for them.

