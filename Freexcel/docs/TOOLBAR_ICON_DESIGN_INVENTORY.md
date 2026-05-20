# Freexcel Toolbar Icon Design Inventory

**Date:** 2026-05-20
**Status:** Draft for review before implementation
**Scope:** Titlebar, Quick Access Toolbar, ribbon toolbar commands, backstage commands, sheet-tab/status commands.

This document lists the command wording currently exposed by the Freexcel toolbar surface and proposes a consistent large and small icon treatment for each command. It is intentionally a design approval document; implementation should wait until the list and style rules are accepted.

## Global Icon Direction

Freexcel should use a restrained Excel-like icon family: flat vector symbols, clear silhouettes, modest color accents, and no heavy outlines. The aim is readable and convenient, not decorative.

| Rule | Proposed standard |
|---|---|
| App icon reuse | Use the same FREE/X app icon for executable, window titlebar, taskbar, Alt+Tab, Start Menu shortcut, backstage app identity, splash/loading, About, and any pinned/recent file badges that need the app mark. |
| Large ribbon icons | 40x40 artwork for large stacked ribbon commands such as Paste, Conditional Formatting, Format as Table, PivotTable, charts, Zoom, Help; the surrounding button is taller/wider like Excel. |
| Small ribbon icons | 24x24 artwork for compact horizontal ribbon rows, QAT, menu items, and titlebar commands; align these icons toward the lower text baseline in horizontal icon+label rows, matching Excel. |
| Stroke | 1.5-1.75 px at 24, 2-2.25 px at 40, round caps/joins. Avoid squeezed geometry; icons should preserve aspect ratio and be optically centered. |
| Fill model | Mostly outline icons with one accent fill block where useful. Accent blocks should echo Excel: green for sheet/table/data, blue for insert/navigation, orange/yellow for warning/review, red only for delete/error. |
| Text icons | Font styling commands may remain typographic, but should be drawn in the same icon slot with consistent baseline, size, and weight. |
| Dropdown indicator | Use a shared 8x8 chevron aligned to the right/bottom edge; do not bake chevrons into each icon unless the command itself is a dropdown-only command. |
| Disabled state | Same geometry, 38-45% opacity, no grayscale blur. |

## Draft Icon Graphics

The atlas below is the first-pass graphic direction for review. The current application icon is accepted and should not be redesigned in this pass. The command tables use exact-size PNG previews exported from crisp SVG source icons, so Markdown viewers display the same pixels as the rendered review sheets. The app icon previews are extracted directly from `src/Freexcel.App.Host/Resources/Freexcel.ico`.

The command tables use these base graphics plus small overlays for variants: for example, Save As uses Save plus a star, Delete Note uses Comment plus an X, and Calculate Sheet uses Page plus Refresh. This keeps the system consistent while avoiding one-off glyphs that become too small or misaligned. The editable generator is `assets/command-icons/generate-command-icons.ps1`; `assets/command-icons/render-command-pngs.mjs` exports the PNG previews used by this document.

![Draft Freexcel toolbar icon atlas](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/toolbar-icon-design-atlas.png>)

### Current Application Icon Sizes

These are extracted from the current Freexcel application icon and are included only for reference and reuse. They are not redesign proposals.

| 16 px | 24 px | 32 px | 40 px | 48 px | 256 px |
|---|---|---|---|---|---|
| ![Current Freexcel app icon 16 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-16.png>) | ![Current Freexcel app icon 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-24.png>) | ![Current Freexcel app icon 32 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-32.png>) | ![Current Freexcel app icon 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-40.png>) | ![Current Freexcel app icon 48 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-48.png>) | ![Current Freexcel app icon 256 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-256.png>) |

## Titlebar and App Shell

| Surface | Wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|---|
| App identity | Freexcel | ![Freexcel 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-40.png>) | ![Freexcel 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/app-icon/freexcel-current-24.png>) | Accepted current FREE/X app mark; no redesign in this pass | Same accepted mark simplified at 24 px where needed | Must be the single source used for app, titlebar, taskbar, Start Menu, About, and backstage. |
| QAT | Save | ![Save 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/save.png>) | ![Save 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/save.png>) | Floppy disk with lower label block | Same disk, heavier outer shape | Similar to Excel Save; use white stroke on titlebar. |
| QAT | Undo | ![Undo 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/undo.png>) | ![Undo 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/undo.png>) | Counterclockwise curved arrow | Same arrow | Use a broad arc, not a tiny hook. |
| QAT | Redo | ![Redo 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/redo.png>) | ![Redo 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/redo.png>) | Clockwise curved arrow | Same arrow | Mirror Undo. |
| System | Minimize | ![Minimize 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/minimize.png>) | ![Minimize 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/minimize.png>) | Horizontal line | Same line | Native titlebar scale, white stroke. |
| System | Maximize/Restore | ![Maximize/Restore 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/maximize-restore.png>) | ![Maximize/Restore 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/maximize-restore.png>) | Square, restore uses overlapping squares | Same square/overlap | Toggle state should change icon. |
| System | Close | ![Close 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/close.png>) | ![Close 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/close.png>) | X | Same X | 45-degree strokes, centered. |
| Backstage return | Back to workbook | ![Back to workbook 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/back-to-workbook.png>) | ![Back to workbook 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/back-to-workbook.png>) | Left arrow in circle | Left arrow in circle | Match the existing app glyph and use on the green backstage rail. |

