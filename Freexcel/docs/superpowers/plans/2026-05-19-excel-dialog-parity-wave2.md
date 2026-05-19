# Excel Dialog Parity Wave 2 Plan

## Status

Wave 1 replaces prompt-driven workbook operations with local modal dialogs for formatting, navigation, sorting/filtering, data tools, scenarios, protection, and validation range selection.

Wave 2 first pass is implemented for local chart, PivotTable/PivotChart, object/picture, Page Setup, and Name Manager entry points. The remaining Wave 2 items are the deeper Excel panes and galleries that need richer workbook models, renderer support, or larger UI surfaces.

## Implemented First Pass

- Insert Chart / Recommended Charts picker.
- PivotChart Change Type dialog.
- PivotTable creation dialog with source, destination, and field-list options.
- PivotTable Change Data Source dialog.
- Insert Slicer and Insert Timeline dialogs.
- Hyperlink dialog.
- Picture/object size, rotation, crop, shape gradient, alt text, comment, and text box entry dialogs.
- Page Setup reuse for custom margins, scaling, and print titles.
- Name Manager reuse for Define Name.

## Dialog Surfaces

1. Chart creation and editing
   - [Done first pass] Insert Chart / Recommended Charts picker.
   - [Done first pass] Change Chart Type and Move Chart result dialogs.
   - [Done first pass] Select Data Source result dialog.
   - [Remaining] Wire non-Pivot Change Chart Type / Move Chart / Select Data Source once chart edit commands exist.
   - [Remaining] Format Chart Area, Axis, Data Series, Data Labels, Trendline, Error Bars, and Legend panes.

2. PivotTable and PivotChart workflows
   - [Done first pass] Create PivotTable dialog with source/range and destination picker.
   - [Existing/partial] PivotTable Fields pane with layout zones and field settings dialogs.
   - [Done first pass] Pivot filters and slicer/timeline insert dialogs.
   - [Remaining] PivotTable Fields search, deferred updates, group/ungroup, calculated field/item dialogs.

3. Object and drawing formatting
   - [Done first pass] Format Shape / Picture dialog entry points for size, rotation, crop, gradient, colors, alt text, and text options.
   - [Remaining] Selection Pane and object visibility/order controls.
   - [Done first pass] Hyperlink and comment/note dialogs where workbook objects need non-cell editing surfaces.

4. Richer galleries and pickers
   - [Existing/partial] Theme colors, standard colors, and custom RGB picker parity across common color entry points.
   - [Existing/partial] Border gallery presets, line styles, diagonal borders, and live preview integration.
   - Cell Styles, Table Styles, chart styles, and conditional formatting rule galleries.

5. Print/page and workbook environment dialogs
   - [Done first pass] Full Page Setup dialog tabs, print titles, margins, header/footer, and sheet options.
   - [Done first pass] Name Manager / Define Name dialog reuse with reference picker text.
   - Options-adjacent workbook settings that affect calculation, proofing, display, and compatibility.

## Verification Expectations

- Each dialog surface gets planner or model tests before wiring to `MainWindow`.
- UI-only XAML coverage should verify required tabs, controls, and command routing.
- Any dialog that edits workbook state must have at least one command-level test proving the selected options are honored.
- WPF tests should be run with stale `Freexcel.App.Host` processes cleared first to avoid locked build outputs.
