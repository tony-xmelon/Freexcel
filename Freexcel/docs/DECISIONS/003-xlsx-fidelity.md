# ADR-003: XLSX Fidelity Contract — Model-Based XLSX Re-Save

**Date**: 2026-05-12  
**Status**: Accepted, revised 2026-05-14

## Context

ClosedXML 0.105.0 is used for `.xlsx` I/O. Real-world `.xlsx` files contain features we do not fully support yet (charts, pivot tables, VBA, slicers, external links, theme colors, embedded objects). We need a clear policy on what happens when a user opens such a file and saves it from Freexcel.

The current `XlsxFileAdapter.Save()` implementation creates a fresh `XLWorkbook` from the Freexcel model. It does not retain the original OOXML package as a template, so unknown package parts cannot be preserved by the current adapter contract.

## Decision

- Freexcel v1 uses model-based XLSX save. It preserves only features represented in `Core.Model` and explicitly written by `XlsxFileAdapter`.
- Unsupported or unknown OOXML parts are not preserved on save in v1. This includes VBA projects, unsupported charts, pivot caches/tables, slicers, external workbook links, embedded objects, and any custom package parts not modeled by Freexcel.
- Theme and indexed colors cannot be resolved to RGB without the workbook theme context, so they are mapped to black on load with a code comment explaining the limitation
- Supported features should round-trip faithfully: cell values (all `ScalarValue` subtypes), formulas, cached formula values where available, sheet names, row heights, column widths, basic font/fill/border styles, named ranges, conditional formatting rules we model, data validation rules we model, freeze panes, and merged regions.
- The calc-chain part of `.xlsx` is explicitly ignored on load; we build our own dependency graph from formulas
- Workbook name defaults to "Untitled" on load (not a random filename)

## Rationale

"Do not silently overpromise file fidelity" is the guiding principle for v1. True preservation of unsupported OOXML parts requires either a package-preserving save pipeline or a template-based adapter API that carries the source package through load/edit/save.

## Consequences

Users who open complex workbooks and save them from Freexcel may lose unsupported workbook features. The UI should warn users before saving over `.xlsx` files that contain unsupported features once detection exists.

A future fidelity pass should add a package-preserving save mode for existing `.xlsx` files. That work needs a revised file-session abstraction, because the current `IFileAdapter` interface only accepts a model on save.