## File / Backstage

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| New | ![New 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/new.png>) | ![New 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/new.png>) | Blank document page | Blank document page | No grid overlay; keep the silhouette clear for document creation. |
| Open | ![Open 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/open.png>) | ![Open 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/open.png>) | Centered taller vertical open folder | Open folder | Plain black outline to match Excel menu glyph style. |
| Save | ![Save 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/save.png>) | ![Save 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/save.png>) | Floppy disk | Floppy disk | Reuse QAT Save geometry. |
| Save As | ![Save As 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/save-as.png>) | ![Save As 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/save-as.png>) | Floppy disk plus top-right star | Floppy plus star | Star indicates creating a new saved copy. |
| Print | ![Print 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/print.png>) | ![Print 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/print.png>) | Printer with sheet | Printer | Reuse Page Layout Print style. |
| Export | ![Export 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/export.png>) | ![Export 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/export.png>) | Document with internal outbound arrow | Arrow inside document | Works for PDF/XPS export without breaking the page silhouette. |
| Close | ![Close 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/close.png>) | ![Close 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/close.png>) | Workbook page with small X | X on document | Red accent only for X. |
| Options | ![Options 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/options.png>) | ![Options 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/options.png>) | Cog wheel | Cog wheel | Use a toothed cog silhouette, not a sunburst. ImageMso reference: ApplicationOptionsDialog. |
| Recent | ![Recent 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/recent.png>) | ![Recent 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/recent.png>) | Clock over document | Document plus clock | Use neutral gray/green. |
| Info | ![Info 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/info.png>) | ![Info 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/info.png>) | Readable circle i | Readable circle i | Keep dot close enough to the stem to read as a single i. |
| Account | ![Account 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/account.png>) | ![Account 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/account.png>) | Person circle | Person | Only if visible in backstage rail. |
| Share | ![Share 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/share.png>) | ![Share 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/share.png>) | Three connected nodes or outbound arrow | Share nodes | Use blue/data accent. |

## Home Tab

### Clipboard

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Paste | ![Paste 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/paste.png>) | ![Paste 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/paste.png>) | Clipboard with paper | Clipboard only | Large icon should use the full 40 px artwork size and feel visually dominant. |
| Cut | ![Cut 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/cut.png>) | ![Cut 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/cut.png>) | Scissors | Scissors | Larger handles, not compressed. |
| Copy | ![Copy 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/copy.png>) | ![Copy 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/copy.png>) | Two overlapping pages | Two pages | Avoid tiny internal lines. |
| Format Painter | ![Format Painter 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/format-painter.png>) | ![Format Painter 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/format-painter.png>) | Broad rectangular stylized brush | Paintbrush | Broad green bristle block with yellow paint accent. ImageMso reference: FormatPainter. |
| Paste Special | ![Paste Special 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/paste-special.png>) | ![Paste Special 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/paste-special.png>) | Clipboard plus small grid/star | Clipboard plus dot | Menu-level variant. |

### Font

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Font Family | N/A | N/A | No icon; dropdown field | No icon | Keep as text control. |
| Font Size | N/A | N/A | No icon; dropdown field | No icon | Keep as text control. |
| Grow Font | ![Grow Font 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/grow-font.png>) | ![Grow Font 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/grow-font.png>) | Large A plus upward arrow | A with up chevron | Optically align A baseline. ImageMso reference: GrowFont. |
| Shrink Font | ![Shrink Font 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/shrink-font.png>) | ![Shrink Font 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/shrink-font.png>) | Large A plus downward arrow | A with down chevron | Mirror Grow Font. ImageMso reference: ShrinkFont. |
| Bold | ![Bold 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/bold.png>) | ![Bold 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/bold.png>) | Bold B | Bold B | Use Segoe UI Semibold/Bold inside icon slot. |
| Italic | ![Italic 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/italic.png>) | ![Italic 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/italic.png>) | Italic I | Italic I | Same baseline as Bold. |
| Underline | ![Underline 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/underline.png>) | ![Underline 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/underline.png>) | U with underline | U underline | Same baseline as Bold. |
| Double Underline | ![Double Underline 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/double-underline.png>) | ![Double Underline 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/double-underline.png>) | U with double underline | U double underline | Menu-level variant. |
| Strikethrough | ![Strikethrough 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/strikethrough.png>) | ![Strikethrough 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/strikethrough.png>) | S with horizontal stroke | S strike | Same baseline as Bold. ImageMso reference: Strikethrough. |
| Borders | ![Borders 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/borders.png>) | ![Borders 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/borders.png>) | 3x3 cell grid with selected border | 3x3 grid | Use black border accent. |
| Border presets | ![Border presets 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/border-presets.png>) | ![Border presets 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/border-presets.png>) | Grid with highlighted edge | Grid edge | Use shared Border base plus edge variant. |
| Fill Color | ![Fill Color 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fill-color.png>) | ![Fill Color 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fill-color.png>) | Paint bucket over color strip | Bucket plus strip | Yellow fill strip like Excel. ImageMso reference: CellFillColorPicker. |
| Font Color | ![Font Color 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/font-color.png>) | ![Font Color 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/font-color.png>) | A over color strip | A plus strip | Red default strip. ImageMso reference: FontColorPicker. |
| Theme Colors | ![Theme Colors 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/theme-colors.png>) | ![Theme Colors 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/theme-colors.png>) | Color swatches grid | Three swatches | Use shared color palette geometry. |

