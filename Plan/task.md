# Freexcel — Task Tracker

## Phase 0 — Foundations

- [x] Create solution and projects (Refactored to Freexcel)
- [x] Set up dependency rules
- [x] Configure DI & Serilog
- [x] WPF shell layout
- [x] 75 tests passing

## Phase 1a — Core Model & Formula Engine

- [x] Formula lexer/parser/evaluator (16 functions)
- [x] Dependency graph & topological recalc
- [x] Cycle detection
- [x] Command bus (undo/redo)

## Phase 1b — Virtualized Grid UI

- [x] `IViewportService` for engine-UI coordination
- [x] Custom `GridView` WPF control (DrawingContext rendering)
- [x] Grid virtualization (rendering only visible area)
- [x] Mouse selection & hit testing
- [x] Keyboard navigation (Arrows, Enter, Tab)
- [x] Formula bar integration (editing cells)
- [x] Native Save/Load format (JSON)
- [x] Ensure 100k row performance (O(visible) rendering)

## Phase 2 — XLSX & Advanced Engine

- [x] XLSX import/export (ClosedXML) — style round-trip, fidelity contract, CSV adapter
- [x] Cell styling (Colors, Fonts, Borders) — StyleId registry, CellStyle with IEquatable
- [x] Volatile functions (NOW, RAND, TODAY) — dirty-first evaluation order
- [x] Cross-sheet references (Sheet1!A1) — SheetQualifier token, workbook threaded through evaluator
- [x] Find and Replace — FindReplaceService in Core.Commands, WPF dialog, Ctrl+F/H
- [ ] Basic Charting
- [ ] Multi-threaded recalculation
