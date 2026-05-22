# Freexcel Command Surface Parity

**Status:** working audit  
**Last updated:** 2026-05-21

This document tracks Freexcel's visible command surface against Excel for Windows. The goal is Excel parity for commands we choose to support, and an explicit exclusion list for commands that depend on Microsoft cloud services, proprietary runtimes, or very large subsystems.

## Status Legend

| Status | Meaning |
|---|---|
| Implemented | Works like Excel for the supported model |
| Partial | Works but missing something; see Notes |
| Not Implemented | Absent; not yet built |
| Deferred | Explicitly postponed because it needs a larger subsystem or interaction architecture |
| Excluded | Out of scope (cloud / proprietary / large subsystem) |

Coverage is computed as **(Implemented + Partial) / (Implemented + Partial + Not Implemented) x 100**. Excluded and Deferred commands are reported separately.

---

## Coverage Summary

<!-- command-inventory:coverage-summary:start -->
| Tab | Implemented | Partial | Not Implemented | Deferred | Excluded | **Coverage** |
|---|---:|---:|---:|---:|---:|---:|
| File/Backstage | 8 | 4 | 0 | 0 | 3 | **100%** |
| QAT | 3 | 0 | 0 | 0 | 1 | **100%** |
| Home | 48 | 8 | 0 | 0 | 1 | **100%** |
| Insert | 10 | 3 | 0 | 1 | 9 | **100%** |
| Draw | 8 | 3 | 0 | 1 | 1 | **100%** |
| Page Layout | 16 | 1 | 0 | 0 | 0 | **100%** |
| Formulas | 16 | 1 | 0 | 0 | 0 | **100%** |
| Data | 17 | 1 | 0 | 0 | 2 | **100%** |
| Review | 8 | 2 | 0 | 0 | 6 | **100%** |
| View | 12 | 1 | 0 | 0 | 4 | **100%** |
| Sheet Tabs | 9 | 0 | 0 | 0 | 0 | **100%** |
| Help | 3 | 0 | 0 | 0 | 3 | **100%** |
| **TOTAL** | **158** | **24** | **0** | **2** | **30** | **100%** |
<!-- command-inventory:coverage-summary:end -->

---

## Explicitly Excluded

These features are out of scope and should not be treated as bugs when absent.

| Area | Excel Feature | Freexcel Decision | Reason |
|---|---|---|---|
| Collaboration | Cloud links, Microsoft 365 co-authoring, presence, permissions | Excluded | Requires identity, OneDrive/SharePoint/cloud sync, remote conflict resolution. Local Windows Share remains in scope for saved files. |
| Automation | VBA projects, macro execution, COM add-ins, Office Scripts | Excluded for v1 | Proprietary/runtime security surface. |
| BI/Data Model | Power Pivot, Power Query/M, data model relationships, OLAP cubes | Excluded for v1 | Large external query/runtime subsystem. |
| External Services | Stock/geography linked data types, live web queries, Teams comments, online version history, online template discovery | Excluded | Depends on Microsoft services or authenticated cloud APIs. |
| Enterprise Controls | IRM, sensitivity labels, encrypted collaboration policies | Excluded | Depends on Microsoft 365 tenant infrastructure. |

## Deferred Architectural Features

Not cloud/proprietary exclusions, but require larger architecture before adding UI.

| Area | Excel Feature | Freexcel Decision |
|---|---|---|
| Window Management | New Window, View Side by Side, Synchronous Scrolling, Reset Window Position, Switch Windows | Deferred until multi-window workbook hosting exists |
| Theme System | Themes, theme colors, theme fonts, theme effects | Partial; deeper OOXML effect semantics deferred |
| Advanced Chart Families | Surface, treemap, sunburst, histogram, Pareto, box-and-whisker, waterfall, funnel, map, 3D | Deferred - recognized from XLSX where detected and blocked from broken authoring/rendering; mixed drawing-part retention for unsupported chart families remains partial until per-family data model and package writer support exist |

## Commands Parity Closeout Scope

The May 2026 closeout targets the remaining Partial rows where Freexcel already has the underlying model:
paste matrix completion, persistent Format Painter, alignment and shrink-to-fit style state,
AutoFit measurement, Format Cells dialog coverage, Flash Fill inference, and PDF/XPS export options.