### Alignment

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Top Align | ![Top Align 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/top-align.png>) | ![Top Align 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/top-align.png>) | Lines pinned to top | Top lines | Same line family as other alignment icons. ImageMso reference: AlignTopExcel. |
| Middle Align | ![Middle Align 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/middle-align.png>) | ![Middle Align 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/middle-align.png>) | Lines centered vertically | Middle lines | Use consistent 3-line motif. ImageMso reference: AlignMiddleExcel. |
| Bottom Align | ![Bottom Align 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/bottom-align.png>) | ![Bottom Align 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/bottom-align.png>) | Lines pinned to bottom | Bottom lines | Same canvas height. ImageMso reference: AlignBottomExcel. |
| Align Left | ![Align Left 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/align-left.png>) | ![Align Left 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/align-left.png>) | Lines left aligned | Left lines | Use three horizontal strokes. ImageMso reference: AlignLeft. |
| Center | ![Center 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/center.png>) | ![Center 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/center.png>) | Lines centered | Center lines | Same stroke lengths. ImageMso reference: AlignCenter. |
| Align Right | ![Align Right 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/align-right.png>) | ![Align Right 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/align-right.png>) | Lines right aligned | Right lines | Same stroke lengths. ImageMso reference: AlignRight. |
| Orientation | ![Orientation 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/orientation.png>) | ![Orientation 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/orientation.png>) | Slanted "ab" with diagonal arrow | Slanted ab | Similar to Excel text orientation. |
| Decrease Indent | ![Decrease Indent 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/decrease-indent.png>) | ![Decrease Indent 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/decrease-indent.png>) | Lines with left arrow | Left arrow plus lines | Arrow should not squeeze text lines. |
| Increase Indent | ![Increase Indent 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/increase-indent.png>) | ![Increase Indent 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/increase-indent.png>) | Lines with right arrow | Right arrow plus lines | Mirror Decrease Indent. |
| Wrap Text | ![Wrap Text 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/wrap-text.png>) | ![Wrap Text 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/wrap-text.png>) | Text lines with return arrow | Return arrow over lines | Needs larger, clearer arrow than current. ImageMso reference: WrapText. |
| Merge & Center | ![Merge & Center 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/merge-center.png>) | ![Merge & Center 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/merge-center.png>) | Two cells merging with bidirectional arrows | Merge arrows in grid | Excel-like horizontal arrows across cell boundary. ImageMso reference: AlignCenter. |
| Shrink to Fit | ![Shrink to Fit 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/shrink-to-fit.png>) | ![Shrink to Fit 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/shrink-to-fit.png>) | Text line compressed between inward arrows | Inward arrows | Menu/dialog variant. |
| Distributed/Justify | ![Distributed/Justify 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/distributed-justify.png>) | ![Distributed/Justify 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/distributed-justify.png>) | Equal-width horizontal lines | Justify lines | Dialog/menu variant. |

### Number

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Number Format | N/A | N/A | No icon; dropdown field | No icon | Keep as text control. |
| Accounting/Currency | ![Accounting/Currency 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/accounting-currency.png>) | ![Accounting/Currency 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/accounting-currency.png>) | Currency symbol over cell | Currency symbol | Use selected currency glyph from locale if possible; fallback $. ImageMso reference: AccountingFormat. |
| Percent Style | ![Percent Style 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/percent-style.png>) | ![Percent Style 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/percent-style.png>) | Percent sign | Percent sign | Larger than current. ImageMso reference: ApplyPercentageFormat. |
| Comma Style | ![Comma Style 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/comma-style.png>) | ![Comma Style 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/comma-style.png>) | Comma with number dots | Comma | Avoid tiny punctuation-only look by using a cell hint. ImageMso reference: ApplyCommaFormat. |
| Increase Decimal | ![Increase Decimal 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/increase-decimal.png>) | ![Increase Decimal 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/increase-decimal.png>) | .0 to .00 with right arrow | .0 plus arrow | Make numerals legible. |
| Decrease Decimal | ![Decrease Decimal 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/decrease-decimal.png>) | ![Decrease Decimal 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/decrease-decimal.png>) | .00 to .0 with left arrow | .0 minus arrow | Mirror Increase Decimal. |
| Date/Time formats | ![Date/Time formats 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/date-time-formats.png>) | ![Date/Time formats 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/date-time-formats.png>) | Calendar/clock | Calendar | Menu-level variant. |
| Fraction/Scientific/Text | ![Fraction/Scientific/Text 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fraction-scientific-text.png>) | ![Fraction/Scientific/Text 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fraction-scientific-text.png>) | 1/2, E+, or T in cell | Symbol in cell | Menu-level variants. |

### Styles

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Conditional Formatting | ![Conditional Formatting 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/conditional-formatting.png>) | ![Conditional Formatting 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/conditional-formatting.png>) | Cell grid with colored rule dots | Rule dots in grid | Excel uses colored cells; keep as full-size 40 px color-accent artwork. ImageMso reference: ConditionalFormattingMenu. |
| Format as Table | ![Format as Table 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/format-as-table.png>) | ![Format as Table 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/format-as-table.png>) | Green table with header row | Table grid | Use green header band. ImageMso reference: FormatAsTableGallery. |
| Cell Styles | ![Cell Styles 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/cell-styles.png>) | ![Cell Styles 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/cell-styles.png>) | Cell tile with brush/star | Styled cell | Should differ from Format as Table. ImageMso reference: CellStylesGallery. |

### Cells

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Insert | ![Insert 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/insert.png>) | ![Insert 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/insert.png>) | Grid with plus | Plus in grid | Use green plus. |
| Delete | ![Delete 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/delete.png>) | ![Delete 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/delete.png>) | Grid with X | X in grid | Red X, not full red icon. |
| Format | ![Format 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/format.png>) | ![Format 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/format.png>) | Grid with ruler/gear | Grid plus ruler | Avoid reusing Format Painter. |
| Row Height | ![Row Height 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/row-height.png>) | ![Row Height 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/row-height.png>) | Row with vertical ruler | Row ruler | Menu-level variant. |
| Column Width | ![Column Width 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/column-width.png>) | ![Column Width 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/column-width.png>) | Column with horizontal ruler | Column ruler | Menu-level variant. |
| AutoFit | ![AutoFit 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/autofit.png>) | ![AutoFit 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/autofit.png>) | Cell edges with inward/outward arrows | Fit arrows | Menu-level variant. |
| Hide/Unhide | ![Hide/Unhide 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/hide-unhide.png>) | ![Hide/Unhide 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/hide-unhide.png>) | Grid with eye/hidden slash | Eye/slash | Menu-level variant. |
| Format Cells | ![Format Cells 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/format-cells.png>) | ![Format Cells 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/format-cells.png>) | Dialog rectangle with grid | Small dialog/grid | Ctrl+1 command. |

