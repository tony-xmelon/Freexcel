# Freexcel Menu and Toolbar Parity

**Last updated:** 2026-05-19
**Purpose:** Tracks individual ribbon button and menu-item fidelity against Excel for Windows.

## Coverage Summary

<!-- command-inventory:coverage-summary:start -->
| Tab | Implemented | Partial | Not Implemented | Deferred | Excluded | Coverage |
|---|---:|---:|---:|---:|---:|---:|
| File/Backstage | 8 | 4 | 0 | 0 | 3 | **100%** |
| QAT | 3 | 0 | 0 | 0 | 1 | **100%** |
| Home | 48 | 8 | 0 | 0 | 1 | **100%** |
| Insert | 10 | 3 | 0 | 1 | 9 | **100%** |
| Draw | 8 | 2 | 0 | 1 | 1 | **100%** |
| Page Layout | 16 | 1 | 0 | 0 | 0 | **100%** |
| Formulas | 16 | 1 | 0 | 0 | 0 | **100%** |
| Data | 17 | 1 | 0 | 0 | 2 | **100%** |
| Review | 8 | 2 | 0 | 0 | 6 | **100%** |
| View | 12 | 1 | 0 | 0 | 4 | **100%** |
| Sheet Tabs | 9 | 0 | 0 | 0 | 0 | **100%** |
| Help | 3 | 0 | 0 | 0 | 3 | **100%** |
| **TOTAL** | **158** | **23** | **0** | **2** | **30** | **100%** |
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
| Save | Implemented | Ctrl+S |
| Save As | Implemented | |
| Print Preview | Implemented | |
| Export to PDF/XPS | Partial | Deterministic PDF export uses the print renderer and PDFsharp-WPF raster pages; active-sheet, selected-range, and entire-visible-workbook scopes plus open-after-publish are supported; XPS export remains available with the same option summary; full Excel PDF publish options remain partial |
| Close | Implemented | |
| Options | Partial | General, Formulas, View, and Save subsets including calculation/error-checking and formula bar preferences |
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
| Paste Special | Implemented | Supported modes are undoable; external rich-object paste excluded |
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
| Font Color | Implemented | |
| Fill Color | Implemented | |
| Borders (presets) | Implemented | |
| Full Border Gallery | Partial | Expanded preset gallery with remembered line color/style; interactive draw/erase border tools deferred |
| Theme Colors | Partial | Preset color schemes plus Customize Colors entry point through the theme dialog |

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
| Custom Number Format | Partial | Broader Format Cells catalog plus editable custom format codes; supports invariant conditional sections, color prefixes, escaped literals, variable decimals, fractions, scientific notation, elapsed time, and comma scaling; locale/LCID details partial |
| Increase/Decrease Decimal | Implemented | |
| Comma Style | Implemented | |
| Currency Style | Implemented | |
| Percentage Style | Implemented | |
| Full locale/accounting fidelity | Partial | Invariant/accounting subset; full Excel/OS locale fidelity partial |

### Styles

| Item | Status | Notes |
|---|---|---|
| Conditional Formatting | Partial | Authoring/editing available for modeled rules; grid rendering covers cell value, formulas, above/below average, top/bottom, duplicate/unique, text, blank/nonblank, error/no-error, color scales, and data bars; full Excel icon rendering taxonomy and simplified manager remain partial |
| Format as Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, and one-step undo for table creation plus styling; command-level and XLSX-loaded table value filters hide non-matching data rows with multi-column AND, blank inclusion, and totals-row exclusion semantics; structured-reference formulas, totals-row calculations, and full table style galleries remain partial |
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
| Flash Fill | Partial | Expanded deterministic inference including common first-name/last-name contact patterns; full Excel inference partial |
| Clear All | Implemented | |
| Clear Formats/Contents/Comments/Hyperlinks | Implemented | |
| Sort | Implemented | |
| Filter | Implemented | |
| Find | Implemented | Ctrl+F |
| Replace | Implemented | Ctrl+H |
| Go To | Implemented | Ctrl+G/F5 |
| Go To Special | Implemented | |
| Select Objects | Excluded | Object drag handles deferred |

---

## Insert Tab

