# ADR-003: XLSX Fidelity Contract — Preserve Unknown Features on Re-Save

**Date**: 2026-05-12  
**Status**: Accepted

## Context

ClosedXML 0.105.0 is used for `.xlsx` I/O. Real-world `.xlsx` files contain features we don't support in v1 (charts, pivot tables, conditional formatting, VBA, theme colors). We need a clear policy on what happens to those features when a user opens such a file and re-saves it.

## Decision

- We do not attempt to re-save unsupported features — ClosedXML's default behavior is to preserve unknown parts it doesn't understand when writing
- Theme and indexed colors cannot be resolved to RGB without the workbook theme context, so they are mapped to black on load with a code comment explaining the limitation
- Supported features round-trip faithfully: cell values (all ScalarValue subtypes), formulas, row heights, column widths, basic font/fill/border styles
- The calc-chain part of `.xlsx` is explicitly ignored on load; we build our own dependency graph from formulas
- Workbook name defaults to "Untitled" on load (not a random filename)

## Rationale

"Do not corrupt what you cannot read" is the guiding principle. Losing chart data is acceptable; corrupting it is not.

## Consequences

Users who open files with theme colors will see black where those colors were. This is documented as a Phase 2 limitation. A future pass can resolve theme colors by passing the theme context to the mapper.