### Editing

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| AutoSum | ![AutoSum 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/autosum.png>) | ![AutoSum 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/autosum.png>) | Sigma | Sigma | Large sigma should occupy 24 px height. ImageMso reference: AutoSum. |
| Fill | ![Fill 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fill.png>) | ![Fill 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fill.png>) | Down arrow into cells | Arrow into cells | Use for Fill menu. |
| Fill Series | ![Fill Series 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fill-series.png>) | ![Fill Series 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fill-series.png>) | Numbered cells with arrow | Cells plus arrow | Menu-level variant. |
| Flash Fill | ![Flash Fill 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/flash-fill.png>) | ![Flash Fill 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/flash-fill.png>) | Lightning bolt over cells | Lightning bolt | Yellow accent. |
| Clear | ![Clear 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/clear.png>) | ![Clear 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/clear.png>) | Eraser over cell | Eraser | Distinct from Delete. |
| Sort | ![Sort 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/sort.png>) | ![Sort 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/sort.png>) | A/Z with arrow | A/Z arrow | General sort. |
| Sort Ascending | ![Sort Ascending 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/sort-ascending.png>) | ![Sort Ascending 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/sort-ascending.png>) | A over Z with down arrow | A-Z arrow | Use current Excel convention. ImageMso reference: SortAscendingExcel. |
| Sort Descending | ![Sort Descending 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/sort-descending.png>) | ![Sort Descending 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/sort-descending.png>) | Z over A with down arrow | Z-A arrow | Mirror ascending. ImageMso reference: SortDescendingExcel. |
| Filter | ![Filter 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/filter.png>) | ![Filter 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/filter.png>) | Funnel | Funnel | Larger funnel, no compression. ImageMso reference: Filter. |
| Find | ![Find 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/find.png>) | ![Find 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/find.png>) | Magnifying glass | Magnifier | Reuse Search geometry. ImageMso reference: FindDialog. |
| Replace | ![Replace 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/replace.png>) | ![Replace 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/replace.png>) | Magnifier plus circular arrows | Magnifier arrows | Menu/dialog variant. ImageMso reference: ReplaceDialog. |
| Go To | ![Go To 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/go-to.png>) | ![Go To 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/go-to.png>) | Arrow into target cell | Target arrow | Menu/dialog variant. |
| Go To Special | ![Go To Special 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/go-to-special.png>) | ![Go To Special 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/go-to-special.png>) | Target with spark/star | Target star | Menu/dialog variant. |

## Insert Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| PivotTable | ![PivotTable 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/pivottable.png>) | ![PivotTable 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/pivottable.png>) | Grid with pivot arrows and green corner | Pivot grid | Distinct from Table by pivot arrows. |
| Table | ![Table 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/table.png>) | ![Table 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/table.png>) | Green table header grid | Table grid | Reuse Format as Table base where possible. |
| Picture | ![Picture 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/picture.png>) | ![Picture 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/picture.png>) | Landscape image frame | Image frame | Blue sky/green ground accent. |
| Shapes | ![Shapes 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/shapes.png>) | ![Shapes 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/shapes.png>) | Overlapping rectangle/circle/line | Shapes trio | Menu button. |
| Rectangle | ![Rectangle 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/rectangle.png>) | ![Rectangle 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/rectangle.png>) | Rectangle outline | Rectangle | Shape picker item. |
| Ellipse | ![Ellipse 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/ellipse.png>) | ![Ellipse 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/ellipse.png>) | Ellipse outline | Ellipse | Shape picker item. |
| Line | ![Line 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/line.png>) | ![Line 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/line.png>) | Diagonal line | Line | Shape picker item. |
| Column/Bar Chart | ![Column/Bar Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/column-bar-chart.png>) | ![Column/Bar Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/column-bar-chart.png>) | Column chart | Columns | Chart accent palette. |
| Line Chart | ![Line Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/line-chart.png>) | ![Line Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/line-chart.png>) | Line graph with points | Line graph | Chart accent palette. |
| Pie/Doughnut Chart | ![Pie/Doughnut Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/pie-doughnut-chart.png>) | ![Pie/Doughnut Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/pie-doughnut-chart.png>) | Pie circle with slice | Pie slice | Chart accent palette. |
| Scatter/Bubble Chart | ![Scatter/Bubble Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/scatter-bubble-chart.png>) | ![Scatter/Bubble Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/scatter-bubble-chart.png>) | Scatter points | Scatter points | Chart accent palette. |
| Area Chart | ![Area Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/area-chart.png>) | ![Area Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/area-chart.png>) | Filled area graph | Area graph | Chart accent palette. |
| Stock/Radar Chart | ![Stock/Radar Chart 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/stock-radar-chart.png>) | ![Stock/Radar Chart 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/stock-radar-chart.png>) | Financial chart line | Financial graph | Could share Financial icon. |
| Sparklines | ![Sparklines 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/sparklines.png>) | ![Sparklines 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/sparklines.png>) | Tiny line in cell | Sparkline | Reuse line graph but cell-sized. |
| Text Box | ![Text Box 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/text-box.png>) | ![Text Box 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/text-box.png>) | T inside rectangle | T box | Similar to Excel text box. |
| Header & Footer | ![Header & Footer 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/header-footer.png>) | ![Header & Footer 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/header-footer.png>) | Page with top/bottom bands | Page bands | Reuse Page icon family. |
| Symbol | ![Symbol 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/symbol.png>) | ![Symbol 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/symbol.png>) | Omega | Omega | Keep typographic and centered. |
| Hyperlink | ![Hyperlink 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/hyperlink.png>) | ![Hyperlink 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/hyperlink.png>) | Chain link | Chain link | Blue accent. |
| Comment/Note | ![Comment/Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/comment-note.png>) | ![Comment/Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/comment-note.png>) | Speech bubble/note box | Comment bubble | Reuse Review note icon. |

