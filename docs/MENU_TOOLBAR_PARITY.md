# Freexcel Menu and Toolbar Parity

**Last updated:** 2026-05-21
**Purpose:** Tracks individual ribbon button and menu-item fidelity against Excel for Windows.

## Coverage Summary

<!-- command-inventory:coverage-summary:start -->
| Tab | Implemented | Partial | Not Implemented | Deferred | Excluded | Coverage |
|---|---:|---:|---:|---:|---:|---:|
| File/Backstage | 8 | 4 | 0 | 0 | 3 | **100%** |
| QAT | 3 | 0 | 0 | 0 | 1 | **100%** |
| Home | 48 | 8 | 0 | 0 | 1 | **100%** |
| Insert | 10 | 3 | 0 | 1 | 9 | **100%** |
| Draw | 9 | 3 | 0 | 1 | 1 | **100%** |
| Page Layout | 16 | 1 | 0 | 0 | 0 | **100%** |
| Formulas | 16 | 1 | 0 | 0 | 0 | **100%** |
| Data | 17 | 1 | 0 | 0 | 2 | **100%** |
| Review | 8 | 2 | 0 | 0 | 6 | **100%** |
| View | 12 | 1 | 0 | 0 | 4 | **100%** |
| Sheet Tabs | 9 | 0 | 0 | 0 | 0 | **100%** |
| Help | 3 | 0 | 0 | 0 | 3 | **100%** |
| **TOTAL** | **159** | **24** | **0** | **2** | **30** | **100%** |
<!-- command-inventory:coverage-summary:end -->

Coverage = (Implemented + Partial) / (Implemented + Partial + Not Implemented). Deferred and Excluded items are reported separately.

## Status Legend

| Status | Meaning |
|---|---|
| Implemented | Works like Excel |
| Partial | Works but incomplete; see Notes |
| Not Implemented | Absent; not yet built |
| Deferred | Explicitly postponed because it needs a larger subsystem or interaction architecture |
| Excluded | Out of scope (cloud/proprietary/large subsystem) |

Closeout alignment note: the May 2026 command parity closeout now reflects completed Home-tab cleanup for persistent
Format Painter, alignment and shrink-to-fit style state, AutoFit measurement, and Format Cells dialog coverage. Remaining
Partial rows continue to track intentionally bounded fidelity gaps such as custom/locale number formats, conditional
formatting manager/rendering breadth, table/style theme depth, Flash Fill inference, and PDF/XPS export options. Advanced
chart-family authoring/rendering remains Deferred until each family has a data model and renderer.
Ribbon overflow now keeps collapsed group menus closer to Excel by preserving cloned menu checked state,
input gesture text, and dynamic menu-open behavior instead of reducing collapsed groups to static labels.

---

## File Menu / Backstage

| Item | Status | Notes |
|---|---|---|
| New | Implemented | Ctrl+N |
| Open | Implemented | Ctrl+O |
| Save | Implemented | Ctrl+S; Backstage caption exposes a visible access key |
| Save As | Implemented | Backstage caption exposes a visible access key |
| Print Preview | Implemented | |
| Export to PDF/XPS | Partial | Deterministic PDF export uses the print renderer and PDFsharp-WPF raster pages; active-sheet, selected-range, entire-visible-workbook, page-range, page-count validation, standard/minimum-size quality options, extensionless `.pdf`/explicit `.xps` path normalization, access-keyed publish options, and open-after-publish options are supported; requested document properties embed workbook-name title plus Freexcel author/subject/keywords metadata for PDF and XPS package core properties; selectable/vector PDF text and remaining full Excel PDF publish options remain partial |
| Close | Implemented | Backstage caption exposes a visible access key |
| Options | Partial | General, Formulas, View, and Save subsets including calculation/error-checking and formula bar preferences; sidebar categories, editable fields, option toggles, and OK/Cancel expose keyboard access keys |
| Recent Files | Implemented | |
| Info panel | Partial | Protection/accessibility summary, workbook statistics, accessibility and formula-error counts, and file properties |
| Share | Partial | Windows Share for saved local files; missing or unsaved local files route through Save As first; Microsoft 365 cloud links/coauthoring excluded |
| Check In/Out | Excluded | SharePoint |
| Online Templates | Excluded | |
| XLSX unsupported-feature warnings | Implemented | |
| Account | Partial | No MS account integration |

