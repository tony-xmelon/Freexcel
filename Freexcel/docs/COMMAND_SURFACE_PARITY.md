# Freexcel Command Surface Parity

**Status:** working audit  
**Last updated:** 2026-05-15

This document tracks Freexcel's visible command surface against Excel for Windows. The goal is Excel parity for commands we choose to support, and an explicit exclusion list for commands that depend on Microsoft cloud services, proprietary runtimes, or very large subsystems.

Microsoft's own support docs describe the common Excel ribbon tabs as Home, Insert, Page Layout, Formulas, Data, Review, and View. They also describe modern Share/co-authoring as a Microsoft 365 and cloud-storage workflow, while legacy Shared Workbook is no longer a primary Review-tab feature in current Excel.

References:

- Microsoft Support, "Use a screen reader to explore and navigate Excel": https://support.microsoft.com/en-us/office/use-a-screen-reader-to-explore-and-navigate-excel-cbf024e8-2abd-4764-b639-f24eed659a53
- Microsoft Support, "Collaborate on Excel workbooks at the same time with co-authoring": https://support.microsoft.com/en-us/office/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring-7152aa8b-b791-414c-a3bb-3024e46fb104
- Microsoft Support, "What happened to shared workbooks in Excel?": https://support.microsoft.com/en-us/office/what-happened-to-shared-workbooks-in-excel-150fc205-990a-4763-82f1-6c259303fe05

## Explicitly Excluded

These features are out of scope and should not be treated as bugs when absent. UI should either omit them or clearly label them as unsupported.

| Area | Excel Feature | Freexcel Decision | Reason |
|---|---|---|---|
| Collaboration | Share, cloud links, Microsoft 365 co-authoring, presence, permissions | Excluded | Requires identity, OneDrive/SharePoint/cloud sync, remote conflict resolution, and service integrations. |
| Automation | VBA projects, macro execution, COM add-ins, Office Scripts | Excluded for v1 | Proprietary/runtime security surface. Freexcel may later add its own sandboxed scripting, not VBA compatibility. |
| BI/Data Model | Power Pivot, Power Query/M engine, data model relationships, OLAP cubes | Excluded for v1 | Large external query/runtime subsystem. Basic CSV/XLSX import remains in scope. |
| External Services | Stock/geography linked data types, live web queries, Teams comments, online version history | Excluded | Depends on Microsoft services or authenticated cloud APIs. |
| Enterprise Controls | IRM, sensitivity labels, encrypted collaboration policies | Excluded | Depends on Microsoft 365 tenant infrastructure. |

## Deferred Architectural Features

These are not cloud/proprietary exclusions, but they require larger architecture that should be designed explicitly before adding UI.

| Area | Excel Feature | Freexcel Decision | Reason |
|---|---|---|---|
| Window Management | New Window, Arrange All, View Side by Side, Synchronous Scrolling, Reset Window Position, Switch Windows | Deferred until multi-window workbook hosting exists | Current Freexcel host is a single workbook window. Implementing these faithfully requires multiple live windows over the same workbook/session, command routing across windows, synchronized scroll state, and lifecycle handling. |
| Split Panes | Independent split-pane scrolling | Deferred after split pane baseline | Current implementation stores split pane state and renders split bars. Excel-like independent pane scrolling needs per-pane viewport state and input routing. |
| Theme System | Themes, theme colors, theme fonts, theme effects | Deferred until workbook-level theme model exists | Excel themes affect styles, charts, shapes, color palettes, font pairs, and XLSX theme parts. Freexcel currently stores concrete colors/fonts, so exposing theme editing as if it were real would be misleading. |
| Worksheet Background | Page Layout > Background image | Deferred until worksheet background image model and XLSX media relationship handling exists | Excel sheet backgrounds are display-only worksheet images, distinct from printable pictures. Freexcel does not yet have a non-printing sheet-background layer. |

## Current Parity Summary