Advanced chart families stay Deferred until each family has a data model and renderer. Freexcel detects common
unsupported chart package families and presents disabled or clearly-labeled commands rather than claiming authored
rendering support. Lossless mixed drawing-part retention remains a package-writer limitation for this closeout.
Ribbon overflow now keeps collapsed group menus closer to Excel by preserving cloned menu checked state,
input gesture text, and dynamic menu-open behavior instead of reducing collapsed groups to static labels.

---

## File / Backstage

> **Tab coverage: 8 Implemented + 4 Partial = 100% of 12 in-scope commands (3 Excluded)**

| Command | Status | Notes |
|---|---|---|
| New (Ctrl+N) | Implemented | |
| Open (Ctrl+O) | Implemented | |
| Save (Ctrl+S) | Implemented | Reuses current workbook path; Backstage caption exposes a visible access key |
| Save As | Implemented | Backstage caption exposes a visible access key |
| Print Preview | Implemented | Honors paper/orientation/margins/headers/print area |
| Export to PDF/XPS | Partial | Deterministic PDF export uses the existing print renderer and PDFsharp-WPF raster pages; active-sheet, selected-range, entire-visible-workbook, page-range, page-count validation, standard/minimum-size quality options, ignore-print-areas, extensionless `.pdf`/explicit `.xps` path normalization, access-keyed publish options, open-after-publish options, and PDF sheet-name bookmarks with page-range filtering are supported; requested PDF document properties embed workbook-name title plus Freexcel author/subject/keywords metadata; XPS export remains available with format-aware option summaries and writes the same modeled title/creator/subject/keywords subset into package core properties; selectable/vector PDF text, heading bookmark variants, and remaining full Excel PDF publish options remain partial |
| Close | Implemented | Backstage caption exposes a visible access key |
| Options | Partial | General, Formulas, View, and Save subsets including calculation/error-checking and formula bar preferences; sidebar categories, editable fields, option toggles, and OK/Cancel expose keyboard access keys |
| Recent Files | Implemented | |
| Info panel | Partial | Protection/accessibility summary, workbook statistics, accessibility and formula-error counts, and file properties |
| Share | Partial | Windows Share for saved local files; missing or unsaved local files route through Save As first; Microsoft 365 cloud links/coauthoring excluded |
| Check In/Out | Excluded | SharePoint workflow |
| Online Templates | Excluded | Microsoft online template discovery |
| Open XLSX unsupported-feature warnings | Implemented | Names VBA/Power Query/data model/etc. |
| Account | Partial | Explains no Microsoft account integration |

## Quick Access Toolbar