## Quick Access Toolbar

| Item | Status | Notes |
|---|---|---|
| Save | Implemented | |
| Undo | Implemented | |
| Redo | Implemented | |
| Customize QAT | Excluded | Low v1 value |

---

## Home Tab

### Clipboard

| Item | Status | Notes |
|---|---|---|
| Cut | Implemented | Cut marquee; paste consumes cut state |
| Copy | Implemented | |
| Paste | Implemented | Internal values/formulas/formats/all and external text paste covered |
| Paste Special | Implemented | Supported modes are undoable with arithmetic-operation radio buttons (None/Add/Subtract/Multiply/Divide); all dialog choices and OK/Cancel expose access keys; external rich-object paste excluded |
| Format Painter | Implemented | Single-click and persistent double-click modes |

### Font

| Item | Status | Notes |
|---|---|---|
| Font Family | Implemented | |
| Font Size | Implemented | |
| Grow/Shrink Font | Implemented | |
| Bold | Implemented | Ctrl+B |
| Italic | Implemented | Ctrl+I |
| Underline | Implemented | Ctrl+U |
| Double Underline | Implemented | |
| Strikethrough | Implemented | Ctrl+5 |
| Font Color | Implemented | Shared color picker exposes custom color and button access keys. |
| Fill Color | Implemented | Shared color picker exposes custom color and button access keys. |
| Borders (presets) | Implemented | |
| Full Border Gallery | Partial | Expanded preset gallery with remembered line color/style; interactive draw/erase border tools deferred |
| Theme Colors | Partial | Preset color schemes plus Customize Colors entry point through an access-keyed theme dialog |

### Alignment

| Item | Status | Notes |
|---|---|---|
| Horizontal Align | Implemented | Left/Center/Right |
| Vertical Align | Implemented | Top/Middle/Bottom |
| Wrap Text | Implemented | |
| Merge & Center | Implemented | |
| Indent +/- | Implemented | |
| Text Rotation presets | Implemented | |
| Distributed/Justify | Implemented | Style, dialog, renderer, XLSX IO |
| Shrink to Fit | Implemented | Style, dialog, renderer, XLSX IO |
| Format Cells Alignment dialog | Implemented | Supported alignment model |

### Number

| Item | Status | Notes |
|---|---|---|
| Number Format dropdown | Implemented | |
| General/Number/Currency | Implemented | |
| Accounting/Date/Time | Implemented | |
| Percentage/Fraction/Scientific/Text | Implemented | |
| Custom Number Format | Partial | Broader Format Cells catalog plus editable custom format codes; supports invariant conditional sections for numbers and date/time values, named colors, default indexed `Color1`-through-`Color56` prefixes for numeric/date/text sections, escaped literals including escaped layout directive characters, active percent scaling with token placement and quoted/escaped literal handling, date/time with long and compact AM/PM markers, contextual month/minute token handling across quoted literals, five-`m` month initials, rounded clock and elapsed fractional seconds, elapsed-time, and text-section spacing/fill directive cleanup, variable decimals, variable and fixed-denominator fractions, scientific notation, elapsed time, comma scaling, visible currency symbols from LCID tokens, and deterministic decimal/group/date separators for selected modeled LCIDs including US, East Asian, European, and Latin American Spanish variants; full locale/LCID and workbook palette/theme overrides remain partial |
| Increase/Decrease Decimal | Implemented | |
| Comma Style | Implemented | |
| Currency Style | Implemented | |
| Percentage Style | Implemented | |
| Full locale/accounting fidelity | Partial | Invariant/accounting subset with LCID currency-symbol preservation, modeled numeric/date separators for `404`, `405`, `406`, `407`, `409`, `40B`, `40C`, `40E`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `419`, `41D`, `41F`, `422`, `804`, `807`, `813`, `816`, `C04`, `C0A`, `1009`, and `100C`, and date/time/elapsed-time/text layout directive cleanup; full Excel/OS locale fidelity and exact accounting layout widths remain partial |