## Draw Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Rectangle | ![Rectangle 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/rectangle.png>) | ![Rectangle 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/rectangle.png>) | Rectangle outline | Rectangle | Same as Insert Shapes. |
| Ellipse | ![Ellipse 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/ellipse.png>) | ![Ellipse 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/ellipse.png>) | Ellipse outline | Ellipse | Same as Insert Shapes. |
| Line | ![Line 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/line.png>) | ![Line 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/line.png>) | Diagonal line | Line | Same as Insert Shapes. |
| Bring Forward | ![Bring Forward 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/bring-forward.png>) | ![Bring Forward 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/bring-forward.png>) | Two overlapping shapes, front arrow up | Front shape arrow | Blue accent. |
| Send Backward | ![Send Backward 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/send-backward.png>) | ![Send Backward 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/send-backward.png>) | Two overlapping shapes, back arrow down | Back shape arrow | Mirror Bring Forward. |
| Size | ![Size 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/size.png>) | ![Size 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/size.png>) | Shape with corner handles | Corner handles | Use ruler accent if needed. |
| Rotate | ![Rotate 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/rotate.png>) | ![Rotate 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/rotate.png>) | Curved rotate arrow around shape | Rotate arrow | Use large arc. |
| Fill Color | ![Fill Color 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fill-color.png>) | ![Fill Color 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fill-color.png>) | Paint bucket over shape | Bucket | Shared fill style. ImageMso reference: CellFillColorPicker. |
| Outline Color | ![Outline Color 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/outline-color.png>) | ![Outline Color 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/outline-color.png>) | Shape outline with pen | Outline pen | Shared border style. |
| Alt Text | ![Alt Text 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/alt-text.png>) | ![Alt Text 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/alt-text.png>) | T lines beside image | Text plus image | Review/accessibility adjacent. |
| Crop | ![Crop 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/crop.png>) | ![Crop 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/crop.png>) | Crop corners over image | Crop corners | Keep if visible in toolbar/menus. |
| Effects | ![Effects 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/effects.png>) | ![Effects 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/effects.png>) | Shape with shadow/spark | Shadow spark | Subtle purple/blue accent, not dominant. |

## Page Layout Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Margins | ![Margins 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/margins.png>) | ![Margins 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/margins.png>) | Page with margin guides | Page margins | Page family. |
| Orientation | ![Orientation 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/orientation.png>) | ![Orientation 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/orientation.png>) | Portrait/landscape pages | Rotated page | Excel-like page rotation. |
| Paper Size | ![Paper Size 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/paper-size.png>) | ![Paper Size 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/paper-size.png>) | Page with size arrows | Page size arrows | Page family. |
| Print Area | ![Print Area 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/print-area.png>) | ![Print Area 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/print-area.png>) | Grid with print boundary | Grid boundary | Dashed print box. |
| Breaks | ![Breaks 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/breaks.png>) | ![Breaks 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/breaks.png>) | Page with dashed break line | Dashed page | Reuse Page Break. |
| Background | ![Background 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/background.png>) | ![Background 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/background.png>) | Image behind grid | Image/grid | Picture accent. |
| Print Titles | ![Print Titles 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/print-titles.png>) | ![Print Titles 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/print-titles.png>) | Page with repeated header row | Header row page | Page/header family. |
| Scale to Fit | ![Scale to Fit 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/scale-to-fit.png>) | ![Scale to Fit 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/scale-to-fit.png>) | Page with diagonal scale arrows | Scale arrows | Reuse Scale icon. |
| Print Gridlines | ![Print Gridlines 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/print-gridlines.png>) | ![Print Gridlines 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/print-gridlines.png>) | Grid plus printer | Grid/printer | Small icon can be grid only with print dot. |
| Print Headings | ![Print Headings 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/print-headings.png>) | ![Print Headings 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/print-headings.png>) | A/1 headers on grid | Headers grid | Keep letters/numbers legible. |
| Themes | ![Themes 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/themes.png>) | ![Themes 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/themes.png>) | Color palette with page | Palette/page | Theme accent. |
| Colors | ![Colors 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/colors.png>) | ![Colors 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/colors.png>) | Swatch grid | Swatches | Reuse color system. |
| Fonts | ![Fonts 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/fonts.png>) | ![Fonts 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/fonts.png>) | A with theme mark | A/theme | Typography icon. |
| Effects | ![Effects 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/effects.png>) | ![Effects 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/effects.png>) | Spark/shadow shape | Effects shape | Same as Draw effects. |
| Header/Footer | ![Header/Footer 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/header-footer.png>) | ![Header/Footer 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/header-footer.png>) | Page with top/bottom bands | Page bands | Shared with Insert. |
| Page Setup | ![Page Setup 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/page-setup.png>) | ![Page Setup 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/page-setup.png>) | Page with gear | Page gear | Dialog command. |
| Center on page | ![Center on page 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/center-on-page.png>) | ![Center on page 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/center-on-page.png>) | Page with centered grid | Centered grid | Dialog/menu variant. ImageMso reference: AlignCenter. |
| Page Order | ![Page Order 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/page-order.png>) | ![Page Order 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/page-order.png>) | Two pages with order arrow | Page arrow | Dialog/menu variant. |

