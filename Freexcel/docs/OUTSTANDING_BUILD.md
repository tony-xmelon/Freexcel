# Freexcel Outstanding Build List

**Last updated:** 2026-05-18  
**Basis:** reviewed the repository Markdown files and cross-checked the active codebase under `src/` and `tests/`.

This is the current source-of-truth backlog for features still outstanding to build. Older planning docs are useful historical context, but several items they list as future work are now implemented.

## Current Code Baseline

Confirmed present in code and tests:

- Core spreadsheet shell, command bus, undo/redo, virtualized WPF grid, multi-sheet UI, native/CSV/XLSX adapters.
- Broad formula library: ~165 functions implemented across Math/Trig, Statistical, Logical, Lookup/Reference, Text, Date/Time, Financial, and Information categories. Includes modern lookup and dynamic-array functions such as `XLOOKUP`, `XMATCH`, `SEQUENCE`, `RANDARRAY`, `FILTER`, `SORT`, `SORTBY`, `UNIQUE`, `TAKE`, `DROP`, `CHOOSEROWS`, `CHOOSECOLS`, `VSTACK`, `HSTACK`, `TOROW`, `TOCOL`, `WRAPROWS`, `WRAPCOLS`, and `EXPAND`. `LAMBDA` and `LET` are not yet implemented; statistical distribution functions and financial bond math are the other major outstanding formula gaps (see `docs/FUNCTION_PARITY.md`).
- Spill infrastructure and formula AST caching in recalculation.
- Formula reference rewriting for insert/delete/paste/autofill paths.
- Autofill drag UI and `AutofillCommand`; Flash Fill command/service baseline.
- Sort/filter, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Goal Seek, Scenario Manager, Forecast Sheet, one- and two-variable Data Tables, Subtotal, grouping/outline.
- Conditional formatting model/UI for cell-value, formula, top/bottom/above-average, color scale, and data bar baselines.
- Page layout, page setup, print/export, custom views, workbook/theme commands, chart/object/theme baselines.
- Slicer, timeline, and external-link metadata: loaded from XLSX, retained in-memory, and written back on save (package-preserving round-trip); UI rendering and interaction for slicers/timelines is not yet built.
- PivotTable model-first XLSX persistence: PivotTable definitions are loaded, retained, and saved; basic static output materialization is implemented; full aggregation engine, refresh behavior, and creation UI are outstanding.
- Unsupported XLSX feature detection and open/save warnings for macros, Power Query, data model/Power Pivot, linked data types, threaded comments, track changes, structured Excel tables, chart/dialog/macro sheet types, form controls/ActiveX, digital signatures, custom ribbon UI, Office add-ins/web extensions, SmartArt diagrams, printer settings, embedded objects, custom XML, unsupported conditional formatting, drawing objects, sparklines, and unsupported chart package parts.

## Highest Priority Outstanding Work

1. **XLSX corpus and fidelity proof**
   - Current corpus report shows 35 manifest rows: 10 generated supported-pass fixtures and 25 generated known-gap fixtures.
   - Build the planned 100+ workbook corpus with public/open-license, local-private, and regression workbooks.
   - Expand corpus checks from structural smoke tests to per-feature comparisons.
   - Publish pass/fail rate by workbook and feature bucket before claiming 95% fidelity.

2. **Package-preserving XLSX save path**
   - Current save is model-based, so unsupported OOXML parts are detected/disclosed but not preserved.
   - Add a package-preserving save pipeline or source-template save API before promising higher-fidelity round trips for complex workbooks.

3. **Release documentation and packaging**
   - Write `USER_GUIDE.md`.
   - Write `TROUBLESHOOTING.md`.
   - Reconcile stale root planning docs with this current backlog.
   - Add/verify MSIX release automation and release-note workflow.
   - Run a real accessibility pass with keyboard-only and screen-reader validation.

