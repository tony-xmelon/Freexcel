# Freexcel Command Surface Parity

**Status:** working audit  
**Last updated:** 2026-05-18

This document tracks Freexcel's visible command surface against Excel for Windows. The goal is Excel parity for commands we choose to support, and an explicit exclusion list for commands that depend on Microsoft cloud services, proprietary runtimes, or very large subsystems.

## Status Legend

| Status | Meaning |
|---|---|
| Implemented | Works like Excel for the supported model |
| Partial | Works but missing something; see Notes |
| Not Implemented | Absent; not yet built |
| Excluded | Out of scope (cloud / proprietary / large subsystem) |

Coverage is computed as **(Implemented + Partial) / (Implemented + Partial + Not Implemented) x 100**. Excluded commands are reported separately.

---

## Coverage Summary

| Tab | Implemented | Partial | Not Implemented | Excluded | **Coverage** |
|---|---:|---:|---:|---:|---:|
| File/Backstage | 7 | 3 | 0 | 3 | **100%** |
| QAT | 3 | 0 | 1 | 0 | **75%** |
| Home | 36 | 7 | 1 | 0 | **98%** |
| Insert | 14 | 5 | 9 | 5 | **68%** |
| Draw | 7 | 0 | 3 | 1 | **70%** |
| Page Layout | 17 | 1 | 0 | 0 | **100%** |
| Formulas | 15 | 1 | 1 | 0 | **94%** |
| Data | 15 | 1 | 1 | 2 | **94%** |
| Review | 10 | 2 | 2 | 4 | **86%** |
| View | 13 | 1 | 4 | 0 | **78%** |
| Sheet Tabs | 9 | 0 | 0 | 0 | **100%** |
| Help | 3 | 0 | 0 | 3 | **100%** |
| **TOTAL** | **149** | **21** | **22** | **18** | **89%** |

---

## Explicitly Excluded

These features are out of scope and should not be treated as bugs when absent.

| Area | Excel Feature | Freexcel Decision | Reason |
|---|---|---|---|
| Collaboration | Share, cloud links, Microsoft 365 co-authoring, presence, permissions | Excluded | Requires identity, OneDrive/SharePoint/cloud sync, remote conflict resolution. |
| Automation | VBA projects, macro execution, COM add-ins, Office Scripts | Excluded for v1 | Proprietary/runtime security surface. |
| BI/Data Model | Power Pivot, Power Query/M, data model relationships, OLAP cubes | Excluded for v1 | Large external query/runtime subsystem. |
| External Services | Stock/geography linked data types, live web queries, Teams comments, online version history, online template discovery | Excluded | Depends on Microsoft services or authenticated cloud APIs. |
| Enterprise Controls | IRM, sensitivity labels, encrypted collaboration policies | Excluded | Depends on Microsoft 365 tenant infrastructure. |

## Deferred Architectural Features

Not cloud/proprietary exclusions, but require larger architecture before adding UI.

| Area | Excel Feature | Freexcel Decision |
|---|---|---|
| Window Management | New Window, View Side by Side, Synchronous Scrolling, Reset Window Position, Switch Windows | Deferred until multi-window workbook hosting exists |
| Split Panes | Full Excel split-pane scrollbar interaction polish | Partial after split pane scroll model |
| Theme System | Themes, theme colors, theme fonts, theme effects | Partial; deeper OOXML effect semantics deferred |
| Advanced Chart Families | Stock, surface, radar, treemap, sunburst, histogram, Pareto, box-and-whisker, waterfall, funnel, map, 3D | Deferred until per-family data model and renderer exist |

---

## File / Backstage

> **Tab coverage: 7 Implemented + 3 Partial = 100% of 10 in-scope commands (3 Excluded)**

