# ADR-005: Cross-Sheet Formula References — Workbook Passed Through Evaluator Chain

**Date**: 2026-05-12  
**Status**: Accepted

## Context

Excel supports cross-sheet cell references in formulas (e.g. `Sheet1!A1`). The existing formula engine only had access to the current `Sheet` during evaluation. To resolve `Sheet1!A1`, the evaluator needs to look up another sheet by name from the workbook.

## Decision

- Lexer: `Sheet1!A1` is tokenized as `[Identifier: "Sheet1"]` `[SheetQualifier: "!"]` `[CellRef: "A1"]`; quoted sheet names (`'My Sheet'!A1`) are a Phase 2 known limitation (not supported)
- Parser: `CellRefNode` and `RangeRefNode` gain an optional `string? SheetName` property; mismatched sheet names on a range's start/end throw `FormulaParseException`
- `IEvalContext` gains two cross-sheet overloads: `GetCellValue(string sheetName, uint row, uint col)` and `GetRangeValues(string sheetName, ...)`
- `FormulaEvaluator` accepts an optional `Workbook?` parameter (null = single-sheet mode for backwards compatibility)
- `SheetEvalContext.GetCellValue(sheetName, ...)` looks up the sheet by name and returns `ErrorValue.Ref` for unknown sheets
- `RecalcEngine.RegisterFormulaDependencies` now requires `Workbook workbook` and resolves cross-sheet `CellRefNode`s to the correct `SheetId` for dependency tracking
- **Critical**: Both call sites in `MainWindow.xaml.cs` pass `_workbook` explicitly — omitting it silently drops cross-sheet dependencies

## Rationale

Passing `Workbook?` as an optional parameter preserves backward compatibility with existing single-sheet tests while enabling multi-sheet evaluation. `ErrorValue.Ref` for unknown sheets matches Excel's `#REF!` behavior.

## Consequences

Quoted sheet names are not supported (phase-2 limitation, documented in Lexer with a comment). Renaming a sheet would break formula references — name-based lookup is used for simplicity in v1.
