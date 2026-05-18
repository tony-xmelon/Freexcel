# Freexcel Next Development Phases

**Last updated:** 2026-05-18  
**Current state:** Core formula engine (214 documented Excel functions), broad command surface, XLSX round-trip, virtualized WPF UI, and expanded PivotTable/PivotChart core fidelity are complete; remaining work is statistical/financial formula completeness, advanced PivotTable UI/semantics, advanced UI features, performance at scale, and corpus expansion.

---

## Phase 6: Formula Completeness (estimated: 2-3 sprints)

### 6A: LAMBDA and LET

- Implement `LET` (named sub-expression binding) as a self-contained expression-level feature in the formula parser and evaluator.
- Implement `LAMBDA` (user-defined function values), which requires storing and calling anonymous function objects through the dependency graph.
- Once `LAMBDA` is available, implement the higher-order array helpers: `MAP`, `REDUCE`, `SCAN`, `BYROW`, `BYCOL`, `MAKEARRAY`.
- Add tests verifying recursive LAMBDA patterns and correct spill interaction.

### 6B: Statistical Distributions

- Implement the normal distribution family: `NORM.DIST`, `NORM.INV`, `NORM.S.DIST`, `NORM.S.INV`, `STANDARDIZE`.
- Implement t-, F-, and chi-squared families: `T.DIST`, `T.INV`, `T.TEST`, `F.DIST`, `F.INV`, `F.TEST`, `CHISQ.DIST`, `CHISQ.INV`, `CHISQ.TEST`.
- Implement discrete distributions: `BINOM.DIST`, `BINOM.INV`, `NEGBINOM.DIST`, `POISSON.DIST`, `HYPERGEOM.DIST`.
- Implement remaining continuous distributions and descriptive helpers: `BETA.DIST`, `BETA.INV`, `GAMMA.DIST`, `GAMMA.INV`, `LOGNORM.DIST`, `LOGNORM.INV`, `EXPON.DIST`, `WEIBULL.DIST`, `CONFIDENCE.NORM`, `CONFIDENCE.T`, `FREQUENCY`, `SKEW`, `SKEW.P`, `KURT`.

### 6C: Financial Bond Math

- Implement accrued-interest and settlement functions: `ACCRINT`, `DISC`, `INTRATE`, `RECEIVED`.
- Implement coupon analytics: `COUPDAYBS`, `COUPDAYS`, `COUPDAYSNC`, `COUPNCD`, `COUPNUM`, `COUPPCD`.
- Implement price/yield functions: `PRICE`, `PRICEDISC`, `PRICEMAT`, `YIELD`, `YIELDDISC`, `YIELDMAT`, `DURATION`, `MDURATION`.
- Implement odd-period and depreciation functions: `ODDFPRICE`, `ODDFYIELD`, `ODDLPRICE`, `ODDLYIELD`, `DB`, `DDB`, `VDB`, `SYD`, `AMORDEGRC`, `AMORLINC`, and related helpers (`CUMIPMT`, `CUMPRINC`, `IPMT`, `PPMT`, `EFFECT`, `NOMINAL`, `FVSCHEDULE`, `MIRR`, `XIRR`, `XNPV`, `PDURATION`, `RRI`, `TBILLEQ`, `TBILLPRICE`, `TBILLYIELD`, `DOLLARDE`, `DOLLARFR`).

### 6D: Remaining Lookup and Information Gaps

- Implement `OFFSET` (volatile range-reference function; requires special handling in the dependency graph to avoid stale cache invalidation).
- Implement `FORMULATEXT` (returns the formula string of a referenced cell).
- Implement `ISFORMULA`, `ISREF`, `CELL`, `INFO`.

---

## Phase 7: Advanced UI Polish (estimated: 2-3 sprints)

### 7A: PivotTable and PivotChart Authoring Polish

