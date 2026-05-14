# Freexcel — Execution Plan: Path A + Path B (Selective)
**Scope**: Stabilization + Pivot Tables + Autofill/Flash Fill  
**Duration**: 6–8 weeks  
**Target Release**: v1.5 (late June / early July 2026)

---

## Scope Definition

### ✅ Include (Path A + Path B Selective)
- Path A: Code audit, perf profiling, test expansion, UI polish, docs
- Path B: **Pivot tables** (4 weeks)
- Path B: **Autofill / Flash Fill** (1–2 weeks)

### ⏸ Defer (for later)
- Multi-threaded recalculation (Phase 4 remainder)
- Dynamic arrays (FILTER, SORT, UNIQUE with spill)
- Path C: AI integration prep

---

## Sprint Breakdown

### **Sprint 1: Foundation (Week 1–2)** ✅
**Goal**: Establish baseline, audit codebase, expand test corpus  

#### Week 1: Diagnostics & Code Audit ✅
- [x] **1.1** Run full test suite, document any failures
- [x] **1.2** Run static analysis (FxCop, Roslynator warnings)
- [x] **1.3** Compile with `TreatWarningsAsErrors=true`, fix all warnings
- [x] **1.4** Benchmark current recalc speed (10k, 100k, 1M cells)
- [ ] **1.5** Review Core.Formula exception handling (null-safety audit)
- [ ] **1.6** Create `PERF_BASELINE.md` documenting v1.0 metrics

**Deliverable**: Clean build, no warnings, baseline metrics

#### Week 2: Test Corpus & CI
- [ ] **2.1** Collect 50–100 real `.xlsx` files (government datasets, Wikipedia tables, sample models)
- [ ] **2.2** Add round-trip regression test to CI (`TestRoundTripXlsx` parametrized)
- [ ] **2.3** Document fidelity contract: what we preserve, what we drop
- [ ] **2.4** Create `FIDELITY_REPORT.md` listing feature coverage (% pass rate on corpus)
- [ ] **2.5** Fix any regressions discovered in corpus (update UI or Core as needed)
- [ ] **2.6** Set up GitHub Releases automation (optional, but good to have)

**Deliverable**: 100+ XLSX files tested in CI, fidelity documented

---

### **Sprint 2: Polish & Stabilization (Week 3–4)**
**Goal**: Ship v1.0 feature-complete and user-ready  

