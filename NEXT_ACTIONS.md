# Freexcel - Next Immediate Actions (May 15, 2026)
**Current Status**: Excel command-surface parity audit in progress  
**Baseline Health**: ✅ Excellent (767 tests passing, 0 warnings)

## Current Highest-Value Parity Work

1. Page Layout: design deferred theme/background architecture.
2. View: add arrange-window behavior and independent split-pane scrolling.
3. Sheet tabs: extend grouped-sheet propagation beyond direct cell edits/common formatting/page setup/row-column structure/pictures/text boxes/basic shapes/basic object size-rotation-fill-outline into advanced object effects and supported data commands.
4. Charts: extend fidelity beyond title/axis-title/legend layout into labels, secondary axes, trendlines, combo charts, and advanced formatting.
5. Pictures/objects: add interactive resize/rotation handles, crop, gradients, effects, and richer formatting.

See `docs/COMMAND_SURFACE_PARITY.md` and `docs/SHORTCUT_PARITY_MATRIX.md` for the current command and shortcut audit.

---

## TODAY (May 13) — COMPLETE ✅

- [x] Review workspace documentation (BUILD_PLAN.md, task.md, ARCHITECTURE.md)
- [x] Create NEXT_STEPS.md (strategic planning)
- [x] Create EXECUTION_PLAN.md (6–8 week roadmap)
- [x] Run full test suite: **767/767 passing** ✅
- [x] Build with warnings-as-errors: **0 warnings** ✅
- [x] Create SPRINT1_DIAGNOSTICS.md (baseline report)

---

## NEXT 3 DAYS (May 14-16) — Sprint 1 Completion

### Day 1 (Tuesday, May 14): Performance Benchmarks

**Goal**: Establish recalc speed baseline

**Tasks**:
1. Create test XLSX files (if not existing):
   - `10k.xlsx` — 10,000 cells with formulas (10% formula density)
   - `100k.xlsx` — 100,000 cells with formulas
   - `1m.xlsx` — 1,000,000 cells with values (for memory test)
   
   **Quick way**: 
   ```csharp
   // In a new test file: PerformanceBenchmarkTests.cs
   var workbook = new Workbook();
   var sheet = workbook.Sheets[0];
   
   // Fill 10,000 rows with data
   for (uint row = 1; row <= 10000; row++)
   {
       sheet.SetCell(new CellAddress(sheet.Id, row, 1), new NumberValue(row));
       sheet.SetCell(new CellAddress(sheet.Id, row, 2), new NumberValue(row * 2));
       if (row % 10 == 0) // 10% formula density
       {
           sheet.SetCell(new CellAddress(sheet.Id, row, 3), 
               new FormulaCell($"=A{row}+B{row}"));
       }
   }
   ```

2. Run benchmarks:
   ```csharp
   var sw = Stopwatch.StartNew();
   engine.RecalcWorkbook(workbookId);
   sw.Stop();
   Console.WriteLine($"10k cells: {sw.ElapsedMilliseconds}ms");
   ```

3. Record results in `PERF_BASELINE.md`

**Success criteria**:
- 10k recalc: <100ms
- 100k recalc: <1s
- 1M load: <5s, <200MB memory

---

### Day 2 (Wednesday, May 15): Core.Formula Safety Audit

**Goal**: Identify any null-reference or exception handling gaps

**Tasks**:
1. Review `Core.Formula/FormulaEvaluator.cs`:
   - [ ] Null-check on workbook resolution
   - [ ] Null-check on sheet/cell lookup
   - [ ] Error handling for circular refs
   - [ ] Type mismatch handling (e.g., text + number)
   - [ ] Range expansion edge cases (empty range, single cell)

2. Add defensive null-checks (nullability inspection):
   ```csharp
   // Example: In FormulaEvaluator.Evaluate()
   if (workbook == null) throw new ArgumentNullException(nameof(workbook));
   if (sheet == null) throw new InvalidOperationException("Sheet not found");
   ```

3. Run full test suite again after changes:
   ```powershell
   dotnet test Freexcel.slnx --verbosity normal
   ```

**Success criteria**:
- All tests still passing
- 0 new compiler warnings
- Comments added explaining risky areas

---

### Day 3 (Thursday, May 16): Fidelity Contract Planning

**Goal**: Prepare for round-trip XLSX testing (Sprint 2)