## Formulas Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Insert Function | ![Insert Function 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/insert-function.png>) | ![Insert Function 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/insert-function.png>) | fx in cell or circle | fx | Should be clear and larger than current. ImageMso reference: FunctionWizard. |
| AutoSum | ![AutoSum 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/autosum.png>) | ![AutoSum 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/autosum.png>) | Sigma | Sigma | Reuse Home AutoSum. ImageMso reference: AutoSum. |
| Logical | ![Logical 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/logical.png>) | ![Logical 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/logical.png>) | TRUE/FALSE blocks | T/F blocks | Function category. |
| Text | ![Text 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/text.png>) | ![Text 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/text.png>) | T with quote marks | T quotes | Function category. |
| Date & Time | ![Date & Time 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/date-time.png>) | ![Date & Time 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/date-time.png>) | Calendar plus clock | Calendar/clock | Function category. |
| Lookup & Reference | ![Lookup & Reference 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/lookup-reference.png>) | ![Lookup & Reference 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/lookup-reference.png>) | Magnifier over table | Magnifier/table | Function category. |
| Math & Trig | ![Math & Trig 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/math-trig.png>) | ![Math & Trig 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/math-trig.png>) | Radical/pi/sigma | Math symbol | Function category. |
| More Functions | ![More Functions 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/more-functions.png>) | ![More Functions 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/more-functions.png>) | Ellipsis with fx | fx ellipsis | Function category. |
| Financial | ![Financial 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/financial.png>) | ![Financial 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/financial.png>) | Currency graph | Currency graph | Function category. |
| Name Manager | ![Name Manager 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/name-manager.png>) | ![Name Manager 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/name-manager.png>) | Label list | Label/list | Defined names group. |
| Define Name | ![Define Name 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/define-name.png>) | ![Define Name 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/define-name.png>) | Tag label with plus | Tag plus | Defined names group. |
| Use in Formula | ![Use in Formula 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/use-in-formula.png>) | ![Use in Formula 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/use-in-formula.png>) | Tag inserted into formula | Tag/fx | Defined names group. |
| Create from Selection | ![Create from Selection 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/create-from-selection.png>) | ![Create from Selection 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/create-from-selection.png>) | Grid to labels | Grid labels | Defined names group. |
| Trace Precedents | ![Trace Precedents 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/trace-precedents.png>) | ![Trace Precedents 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/trace-precedents.png>) | Arrow from left cells to active cell | Incoming arrows | Formula auditing. |
| Trace Dependents | ![Trace Dependents 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/trace-dependents.png>) | ![Trace Dependents 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/trace-dependents.png>) | Arrow from active cell to right cells | Outgoing arrows | Formula auditing. |
| Remove Arrows | ![Remove Arrows 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/remove-arrows.png>) | ![Remove Arrows 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/remove-arrows.png>) | Formula arrows with X | Arrow X | Red X accent. |
| Show Formulas | ![Show Formulas 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/show-formulas.png>) | ![Show Formulas 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/show-formulas.png>) | Cell with =A1 | =A1 cell | Should be legible at 16. |
| Error Checking | ![Error Checking 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/error-checking.png>) | ![Error Checking 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/error-checking.png>) | Warning triangle over formula | Warning triangle | Yellow accent. ImageMso reference: ErrorChecking. |
| Evaluate Formula | ![Evaluate Formula 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/evaluate-formula.png>) | ![Evaluate Formula 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/evaluate-formula.png>) | fx with step arrow | fx step | Debug/evaluate. |
| Watch Window | ![Watch Window 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/watch-window.png>) | ![Watch Window 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/watch-window.png>) | Eye/watch over cell | Eye/cell | Do not use tiny clock only. |
| R1C1 Reference Style | ![R1C1 Reference Style 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/r1c1-reference-style.png>) | ![R1C1 Reference Style 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/r1c1-reference-style.png>) | R1C1 in grid | R1C1 cell | Text must be simplified for small. |
| Calculation Options | ![Calculation Options 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/calculation-options.png>) | ![Calculation Options 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/calculation-options.png>) | Gear plus calculator/fx | Gear/fx | Dropdown. ImageMso reference: ApplicationOptionsDialog. |
| Calculate Now | ![Calculate Now 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/calculate-now.png>) | ![Calculate Now 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/calculate-now.png>) | Refresh arrows over fx | Refresh/fx | Reuse Refresh motif. ImageMso reference: CalculateNow. |
| Calculate Sheet | ![Calculate Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/calculate-sheet.png>) | ![Calculate Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/calculate-sheet.png>) | Sheet with refresh arrows | Sheet refresh | Distinct from Calculate Now. ImageMso reference: CalculateNow. |

## Data Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Get Data | ![Get Data 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/get-data.png>) | ![Get Data 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/get-data.png>) | Database cylinder into grid | Database arrow | Green/data accent. ImageMso reference: GetExternalDataFromText. |
| Refresh All | ![Refresh All 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/refresh-all.png>) | ![Refresh All 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/refresh-all.png>) | Circular arrows | Refresh arrows | Larger, open circle. ImageMso reference: RefreshAll. |
| Sort | ![Sort 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/sort.png>) | ![Sort 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/sort.png>) | A/Z with arrow | A/Z arrow | Shared Home Editing sort. |
| Filter | ![Filter 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/filter.png>) | ![Filter 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/filter.png>) | Funnel | Funnel | Shared Home Editing filter. ImageMso reference: Filter. |
| Advanced Filter | ![Advanced Filter 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/advanced-filter.png>) | ![Advanced Filter 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/advanced-filter.png>) | Funnel with gear/sliders | Funnel gear | Data-specific variant. ImageMso reference: Filter. |
| Text to Columns | ![Text to Columns 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/text-to-columns.png>) | ![Text to Columns 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/text-to-columns.png>) | Text lines splitting into columns | Split columns | Needs strong column separation. |
| Remove Duplicates | ![Remove Duplicates 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/remove-duplicates.png>) | ![Remove Duplicates 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/remove-duplicates.png>) | Duplicate rows with X | Rows X | Red X accent. |
| Data Validation | ![Data Validation 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/data-validation.png>) | ![Data Validation 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/data-validation.png>) | Cell with checkmark | Check cell | Green check. |
| Consolidate | ![Consolidate 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/consolidate.png>) | ![Consolidate 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/consolidate.png>) | Multiple grids into one | Merge grids | Data accent. |
| Goal Seek | ![Goal Seek 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/goal-seek.png>) | ![Goal Seek 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/goal-seek.png>) | Target with arrow | Target arrow | What-if group. |
| Scenario Manager | ![Scenario Manager 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/scenario-manager.png>) | ![Scenario Manager 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/scenario-manager.png>) | Stacked cards/table | Scenario cards | What-if group. |
| Data Table | ![Data Table 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/data-table.png>) | ![Data Table 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/data-table.png>) | Grid with variable markers | Variable grid | What-if group. |
| Forecast Sheet | ![Forecast Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/forecast-sheet.png>) | ![Forecast Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/forecast-sheet.png>) | Line chart with future dotted line | Forecast line | Chart/data accent. |
| Subtotal | ![Subtotal 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/subtotal.png>) | ![Subtotal 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/subtotal.png>) | Sigma in grouped rows | Sigma rows | Data outline. |
| Group | ![Group 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/group.png>) | ![Group 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/group.png>) | Bracket plus rows | Group bracket | Outline group. |
| Ungroup | ![Ungroup 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/ungroup.png>) | ![Ungroup 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/ungroup.png>) | Bracket minus rows | Ungroup bracket | Outline group. |
| Show Detail | ![Show Detail 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/show-detail.png>) | ![Show Detail 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/show-detail.png>) | Plus in outline bracket | Plus bracket | Excel outline convention. |
| Hide Detail | ![Hide Detail 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/hide-detail.png>) | ![Hide Detail 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/hide-detail.png>) | Minus in outline bracket | Minus bracket | Excel outline convention. |
| Flash Fill | ![Flash Fill 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/flash-fill.png>) | ![Flash Fill 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/flash-fill.png>) | Lightning over cells | Lightning | Shared Home Editing flash. |
| Analyze Data | ![Analyze Data 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/analyze-data.png>) | ![Analyze Data 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/analyze-data.png>) | Chart plus sparkle | Chart sparkle | Data insight command. |

