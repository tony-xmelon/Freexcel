# ADR-003: XLSX Fidelity Contract — Model-Based XLSX Re-Save

**Date**: 2026-05-12  
**Status**: Accepted, revised 2026-05-16

## Context

ClosedXML 0.105.0 is used for `.xlsx` I/O. Real-world `.xlsx` files contain features we do not fully support yet (charts, pivot tables, VBA, slicers, external links, theme colors, embedded objects). We need a clear policy on what happens when a user opens such a file and saves it from Freexcel.

The current `XlsxFileAdapter.Save()` implementation creates a fresh `XLWorkbook` from the Freexcel model. It does not retain the original OOXML package as a template, so unknown package parts cannot be preserved by the current adapter contract.

## Decision

- Freexcel v1 uses model-based XLSX save. It preserves only features represented in `Core.Model` and explicitly written by `XlsxFileAdapter`.
- Unsupported or unknown OOXML parts are not preserved on save in v1. This includes VBA projects, unsupported charts, pivot caches/tables, slicers, external workbook links, embedded objects, and any custom package parts not modeled by Freexcel.
- Freexcel has a native workbook theme model scaffold with `.xlsx` theme-part load/save, loaded-cell-style theme-color resolution, drawing-object theme color references, and chart theme-color rendering from native references. Until the XLSX chart adapters consume that model fully, chart theme and indexed colors may still be mapped incompletely on load.
- Supported features should round-trip faithfully: cell values (all `ScalarValue` subtypes), formulas, cached formula values where available, sheet names, row heights, column widths, basic font/fill/border styles, named ranges, conditional formatting rules we model, data validation rules we model, freeze panes, and merged regions.
- The calc-chain part of `.xlsx` is explicitly ignored on load; we build our own dependency graph from formulas
- Workbook name defaults to "Untitled" on load (not a random filename)

## Rationale

"Do not silently overpromise file fidelity" is the guiding principle for v1. True preservation of unsupported OOXML parts requires either a package-preserving save pipeline or a template-based adapter API that carries the source package through load/edit/save.

## Consequences

Users who open complex workbooks and save them from Freexcel may lose unsupported workbook features. The UI should warn users before saving over `.xlsx` files that contain unsupported features once detection exists.

A future fidelity pass should add a package-preserving save mode for existing `.xlsx` files. That work needs a revised file-session abstraction, because the current `IFileAdapter` interface only accepts a model on save.
