# Shortcut Parity Matrix

**Last updated:** 2026-05-15

This matrix tracks Excel-for-Windows shortcut fidelity for the visible Freexcel command surface. Status values use the command-surface contract: Parity, Partial, Excluded, or Missing.

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
| Clipboard | Ctrl+V | Partial | Paste and basic paste-special modes exist; full Excel paste matrix remains partial. |
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
| Sheet Tabs | Ctrl+Page Up / Ctrl+Page Down | Parity | Moves to previous/next visible worksheet. |
| Sheet Tabs | Shift+F11 | Parity | Inserts a worksheet. |
| Insert | Alt+= | Parity | Inserts SUM through AutoSum. |
| Insert | Ctrl+K | Parity | Opens Insert Hyperlink for the active cell. |
| Editing | Ctrl+; / Ctrl+Shift+; | Parity | Inserts current date / current time. |
| Editing | Ctrl+D / Ctrl+R | Parity | Fill Down / Fill Right. |
| Formatting | Ctrl+5 | Parity | Toggle strikethrough. |
| Formulas | F4 while editing a formula reference | Partial | Cycles local, sheet-qualified, quoted-sheet, and simple external-workbook A1 references through relative/absolute modes. Structured references and complex external references are not complete. |
| Ribbon | Alt+F/H/N/P/M/A/R/W | Partial | Opens File backstage or selects the File/Home/Insert/Page Layout/Formulas/Data/Review/View ribbon tabs. Per-command keytip overlays are not implemented. |

## Next Shortcut Work

1. Add UI automation coverage for WPF key routing.
2. Extend F4 from A1 reference cycling into repeat-last-command and structured/complex external formula reference forms.
3. Extend ribbon keytips from tab selection into per-command keytip overlays.