**Tasks**:
1. Create `docs/FIDELITY_CONTRACT.md`:
   ```markdown
   # Freexcel XLSX Fidelity Contract (v1.5)
   
   ## What We Preserve
   - Cell values (numbers, text, dates, errors)
   - Formulas (basic functions, cross-sheet refs)
   - Cell formatting (font, color, borders, alignment)
   - Sheet names, multiple sheets
   - Named ranges
   - Data validation
   - Conditional formatting
   - Freeze panes
   - Print settings
   
   ## What We Drop (OK for v1)
   - Charts (read but don't render in UI)
   - Pivot tables (read structure, not full calc)
   - VBA macros (silently dropped)
   - OLE objects
   - Theme colors (mapped to black)
   - Quoted sheet names (`'My Sheet'!A1`) for parser-supported formulas
   
   ## What We Lose (Acceptable)
   - Theme context (indexed colors → black)
   - Cell comments
   - Hyperlinks (TODO v2.0)
   - Some hyperlink text rotations (read as 0°)
   
   ## Test Corpus Requirements
   - Minimum: 100+ real XLSX files
   - Variety: simple sheets, multi-sheet, formulas, formatting
   - Coverage: 95%+ should round-trip without data loss
   ```

2. Identify 3–5 sources for XLSX test corpus:
   - [ ] World Bank data: data.worldbank.org/data-catalog
   - [ ] Kaggle: kaggle.com/datasets (filter CSV → XLSX)
   - [ ] GitHub: search "excel sample files"
   - [ ] Wikipedia table exports (via Tools → Download as CSV → convert to XLSX)
   - [ ] Your own local XLSX files (if safe to share)

3. Document expected pass rate target: **>95%** (250+ of 261 files)

**Success criteria**:
- FIDELITY_CONTRACT.md written and reviewed
- 3+ data sources identified
- Pass rate target documented

---

## WEEKS 2-8 Overview (May 17 — July 10)

| Week | Sprint | Focus | Deliverable |
|------|--------|-------|-------------|
| 2 | 2a | Test corpus collection | 100+ XLSX files in CI |
| 2 | 2b | Fidelity testing | Round-trip pass rate report |
| 3 | 3 | UI/UX polish | Accessibility tested, docs complete |
| 4 | 4 | v1.0 release | GitHub Release v1.0.0 + MSIX |
| 5 | 5a | Pivot engine | IPivotTable interface, aggregation |
| 5 | 5b | Pivot UI | Rendering, field filtering |
| 6 | 6 | Autofill engine | Pattern detection + FillSeriesCommand |
| 7 | 7 | Autofill UI | Drag-fill handle, preview tooltip |
| 8 | 8 | v1.5 release | GitHub Release v1.5.0 + pivots + autofill |

---

## Critical Decision Points

**By end of Week 1 (May 17)**:
- [ ] Confirm performance baseline meets targets (or plan optimization)
- [ ] Confirm no critical null-safety issues found
- [ ] Confirm test corpus collection plan is viable

**By end of Week 2 (May 24)**:
- [ ] 100+ XLSX files collected and tested
- [ ] Fidelity report shows pass rate
- [ ] Any blocking issues escalated

**By end of Week 4 (June 7)**:
- [ ] v1.0 release candidate ready for testing
- [ ] All documentation complete and reviewed

---

## Command Quick Reference

**Build & test**:
```powershell
cd e:\Users\anton\Documents\Claude\Freexcel
dotnet test Freexcel.slnx --verbosity normal
dotnet build Freexcel.slnx /p:TreatWarningsAsErrors=true
```

**Run app (after build)**:
```powershell
dotnet run --project src/Freexcel.App.Host/Freexcel.App.Host.csproj
```

**Create benchmark test file**:
```powershell
# Open Freexcel.Core.Calc.Tests\PerformanceBenchmarkTests.cs (create if missing)
# Add [Fact] public void Benchmark_10kCellRecalc() { ... }
```

---

## Checkpoint: Sprint 1 Complete Criteria

✅ **Already met**:
- [x] Full test suite green (767/767)
- [x] Zero compiler warnings
- [x] Baseline code quality assessed

📝 **To complete by Friday (May 17)**:
- [ ] Performance benchmarks run and documented
- [ ] Core.Formula safety audit complete
- [ ] FIDELITY_CONTRACT.md written
- [ ] Test corpus collection plan finalized

**Go/No-Go Meeting**: Friday May 17, 10am  
**Decision**: Proceed to Sprint 2 if all criteria met ✅

---

## Questions / Blockers

If you hit any issues:
1. **Test failures**: Run single test with verbose output
   ```powershell
   dotnet test Freexcel.slnx --filter "TestName" --verbosity detailed
   ```

2. **Build failures**: Clean and rebuild
   ```powershell
   dotnet clean Freexcel.slnx
   dotnet build Freexcel.slnx
   ```

3. **Performance concerns**: Check Task Manager while running benchmarks; if CPU/RAM spikes oddly, might indicate GC pressure or formula complexity

**Let's ship this! 🚀**