### Styles

| Item | Status | Notes |
|---|---|---|
| Conditional Formatting | Partial | Authoring/editing available for modeled rules with access-keyed value/format fields, visual-rule threshold/color fields, option toggles, and OK/Cancel; Conditional Formatting > Icon Sets exposes Excel-like grouped Directional/Shapes/Indicators/Ratings presets with direct one-click rules plus More Rules; grid rendering covers cell value, formulas, above/below average, top/bottom, duplicate/unique, text, blank/nonblank, error/no-error, color scales, data bars, and visible 3/4/5-band icon sets with style-aware arrows, traffic lights, signs, symbols, flags, ratings, quarters, boxes, reverse/icons-only display, and authored percent/number thresholds; simplified manager remains partial |
| Format as Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, access-keyed range/header controls, one-step undo for table creation plus styling, and an Excel-scale Light/Medium/Dark gallery with swatch previews; command-level and XLSX-loaded table value filters hide non-matching data rows with multi-column AND, blank inclusion, and totals-row exclusion semantics; totals-row labels and common functions (`sum`, `average`, `count`, `countNums`, `min`, `max`) can be materialized with undo; structured-reference formula evaluation and full table style theme semantics remain partial |
| Cell Styles | Partial | Expanded built-in preset gallery backed by reusable `StyleDiff` planners; Accent 20% presets resolve against the active workbook theme; full workbook named styles remain deferred |

### Cells

| Item | Status | Notes |
|---|---|---|
| Insert Cells/Rows/Columns/Sheets | Implemented | |
| Delete Cells/Rows/Columns/Sheets | Implemented | |
| Row Height | Implemented | |
| Column Width | Implemented | |
| AutoFit Row/Column | Implemented | Measurement-based estimate |
| Hide/Unhide Rows/Columns/Sheets | Implemented | |
| Format Cells dialog | Implemented | Ctrl+1; supported style model |

### Editing

| Item | Status | Notes |
|---|---|---|
| AutoSum | Implemented | Alt+= |
| Fill Down/Right/Up/Left | Implemented | Ctrl+D/R |
| Fill Series | Implemented | |
| Flash Fill | Partial | Expanded deterministic inference including common first-name/last-name contact patterns, dotted/underscored/hyphenated email display-name cleanup, shared-domain email generation with `.`, `_`, or `-` first/last, first-initial/last, and last/first-initial separators, and first/last-initial email aliases; full Excel inference partial |
| Clear All | Implemented | |
| Clear Formats/Contents/Comments/Hyperlinks | Implemented | |
| Sort | Implemented | |
| Filter | Implemented | |
| Find | Implemented | Ctrl+F; dialog field, options, Find Next, and Close expose access keys |
| Replace | Implemented | Ctrl+H; dialog fields, options, Replace All, and Close expose access keys |
| Go To | Implemented | Ctrl+G/F5 |
| Go To Special | Implemented | |
| Select Objects | Excluded | Object drag handles deferred |

---

## Insert Tab

