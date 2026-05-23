# Phase 3 ODS Open Support Research

Date: 2026-05-23

## Goal

Evaluate practical `.ods` open support for Freexcel after Phase 1 Open XML/text support and Phase 2 legacy `.xls` support.

## Options Reviewed

### GemBox.Spreadsheet

GemBox.Spreadsheet has the broadest direct spreadsheet format coverage among the reviewed .NET options. Its supported-format documentation lists read/write support for XLSX, XLSB, XLS, ODS, CSV, and TXT, and its API documentation says `ExcelFile.Load` supports `.ods` and `.ots`.

Pros:
- Mature, actively maintained commercial .NET spreadsheet component.
- Direct `.ods` load support without needing to implement ODF XML/package parsing ourselves.
- Also covers `.xlsb`, which is the other difficult Excel format still outstanding.
- Can likely map cells, sheets, basic styles, formulas, and dates more reliably than a hand-rolled reader.

Cons:
- Commercial dependency. Free mode has limitations and is probably not suitable for unrestricted tester builds unless the licensing terms fit our distribution plan.
- Brings a second spreadsheet object model alongside ClosedXML and ExcelDataReader.

Sources:
- https://www.gemboxsoftware.com/spreadsheet/docs/supported-file-formats.html
- https://www.gemboxsoftware.com/spreadsheet/docs/GemBox.Spreadsheet.ExcelFile.html

### AODL / ODF Toolkit .NET

AODL is the historical .NET module of the ODF Toolkit. The Apache OpenOffice wiki describes spreadsheet loading/manipulation as supported but also notes spreadsheet support was “not complete yet.”

Pros:
- Purpose-built around OpenDocument.
- Avoids commercial spreadsheet dependency.

Cons:
- Very old project surface; documentation is from the OpenOffice era.
- Likely requires significant glue code to map ODS content into Freexcel’s workbook model.
- Higher risk for modern .NET, formula, style, and edge-case compatibility.

Sources:
- https://wiki.openoffice.org/wiki/AODL
- https://wiki.openoffice.org/wiki/AODL_FAQ

### NPOI

NPOI is an actively maintained .NET port of Apache POI and is strong for Microsoft Office binary/OOXML formats. Its public project description focuses on Office binary and OOXML formats, not ODS.

Pros:
- Open source and familiar in .NET spreadsheet work.
- Useful for `.xls`/`.xlsx` style work, though Phase 2 already uses ExcelDataReader for `.xls`.

Cons:
- No clear ODS read support in its primary project description.
- Would not solve Phase 3 directly without additional ODF parser work.

Source:
- https://github.com/nissl-lab/npoi

## Recommendation

Do not start `.ods` implementation until we choose a licensing path.

If commercial dependencies are acceptable, use GemBox.Spreadsheet for Phase 3. Scope the first implementation to open-only `.ods`: sheets, scalar cell values, formulas as text where available, dates, booleans, basic number formats, and basic styles. Save should remain `.xlsx` until round-trip fidelity is proven.

If commercial dependencies are not acceptable, defer `.ods` and consider a focused in-house ODS reader only for values/formulas from `content.xml`. That would be lower fidelity but controllable. It should be treated as a separate mini-project with its own fixtures from LibreOffice/Google Sheets exports.

## Suggested Phase 3 Acceptance Criteria

- `.ods` appears in Open but not Save As.
- Opening a LibreOffice-generated `.ods` with multiple sheets preserves sheet names and scalar values.
- Dates and booleans map into Freexcel scalar values.
- Formula text is preserved where ODS exposes it in a usable form.
- Unsupported ODS features do not block opening; they produce a clear best-effort warning if needed.