## Review Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Spell Check | ![Spell Check 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/spell-check.png>) | ![Spell Check 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/spell-check.png>) | ABC with checkmark | ABC check | Yellow/green review accent. |
| Accessibility Checker | ![Accessibility Checker 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/accessibility-checker.png>) | ![Accessibility Checker 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/accessibility-checker.png>) | Person/check in circle | Accessibility check | Excel-like accessibility person. ImageMso reference: AccessibilityChecker. |
| New Note | ![New Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/new-note.png>) | ![New Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/new-note.png>) | Note bubble with plus | Bubble plus | Use yellow note fill. |
| Edit Note | ![Edit Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/edit-note.png>) | ![Edit Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/edit-note.png>) | Note bubble with pencil | Bubble pencil | Note family. |
| Delete Note | ![Delete Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/delete-note.png>) | ![Delete Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/delete-note.png>) | Note bubble with X | Bubble X | Red X accent. |
| Previous Note | ![Previous Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/previous-note.png>) | ![Previous Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/previous-note.png>) | Note bubble with left arrow | Bubble left | Navigation pair. |
| Next Note | ![Next Note 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/next-note.png>) | ![Next Note 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/next-note.png>) | Note bubble with right arrow | Bubble right | Navigation pair. |
| Show Notes | ![Show Notes 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/show-notes.png>) | ![Show Notes 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/show-notes.png>) | Note list | Note list | List of bubbles. |
| Protect Sheet | ![Protect Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/protect-sheet.png>) | ![Protect Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/protect-sheet.png>) | Sheet with lock | Sheet lock | Protect accent. ImageMso reference: SheetProtect. |
| Protect Workbook | ![Protect Workbook 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/protect-workbook.png>) | ![Protect Workbook 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/protect-workbook.png>) | Workbook with lock | Workbook lock | Protect accent. ImageMso reference: SheetProtect. |
| Allow Edit Ranges | ![Allow Edit Ranges 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/allow-edit-ranges.png>) | ![Allow Edit Ranges 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/allow-edit-ranges.png>) | Unlocked cells with pencil | Unlock/pencil | Protect group. |
| Share | ![Share 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/share.png>) | ![Share 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/share.png>) | Share nodes/outbound arrow | Share nodes | Reuse File Share. |
| Statistics | ![Statistics 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/statistics.png>) | ![Statistics 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/statistics.png>) | Small bar chart | Bar chart | Neutral/chart accent. |

## View Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Normal | ![Normal 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/normal.png>) | ![Normal 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/normal.png>) | Grid worksheet | Grid | View mode. |
| Page Break Preview | ![Page Break Preview 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/page-break-preview.png>) | ![Page Break Preview 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/page-break-preview.png>) | Grid with blue dashed breaks | Dashed grid | View mode. |
| Page Layout | ![Page Layout 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/page-layout.png>) | ![Page Layout 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/page-layout.png>) | Page with worksheet | Page/grid | View mode. |
| Custom Views | ![Custom Views 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/custom-views.png>) | ![Custom Views 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/custom-views.png>) | Eye over page/grid | Eye grid | View mode. |
| Gridlines | ![Gridlines 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/gridlines.png>) | ![Gridlines 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/gridlines.png>) | Grid lines checkbox | Grid | CheckBox may keep text plus optional icon. |
| Headings | ![Headings 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/headings.png>) | ![Headings 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/headings.png>) | A/1 headers | Header grid | CheckBox may keep text plus optional icon. |
| Ruler | ![Ruler 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/ruler.png>) | ![Ruler 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/ruler.png>) | Ruler | Ruler | CheckBox may keep text plus optional icon. |
| Formula Bar | ![Formula Bar 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/formula-bar.png>) | ![Formula Bar 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/formula-bar.png>) | fx bar | fx bar | CheckBox may keep text plus optional icon. |
| Freeze Panes | ![Freeze Panes 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/freeze-panes.png>) | ![Freeze Panes 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/freeze-panes.png>) | Grid with frozen top/left bands | Frozen grid | Use blue/gray frozen bands. |
| Split | ![Split 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/split.png>) | ![Split 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/split.png>) | Grid split into panes | Split grid | Distinct from Freeze. |
| Zoom | ![Zoom 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom.png>) | ![Zoom 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom.png>) | Magnifying glass with plus | Magnifier plus | Shared status zoom. ImageMso reference: ZoomDialog. |
| Zoom Out | ![Zoom Out 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-out.png>) | ![Zoom Out 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-out.png>) | Magnifying glass minus | Magnifier minus | Status/ribbon variant. ImageMso reference: ZoomDialog. |
| Zoom to 100% | ![Zoom to 100% 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-to-100.png>) | ![Zoom to 100% 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-to-100.png>) | 100% in magnifier | 100% | Keep text legible. ImageMso reference: ZoomDialog. |
| Zoom In | ![Zoom In 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-in.png>) | ![Zoom In 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-in.png>) | Magnifying glass plus | Magnifier plus | Status/ribbon variant. ImageMso reference: ZoomDialog. |
| Zoom to Selection | ![Zoom to Selection 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-to-selection.png>) | ![Zoom to Selection 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-to-selection.png>) | Magnifier over selected cell range | Magnifier/range | Use dashed selection box. ImageMso reference: ZoomDialog. |
| New Window | ![New Window 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/new-window.png>) | ![New Window 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/new-window.png>) | Window plus | Window plus | Multi-window deferred but design ready. |
| Arrange All | ![Arrange All 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/arrange-all.png>) | ![Arrange All 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/arrange-all.png>) | Tiled windows | Tiled windows | View window group. |
| View Side by Side | ![View Side by Side 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/view-side-by-side.png>) | ![View Side by Side 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/view-side-by-side.png>) | Two windows side by side | Two windows | View window group. |
| Synchronous Scrolling | ![Synchronous Scrolling 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/synchronous-scrolling.png>) | ![Synchronous Scrolling 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/synchronous-scrolling.png>) | Two windows with linked arrows | Linked arrows | View window group. |
| Reset Window Position | ![Reset Window Position 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/reset-window-position.png>) | ![Reset Window Position 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/reset-window-position.png>) | Two windows with reset arrow | Reset windows | View window group. |
| Switch Windows | ![Switch Windows 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/switch-windows.png>) | ![Switch Windows 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/switch-windows.png>) | Overlapping windows | Windows | View window group. |

