# Freexcel XLSX Fidelity Contract

**Status:** v1 working contract  
**Last updated:** 2026-05-14

Freexcel currently saves `.xlsx` files from the in-memory workbook model. This means the saved file contains the features Freexcel understands and writes explicitly. It is not a byte-preserving or package-preserving editor for unsupported OOXML parts yet.

## Preserved On XLSX Round-Trip

- Workbook sheets and Excel-compatible sheet names (unique, <=31 chars, no `: \ / ? * [ ]`)
- Cell values: blank, number, text, boolean, date/time, and error values
- Formulas and cached formula values where available, including quoted cross-sheet references Freexcel can parse
- Row heights and column widths
- Hidden sheets, hidden rows/columns, freeze panes, worksheet tab colors
- Basic styles: font weight, font color, fill color, borders, alignment, wrap text, and number format IDs we model
- Named ranges that can be mapped to Freexcel ranges
- Cell-value conditional formatting rules we model
- Data validation rules we model
- Merged regions
- Modeled page layout settings: print area, margins, orientation, paper size, print gridlines/headings, and scale-to-fit
- Modeled worksheet objects: comments, hyperlinks, basic charts, sparklines, text boxes, and basic drawing shapes

## Best-Effort Or Partial

- Conditional formatting beyond modeled rules may be skipped.
- Data validation formulas are preserved only for supported rule shapes.
- Theme and indexed colors may be mapped incorrectly because Freexcel does not currently retain full theme context.
- Formula compatibility depends on the current parser/function library. Unsupported Excel syntax may load as text/formula text but fail Freexcel calculation.

## Not Preserved In v1 Model-Based Save

- VBA macros and VBA projects
- Pivot tables, pivot caches, slicers, and timelines
- Unsupported charts and chart formatting
- Microsoft 365 Share/co-authoring state, cloud permissions, presence, and version history
- External workbook links and linked data model artifacts
- Embedded/OLE objects
- Custom OOXML package parts not represented in `Core.Model`
- Unsupported workbook, worksheet, view, print, protection, and metadata settings

## Explicit Product Exclusions

The following Excel features are not Freexcel parity targets unless a future design document explicitly brings them into scope:

- Microsoft 365 Share/co-authoring, OneDrive/SharePoint permissions, Teams-linked sharing, and live collaborator presence.
- VBA compatibility, macro execution, COM add-ins, and Office Scripts.
- Power Query, Power Pivot, OLAP/data model features, and Microsoft linked data types.
- Enterprise Microsoft 365 controls such as sensitivity labels and IRM.

See [COMMAND_SURFACE_PARITY.md](COMMAND_SURFACE_PARITY.md) for the command-level parity matrix.

## Required Before Claiming Higher Fidelity

- Add a package-preserving save pipeline or source-template save API.
- Add a curated XLSX corpus and report pass/fail per feature class.
- Extend unsupported-feature detection and user warnings as new unsupported OOXML classes are discovered.
- Keep this contract aligned with executable tests in `tests/Freexcel.Core.IO.Tests`.