#### Week 3: UI/UX Polish
- [ ] **3.1** Audit keyboard shortcuts against Excel standard (F2, Ctrl+~, Ctrl+`, etc.)
- [ ] **3.2** Add missing shortcuts (if any) to MainWindow.xaml.cs
- [ ] **3.3** Improve error messages in dialogs (user-friendly language, actionable guidance)
- [ ] **3.4** Test accessibility (tab order, screen reader with NVDA)
- [ ] **3.5** Add context help / tooltips to key UI elements (formula bar, style buttons)
- [ ] **3.6** Review font/color picker dialogs for UX (consistency, clarity)

**Deliverable**: Keyboard-navigable UI, improved error handling, accessibility tested

#### Week 4: Documentation & v1.0 Release
- [ ] **4.1** Write `USER_GUIDE.md` (file operations, basic formulas, formatting, charts)
- [ ] **4.2** Expand `ARCHITECTURE.md` with data flow diagrams (Mermaid)
- [ ] **4.3** Finalize all ADRs (check for any missing decisions)
- [ ] **4.4** Write `TROUBLESHOOTING.md` (known issues, workarounds)
- [ ] **4.5** Tag `v1.0.0` in git
- [ ] **4.6** Create GitHub Release with v1.0 MSIX + release notes

**Deliverable**: v1.0 release with full documentation

---

### **Sprint 3: Pivot Tables Part 1 (Week 5–6)**
**Goal**: Read and display pivot tables; basic functionality  

#### Week 5: Pivot Table Engine Foundation
- [ ] **5.1** Create `Freexcel.Core.Pivots` project (new)
- [ ] **5.2** Define `IPivotTable` interface:
  ```csharp
  public interface IPivotTable
  {
      string Name { get; }
      CellAddress TopLeftCell { get; }
      IReadOnlyList<string> RowFields { get; }
      IReadOnlyList<string> ColumnFields { get; }
      IReadOnlyList<string> DataFields { get; }
      IReadOnlyList<PivotRow> GetRows();
  }
  ```
- [ ] **5.3** Implement pivot aggregation engine (SUM, COUNT, AVERAGE, etc.)
- [ ] **5.4** Add `ParsePivotFromXlsx` method to `XlsxFileAdapter`
- [ ] **5.5** Extend `Workbook` model to include `PivotTables` collection
- [ ] **5.6** Write 20+ unit tests for aggregation (various data shapes)

**Deliverable**: Pivot table reading from XLSX, aggregation engine functional

#### Week 6: Pivot Table UI & Rendering
- [ ] **6.1** Extend `GridView` to recognize and render pivot tables differently
- [ ] **6.2** Render pivot table structure (row/column headers, grouped rows, subtotals)
- [ ] **6.3** Add pivot table properties dialog (list fields, edit aggregations)
- [ ] **6.4** Implement pivot field filtering (checkbox list for row/column filtering)
- [ ] **6.5** Add "Refresh Pivot" command to recalculate on source data change
- [ ] **6.6** Write integration tests (20+ scenarios: sorting, filtering, refresh)

**Deliverable**: Pivot tables display and refresh correctly; UI for basic manipulation

---

### **Sprint 4: Autofill & Polish (Week 7–8)**
**Goal**: Autofill/Flash Fill + final polish for v1.5 release  

#### Week 7: Autofill Engine
- [ ] **7.1** Implement pattern detection:
  - [ ] **7.1a** Linear sequences (1, 2, 3, ...)
  - [ ] **7.1b** Date sequences (2024-01-01, 2024-01-02, ...)
  - [ ] **7.1c** Geometric sequences (2, 4, 8, ...)
  - [ ] **7.1d** Text sequences (A, B, C, ...; Q1, Q2, Q3, ...)
  - [ ] **7.1e** Mixed patterns (Jan 1, Jan 2, ...; Row1, Row2, ...)
- [ ] **7.2** Create `IAutofillService`:
  ```csharp
  public interface IAutofillService
  {
      bool TryDetectPattern(IReadOnlyList<ScalarValue> samples, out AutofillPattern pattern);
      IReadOnlyList<ScalarValue> FillSeries(AutofillPattern pattern, uint count);
  }
  ```
- [ ] **7.3** Add `FillSeriesCommand` to command bus
- [ ] **7.4** Write 30+ unit tests (edge cases: empty cells, mixed types, etc.)

**Deliverable**: Pattern detection engine, undo-safe fill via command bus

#### Week 8: Autofill UI + v1.5 Release
- [ ] **8.1** Add drag-fill-handle to `GridView` (cursor changes to crosshair over bottom-right cell corner)
- [ ] **8.2** Implement auto-fill on drag: detect pattern from first 2–3 cells, suggest fill
- [ ] **8.3** Show preview tooltip of fill result before releasing mouse
- [ ] **8.4** Keyboard shortcut: Shift+Drag or Ctrl+D for autofill
- [ ] **8.5** Test all scenarios: 20+ workflows (fill down, fill series, pattern detection)
- [ ] **8.6** Create quick-start video demo (autofill example)
- [ ] **8.7** Tag `v1.5.0` and publish GitHub Release

**Deliverable**: v1.5 with autofill, pivot tables, full documentation

---

## Daily Standup Checklist

Use this to track progress daily:

```markdown
### Daily Status (Week X, Day Y)

**Completed Today**:
- [ ] Task X.Y: Description

**In Progress**:
- [ ] Task X.Y: Description (% done)

**Blocked**:
- [ ] Task X.Y: Reason

**Tomorrow's Plan**:
- [ ] Task X.Y
- [ ] Task X.Y
```

---

## Key Decisions (To Be Made)

1. **Pivot table read-only vs. editable?**  
   → Recommend: **Read-only in v1.5** (skip drag-and-drop field editor). Add edit capability in v2.0.

2. **Autofill: should it fill formulas or values?**  
   → Recommend: **Fill formulas** (common Excel behavior). E.g., `=A1*2` → `=A2*2` → `=A3*2`

3. **Test corpus: where to store 100+ XLSX files?**  
   → Recommend: `tests/Freexcel.Fixtures/xlsx/` directory (git-lfs if file size > 100MB total)

4. **Release approach: GitHub Releases + MSIX, or NuGet?**  
   → Recommend: **GitHub Releases + MSIX** for desktop app (NuGet is for libraries)

---

## Testing Strategy

### Unit Tests (by sprint)
- Sprint 1: Code audit fixes (warnings → errors)
- Sprint 2: Polish tests (a11y, keyboard nav)
- Sprint 3: Pivot aggregation (30+ tests), pivot rendering (20+ tests)
- Sprint 4: Autofill patterns (40+ tests), autofill UI (20+ tests)

### Integration Tests
- Sprint 1: Round-trip 100 real XLSX files, document pass/fail
- Sprint 2: End-to-end workflows (open → edit → save → reopen)
- Sprint 3: Pivot refresh on data change (10+ scenarios)
- Sprint 4: Autofill + sort/filter interaction (15+ scenarios)

### Performance Tests
- Baseline (Sprint 1): 10k, 100k, 1M cell recalc times
- Pivot tables (Sprint 3): Open 50-row pivot, aggregate, refresh speed
- Autofill (Sprint 4): Detect pattern on 1k-row series in <100ms

### User Acceptance Testing (Optional, but valuable)
- End of Sprint 2 (v1.0): Share with 3–5 early users, collect feedback
- End of Sprint 4 (v1.5): Share pivots + autofill demo, iterate on UX

---

## Parallel Work (If Multiple People)

If you have collaborators:

- **Person A**: Sprint 1 diagnostics + Sprint 2 documentation
- **Person B**: Sprint 3 pivot engine + UI
- **Person C**: Sprint 4 autofill engine + UI

Or:
- **Person A**: Pivots (entire Sprints 3–4 pivot tasks)
- **Person B**: Autofill (entire Sprints 3–4 autofill tasks)

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Pivot table implementation takes >4 weeks | Start with read-only; defer edit/drag-drop to v2.0 |
| Autofill pattern detection misses edge cases | Build exhaustive test matrix first; review real-world examples |
| XLSX corpus roundtrip reveals many failures | Triage: document known limitations; fix highest-impact bugs only in v1.5 |
| UI polish scope creeps | Lock scope by end of Week 2; defer remaining polish to v1.5 |
| Multi-threading pressure mid-sprint | Reassure: multithreading deferred; v1.5 ships single-threaded, which is fine |

---

## Checkpoint Criteria (Gate Before v1.5 Release)

**All of the following must be true**:

- [ ] All compiler warnings fixed (`TreatWarningsAsErrors=true` passes)
- [ ] Full test suite green: `dotnet test Freexcel.slnx --verbosity normal` shows 0 failures
- [ ] 100+ XLSX files roundtrip with documented fidelity (>80% pass rate)
- [ ] Keyboard shortcuts work without UI lag (<50ms)
- [ ] Accessibility: tab order correct, screen reader announces key elements
- [ ] Pivot tables: open/save 50+ pivot XLSX files without data loss
- [ ] Autofill: correctly detects 10+ pattern types; fill speed <100ms
- [ ] Documentation: USER_GUIDE, ARCHITECTURE, TROUBLESHOOTING, ADRs complete
- [ ] GitHub Release v1.5.0 created with changelog + MSIX download link

**Go/No-Go Meeting**: End of Sprint 4, review criteria, decide on release

---

## Success Metrics (End of v1.5)

- **Code Quality**: Zero compiler warnings, <5 open bugs, 80%+ test coverage on Core projects
- **Performance**: 100k-cell scroll 60fps, 1MB XLSX open <2s, pivot refresh <500ms
- **Features**: Pivots work end-to-end, autofill covers 95% of use cases
- **User Feedback**: Early testers report "feels solid" and "ready to use"
- **Community**: 200+ GitHub stars, 100+ downloads in first month (v1.5)

---

## Next Action: Begin Sprint 1

**Today (May 13, 2026)**:
1. Run full test suite
2. Run static analysis
3. Start 1.1–1.3 (diagnostics)

**By end of Week 1**:
- Baseline metrics documented
- Clean build (no warnings)
- Decisions locked (pivot read-only? autofill fills formulas?)

**Let's go! 🚀**