| Command | Status | Notes |
|---|---|---|
| New (Ctrl+N) | Implemented | |
| Open (Ctrl+O) | Implemented | |
| Save (Ctrl+S) | Implemented | Reuses current workbook path |
| Save As | Implemented | |
| Print Preview | Implemented | Honors paper/orientation/margins/headers/print area |
| Export to PDF/XPS | Partial | XPS-backed; full Excel PDF options partial |
| Close | Implemented | |
| Options | Partial | Subset of Excel options |
| Recent Files | Implemented | |
| Info panel | Partial | Protection/accessibility info only |
| Share | Excluded | Requires Microsoft 365 cloud |
| Check In/Out | Excluded | SharePoint workflow |
| Online Templates | Excluded | Microsoft online template discovery |
| Open XLSX unsupported-feature warnings | Implemented | Names VBA/Power Query/data model/etc. |
| Account | Partial | Explains no Microsoft account integration |

## Quick Access Toolbar

> **Tab coverage: 3 Implemented + 0 Partial = 75% of 4 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Save | Implemented | |
| Undo | Implemented | |
| Redo | Implemented | |
| Customize QAT | Excluded | Low v1 value |

---

## Home Tab

> **Tab coverage: 36 Implemented + 7 Partial = 98% of 44 in-scope commands**

### Clipboard

| Command | Status | Notes |
|---|---|---|
| Cut (Ctrl+X) | Partial | Copy + clear; no marching-ants state |
| Copy (Ctrl+C) | Implemented | |
| Paste (Ctrl+V) | Partial | Basic + paste-special; full matrix partial |
| Paste Special (values/formulas/formats/transpose/arithmetic/link/column-widths/picture) | Partial | Most modes implemented |
| Format Painter | Not Implemented | |

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
| Font Color | Implemented | |
| Fill/Highlight Color | Implemented | |
| Borders (presets) | Implemented | |
| Full Border Gallery | Partial | Preset subset only |
| Theme Colors | Partial | Baseline; deep effects deferred |

### Alignment

| Command | Status | Notes |
|---|---|---|
| Horizontal Alignment (Left/Center/Right) | Implemented | |
| Vertical Alignment (Top/Middle/Bottom) | Implemented | |
| Wrap Text | Implemented | |
| Merge & Center | Implemented | Undoable; F4 repeat |
| Indent (increase/decrease) | Implemented | |
| Text Rotation presets | Implemented | |
| Distributed/Justify alignment | Partial | |
| Shrink to Fit | Partial | |
| Format Cells Alignment dialog | Partial | |

### Number

| Command | Status | Notes |
|---|---|---|
| Number Format dropdown | Implemented | |
| General/Number/Currency/Accounting/Date/Time/Percentage/Fraction/Scientific/Text | Implemented | |
| Custom Number Format | Partial | Subset of Excel format codes |
| Increase/Decrease Decimal | Implemented | |
| Comma Style | Implemented | |
| Currency Style | Implemented | |
| Percentage Style | Implemented | |
| Full Excel locale/accounting fidelity | Partial | |

### Styles

| Command | Status | Notes |
|---|---|---|
| Conditional Formatting | Partial | Most rules; icon sets partial; rule manager simplified |
| Format as Table | Partial | Formatting only; no full table semantics |
| Cell Styles | Partial | Limited preset styles |

### Cells

| Command | Status | Notes |
|---|---|---|
| Insert Cells/Rows/Columns/Sheets | Implemented | |
| Delete Cells/Rows/Columns/Sheets | Implemented | |
| Row Height | Implemented | |
| Column Width | Implemented | |
| AutoFit Row/Column | Partial | |
| Hide/Unhide Rows/Columns/Sheets | Implemented | |
| Format Cells dialog (Ctrl+1) | Partial | Narrower than Excel |

### Editing

| Command | Status | Notes |
|---|---|---|
| AutoSum (Alt+=) | Implemented | |
| Fill Down/Right/Up/Left (Ctrl+D/R) | Implemented | |
| Fill Series | Implemented | |
| Flash Fill | Partial | Baseline pattern; not full Excel inference |
| Clear All/Formats/Contents/Comments/Hyperlinks | Implemented | |
| Sort | Implemented | |
| Filter | Implemented | |
| Find (Ctrl+F) | Implemented | |
| Replace (Ctrl+H) | Implemented | |
| Go To (Ctrl+G / F5) | Implemented | |
| Go To Special | Implemented | Blanks/constants/formulas/comments/validation/visible |
| Select Objects | Excluded | Niche; drag handles deferred |

---

## Insert Tab