| Item | Status | Notes |
|---|---|---|
| PivotTable | Partial | Creates worksheet-range PivotTables on the current sheet or a new worksheet; create dialog source/placement choices expose access keys; Field List action buttons expose access keys; PivotTable Options choices expose access keys including undoable "For empty cells show" text; materialized value cells apply supported built-in and custom workbook-catalog value-field number format IDs; missing matrix intersections can display modeled empty-cell text; label/value filter dialogs expose access-keyed fields and OK/Cancel; checked-item filter search/select-all and the tabbed Value Field Settings dialog expose access-keyed fields, tabs, and OK/Cancel; Value Field Settings exposes a broader built-in preset catalog and edits custom format codes; model-first load/save |
| Recommended PivotTables | Excluded | Proprietary heuristics |
| Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, access-keyed range/header controls, and one-step undo via the same path as Format as Table; the shared Format as Table gallery exposes Excel-scale Light/Medium/Dark style choices with swatch previews; table value filters execute for command and XLSX-loaded metadata; totals-row labels and common functions can be materialized with undo; structured-reference formula evaluation and full table style theme semantics remain partial |
| Picture (from file) | Implemented | |
| Online Pictures | Excluded | |
| Shapes | Implemented | Rect/ellipse/line |
| Icons | Excluded | Proprietary Microsoft icon library |
| 3D Models | Excluded | |
| SmartArt | Excluded | Retained part |
| Screenshot | Excluded | OS-level feature |
| Chart - column/bar/line/area | Implemented | Select Data Source, Move Chart, Insert Chart, and chart format dialogs expose keyboard access keys for modeled fields and option controls |
| Chart - pie/doughnut/scatter/bubble | Implemented | |
| Chart - stock/radar | Implemented | |
| Chart - surface/treemap/sunburst/histogram | Deferred | Recognized from XLSX where detected; authoring/rendering and lossless package writing need per-family model/renderer |
| Chart - waterfall/funnel/map/3D | Deferred | Recognized from XLSX where detected; authoring/rendering and lossless package writing need per-family model/renderer |
| Recommended Charts | Excluded | Proprietary heuristics |
| Sparklines (line/column/win-loss) | Implemented | |
| Text Box | Implemented | |
| Header & Footer | Implemented | Presets, section fields, token buttons, options, and OK/Cancel expose access keys |
| WordArt | Excluded | |
| Symbols | Implemented | Picker Cancel action exposes a keyboard access key. |
| Hyperlink | Implemented | Ctrl+K |
| Comment/Note | Partial | Insert tab creates local threaded comments; Review tab also keeps simple note commands. Full threaded conversation/reply UI remains partial |
| Equation | Excluded | |

---

## Draw Tab

| Item | Status | Notes |
|---|---|---|
| Rectangle | Implemented | |
| Ellipse | Implemented | |
| Line | Implemented | |
| Freehand Ink | Excluded | |
| Bring Forward | Implemented | |
| Send Backward | Implemented | |
| Object Size/Rotation | Implemented | Command-based |
| Fill Color | Implemented | Shared color picker exposes custom color and button access keys. |
| Outline Color | Implemented | |
| Alt Text | Implemented | |
| Interactive drag handles | Deferred | Needs object-selection/adornment layer |
| Crop | Partial | Image crop/reset commands render and persist to native JSON/XLSX; interactive handles pending |
| Gradients/Effects | Partial | Shape gradient fill with dedicated access-keyed start/end color pickers and shadow effect with native JSON/XLSX persistence; full Excel gradient gallery and additional effect types pending |
| Selection Pane | Partial | Lists sheet objects with per-item visibility checkboxes, search/filter controls, access-keyed Show All / Hide All bulk controls, Bring Forward / Send Backward reorder buttons, model-backed object renaming with undo plus Native JSON and XLSX `cNvPr` name persistence for supported drawing objects, and OK/Cancel; drag-reorder within the list remains pending |

---

## Page Layout Tab

