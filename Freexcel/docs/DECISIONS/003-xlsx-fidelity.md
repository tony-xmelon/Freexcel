# ADR-003: XLSX Fidelity Contract — Model-Based XLSX Re-Save

**Date**: 2026-05-12  
**Status**: Accepted, revised 2026-05-17

## Context

ClosedXML 0.105.0 is used for `.xlsx` I/O. Real-world `.xlsx` files contain features we do not fully support yet (charts, pivot tables, VBA, slicers, external links, theme colors, embedded objects). We need a clear policy on what happens when a user opens such a file and saves it from Freexcel.

The original `XlsxFileAdapter.Save()` implementation created a fresh `XLWorkbook` from the Freexcel model. That lost unknown OOXML package parts when users saved a workbook opened from Excel.

## Decision

- Freexcel uses a model-based XLSX writer for supported workbook content, then preserves source package entries from workbooks opened from `.xlsx` when those entries are not produced by the model writer.
- PivotTables are model-first supported: Freexcel loads pivot-cache and PivotTable metadata, strips pivot parts only from the temporary ClosedXML load copy when needed, and restores native pivot package references on save. Pivot refresh, aggregation, layout editing, slicers, and timelines remain later phases.
- Unsupported or unknown OOXML package parts are retained best-effort on save for workbooks opened from `.xlsx`, including copied package entries, content type declarations, and relationships to copied package targets. Freexcel does not execute or deeply edit those features.
- Freexcel has a native workbook theme model scaffold with `.xlsx` theme-part load/save, loaded-cell-style theme-color resolution, drawing-object theme color references, and chart theme-color rendering from native references. Until the XLSX chart adapters consume that model fully, chart theme and indexed colors may still be mapped incompletely on load.
- Supported features should round-trip faithfully: cell values (all `ScalarValue` subtypes), formulas, cached formula values where available, sheet names, row heights, column widths, basic font/fill/border styles, named ranges, conditional formatting rules we model, data validation rules we model, freeze panes, and merged regions.
- The calc-chain part of `.xlsx` is explicitly ignored on load; we build our own dependency graph from formulas
- Workbook name defaults to "Untitled" on load (not a random filename)

## Rationale

"Do not silently overpromise file fidelity" is the guiding principle. The source-package merge prevents unsupported package assets from being dropped while Freexcel continues to own the supported workbook parts it can model and write.

## Consequences

Users who open complex workbooks and save them from Freexcel should retain unsupported package assets, but Freexcel still cannot guarantee semantic correctness for unsupported XML embedded inside workbook or worksheet parts that the model writer replaces. The UI should keep warning users when unsupported features are detected until the corpus proves each class.

Future fidelity passes should add targeted XML-level merge tests for each unsupported feature class in the corpus, especially workbook/worksheet embedded elements such as slicer, timeline, and table references.
