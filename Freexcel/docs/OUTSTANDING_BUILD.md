# Freexcel Outstanding Build List

**Last updated:** 2026-05-23
**Basis:** reviewed the repository Markdown files and cross-checked the active codebase under `src/` and `tests/`.

This is the current source-of-truth backlog for features still outstanding to build. Older planning docs are useful historical context, but several items they list as future work are now implemented.

## Current Code Baseline

Confirmed present in code and tests:

- Core spreadsheet shell, command bus, undo/redo, virtualized WPF grid, multi-sheet UI, native/CSV/XLSX adapters.
- Formula engine at 345/345 in-scope functions with catalog guards and category-focused Excel parity tests. This includes modern lookup/dynamic-array functions (`XLOOKUP`, `XMATCH`, `SEQUENCE`, `RANDARRAY`, `FILTER`, `SORT`, `SORTBY`, `UNIQUE`, `TAKE`, `DROP`, `CHOOSEROWS`, `CHOOSECOLS`, `VSTACK`, `HSTACK`, `TOROW`, `TOCOL`, `WRAPROWS`, `WRAPCOLS`, `EXPAND`), higher-order formulas (`LET`, `LAMBDA`, `MAP`, `REDUCE`, `SCAN`, `BYROW`, `BYCOL`, `MAKEARRAY`), statistical distributions, financial bond/depreciation helpers, database functions, `HYPERLINK`, discrete engineering base/bit functions, locale-specific text helpers (`ASC`, `DBCS`, `PHONETIC`, `BAHTTEXT`), and local web-text helpers (`ENCODEURL`, `FILTERXML`). Formula hardening now includes Excel cached-result fixtures, inverse/round-trip property tests, dynamic-array error/volatility edge guards, and structured-reference current-row/spaced-header coverage; remaining formula work is ongoing parity proof as new edge cases are discovered (see `docs/FUNCTION_PARITY.md`).
- Spill infrastructure and formula AST caching in recalculation.
- Formula reference rewriting for insert/delete/paste/autofill paths.
- Autofill drag UI and `AutofillCommand`; Flash Fill command/service baseline.
- Sort/filter, Advanced Filter copy-to replacement semantics, Text to Columns, Remove Duplicates, Data Validation, Consolidate, Goal Seek, Scenario Manager, Forecast Sheet, one- and two-variable Data Tables, Subtotal, grouping/outline.
- Conditional formatting model/UI for cell-value, formula, top/bottom/above-average, color scale, and data bar baselines.
- Page layout, page setup, print/export, custom views, workbook/theme commands, chart/object/theme baselines.
- Slicer/timeline metadata, authored state, pane controls, cache relationships, native floating drawing-anchor retention, Insert commands, and connected PivotTable filtering are implemented.
- PivotTable functional core is implemented, including creation, refresh, field layout/source/options changes, filtering/grouping/sorting, Show Values As, calculated fields/items, built-in and custom workbook-catalog value-field number formats, GETPIVOTDATA, Show Details, PivotChart sync, slicer/timeline integration, external/OLAP pivot-cache source metadata load/save, custom PivotStyle definition metadata load/save, and PivotChart chart-space design metadata round-trip for `pivotFmts`, external-data relationship pointers plus package relationship type/target/target-mode metadata, plot-area and legend manual layout metadata, 3D view metadata, date-system/language, color-map overrides, print settings, style ids, chart protection flags, rounded corners, auto-title-deleted state, hidden-row-data visibility, blank-display behavior, data-table options, and data-label-over-maximum flags. PivotChart Options now edits field buttons, data-table/legend-key display, rounded corners, hidden-row data visibility, and blank-cell display mode. Remaining gaps are exact PivotStyle gallery UI/rendering semantics, richer PivotChart layout/design editing beyond these chart-space flags, and external/OLAP/data-model refresh or execution.
- Unsupported XLSX feature detection and open/save warnings for macros, Power Query, data model/Power Pivot, linked data types, threaded comments, track changes, chart/dialog/macro sheet types, form controls/ActiveX, digital signatures, custom ribbon UI, Office add-ins/web extensions, SmartArt diagrams, embedded objects, and unsupported chart package parts, with retained-opaque package wording rather than general package-loss wording.

## Highest Priority Outstanding Work

1. **XLSX corpus and fidelity proof**
   - Current manifest has 101 rows: 48 generated rows, 25 public Tealeg rows, 20 optional local-private rows, and 8 regression formula-cache workbooks.
   - Continue growing the 100+ row baseline with public/open-license, local-private, and regression workbooks.
   - Continue expanding corpus checks from model-summary stability into deeper per-feature comparisons.
   - Add more Excel-authored formula-result fixtures that compare Freexcel evaluation against cached Excel results for newly discovered high-risk edge semantics, especially volatility and spill boundaries.
   - Publish pass/fail rate by workbook and feature bucket before claiming 95% fidelity.

2. **Package-preserving XLSX save path**
   - Package-preserving XLSX save exists as a best-effort source-package merge.
   - Remaining work is broader retention coverage, deeper semantic comparisons, and manual desktop Excel open/save/reopen validation.

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
   - Richer combo-chart mixes and advanced chart families such as surface, treemap, sunburst, histogram, Pareto, box-and-whisker, waterfall, funnel, map, and deeper 3D variants; 3D clustered column/bar, 3D line, 3D area, and 3D pie now have standard OOXML package/rendering paths, and stock chart parity now includes high-low-close, open-high-low-close, volume stock package/rendering paths, date-axis rendering, and up/down bar candlestick rendering but still needs deeper formatting preset polish.
   - Deeper OOXML effect semantics and broader chart-theme extraction.
   - Arbitrary pie/doughnut data-label text angles and richer tick placement beyond renderer constraints.
   - Interactive picture/object resize and rotation handles.
   - Crop, gradients, richer effects, richer text/shape formatting, and selection-handle polish.

3. **Conditional formatting**
   - Continue hardening advanced conditional-format semantics beyond current color scale, data bar, and icon-set model/UI/XLSX coverage.
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

- VBA macros, COM add-ins, Office web add-ins, and Office Scripts.
- Power Query, Power Pivot, OLAP/data model features, and Microsoft linked data types.
- Microsoft 365 Share/co-authoring, cloud permissions, presence, Teams-linked sharing, online template discovery, and version history.
- Enterprise Microsoft 365 controls such as sensitivity labels and IRM.
- Full Excel Help/search/support-account/training-template flows.

If any excluded area becomes a product goal, it should get a design document before implementation. Slicers/timelines and PivotTables are now active parity surfaces with documented remaining native-fidelity gaps rather than broad exclusions.

## Historical Docs To Treat Carefully

Stale root sprint/planning documents were removed on 2026-05-17 because they contained obsolete test counts, old release timelines, and outdated feature-scope claims.

Treat `docs/superpowers/plans/*` and `docs/superpowers/specs/*` as historical implementation notes only. Prefer this document, `docs/COMMAND_SURFACE_PARITY.md`, `docs/SHORTCUT_PARITY_MATRIX.md`, `docs/FIDELITY_CONTRACT.md`, and `docs/XLSX_CORPUS_REPORT.md` for current build status.

