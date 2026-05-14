# Freexcel — Next Build Steps Plan  
**Date**: May 13, 2026  
**Current Phase**: 4 (Power Features) — ~95% complete  
**Build Status**: ✅ All tests passing, v4.6 features complete

---

## Executive Summary

Freexcel has matured from MVP to a capable spreadsheet application. **Phases 0–4.6** are complete:
- ✅ Core formula engine with 50+ functions
- ✅ XLSX round-trip fidelity 
- ✅ Virtualized grid for 100k+ row performance
- ✅ Advanced data features (sort, filter, conditional formatting, data validation)
- ✅ Print & PDF export
- ✅ Multi-sheet support with tabs

**Remaining in Phase 4**: Multi-threaded recalculation (currently single-threaded UI assumption)  
**Phase 5**: Scripting + optional AI copilot (deferred pending community interest)

---

## Three Strategic Paths Forward

### Path A: Stabilization & Polish (3–4 weeks)
**Goal**: Production-ready v1.0 release  
**Focus**: Bug fixes, performance tuning, documentation, user testing

**Tasks**:
1. **Code audit** — Review all Core projects for null-safety, exception handling, edge cases
2. **Performance profiling** — Measure recalc speed on real-world XLSX files (1MB–10MB)
3. **Test fixture expansion** — Add 50+ more XLSX test cases (government data, Wikipedia tables, real financial models)
4. **UI polish** — Keyboard shortcuts, accessibility, error messages
5. **Documentation** — User guide, formula reference, ADRs for recent decisions
6. **CI/CD** — Set up automated MSIX packaging and GitHub Releases

**Deliverable**: `Freexcel-v1.0.msix` ready for public release

---

### Path B: Feature Expansion (4–8 weeks)
**Goal**: Broader feature coverage for power users  
**Focus**: Phase 4 remainder + early Phase 5

**High-priority tasks** (in order):
1. **Multi-threaded recalculation** (2–3 weeks)
   - Background recalc thread pool
   - Thread-safe dependency graph
   - Progress reporting UI
   - Cancellation support
   - Validate no regressions in formula accuracy

2. **Pivot tables** (4+ weeks) 
   - Data aggregation engine
   - Pivot table UI (drag-and-drop fields)
   - Grouping and filtering
   - XLSX read/write support
   - Test against 100+ real pivot files

3. **Autofill / Flash Fill** (1–2 weeks)
   - Pattern detection (sequence, date ramps, text sequences)
   - UI: drag fill handle, smart suggestions
   - Command-bus integration for undo

4. **Dynamic arrays** (2–3 weeks) — *depends on multi-threading*
   - `FILTER()`, `SORT()`, `UNIQUE()` function implementations
   - Spill semantics (formula occupies multiple cells)
   - Dependency graph updates for array spillage
   - Recalc order: array formulas first

**Deliverable**: `Freexcel-v1.5` with power-user features

---

### Path C: Foundation for AI Integration (2–3 weeks prep)
**Goal**: Lay groundwork for future scripting & AI copilot  
**Focus**: Architecture, not full implementation yet

**Tasks**:
1. **Define AI surface API** in new `Freexcel.Core.AI` project
   ```csharp
   IFormulaAssistant — ProposeFormula(), ExplainFormula()
   IDataAssistant — SuggestNormalization(), PreviewBulkEdit()
   IAuditLog — every AI action logged & reversible
   ```

2. **Add C# scripting support** (optional)
   - Expose via Roslyn for sandboxed execution
   - Narrow command surface (`ApplyCommand()` wrapper)
   - Logging & audit trail

3. **Audit tool restrictions**
   - Review all public APIs in Core projects
   - Ensure no direct workbook mutation outside command bus
   - Document safe vs. unsafe operations for external tools

**Deliverable**: `Freexcel.Core.AI` project with documented surface, ready for LLM integration

---

## Recommended Next Step

**Start with Path A (Stabilization)** — takes 3–4 weeks, de-risks v1.0 release:

### Week 1: Code & Performance Audit
- [ ] Run static analysis (`dotnet roslynator`, FxCop rules)
- [ ] Review exception handling in Core.Formula (most crash-prone)
- [ ] Benchmark recalc speed on 10k, 100k, 1M cells
- [ ] Document baseline performance numbers
- [ ] Fix any low-hanging perf wins (avoid premature optimization)

### Week 2: Test Corpus Expansion
- [ ] Collect 50–100 real `.xlsx` files (government datasets, sample spreadsheets from GitHub)
- [ ] Add round-trip regression tests to CI
- [ ] Track fidelity failures (what we drop, what we preserve)
- [ ] Create `FIDELITY_REPORT.md` documenting supported/unsupported features