| Item | Status | Notes |
|---|---|---|
| PivotTable | Partial | Creates worksheet-range PivotTables on the current sheet or a new worksheet; model-first load/save |
| Recommended PivotTables | Excluded | Proprietary heuristics |
| Table | Partial | Creates structured table metadata with generated headers, AutoFilter flag, style name, visible banding, and one-step undo via the same path as Format as Table; table value filters execute for command and XLSX-loaded metadata; structured-reference formulas, totals-row calculations, and full table style galleries remain partial |
| Picture (from file) | Implemented | |
| Online Pictures | Excluded | |
| Shapes | Implemented | Rect/ellipse/line |
| Icons | Excluded | Proprietary Microsoft icon library |
| 3D Models | Excluded | |
| SmartArt | Excluded | Retained part |
| Screenshot | Excluded | OS-level feature |
| Chart - column/bar/line/area | Implemented | |
| Chart - pie/doughnut/scatter/bubble | Implemented | |
| Chart - stock/radar | Implemented | |
| Chart - surface/treemap/sunburst/histogram | Deferred | Recognized from XLSX where detected; authoring/rendering and lossless package writing need per-family model/renderer |
| Chart - waterfall/funnel/map/3D | Deferred | Recognized from XLSX where detected; authoring/rendering and lossless package writing need per-family model/renderer |
| Recommended Charts | Excluded | Proprietary heuristics |
| Sparklines (line/column/win-loss) | Implemented | |
| Text Box | Implemented | |
| Header & Footer | Implemented | |
| WordArt | Excluded | |
| Symbols | Implemented | |
| Hyperlink | Implemented | Ctrl+K |
| Comment/Note | Implemented | |
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
| Fill Color | Implemented | |
| Outline Color | Implemented | |
| Alt Text | Implemented | |
| Interactive drag handles | Deferred | Needs object-selection/adornment layer |
| Crop | Partial | Image crop/reset commands render and persist to native JSON/XLSX; interactive handles pending |
| Gradients/Effects | Partial | Shape gradient fill and shadow effect with native JSON/XLSX persistence; full Excel effect gallery pending |

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
| Themes | Partial | Presets plus custom theme dialog reachable from Themes, Theme Colors, Theme Fonts, and Theme Effects; deep OOXML effects deferred |
| Colors preset menu | Implemented | |
| Fonts preset menu | Implemented | |
| Effects preset menu | Implemented | |
| Header/Footer editing | Implemented | |
| Page Setup dialog | Implemented | |
| Center on page | Implemented | |
| Page Order | Implemented | |

---

## Formulas Tab

| Item | Status | Notes |
|---|---|---|
| Insert Function | Implemented | |
| AutoSum variants | Implemented | |
| Logical menu | Implemented | |
| Text menu | Implemented | |
| Date & Time menu | Implemented | |
| Lookup & Reference menu | Implemented | |
| Math & Trig menu | Implemented | |
| Name Manager | Implemented | |
| Define Name | Implemented | |
| Use in Formula | Implemented | |
| Create from Selection | Implemented | |
| Trace Precedents | Implemented | |
| Trace Dependents | Implemented | |
| Remove Arrows | Implemented | |
| Show Formulas | Implemented | Ctrl+` |
| Error Checking | Partial | Issue list plus ribbon entry point to error-checking options, including numbers stored as text, formulas referring to blank cells, and two-digit-year text dates; partial rule taxonomy |
| Evaluate Formula | Implemented | |
| Watch Window | Implemented | |
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
| Advanced Filter | Implemented | |
| Text to Columns | Implemented | |
| Remove Duplicates | Implemented | |
| Data Validation | Implemented | |
| Consolidate | Implemented | |
| Goal Seek | Implemented | |
| Scenario Manager | Implemented | |
| Data Table | Implemented | 1-var/2-var |
| Forecast Sheet | Implemented | No chart UI |
| Subtotal | Implemented | |
| Group/Outline | Implemented | |
| Ungroup | Implemented | |
| Show/Hide Detail | Implemented | |
| Data Model / Power Pivot | Excluded | |
| Flash Fill | Partial | Expanded deterministic inference including common first-name/last-name contact patterns; full Excel inference partial |

---

## Review Tab

| Item | Status | Notes |
|---|---|---|
| Spell Check | Partial | Broader known-corrections text-cell scan with casing-preserving replace, replace-all, and ignore support; no full dictionary/proofing engine |
| Thesaurus | Excluded | Requires external dictionary service |
| Accessibility Checker | Partial | Merged cells, missing/generic alt text, untitled charts, non-descriptive hyperlink text, and default worksheet tab names; full Excel rule taxonomy remains partial |
| Smart Lookup | Excluded | |
| Translate | Excluded | |
| New Note | Implemented | Simple cell notes; threaded comments excluded |
| Edit Note | Implemented | Reuses the note editor with existing note text preloaded |
| Delete Note | Implemented | |
| Previous/Next Note | Implemented | Navigates simple cell notes on the active sheet |
| Show Notes | Implemented | Opens a list of simple cell notes |
| Protect Sheet | Implemented | |
| Allow Edit Ranges | Implemented | |
| Protect Workbook | Implemented | |
| Share | Implemented | Windows Share for saved local files; missing current paths route through Save As |
| Share Workbook (legacy) | Excluded | |
| Track Changes | Excluded | |
| Threaded Comments | Excluded | |
| Statistics | Implemented | |

---

## View Tab

| Item | Status | Notes |
|---|---|---|
| Normal | Implemented | |
| Page Break Preview | Implemented | |
| Page Layout | Implemented | |
| Custom Views | Implemented | |
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
