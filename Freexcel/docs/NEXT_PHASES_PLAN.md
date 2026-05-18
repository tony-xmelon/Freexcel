# Freexcel Next Development Phases

**Last updated:** 2026-05-18  
**Current state:** Formula engine at 320/320 in-scope functions (100%), broad command surface, XLSX round-trip, virtualized WPF UI, and deep PivotTable/PivotChart fidelity (tasks 1–13 complete). Remaining work is advanced PivotTable/slicer/chart UI, performance at scale, and corpus expansion.

---

## Completed

### Phase 6: Formula Completeness ✓

All 320 in-scope Excel functions are implemented and tested:

- **6A** — LET, LAMBDA, MAP, REDUCE, SCAN, BYROW, BYCOL, MAKEARRAY (+ recursive lambda support)
- **6B** — Full statistical distribution suite (normal, t, F, chi-squared, binomial, beta, gamma, Weibull, lognormal, exponential, FREQUENCY, SKEW, KURT, CONFIDENCE)
- **6C** — Complete financial bond math (accrued interest, coupon analytics, price/yield, odd-period, depreciation, IRR/XIRR/XNPV, treasury bills, and all remaining helpers)
- **6D** — OFFSET, FORMULATEXT, ISFORMULA, ISREF, CELL, INFO

See [FUNCTION_PARITY.md](FUNCTION_PARITY.md) for the full function list.

### PivotTable Fidelity (Tasks 1–13) ✓

Core pivot semantics, XLSX round-trip, and refresh propagation are solid:

- Multiple row/column/value/filter fields; nested column matrices
- Grand-total visibility (row and column axes independently)
- Repeated-label suppression; blank-line spacing; compact/outline layout flags
- Row and column label filters; value filters with source-field targeting
- Label and value sorting (both axes); date/number grouping
- Subtotals; calculated fields/items; Show Details (item/subtotal/grand-total/matrix/column-only)
- Values-only and column-only layouts
- PivotChart binding; XLSX-authored round-trip; PivotTable style-name round-trip

---

## Phase 7: Advanced UI Polish (estimated: 2–3 sprints)

### 7A: PivotTable Authoring UI

The model and refresh engine cover the full semantic surface; what remains is the authoring layer:

- Field-list panel with drag-and-drop into row/column/value/filter zones and aggregation-type selector
- Contextual ribbon polish: Refresh button active only when a PivotTable is selected; Design tab style gallery using stored style names
- PivotChart field buttons and filtering controls; chart-type/layout editing mirroring Excel's PivotChart Tools

### 7B: Slicer and Timeline UI

Slicer and timeline metadata already loads/saves; build the interaction layer:

- WPF rendering for slicer tiles and timeline date-range bar
- Click-to-filter: selecting a slicer item filters the connected PivotTable or table
- Timeline drag to filter by date bucket (year/quarter/month/day)
- Insert Slicer / Insert Timeline commands and corresponding XLSX write path

### 7C: Advanced Chart Families

- Stock charts (OHLC/candlestick), radar, surface
- Statistical: histogram, Pareto, box-and-whisker
- Hierarchy: treemap, sunburst
- Modern: waterfall, funnel
- Full chart format pane/dialog UX for all chart families

### 7D: Conditional Formatting and Formatting Polish

- Full icon-set rule support: model, XLSX round-trip, cell rendering, rule-manager UI
- Richer color-scale/data-bar options (midpoint control, axis display, border, fill variants)
- Rule-manager dialog matching Excel's full priority and manage-rules UX

---

## Phase 8: Performance and Scalability (estimated: 1–2 sprints)

### 8A: Multi-threaded Recalculation

- Profile recalculation on large workbooks (50k+ formulas) before committing to threading
- If profiling confirms parallelism as the right fix: thread-safe topological evaluation (partition DAG into independent subgraphs, evaluate in parallel)
- Progress reporting and cancellation for long recalculations
- Result-parity tests against the single-threaded engine

### 8B: Large Workbook XLSX Parse Optimization

- SAX/streaming parse for shared-strings and worksheet XML to avoid full DOM allocation
- Incremental sheet-load: parse only the active sheet on open; load other sheets lazily
- Benchmark open time for a 10 MB+ workbook; publish perf baseline in `docs/PERF_BASELINE.md`

---

## Phase 9: XLSX Corpus Expansion (ongoing)

- Expand from the current 62 manifest rows toward 100+ workbooks
- Add public/open-license workbooks covering every feature bucket (charts, CF, pivot, validation, named ranges, shared formulas, etc.)
- Graduate per-workbook smoke tests to per-feature structural comparisons (cell values, styles, chart series counts, CF rules, etc.)
- Track and publish pass/fail rate by feature bucket; target 95% of supported features passing before any public release claim
- Add regression entries for every bug fix involving XLSX round-trip or formula result discrepancy

---

## Explicitly Excluded (won't change unless a design doc is written)

- **VBA / macros / COM add-ins / Office Scripts / Office web add-ins** — runtime not available; unsupported parts are preserved in the XLSX package and disclosed on open
- **Power Query, Power Pivot, OLAP data model, Microsoft linked data types** — requires Microsoft infrastructure; metadata is preserved in the XLSX package
- **Microsoft 365 co-authoring, cloud sharing, presence, Teams integration, version history** — requires Microsoft 365 identity and services
- **Enterprise controls** — sensitivity labels, IRM, digital signatures
- **Cube functions** (CUBEMEMBER, CUBEVALUE, etc.) — require a live SSAS/Power Pivot connection
- **East Asian locale text functions** (ASC, DBCS, PHONETIC, BAHTTEXT) — locale-specific, out of scope for current target market
- **Cloud/web functions** (WEBSERVICE, FILTERXML, ENCODEURL, RTD) — require external service connectivity