### Week 3: UI/UX Polish
- [ ] Audit keyboard shortcuts against Excel standard (F2, Ctrl+~, Ctrl+`, etc.)
- [ ] Review error messages (are they user-friendly?)
- [ ] Test accessibility (tab order, screen reader support)
- [ ] Add context help tooltips
- [ ] Improve styling dialogs (especially font/color pickers)

### Week 4: Documentation & Release
- [ ] Write `USER_GUIDE.md` (file operations, basic formulas, formatting)
- [ ] Expand `ARCHITECTURE.md` with data flow diagrams
- [ ] Finalize all ADRs
- [ ] Set up GitHub Releases with MSIX auto-publish
- [ ] Tag `v1.0.0` and announce

**Outcome**: A polished, documented, testable v1.0 ready for users.

---

## Multi-Threaded Recalculation (When Starting Path B)

This is the hardest remaining feature. Key design points:

**Current state** (single-threaded):
- UI thread calls `RecalcEngine.RecalcWorkbook()`
- Formula evaluator is synchronous
- Dependency graph iteration is top-down (topological sort)
- UI blocks until recalc completes

**Proposed multi-threaded design**:
1. **Recalc coordinator** — main thread schedules work, coordinates thread pool
2. **Partition strategy** — split dependency graph by level (all cells at level N can recalc in parallel)
3. **Thread-safe cell cache** — `ConcurrentDictionary<CellAddress, CachedValue>` with version stamps
4. **Progress reporting** — background thread posts progress events to UI thread (via `Dispatcher.Invoke()`)
5. **Cancellation** — `CancellationToken` threaded through evaluator chain
6. **Volatile handling** — "dirty all" runs on main thread before parallel phase

**Testing strategy**:
- Add stress tests: 100k cells, 10% formula density, 100 threads racing edits
- Verify formula results identical to single-threaded baseline
- Measure throughput improvement
- Watch for thread safety regressions (use ThreadSanitizer conceptually)

---

## Known Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Multi-threading breaks formula accuracy | Start with narrow lock-based design; validate all formulas match single-threaded baseline |
| Pivot table implementation takes 8+ weeks | Start with read-only pivot display (skip write); defer editable pivots to v1.5 |
| Dynamic arrays interact badly with existing recalc | Design array spillage rules in ADR before coding; build test suite first |
| AI integration reveals unsafe Core APIs | Audit all public methods in Phase 5 prep; enforce narrow surface with wrapper facade |

---

## Checkpoint Criteria

Before declaring each path complete:

**Path A (Stabilization)**:
- [ ] Zero compiler warnings (treat as errors)
- [ ] All edge cases in formula parser covered (test matrix: 500+ unit tests)
- [ ] 100+ XLSX files round-trip with <2% data loss (fidelity documented)
- [ ] UI responds to user input <16ms on mid-range hardware
- [ ] Accessibility: navigable via keyboard alone, tested with screen reader
- [ ] Documentation: 90% of user questions answerable from USER_GUIDE.md

**Path B (Features)**:
- [ ] Multi-threaded recalc: same formula results as single-threaded, within 20% perf tolerance
- [ ] Pivot tables: open/save 50+ pivot-containing XLSX files without corruption
- [ ] Autofill: correctly detects 10+ pattern types (linear, date, geometric, text)
- [ ] Dynamic arrays: `FILTER`, `SORT`, `UNIQUE` work end-to-end with spill; no regressions in existing formulas
- [ ] Integration tests: 50+ workflows (open → pivot → filter → print) automated in CI

**Path C (AI prep)**:
- [ ] `Core.AI` project compiles; no references to App.* projects
- [ ] All Core public APIs reviewed; unsafe ones wrapped in `IAuditLog`
- [ ] ADR written: "AI Surface Design & Audit Trail" 
- [ ] LLM integration doc drafted (for future implementer)

---

## Recommended Immediate Actions (Today)

1. **Run the full test suite** and review any failures:
   ```powershell
   dotnet test Freexcel.slnx --verbosity normal
   ```

2. **Check for compiler warnings**:
   ```powershell
   dotnet build Freexcel.slnx /p:TreatWarningsAsErrors=true
   ```

3. **Profile current recalc speed** on a representative file (you may already have benchmarks; check `tests/Freexcel.Fixtures/`):
   ```csharp
   // Add to an integration test
   var sw = Stopwatch.StartNew();
   recalcEngine.RecalcWorkbook(workbookId);
   sw.Stop();
   Console.WriteLine($"Recalc: {sw.ElapsedMilliseconds}ms");
   ```

4. **Review the Phase 4 task.md** to see what's explicitly left (multi-threading marker):
   - [ ] Multi-threaded recalculation

5. **Create an issue tracker** (or update existing) with Path A weekly goals

---

## Long-Term Vision (12+ months)

- **v1.5** (Q3 2026): Multi-threading, pivots, autofill, dynamic arrays
- **v2.0** (Q1 2027): Scripting (C# + Lua), performance optimization, 500+ functions
- **v2.5+** (2027+): AI copilot, real-time collaboration, cloud sync, mobile companion

---

## Success Metrics

By end of **Path A** (v1.0):
- **Adoption**: 100+ GitHub stars, 50+ users in first month
- **Quality**: <5 open bugs, zero critical regressions from v4.6
- **Performance**: 100k-cell scroll: 60fps, 1MB XLSX open: <2s
- **Completeness**: 90% of Excel basics available; 80% of advanced features (charts, validation, etc.)

By end of **Path B** (v1.5):
- **Power users**: Multi-threading enables 10MB+ workbooks without lag
- **Pivots**: Real-world pivot tables work end-to-end
- **Discoverability**: 50% of users find autofill/dynamic arrays naturally

By end of **Path C prep** (Phase 5 foundation):
- **AI-ready**: All Core APIs audited; AI surface documented and safe
- **Future-proof**: Third-party tools can safely call engine without bypassing commands

---

*Next review date: May 20, 2026. Status: Awaiting decision on Path A vs. Path B vs. Path C.*