| Item | Status | Notes |
|---|---|---|
| Margins | Implemented | |
| Orientation | Implemented | |
| Paper Size | Implemented | |
| Print Area (set/clear) | Implemented | |
| Breaks | Implemented | Manual page breaks |
| Background | Implemented | Display-only tiled |
| Print Titles | Implemented | |
| Scale to Fit | Implemented | |
| Print Gridlines | Implemented | |
| Print Headings | Implemented | |
| Sheet Options | Implemented | |
| Themes | Partial | Presets plus custom theme dialog reachable from Themes, Theme Colors, Theme Fonts, and Theme Effects; dialog preset buttons, metadata fields, color slots, and Save/Cancel expose keyboard access keys; deep OOXML effects deferred |
| Colors preset menu | Implemented | |
| Fonts preset menu | Implemented | |
| Effects preset menu | Implemented | |
| Header/Footer editing | Implemented | Presets, section fields, token buttons, option toggles, and OK/Cancel expose access keys |
| Page Setup dialog | Implemented | Page, Margins, and Sheet tab labels plus footer actions expose access keys |
| Center on page | Implemented | |
| Page Order | Implemented | |

---

## Formulas Tab

| Item | Status | Notes |
|---|---|---|
| Insert Function | Implemented | Search, category, function list, Help, OK, and Cancel expose access keys |
| AutoSum variants | Implemented | |
| Logical menu | Implemented | |
| Text menu | Implemented | |
| Date & Time menu | Implemented | |
| Lookup & Reference menu | Implemented | |
| Math & Trig menu | Implemented | |
| Name Manager | Implemented | Dialog list, name/range fields, and Define/Delete/Close commands expose access keys |
| Define Name | Implemented | Name/range fields and command buttons expose access keys through the named-range manager |
| Use in Formula | Implemented | |
| Create from Selection | Implemented | Dialog choices and OK/Cancel expose access keys |
| Trace Precedents | Implemented | |
| Trace Dependents | Implemented | |
| Remove Arrows | Implemented | |
| Show Formulas | Implemented | Ctrl+` |
| Error Checking | Partial | Issue list plus ribbon entry point to error-checking options, access-keyed issue actions, and supported checks including numbers stored as text, formulas referring to blank cells, two-digit-year text dates, formulas inconsistent with nearby formulas, SUM formulas omitting adjacent cells, and unlocked formula cells; partial rule taxonomy |
| Evaluate Formula | Implemented | Help, Previous, Step Out, Evaluate, Step In, and Close actions expose access keys |
| Watch Window | Implemented | Dialog command buttons expose keyboard access keys. |
| R1C1 Reference Style | Implemented | |
| Calculation Options | Implemented | Manual/auto |
| Calculate Now | Implemented | |
| Calculate Sheet | Implemented | |

---

## Data Tab

| Item | Status | Notes |
|---|---|---|
| Get Data (CSV) | Implemented | |
| Power Query connectors | Excluded | |
| Refresh All | Implemented | Recalc |
| Sort | Implemented | Single/multi-key |
| Filter | Implemented | |
| Advanced Filter | Implemented | Access-keyed action/options/reference controls |
| Text to Columns | Implemented | Wizard exposes access-keyed source mode, delimiter, qualifier, destination, reference picker, and OK/Cancel controls |
| Remove Duplicates | Implemented | |
| Data Validation | Implemented | |
| Consolidate | Implemented | Function, reference list, destination, label options, and Add/Delete/OK/Cancel expose access keys |
| Goal Seek | Implemented | Dialog input labels, status dialog buttons, and OK/Cancel expose access keys |
| Scenario Manager | Implemented | Dialog list, add/edit fields, action buttons, and Close expose access keys. |
| Data Table | Implemented | 1-var/2-var dialog with access-keyed table type and input-cell reference fields |
| Forecast Sheet | Implemented | No chart UI |
| Subtotal | Implemented | |
| Group/Outline | Implemented | |
| Ungroup | Implemented | |
| Show/Hide Detail | Implemented | |
| Data Model / Power Pivot | Excluded | |
| Flash Fill | Partial | Expanded deterministic inference including common first-name/last-name contact patterns, dotted/underscored/hyphenated email display-name cleanup, shared-domain email generation with `.`, `_`, or `-` first/last, first-initial/last, and last/first-initial separators, and first/last-initial email aliases; full Excel inference partial |

---

## Review Tab

| Item | Status | Notes |
|---|---|---|
| Spell Check | Partial | Broader known-corrections text-cell scan with casing-preserving replace, replace-all, ignore support, and internet/email/file-address span skipping; no full dictionary/proofing engine |
| Thesaurus | Excluded | Requires external dictionary service |
| Accessibility Checker | Partial | Merged cells, missing/generic alt text, untitled or generic-titled charts, non-descriptive hyperlink text, default worksheet tab names, and hidden sheets/rows/columns with content; full Excel rule taxonomy remains partial |
| Smart Lookup | Excluded | |
| Translate | Excluded | |
| New Comment | Partial | Threaded comment text can be added/edited/deleted locally through the Review ribbon and Ctrl+Shift+F2; full threaded conversation/reply UI remains partial |
| New Note | Implemented | Simple cell notes |
| Edit Note | Implemented | Reuses the note editor with existing note text preloaded |
| Delete Note | Implemented | |
| Previous/Next Note | Implemented | Navigates simple cell notes on the active sheet |
| Show Notes | Implemented | Opens a list of simple cell notes |
| Protect Sheet | Implemented | Password dialog OK/Cancel expose access keys |
| Allow Edit Ranges | Implemented | Add, remove, and clear allowed ranges with undo support; range field and OK/Cancel expose access keys |
| Protect Workbook | Implemented | Password dialog OK/Cancel expose access keys |
| Share | Implemented | Windows Share for saved local files; missing current paths route through Save As |
| Share Workbook (legacy) | Excluded | |
| Track Changes | Excluded | |
| Threaded Comments | Partial | Local single-message threaded comment model, shortcut, navigation, delete command, and list display are supported; full Excel conversation/reply UI and cloud identity semantics remain partial |
| Statistics | Implemented | |

---

## View Tab

| Item | Status | Notes |
|---|---|---|
| Normal | Implemented | |
| Page Break Preview | Implemented | |
| Page Layout | Implemented | |
| Custom Views | Implemented | Dialog list, actions, Add View name field, and OK/Cancel expose access keys |
| Show Gridlines | Implemented | |
| Show Headings | Implemented | |
| Show Ruler | Implemented | |
| Show Formula Bar | Implemented | |
| Freeze Panes | Implemented | |
| Split | Implemented | Toggle clears frozen panes and supports independent split quadrants, draggable dividers, pane-specific scrollbars, wheel targeting, clipping, and active-state ribbon feedback |
| Zoom | Implemented | |
| Zoom to Selection | Implemented | |
| 100% Zoom | Implemented | |
| New Window | Excluded | Deferred until multi-window hosting |
| Arrange All | Partial | Stores choice and marks the selected menu option; no live multi-window layout |
| View Side by Side | Excluded | Deferred until multi-window hosting |
| Synchronous Scrolling | Excluded | Deferred until multi-window hosting |
| Switch Windows | Excluded | Deferred until multi-window hosting |

---

## Sheet Tab Context Menu

| Item | Status | Notes |
|---|---|---|
| Add Sheet | Implemented | |
| Rename Sheet | Implemented | |
| Delete Sheet | Implemented | |
| Duplicate Sheet | Implemented | |
| Move Left | Implemented | |
| Move Right | Implemented | |
| Tab Color | Implemented | |
| Hide/Unhide Sheet | Implemented | |
| Select All Sheets | Implemented | Group |
| Ungroup Sheets | Implemented | |

---

## Help Tab

| Item | Status | Notes |
|---|---|---|
| Help (opens repo) | Implemented | |
| Send Feedback | Implemented | |
| About | Implemented | |
| Microsoft training | Excluded | |
| Microsoft templates | Excluded | |
| Microsoft accounts | Excluded | |