> **Tab coverage: 14 Implemented + 5 Partial = 68% of 28 in-scope commands (5 Excluded)**

| Command | Status | Notes |
|---|---|---|
| PivotTable | Partial | Creates from selected or cross-sheet source ranges, refreshes existing PivotTables, supports command-level field layout/view/options/source changes including workbook-qualified source ranges, values-only and column-only layouts, nested row/column fields, Compact/Outline/Tabular report-layout state with Compact row-label rendering, top/bottom subtotals, calculated fields/items, date/number grouping, row/column label filters including comparison/between variants, row/column value filters with field targets including between/not-between and above/below-average variants, value/label sorting including column label/value sorting, multi-select page/row/column checked-item filters, Excel-style Show Values As modes including percent totals, running total, difference/% difference, rank, index, and parent-total variants with base field/item settings, common and statistical summary functions, separate row/column grand-total controls, repeated-label/blank-line layout options, PivotTable style-name and style-option round-trip, GETPIVOTDATA lookups, Field List task pane with checkbox toggles and drag/drop reordering, field context-menu sort/select-items/label-filter/value-filter/clear/value-settings entry points, checkbox item-filter dialog, label/value filter dialogs, tabbed Value Field Settings dialog, contextual PivotTable Analyze/Design tabs, ribbon/double-click Show Details drill-down for item/subtotal/grand-total/matrix/column-only data cells, Insert Slicer/Insert Timeline authoring, active slicer and timeline filtering commands and pane controls for connected worksheet-range PivotTables, authored slicer/timeline state round-trip including cross-sheet source data and cache relationships, rendered header/subtotal/grand-total/row-stripe/column-stripe styles for built-in PivotStyle presets, and model-first XLSX load/save including refresh flags and shared-item metadata; exact full-gallery PivotStyle theme semantics, native slicer/timeline floating drawing object fidelity, and external/OLAP/data-model pivot cache behavior remain partial or excluded |
| PivotChart | Partial | Inserts a bound chart from an existing PivotTable, supports bound PivotChart type changes while preserving the PivotTable connection, native `pivotSource` read/write and refresh binding implemented; renders PivotChart field buttons; field buttons open the same sort/filter/value-settings menu used by PivotTable fields; bound chart ranges stay synchronized after PivotTable layout/view changes; full PivotChart Tools layout/design editing remains partial |
| Recommended PivotTables | Excluded | AI/ML heuristics; proprietary |
| Table | Partial | Formatting; not full structured table semantics |
| Picture (from file) | Implemented | |
| Online Pictures | Excluded | |
| Shapes | Implemented | Rectangle/ellipse/line |
| Icons | Excluded | Requires proprietary Microsoft icon library |
| 3D Models | Excluded | |
| SmartArt | Excluded | Retained as package part; no authoring |
| Screenshot | Excluded | OS-level feature (Win+Shift+S) |
| Chart (column/bar/line/area/pie/doughnut/scatter/bubble) | Implemented | |
| Chart (stock/radar/surface/treemap/sunburst/histogram/waterfall/funnel/map) | Not Implemented | Retained as package part |
| Recommended Charts | Excluded | AI/ML heuristics; proprietary |
| Sparklines (line/column/win-loss) | Implemented | |
| Text Box | Implemented | |
| Header & Footer | Implemented | |
| WordArt | Excluded | |
| Symbols | Implemented | |
| Hyperlink (Ctrl+K) | Implemented | |
| Comment/Note | Implemented | |
| Equation | Excluded | |

---

## Draw Tab