| Tab/Surface | Implemented To Excel-Like Baseline | Remaining Parity Gaps |
|---|---|---|
| File / Backstage | New, Open, Save with current-path reuse, Save As, Print, Export, Close, Options, Recent files | Share is excluded. Account is informational only unless a non-cloud account story is designed. |
| Quick Access / Window | Save, Undo, Redo, minimize/maximize/close | Customize Quick Access Toolbar is not implemented. |
| Home / Clipboard | Cut, Copy, Paste, Paste Special values/formulas/formats, transpose, arithmetic operations, paste link, keep source column widths, pasted range pictures, and external bitmap clipboard paste as embedded picture objects with undo/native persistence | Interactive object handles, crop, and advanced picture formatting are partial. |
| Home / Font | Font family/size, grow/shrink font, bold, italic, underline, double underline, strikethrough, Excel Ctrl+2/3/4 font-toggle aliases, colors, fill, border presets, outline/remove-border keyboard shortcuts | Full Excel border gallery, theme colors, effects, and custom font dialog are partial. |
| Home / Alignment | Horizontal/vertical alignment, wrap, merge, indent, text rotation presets | Distributed/justify alignment, shrink-to-fit, full Format Cells alignment dialog are partial. |
| Home / Number | General, number, currency, percent, comma, decimal increase/decrease, date/time/text/custom subset, Excel number-format keyboard shortcuts | Full Excel locale/accounting/fraction/custom format fidelity is partial. |
| Home / Styles | Conditional formatting entry points, clear rules with undo, table formatting, cell styles; supported conditional-format commands propagate across grouped sheets | Conditional-format rule manager and icon sets/data bars/color scales are simplified. Table semantics are mostly formatting, not full Excel structured tables. |
| Home / Cells | Insert/delete cells with shift directions, rows/columns/sheets, row height, column width, hide/unhide, lock cell/protect sheet; row/column structural commands propagate across grouped sheets as one undoable operation | Insert/delete row/column workflows need more Excel dialog polish, but the cell shift semantics are implemented and undoable. |
| Home / Editing | AutoSum, fill directions/series, clear, sort/filter, find/replace, Go To, Go To Special for blanks/constants/formulas/comments/validation/visible cells with disjoint selection rendering | Flash Fill is not implemented. |
| Insert | Table, native chart model commands/rendering for column/line/pie/bar, chart title/axis-title/legend layout model with native save/load and duplicate-sheet preservation, sparklines, hyperlink, comments, symbols, text box, local image-file pictures with basic resize/rotation commands, basic shapes | PivotTables are excluded for v1. XLSX chart package parts are detected as unsupported rather than round-tripped. Chart fidelity remains partial for advanced chart formatting, labels, secondary axes, trendlines, combo charts, and unsupported chart families. Screenshots, 3D models, add-ins, and online pictures are not in scope unless added explicitly. |
| Draw | Rectangle, ellipse, line, text box, bring forward, send backward, command-based size/rotation, fill, and outline colors for shapes and text boxes with native persistence | Freehand ink, pens, selection handles, drag-based object resizing/rotation, crop, gradients, effects, and advanced shape/text formatting are partial. |
| Page Layout | Margins, header/footer margins, orientation, paper size, print area, scale-to-fit, first page number, print-quality DPI, manual page breaks, print titles, print gridlines/headings, header/footer editing with different first-page and odd/even page variants plus scale-with-document/align-with-margins options, Center on page options, page-order selection, black-and-white printing, draft-quality printing, printed cell-error display options, comments/notes print mode, and draggable Page Layout margin guides with undo/grouped-sheet propagation; Page Setup dialog for page/margins/sheet print options with atomic undo; print preview honors paper/orientation/margins/header-footer margins/print area/print gridlines, printed row/column headings, repeated print-title rows/columns with horizontal pagination, printed headers/footers with page tokens, first-page/odd-even variants, configured first page number, and align-with-margins behavior, vertical/horizontal page centering state, down-then-over vs over-then-down page traversal, cell errors as displayed/blank/dash/#N/A, comments printed at end of sheet, and comments printed as displayed beside their in-page cells; native and XLSX save/load preserve page setup, margins/header-footer margins, header/footer variants and flags, centering, page-order, first-page-number, print-quality DPI, black-and-white, draft-quality, print-error, and print-comments values; page setup and header/footer commands propagate across grouped sheets as one undoable operation | Themes and worksheet background remain deferred architectural features. |
| Formulas | Function insertion, category menus for Logical/Text/Date/Lookup/Math, AutoSum variants, named ranges, trace precedents/dependents, show formulas, error checking, calculation options | Watch Window, Evaluate Formula, full error-checking rules, and full R1C1 formula authoring are partial. |
| Data | CSV Get Data, refresh/recalc, sort/filter, Text to Columns, Remove Duplicates, Data Validation, Consolidate; supported data-validation commands propagate across grouped sheets | Power Query connectors are excluded. Advanced sort/filter dialogs, forecast/what-if/group/subtotal are not implemented. |
| Review | Spell check, workbook statistics, comments, protect sheet/workbook, allow edit ranges | Share is excluded. Accessibility checker, threaded comments/notes split, track changes, and language tools are not implemented. |
| View | Normal view, Page Break Preview, Page Layout view with print-area and margin-guide overlays, gridlines/headings toggles, freeze panes, split pane command/state with native and XLSX persistence, Custom Views dialog with Show/Add/Delete and native persistence, zoom controls, formula bar expansion; workbook view commands propagate across grouped sheets as one undoable operation, with page-break/print-area/split overlays in the grid | Arrange windows, independent split-pane scrolling, ruler handles, and full workbook view-mode polish are partial. |
| Sheet Tabs | Add, rename, duplicate, delete, drag reorder, move left/right, hide/unhide, tab color, select all sheets, ungroup sheets, Ctrl/Shift grouped selection, `[Group]` title indicator, navigation, grouped direct cell edits/fill/clear/paste-link/text-to-columns/spell-correction/date-time insertion, grouped common cell formatting, grouped conditional formatting/data validation, grouped row/column structure, grouped Page Layout settings, grouped picture insert/resize/rotate, grouped text box/basic shape insertion, grouped drawing-object size/rotation/fill/outline and shape reordering | Grouped-sheet propagation remains partial for advanced object effects and advanced data commands that Excel applies across grouped sheets. |
| Keyboard | Core navigation, edit, copy/cut/paste, undo/redo, find/replace, Ctrl+A current-region/whole-sheet selection, Ctrl+Space/Shift+Space column-row selection, Ctrl++/Ctrl+- insert-delete shortcuts, Ctrl+9/Ctrl+0 row-column hide/unhide shortcuts, Save/Open/New/Print, Format Cells, Show Formulas, number-format shortcuts, outline/remove-border shortcuts, F4 local/sheet-qualified/quoted-sheet/simple-external A1 formula-reference cycling, tab-level Alt ribbon keytips, core visible command shortcuts | See `docs/SHORTCUT_PARITY_MATRIX.md`; per-command keytip overlays, repeat-last-command F4 behavior, structured/complex-external F4 reference cycling, full insert/delete dialog shortcut matrix, and long-tail Excel shortcuts are not complete. |