## Help Tab

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Help | ![Help 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/help.png>) | ![Help 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/help.png>) | Question mark in circle | Question circle | Help accent. ImageMso reference: Help. |
| Send Feedback | ![Send Feedback 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/send-feedback.png>) | ![Send Feedback 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/send-feedback.png>) | Speech bubble with heart/dot | Feedback bubble | Keep simple, no emoji. |
| About | ![About 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/about.png>) | ![About 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/about.png>) | Circle i with app mark hint | Circle i | About should also show the app icon nearby. |

## Sheet Tabs and Status Bar

| Command wording | Large preview | Small preview | Large icon | Small icon | Notes |
|---|---|---|---|---|---|
| Previous sheet tab | ![Previous sheet tab 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/previous-sheet-tab.png>) | ![Previous sheet tab 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/previous-sheet-tab.png>) | Left chevron | Left chevron | Only show when needed; align left of visible tabs. |
| Next sheet tab | ![Next sheet tab 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/next-sheet-tab.png>) | ![Next sheet tab 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/next-sheet-tab.png>) | Right chevron | Right chevron | Only show when needed; align right of visible tabs. |
| Add Sheet | ![Add Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/add-sheet.png>) | ![Add Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/add-sheet.png>) | Plus in tab shape | Plus | Use 18-24 px button. |
| Rename Sheet | ![Rename Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/rename-sheet.png>) | ![Rename Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/rename-sheet.png>) | Tab with pencil | Pencil/tab | Context menu. |
| Insert Sheet | ![Insert Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/insert-sheet.png>) | ![Insert Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/insert-sheet.png>) | Tab plus | Tab plus | Context menu. |
| Duplicate Sheet | ![Duplicate Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/duplicate-sheet.png>) | ![Duplicate Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/duplicate-sheet.png>) | Two tabs | Two tabs | Context menu. |
| Delete Sheet | ![Delete Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/delete-sheet.png>) | ![Delete Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/delete-sheet.png>) | Tab with X | Tab X | Context menu. |
| Hide Sheet | ![Hide Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/hide-sheet.png>) | ![Hide Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/hide-sheet.png>) | Tab with eye slash | Eye slash/tab | Context menu. |
| Unhide Sheet | ![Unhide Sheet 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/unhide-sheet.png>) | ![Unhide Sheet 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/unhide-sheet.png>) | Tab with eye | Eye/tab | Context menu. |
| Tab Color | ![Tab Color 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/tab-color.png>) | ![Tab Color 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/tab-color.png>) | Tab with color swatch | Swatch/tab | Context menu. |
| Select All Sheets | ![Select All Sheets 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/select-all-sheets.png>) | ![Select All Sheets 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/select-all-sheets.png>) | Stacked tabs with check | Tabs check | Context menu. |
| Ungroup Sheets | ![Ungroup Sheets 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/ungroup-sheets.png>) | ![Ungroup Sheets 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/ungroup-sheets.png>) | Stacked tabs separated | Tabs ungroup | Context menu. |
| Move Left | ![Move Left 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/move-left.png>) | ![Move Left 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/move-left.png>) | Tab with left arrow | Left arrow/tab | Context menu. |
| Move Right | ![Move Right 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/move-right.png>) | ![Move Right 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/move-right.png>) | Tab with right arrow | Right arrow/tab | Context menu. |
| Zoom Out | ![Zoom Out 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-out.png>) | ![Zoom Out 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-out.png>) | Minus | Minus | Status bar, align to slider. ImageMso reference: ZoomDialog. |
| Zoom In | ![Zoom In 40 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/40/zoom-in.png>) | ![Zoom In 24 px](</E:/Users/anton/Documents/Claude/Freexcel/docs/assets/command-icons/24/zoom-in.png>) | Plus | Plus | Status bar, align to slider. ImageMso reference: ZoomDialog. |
| Zoom Slider | N/A | N/A | Thumb on track | N/A | Keep native slider, no custom icon needed. |

## Implementation Notes After Approval

1. Create a single icon catalog where every command maps to one `RibbonCommandIconKind` and optional accent.
2. Replace remaining text-only toolbar glyphs with `RibbonIcon` except controls that should remain textual fields, such as font name, font size, number format, and zoom percentage.
3. Normalize slot sizes before redrawing geometry: small icons should render as 24x24 artwork, large icons as 40x40 artwork, with larger button hit areas and Excel-like bottom alignment for compact icon+label rows.
4. Redraw the small icons separately where needed instead of scaling down large icons mechanically; this should fix the current squashed look.
5. Add screenshot verification for Home plus at least one secondary tab at both normal and narrow widths.




