> **Tab coverage: 3 Implemented + 0 Partial = 100% of 3 in-scope commands (1 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Save | Implemented | |
| Undo | Implemented | |
| Redo | Implemented | |
| Customize QAT | Excluded | Low v1 value |

---

## Home Tab

> **Tab coverage: 40 Implemented + 16 Partial = 100% of 56 in-scope commands (1 Excluded)**

### Clipboard

| Command | Status | Notes |
|---|---|---|
| Cut (Ctrl+X) | Implemented | Defers source clearing until non-overlapping paste, keeps an internal cut clipboard, and shows cut marquee state while pending |
| Copy (Ctrl+C) | Implemented | Copy marquee state |
| Paste (Ctrl+V) | Implemented | Internal values/formulas/formats/all and external text paste covered; unsupported external rich formats are intentionally plain-text |
| Paste Special (values/formulas/formats/transpose/arithmetic/link/column-widths/picture) | Implemented | Supported modes are undoable; all dialog choices and OK/Cancel expose access keys; external OLE/rich-object paste excluded |
| Format Painter | Implemented | Copies source formatting, including style-only cells and multi-cell format patterns, to target cells with undo; supports single-click and persistent double-click painter modes |

### Font

| Command | Status | Notes |
|---|---|---|
| Font Family | Implemented | |
| Font Size | Implemented | Excel-range validated |
| Grow/Shrink Font | Implemented | |
| Bold (Ctrl+B) | Implemented | |
| Italic (Ctrl+I) | Implemented | |
| Underline (Ctrl+U) | Implemented | |
| Double Underline | Implemented | |
| Strikethrough (Ctrl+5) | Implemented | |
| Font Color | Implemented | Shared color picker exposes custom color and button access keys. |
| Fill/Highlight Color | Implemented | |
| Borders (presets) | Implemented | |
| Full Border Gallery | Partial | Expanded preset gallery with remembered line color/style; interactive draw/erase border tools deferred |
| Theme Colors | Partial | Preset color schemes plus Customize Colors entry point through an access-keyed theme dialog; deep effects deferred |

### Alignment

| Command | Status | Notes |
|---|---|---|
| Horizontal Alignment (Left/Center/Right) | Implemented | |
| Vertical Alignment (Top/Middle/Bottom) | Implemented | |
| Wrap Text | Implemented | |
| Merge & Center | Implemented | Undoable; F4 repeat |
| Indent (increase/decrease) | Implemented | |
| Text Rotation presets | Implemented | |
| Distributed/Justify alignment | Implemented | Supported in style model, dialog, renderer, and XLSX IO |
| Shrink to Fit | Implemented | Supported in style model, dialog, renderer, and XLSX IO |
| Format Cells Alignment dialog | Implemented | Covers supported alignment model |

### Number

| Command | Status | Notes |
|---|---|---|
| Number Format dropdown | Implemented | |
| General/Number/Currency/Accounting/Date/Time/Percentage/Fraction/Scientific/Text | Implemented | |
| Custom Number Format | Partial | Broader Format Cells catalog plus editable custom format codes; Format Cells sample previews resolve through the same `NumberFormatter` used by the grid; supports invariant conditional sections for numbers and date/time values, named colors, default indexed `Color1`-through-`Color56` prefixes for numeric/date/text sections, escaped literals including escaped layout directive characters, active percent scaling with token placement and quoted/escaped literal handling, date/time with long and compact AM/PM markers, contextual month/minute token handling across quoted literals, five-`m` month initials, rounded clock and elapsed fractional seconds, elapsed-time, and text-section spacing/fill directive cleanup, variable decimals, variable and fixed-denominator fractions, scientific notation, elapsed time, comma scaling, visible currency symbols from LCID tokens, deterministic decimal/group/date separators for selected modeled LCIDs including US, East Asian, European, Balkan/Baltic, Central Asia/Caucasus, Latin American Spanish variants, French Canada, Commonwealth English variants, African variants, South Africa, Southeast Asian variants, Hebrew/Thai, Arabic/Persian/Urdu variants, and Indian grouping for `en-IN` plus native Indian LCIDs; uncataloged LCID tokens fall back to .NET `CultureInfo` number/date separators while curated overrides remain authoritative; workbook palette/theme overrides and exact Excel accounting layout remain partial |
| Increase/Decrease Decimal | Implemented | |
| Comma Style | Implemented | |
| Currency Style | Implemented | |
| Percentage Style | Implemented | |
| Full Excel locale/accounting fidelity | Partial | Invariant custom/accounting subset implemented; LCID currency symbols plus modeled numeric/date separators for covered US, East Asian, European, Balkan/Baltic, Central Asia/Caucasus, Latin American Spanish variants, French Canada, Commonwealth English variants, African variants, South Africa, Southeast Asian variants, Hebrew/Thai, Arabic/Persian/Urdu variants, and Indian grouping for `en-IN` plus native Indian LCIDs are preserved, uncataloged LCID tokens use .NET `CultureInfo` fallback separators when available, and date/time/elapsed-time/text layout directives are cleaned; exact accounting layout widths, localized accounting names, workbook theme/palette color resolution, and Excel-specific deviations from platform globalization data remain partial |

### Styles

| Command | Status | Notes |
|---|---|---|
| Conditional Formatting | Partial | Most modeled rules; grid rendering covers cell value, formulas, above/below average, top/bottom, duplicate/unique, text, blank/nonblank, error/no-error, color scales, data bars, and visible 3/4/5-band icon sets with style-aware arrows, traffic lights, signs, symbols, flags, ratings, quarters, boxes, reverse/icons-only display, and authored percent/number thresholds; icon-set authoring/editing supports core OOXML styles with show/reverse options, rule dialogs expose access-keyed value/format fields, visual-rule threshold/color fields, option toggles, and OK/Cancel, the ribbon menu exposes grouped Directional/Shapes/Indicators/Ratings one-click presets plus More Rules, and the manager preserves advanced CF fields including Stop If True plus rules outside Current Selection; simplified rule manager remains partial |
| Format as Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, access-keyed range/header controls, one-step undo for table creation plus styling, and an Excel-scale Light/Medium/Dark gallery with swatch previews; command-level and XLSX-loaded table value filters hide non-matching data rows with multi-column AND, blank inclusion, and totals-row exclusion semantics; totals-row labels and common functions (`sum`, `average`, `count`, `countNums`, `min`, `max`) can be materialized with undo; formulas can evaluate and track dependencies for basic data-body column structured references such as `Sales[Amount]`, evaluate whole-table section selectors `#Headers`, `#Data`, `#All`, and `#Totals`, evaluate section-column intersections such as `Sales[[#Totals],[Amount]]`, evaluate scalar current-row references such as `[@Amount]` or `Sales[@Amount]` from table data-body formulas, evaluate qualified and unqualified `#This Row` references such as `Sales[[#This Row],[Amount]:[Tax]]` and `[[#This Row],[Amount]:[Tax]]`, and evaluate multi-column ranges such as `Sales[[Amount]:[Tax]]` and `Sales[[#Data],[Amount]:[Tax]]`; full table style theme semantics remain partial |
| Cell Styles | Partial | Expanded built-in preset gallery backed by reusable `StyleDiff` planners; Accent 20% presets resolve against the active workbook theme; full workbook named-style semantics remain deferred |

### Cells

| Command | Status | Notes |
|---|---|---|
| Insert Cells/Rows/Columns/Sheets | Implemented | |
| Delete Cells/Rows/Columns/Sheets | Implemented | |
| Row Height | Implemented | |
| Column Width | Implemented | |
| AutoFit Row/Column | Implemented | Measurement-based estimate over selected cells |
| Hide/Unhide Rows/Columns/Sheets | Implemented | |
| Format Cells dialog (Ctrl+1) | Implemented | Covers supported Number/Alignment/Font/Fill/Border/Protection model |

### Editing

| Command | Status | Notes |
|---|---|---|
| AutoSum (Alt+=) | Implemented | |
| Fill Down/Right/Up/Left (Ctrl+D/R) | Implemented | |
| Fill Series | Implemented | |
| Flash Fill | Partial | Expanded deterministic inference including common first-name/last-name contact patterns, dotted/underscored/hyphenated email display-name cleanup, shared-domain email generation with `.`, `_`, or `-` first/last, first-initial/last, and last/first-initial separators, and first/last-initial email aliases; Excel's full ML-like inference remains partial |
| Clear All/Formats/Contents/Comments/Hyperlinks | Implemented | |
| Sort | Implemented | |
| Filter | Implemented | |
| Find (Ctrl+F) | Implemented | Find field, options, Format, Find All, Find Next, and Close expose access keys |
| Replace (Ctrl+H) | Implemented | Find/Replace fields, options, Format, Replace All, and Close expose access keys |
| Go To (Ctrl+G / F5) | Implemented | |
| Go To Special | Implemented | Blanks/constants/formulas/comments/validation/visible |
| Select Objects | Excluded | Niche; drag handles deferred |

---

## Insert Tab

> **Tab coverage: 10 Implemented + 3 Partial = 100% of 13 in-scope commands (1 Deferred, 9 Excluded)**

| Command | Status | Notes |
|---|---|---|
| PivotTable | Partial | Creates from selected or cross-sheet source ranges on the current sheet or a new worksheet, refreshes existing PivotTables, supports command-level field layout/view/options/source changes including workbook-qualified source ranges, values-only and column-only layouts, nested row/column fields, Compact/Outline/Tabular report-layout state with Compact row-label rendering, top/bottom subtotals, calculated fields/items, date/number grouping, row/column label filters including comparison/between variants, row/column value filters with field targets including between/not-between and above/below-average variants, access-keyed create/source/placement choices, label/value filter dialog fields and OK/Cancel, value/label sorting including column label/value sorting, multi-select page/row/column checked-item filters with search/select-all/OK/Cancel access keys, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants with base field/item settings, common and statistical summary functions, built-in and custom workbook-catalog value-field number format IDs, broader built-in number-format preset catalog, editable custom value-field format codes on materialized value cells through an access-keyed tabbed Value Field Settings dialog, and PivotTable Options exposes undoable "For empty cells show" text for missing matrix intersections, separate row/column grand-total controls, repeated-label/blank-line layout options, cache "refresh on open" and "save source data" toggles, access-keyed PivotTable Options choices, built-in Light/Medium/Dark PivotStyle name gallery selection with current custom/authored style preservation, PivotTable style-name and style-option round-trip, GETPIVOTDATA lookups, Field List task pane with access-keyed action buttons, checkbox toggles, and drag/drop reordering, field context-menu sort/select-items/label-filter/value-filter/clear/value-settings entry points, checkbox item-filter dialog, label/value filter dialogs, tabbed Value Field Settings dialog, contextual PivotTable Analyze/Design tabs, ribbon/double-click Show Details drill-down for item/subtotal/grand-total/matrix/column-only data cells, Insert Slicer/Insert Timeline authoring, active slicer and timeline filtering commands and pane controls for connected worksheet-range PivotTables, authored slicer/timeline state round-trip including cross-sheet source data and cache relationships, rendered header/subtotal/grand-total/row-stripe/column-stripe styles for built-in PivotStyle presets including explicit `PivotStyleMedium2`, and model-first XLSX load/save including refresh flags and shared-item metadata; exact full-gallery PivotStyle theme semantics, native slicer/timeline floating drawing object fidelity, full Excel number-format picker/catalog UI, and external/OLAP/data-model pivot cache execution remain partial or excluded |
| PivotChart | Partial | Inserts a bound chart from an existing PivotTable, supports bound PivotChart type changes while preserving the PivotTable connection, native `pivotSource` read/write and refresh binding implemented; renders PivotChart field buttons with master and per-button report-filter/axis-field/value-field visibility; PivotChart Options exposes undoable master/report-filter/axis-field/value-field button toggles; Native JSON persists PivotChart binding/style/button option state plus modeled chart design metadata; field buttons open the same sort/filter/value-settings menu used by PivotTable fields; bound chart ranges stay synchronized after PivotTable layout/view changes; full PivotChart Tools layout/design editing remains partial |
| Recommended PivotTables | Excluded | AI/ML heuristics; proprietary |
| Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, access-keyed range/header controls, and one-step undo via the same path as Format as Table; the shared Format as Table gallery exposes Excel-scale Light/Medium/Dark style choices with swatch previews; table value filters execute for command and XLSX-loaded metadata; totals-row labels and common functions can be materialized with undo; formulas can evaluate and track dependencies for basic data-body column structured references such as `Sales[Amount]`, evaluate whole-table section selectors `#Headers`, `#Data`, `#All`, and `#Totals`, evaluate section-column intersections such as `Sales[[#Totals],[Amount]]`, evaluate scalar current-row references such as `[@Amount]` or `Sales[@Amount]` from table data-body formulas, evaluate qualified and unqualified `#This Row` references such as `Sales[[#This Row],[Amount]:[Tax]]` and `[[#This Row],[Amount]:[Tax]]`, and evaluate multi-column ranges such as `Sales[[Amount]:[Tax]]` and `Sales[[#Data],[Amount]:[Tax]]`; full table style theme semantics remain partial |
| Picture (from file) | Implemented | |
| Online Pictures | Excluded | |
| Shapes | Implemented | Rectangle/ellipse/line |
| Icons | Excluded | Requires proprietary Microsoft icon library |
| 3D Models | Excluded | |
| SmartArt | Excluded | Retained as package part; no authoring |
| Screenshot | Excluded | OS-level feature (Win+Shift+S) |
| Chart (column/bar/line/area/pie/doughnut/scatter/bubble) | Implemented | Select Data Source, Move Chart, Insert Chart, and chart format dialogs expose keyboard access keys for modeled fields and option controls |
| Chart (stock/radar) | Implemented | Model, ribbon insertion, renderer, and XLSX read/write paths implemented |
| Chart (surface/treemap/sunburst/histogram/Pareto/box-and-whisker/waterfall/funnel/map/3D) | Deferred | Recognized from XLSX where detected and blocked from broken authoring/rendering; lossless mixed drawing-part retention remains partial until per-family package writer support exists |
| Recommended Charts | Excluded | AI/ML heuristics; proprietary |
| Sparklines (line/column/win-loss) | Implemented | |
| Text Box | Implemented | |
| Header & Footer | Implemented | Presets, section fields, token buttons, options, and OK/Cancel expose access keys |
| WordArt | Excluded | |
| Symbols | Implemented | Picker Cancel action exposes a keyboard access key. |
| Hyperlink (Ctrl+K) | Implemented | |
| Comment/Note | Partial | Insert tab creates local threaded comments; Review tab also keeps simple note commands. Full threaded conversation/reply UI remains partial |
| Equation | Excluded | |

---

## Draw Tab

> **Tab coverage: 8 Implemented + 3 Partial = 100% of 11 in-scope commands (1 Deferred, 1 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Rectangle | Implemented | |
| Ellipse | Implemented | |
| Line | Implemented | |
| Freehand Ink | Excluded | |
| Bring Forward/Send Backward | Implemented | |
| Object Size/Rotation (command-based) | Implemented | |
| Fill Color | Implemented | Shared color picker exposes custom color and button access keys. |
| Outline Color | Implemented | |
| Alt Text | Implemented | |
| Interactive drag handles | Deferred | Needs a dedicated object-selection/adornment layer; command-based size/rotation is implemented |
| Crop | Partial | Image picture crop/reset is undoable, rendered, and persisted in native JSON and XLSX; interactive crop handles remain pending |
| Gradients/Effects | Partial | Authored drawing shapes support two-color gradient fills and a shadow effect with dedicated access-keyed start/end color pickers, undo, and native JSON/XLSX persistence; full Excel gradient gallery and additional effect types remain pending |
| Selection Pane | Partial | Lists sheet objects with per-item visibility checkboxes, search/filter controls, access-keyed Show All / Hide All bulk controls, Bring Forward / Send Backward reorder buttons, model-backed object renaming with undo plus Native JSON and XLSX `cNvPr` name persistence for supported drawing objects, and OK/Cancel; drag-reorder within the list remains pending |

---

## Page Layout Tab

> **Tab coverage: 16 Implemented + 1 Partial = 100% of 17 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Margins | Implemented | |
| Orientation | Implemented | |
| Paper Size | Implemented | |
| Print Area (set/clear) | Implemented | |
| Breaks (manual page breaks) | Implemented | |
| Background (display-only tiled image) | Implemented | |
| Print Titles | Implemented | |
| Scale to Fit | Implemented | |
| Print Gridlines | Implemented | |
| Print Headings | Implemented | |
| Sheet Options (gridlines/headings display) | Implemented | |
| Themes (preset + custom dialog) | Partial | Presets plus custom theme dialog reachable from Themes, Theme Colors, Theme Fonts, and Theme Effects; dialog preset buttons, metadata fields, color slots, and Save/Cancel expose keyboard access keys; deeper OOXML effects deferred |
| Colors/Fonts/Effects preset menus | Implemented | |
| Header/Footer editing | Implemented | First/odd/even variants, presets, section fields, token buttons, option toggles, and OK/Cancel expose access keys |
| Page Setup dialog | Implemented | Page, Margins, and Sheet tab labels plus footer actions expose access keys |
| Center on page | Implemented | |
| Page Order | Implemented | |

---

## Formulas Tab

> **Tab coverage: 16 Implemented + 1 Partial = 100% of 17 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Insert Function dialog | Implemented | Search, category, function list, Help, OK, and Cancel expose access keys |
| AutoSum variants | Implemented | |
| Category function menus (Logical/Text/Date/Lookup/Math) | Implemented | |
| Name Manager | Implemented | Dialog list, name/range fields, and Define/Delete/Close commands expose access keys |
| Define Name | Implemented | Name/range fields and command buttons expose access keys through the named-range manager |
| Use in Formula (named ranges) | Implemented | |
| Create from Selection | Implemented | Top/left/bottom/right label edges create sanitized, unique named ranges with undo; dialog choices and OK/Cancel expose access keys |
| Trace Precedents | Implemented | Multi-level arrows, offscreen markers |
| Trace Dependents | Implemented | |
| Remove Arrows | Implemented | |
| Show Formulas (Ctrl+`) | Implemented | |
| Error Checking | Partial | Issue list plus ribbon entry point to error-checking options, access-keyed issue actions, and supported checks including numbers stored as text, formulas referring to blank cells, two-digit-year text dates, formulas inconsistent with nearby formulas, SUM formulas omitting adjacent cells, and unlocked formula cells; partial rule taxonomy |
| Evaluate Formula (step-through) | Implemented | Help, Previous, Step Out, Evaluate, Step In, and Close actions expose access keys |
| Watch Window | Implemented | Dialog command buttons expose keyboard access keys. |
| R1C1 Reference Style | Implemented | |
| Calculation Options (manual/auto) | Implemented | |
| Calculate Now / Calculate Sheet | Implemented | |

---

## Data Tab

> **Tab coverage: 17 Implemented + 1 Partial = 100% of 18 in-scope commands (2 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Get Data (CSV) | Implemented | |
| Power Query/external connectors | Excluded | |
| Refresh All | Implemented | Recalc |
| Sort (single/multi-key) | Implemented | |
| Filter (auto-filter with conditions) | Implemented | |
| Advanced Filter | Implemented | Criteria range supports AND/OR rows, copy-to output, unique records, undo, and access-keyed action/options/reference controls |
| Text to Columns | Implemented | Wizard exposes access-keyed source mode, delimiter, qualifier, destination, reference picker, and OK/Cancel controls |
| Remove Duplicates | Implemented | |
| Data Validation | Implemented | |
| Consolidate | Implemented | Function, reference list, destination, label options, and Add/Delete/OK/Cancel expose access keys |
| What-If Analysis > Goal Seek | Implemented | Dialog input labels, status dialog buttons, and OK/Cancel expose access keys |
| What-If Analysis > Scenario Manager | Implemented | Dialog list, add/edit fields, action buttons, and Close expose access keys. |
| What-If Analysis > Data Table (1-var/2-var) | Implemented | Dialog exposes access-keyed table type and input-cell reference fields |
| Forecast Sheet | Implemented | Formula-based; no chart UI |
| Subtotal | Implemented | |
| Group/Outline | Implemented | |
| Ungroup | Implemented | |
| Show Detail / Hide Detail | Implemented | |
| Data Model / Power Pivot | Excluded | |
| Flash Fill (Data tab) | Partial | Expanded deterministic inference including common first-name/last-name contact patterns, dotted/underscored/hyphenated email display-name cleanup, shared-domain email generation with `.`, `_`, or `-` first/last, first-initial/last, and last/first-initial separators, and first/last-initial email aliases; Excel's full ML-like inference remains partial |

---

## Review Tab

> **Tab coverage: 8 Implemented + 2 Partial = 100% of 10 in-scope commands (6 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Spell Check | Partial | Broader known-corrections text-cell scan with casing-preserving replace, replace-all, ignore support, and internet/email/file-address span skipping; no full dictionary/proofing engine |
| Thesaurus | Excluded | Requires external dictionary service |
| Accessibility Checker | Partial | Merged cells, missing/generic alt text, untitled or generic-titled charts, non-descriptive hyperlink text, default worksheet tab names, and hidden sheets/rows/columns with content; full Excel rule taxonomy remains partial |
| Smart Lookup / Researcher | Excluded | |
| Translate | Excluded | |
| New Comment | Partial | Threaded comment text can be added/edited/deleted locally through the Review ribbon and Ctrl+Shift+F2; full threaded conversation/reply UI remains partial |
| New Note | Implemented | Simple cell notes |
| Edit Note | Implemented | Reuses the note editor with existing note text preloaded |
| Delete Note | Implemented | |
| Previous/Next Note | Implemented | Navigates simple cell notes on the active sheet |
| Show Notes | Implemented | Opens a list of simple cell notes |
| Protect Sheet | Implemented | Password dialog OK/Cancel expose access keys |
| Allow Edit Ranges | Implemented | Add, remove, and clear allowed ranges with undo support; range field and OK/Cancel expose access keys; partial permissions manager |
| Protect Workbook | Implemented | Password dialog OK/Cancel expose access keys |
| Share | Implemented | Windows Share for saved local files; missing current paths route through Save As |
| Share Workbook (legacy) | Excluded | |
| Track Changes | Excluded | |
| Threaded Comments | Partial | Local single-message threaded comment model, shortcut, navigation, delete command, and list display are supported; full Excel conversation/reply UI and cloud identity semantics remain partial |
| Statistics | Implemented | |

---

## View Tab

> **Tab coverage: 12 Implemented + 1 Partial = 100% of 13 in-scope commands (4 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Normal View | Implemented | |
| Page Break Preview | Implemented | |
| Page Layout View | Implemented | |
| Custom Views | Implemented | Dialog list, actions, Add View name field, and OK/Cancel expose access keys |
| Show Gridlines | Implemented | |
| Show Headings | Implemented | |
| Show Ruler | Implemented | |
| Show Formula Bar | Implemented | |
| Freeze Panes | Implemented | |
| Split Panes | Implemented | Toggle clears frozen panes and supports independent split quadrants, draggable dividers, pane-specific scrollbars, wheel targeting, clipping, and active-state ribbon feedback |
| Zoom | Implemented | 10-400% range |
| Zoom to Selection | Implemented | |
| New Window | Excluded | Insignificant / complex multi-window hosting |
| Arrange All | Partial | Stores choice; no live multi-window |
| View Side by Side | Excluded | Insignificant / complex multi-window hosting |
| Synchronous Scrolling | Excluded | Insignificant / complex multi-window hosting |
| Switch Windows | Excluded | Insignificant / complex multi-window hosting |

---

## Sheet Tab Context Menu

> **Tab coverage: 9 Implemented + 0 Partial = 100% of 9 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Add Sheet | Implemented | |
| Rename Sheet | Implemented | |
| Delete Sheet | Implemented | |
| Duplicate Sheet | Implemented | |
| Move Sheet Left/Right | Implemented | |
| Tab Color | Implemented | |
| Hide/Unhide Sheet | Implemented | |
| Select All Sheets (Group) | Implemented | |
| Ungroup Sheets | Implemented | |

---

## Help Tab

> **Tab coverage: 3 Implemented + 0 Partial = 100% of 3 in-scope commands (3 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Help (opens project repo) | Implemented | |
| Send Feedback (opens issue form) | Implemented | |
| About | Implemented | |
| Microsoft training | Excluded | |
| Microsoft templates | Excluded | |
| Microsoft accounts | Excluded | |

---

## Intentionally Not Blind-Repeatable

These visible workflows are command-based and undoable where applicable, but F4 repeat should not replay them without reopening their workflow UI because Excel's behavior depends on confirmation, external state, or a selected object/window context.

| Area | Command | Reason |
|---|---|---|
| File/Data | Get Data/import | Re-importing stale external content can overwrite a new destination. |
| Data / What-If | Goal Seek, Scenario Manager, Forecast Sheet | Depend on dialog choices and solver state. |
| Review | Protect Workbook, Allow Edit Ranges | Password/protection decisions should be explicit. |
| Formulas | Error Checking options, Ignore Error | Command target is dialog issue/global option, not selection. |
| View / Window | Arrange Windows and deferred multi-window commands | Live multi-window routing is deferred. |
| Sheet Tabs | Delete, move, hide/unhide, duplicate, tab color | Targets a specific sheet tab; can become destructive after first run. |

## Acceptance Rule

Every visible command should be in one of these states:

- **Implemented:** behaves like Excel for the supported model.
- **Partial:** documented with exact missing behavior and tests for what is supported.
- **Not Implemented:** absent; should be eliminated or moved to a documented Deferred/Excluded state.
- **Deferred:** postponed because it needs a larger subsystem or interaction architecture.
- **Excluded:** hidden, disabled, or labeled as unsupported, with the reason listed.

No visible command should silently pretend to support a cloud, proprietary, or complex feature that Freexcel does not actually implement.