## Immediate Parity Backlog

These are the next highest-value gaps because they are visible commands already present in the UI.

1. Add UI automation coverage for the shortcut matrix and extend tab-level ribbon keytips into per-command keytip overlays.
2. Design theme/background Page Layout architecture.
3. Extend grouped-sheet propagation beyond cell edits/formatting/page setup/row-column structure/pictures/text boxes/basic shapes/basic object size-rotation-fill-outline to advanced object effects and supported data commands where Excel applies actions to every grouped sheet.
4. Extend chart fidelity beyond title/axis-title/legend layout into labels, secondary axes, trendlines, combo charts, and advanced formatting.
5. Expand picture/object fidelity beyond pasted range pictures, external bitmap clipboard paste, local image insertion, and command-based object resize/rotation/fill/outline into interactive handles, crop, gradients, effects, and richer object formatting.
6. Add full conditional-format rule manager coverage, including icon sets and richer color scales/data bars.
7. Add remaining View parity for arrange windows and independent split-pane scrolling.
8. Add Data parity for advanced sort/filter dialogs, subtotal, grouping/outline, forecast, and what-if analysis.
9. Keep excluded commands visibly explicit: Share/cloud co-authoring, VBA/macros, Power Query/Power Pivot/data model, PivotTables, and Microsoft linked data types.

## Acceptance Rule

Every visible command should be in one of these states:

- **Parity:** behaves like Excel for the supported model.
- **Partial:** documented with exact missing behavior and tests for what is supported.
- **Excluded:** hidden, disabled, or labeled as unsupported, with the reason listed in this document.

No visible command should silently pretend to support a cloud, proprietary, or complex feature that Freexcel does not actually implement.
