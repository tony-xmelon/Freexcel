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

## Phase 3 — Formatting & UX Polish

- [x] Number format rendering — NumberFormatter in Core.Calc (Task 3.1)
- [x] Cell style rendering — bold, italic, color, fill, borders, alignment (Task 3.2)
- [x] Copy / paste / cut — system clipboard, tab-separated, undo-safe (Task 3.3)
- [x] Multi-sheet tab bar — dynamic, add and rename sheets (Task 3.4)
- [x] Freeze panes — read from XLSX, render divider, clamp scroll (Task 3.5)
- [x] Basic charts — column, line, pie via OxyPlot (Task 3.6)
- [x] Text overflow into empty neighbours, wrap text, vertical alignment (post-3.6)
- [x] F2 / double-click edit entry; recalc formula-cell fix (post-3.6)

## Phase 4 — Power Features

- [x] Sort & filter — column sort asc/desc, filter by value with row hiding (Phase 4.1)
- [x] Expand function library — 50+ functions: IFERROR/IFNA, VLOOKUP/HLOOKUP, INDEX/MATCH, SUMIF/COUNTIF/AVERAGEIF, TEXT/TRIM/UPPER/LOWER/PROPER/SUBSTITUTE/FIND/SEARCH/MID/REPT/VALUE, DATE/YEAR/MONTH/DAY/HOUR/MINUTE/SECOND/WEEKDAY/EDATE/DATEDIF, MOD/POWER/SQRT/INT/CEILING/FLOOR/SIGN/LOG/LN/EXP/PI/FACT/RANDBETWEEN, LARGE/SMALL/RANK/STDEV/MEDIAN (Phase 4.2)
- [x] Conditional formatting — CellValue rules, color scale, data bars, XLSX round-trip (Phase 4.3)
- [x] Named ranges UI — manage dialog, formula resolution (=SUM(MyData)), XLSX round-trip (Phase 4.5)
- [x] Data validation — list dropdowns, number/text/date rules, XLSX round-trip (Phase 4.4)
- [x] Print & PDF/XPS export — WPF PrintDialog + XpsDocument, A4 pagination (Phase 4.6)
- [ ] Multi-threaded recalculation