- Build the full PivotTable field-list panel with row/column/value/filter zone drag-and-drop and aggregation type selector; the Insert tab now has a basic selected-range creation path.
- Extend the current in-memory pivot aggregation beyond multiple row/value fields, command-level field layout changes, single/multi-select page filters, common summaries, date/number grouping, label filters, top/bottom/threshold value filters, sorting, subtotals, calculated fields/items, and Show Details into richer advanced filters and advanced subtotal placement.
- Polish the visible Refresh PivotTable command surface for contextual PivotTable selection.
- Add PivotChart field buttons, PivotChart filtering controls, and chart-type/layout editing that mirrors Excel's PivotChart Tools behavior.
- Extend pivot drill-down beyond the implemented ribbon/double-click Show Details detail-sheet path with richer native cache edge cases and UI polish.

### 7B: Slicer and Timeline UI

- Slicer and timeline metadata is already loaded and saved; build the WPF rendering and interaction layer.
- Implement slicer click-to-filter: selecting a slicer item filters the connected PivotTable or structured table.
- Implement timeline date-range dragging to filter by date bucket (year, quarter, month, day).
- Add Insert Slicer / Insert Timeline commands and the corresponding XLSX write path for new slicers.

### 7C: Advanced Chart Families

- Implement renderer and OOXML write path for stock charts (OHLC/candlestick), radar charts, and surface charts.
- Implement statistical chart types: histogram, Pareto, box-and-whisker.
- Implement hierarchy charts: treemap and sunburst.
- Implement remaining modern types: waterfall, funnel, and map chart (choropleth, requires GeoJSON boundary data).
- Add the full chart format pane/dialog UX for all existing and new chart families.

### 7D: Conditional Formatting and Formatting Polish

- Implement full icon-set rule support: model, XLSX round-trip, cell rendering, and rule-manager UI.
- Add richer color-scale and data-bar options (midpoint control, axis display, border, fill variants).
- Extend the rule-manager dialog to match Excel's full rule-priority and manage-rules UX.

---

## Phase 8: Performance and Scalability (estimated: 1-2 sprints)

### 8A: Multi-threaded Recalculation

- Profile recalculation on large workbooks (50k+ formulas) to identify the bottleneck before committing to threading.
- If profiling confirms thread-parallelism as the correct fix, implement thread-safe topological evaluation: partition the dependency DAG into independent subgraphs and evaluate each in parallel.
- Add progress reporting and cancellation for long recalculations.
- Add result-parity tests against the existing single-threaded engine to prevent non-deterministic divergence.

### 8B: Large Workbook XLSX Parse Optimization

- Implement SAX/streaming parse for shared-strings and worksheet XML to avoid full-document DOM allocation for large files.
- Add incremental sheet-load: parse only the active sheet on open; load other sheets lazily on first access.
- Benchmark open time for a 10 MB+ workbook and publish a new perf baseline in `docs/PERF_BASELINE.md`.

---

## Phase 9: XLSX Corpus Expansion (ongoing)

- Expand the test corpus from the current 37 manifest rows toward the planned 100+ workbook target.
- Add public/open-license workbooks covering every feature bucket (charts, CF, pivot, validation, named ranges, shared formulas, etc.).
- Graduate per-workbook smoke tests to per-feature structural comparisons (cell values, styles, chart series counts, CF rules, etc.).
- Track and publish pass/fail rate by feature bucket; target 95% of supported features passing before any public release claim.
- Add regression entries for every bug fix that involves an XLSX round-trip or formula result discrepancy.

---

## Explicitly Excluded (won't change unless a design doc is written)

- **VBA / macros / COM add-ins / Office Scripts / Office web add-ins** — runtime not available; unsupported parts are preserved in the XLSX package and disclosed on open.
- **Power Query, Power Pivot, OLAP data model, Microsoft linked data types** — requires Microsoft infrastructure; metadata is preserved in the XLSX package.
- **Microsoft 365 co-authoring, cloud sharing, presence, Teams integration, version history** — requires Microsoft 365 identity and services.
- **Enterprise controls** — sensitivity labels, IRM, digital signatures.
- **Cube functions** (CUBEMEMBER, CUBEVALUE, etc.) — require a live SSAS/Power Pivot connection.
- **East Asian locale text functions** (ASC, DBCS, PHONETIC, BAHTTEXT) — locale-specific, out of scope for the current target market.
- **Cloud/web functions** (WEBSERVICE, FILTERXML, ENCODEURL, RTD) — require external service connectivity.