4. **Shortcut and keytip verification**
   - Add UI automation coverage for the shortcut matrix and WPF key routing.
   - Improve keytip overlay placement toward Excel-perfect visual positioning.
   - Extend nested submenu keytips beyond the current covered Conditional Formatting paths as new nested menus appear.
   - Complete long-tail Excel shortcut coverage and the full insert/delete dialog shortcut matrix.

5. **XLSX warning coverage as new gaps are found**
   - Keep unsupported-feature detection aligned with newly discovered OOXML package parts.
   - Add known-gap corpus rows whenever a workbook contains unsupported content that should be disclosed rather than silently lost.

## Product Parity Work Still Outstanding

1. **View and window management**
   - True multi-window workbook hosting for New Window, View Side by Side, Synchronous Scrolling, Reset Window Position, and Switch Windows.
   - Fine split-pane scroll feel parity.
   - Split-pane merged-cell edge cases across non-visible rows/columns.
   - Full workbook view-mode polish beyond the current state/persistence baseline.

2. **Charts, themes, and visual objects**
   - Full chart format panes/dialog UX.
   - Richer combo-chart mixes and advanced chart families such as stock, surface, radar, treemap, sunburst, histogram, Pareto, box-and-whisker, waterfall, funnel, map, and 3D variants.
   - Deeper OOXML effect semantics and broader chart-theme extraction.
   - Arbitrary pie/doughnut data-label text angles and richer tick placement beyond renderer constraints.
   - Interactive picture/object resize and rotation handles.
   - Crop, gradients, richer effects, richer text/shape formatting, and selection-handle polish.

3. **Conditional formatting**
   - Full icon set support in model, rendering, UI, and XLSX round-trip.
   - Richer color scale/data bar options.
   - More complete Excel-style conditional-format rule manager coverage.

4. **Data workflow polish**
   - Full Excel sort/filter dialog UX.
   - Data Validation range-picker UX with live modal collapse/selection.
   - Forecast chart UX rather than only generated forecast-sheet formulas.
   - Full Scenario PivotTable-style reports.
   - Additional polish for advanced Subtotal dialog behavior.

5. **Grouped-sheet propagation**
   - Extend grouped-sheet behavior for advanced object effects.
   - Extend grouped-sheet behavior for supported advanced data commands where Excel applies actions across grouped sheets.

6. **Calculation performance architecture**
   - Recalculation is intentionally single-threaded today.
   - Build multi-threaded recalculation only after large-workbook profiling proves it is needed.
   - If built, add thread-safe dependency graph/evaluation, progress reporting, cancellation, and result parity tests against the single-threaded engine.

## Explicitly Excluded Unless Scope Changes

These are documented exclusions, not current bugs:

- Slicers and timelines.
- VBA macros, COM add-ins, Office web add-ins, and Office Scripts.
- Power Query, Power Pivot, OLAP/data model features, and Microsoft linked data types.
- Microsoft 365 Share/co-authoring, cloud permissions, presence, Teams-linked sharing, online template discovery, and version history.
- Enterprise Microsoft 365 controls such as sensitivity labels and IRM.
- Full Excel Help/search/support-account/training-template flows.

If any excluded area becomes a product goal, it should get a design document before implementation. PivotTables now have a model-first XLSX persistence baseline; aggregation, UI rendering, refresh behavior, and editing remain outstanding PivotTable phases.

## Historical Docs To Treat Carefully

Stale root sprint/planning documents were removed on 2026-05-17 because they contained obsolete test counts, old release timelines, and outdated feature-scope claims.

Treat `docs/superpowers/plans/*` and `docs/superpowers/specs/*` as historical implementation notes only. Prefer this document, `docs/COMMAND_SURFACE_PARITY.md`, `docs/SHORTCUT_PARITY_MATRIX.md`, `docs/FIDELITY_CONTRACT.md`, and `docs/XLSX_CORPUS_REPORT.md` for current build status.