> **Tab coverage: 7 Implemented + 0 Partial = 70% of 10 in-scope commands (1 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Rectangle | Implemented | |
| Ellipse | Implemented | |
| Line | Implemented | |
| Freehand Ink | Excluded | |
| Bring Forward/Send Backward | Implemented | |
| Object Size/Rotation (command-based) | Implemented | |
| Fill Color | Implemented | |
| Outline Color | Implemented | |
| Alt Text | Implemented | |
| Interactive drag handles | Not Implemented | |
| Crop | Not Implemented | |
| Gradients/Effects | Not Implemented | |

---

## Page Layout Tab

> **Tab coverage: 17 Implemented + 1 Partial = 100% of 18 in-scope commands**

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
| Themes (preset + custom dialog) | Partial | Baseline; deeper OOXML effects deferred |
| Colors/Fonts/Effects preset menus | Implemented | |
| Header/Footer editing | Implemented | First/odd/even variants |
| Page Setup dialog | Implemented | |
| Center on page | Implemented | |
| Page Order | Implemented | |

---

## Formulas Tab

> **Tab coverage: 15 Implemented + 1 Partial = 94% of 17 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Insert Function dialog | Implemented | |
| AutoSum variants | Implemented | |
| Category function menus (Logical/Text/Date/Lookup/Math) | Implemented | |
| Name Manager | Implemented | |
| Define Name | Implemented | |
| Use in Formula (named ranges) | Implemented | |
| Create from Selection | Not Implemented | |
| Trace Precedents | Implemented | Multi-level arrows, offscreen markers |
| Trace Dependents | Implemented | |
| Remove Arrows | Implemented | |
| Show Formulas (Ctrl+`) | Implemented | |
| Error Checking | Partial | Issue list; partial rule taxonomy |
| Evaluate Formula (step-through) | Implemented | |
| Watch Window | Implemented | |
| R1C1 Reference Style | Implemented | |
| Calculation Options (manual/auto) | Implemented | |
| Calculate Now / Calculate Sheet | Implemented | |

---

## Data Tab

> **Tab coverage: 15 Implemented + 1 Partial = 94% of 17 in-scope commands (2 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Get Data (CSV) | Implemented | |
| Power Query/external connectors | Excluded | |
| Refresh All | Implemented | Recalc |
| Sort (single/multi-key) | Implemented | |
| Filter (auto-filter with conditions) | Implemented | |
| Advanced Filter | Not Implemented | |
| Text to Columns | Implemented | |
| Remove Duplicates | Implemented | |
| Data Validation | Implemented | |
| Consolidate | Implemented | |
| What-If Analysis > Goal Seek | Implemented | |
| What-If Analysis > Scenario Manager | Implemented | |
| What-If Analysis > Data Table (1-var/2-var) | Implemented | |
| Forecast Sheet | Implemented | Formula-based; no chart UI |
| Subtotal | Implemented | |
| Group/Outline | Implemented | |
| Ungroup | Implemented | |
| Show Detail / Hide Detail | Implemented | |
| Data Model / Power Pivot | Excluded | |
| Flash Fill (Data tab) | Partial | |

---

## Review Tab

> **Tab coverage: 10 Implemented + 2 Partial = 86% of 14 in-scope commands (4 Excluded)**

| Command | Status | Notes |
|---|---|---|
| Spell Check | Partial | Known corrections only; no full dictionary |
| Thesaurus | Excluded | Requires external dictionary service |
| Accessibility Checker | Partial | Merged cells + missing alt text |
| Smart Lookup / Researcher | Excluded | |
| Translate | Excluded | |
| New Comment (note) | Implemented | |
| Delete Comment | Implemented | |
| Edit Comment | Implemented | |
| Show All Comments | Implemented | |
| Protect Sheet | Implemented | |
| Allow Edit Ranges | Implemented | Partial permissions manager |
| Protect Workbook | Implemented | |
| Share Workbook (legacy) | Excluded | |
| Track Changes | Excluded | |
| Threaded Comments | Excluded | |
| Statistics | Implemented | |

---

## View Tab

> **Tab coverage: 13 Implemented + 1 Partial = 78% of 18 in-scope commands**

| Command | Status | Notes |
|---|---|---|
| Normal View | Implemented | |
| Page Break Preview | Implemented | |
| Page Layout View | Implemented | |
| Custom Views | Implemented | |
| Show Gridlines | Implemented | |
| Show Headings | Implemented | |
| Show Ruler | Implemented | |
| Show Formula Bar | Implemented | |
| Freeze Panes | Implemented | |
| Split Panes | Partial | Partial fine-scroll parity |
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
- **Not Implemented:** absent; planned for a future phase.
- **Excluded:** hidden, disabled, or labeled as unsupported, with the reason listed.

No visible command should silently pretend to support a cloud, proprietary, or complex feature that Freexcel does not actually implement.
