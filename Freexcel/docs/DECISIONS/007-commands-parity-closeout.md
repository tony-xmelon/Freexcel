# ADR-007: Commands Parity Closeout Boundaries

**Date**: 2026-05-19
**Status**: Accepted

## Context

Freexcel tracks visible Excel commands and many rows have reached Partial status. Some partial rows are small interaction
gaps over an existing model, while others require substantial renderers, package writers, locale engines, or proprietary
heuristics.

## Decision

Move model-backed command gaps to Implemented when they are undoable, tested, and visible in the UI. Keep advanced chart
families Deferred until each family has a dedicated data model, renderer, and package writer. Keep full locale/accounting
fidelity and full native PDF export Partial while documenting the invariant/accounting subset and the XPS-backed PDF
fallback.

## Consequences

- Command parity is test-backed instead of checklist-driven.
- Clipboard, paste, Format Painter, alignment, AutoFit, Format Cells, and supported Flash Fill behavior can be presented
  as implemented where the model and UI genuinely support them.
- Advanced chart XML can be recognized without exposing non-working authoring commands or fallback rendering.
- Full Excel locale matching, native PDF option parity, and lossless advanced chart package writing remain outside this
  closeout.
