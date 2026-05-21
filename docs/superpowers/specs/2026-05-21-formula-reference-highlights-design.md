# Formula Reference Highlights Design

## Goal

Mimic Excel's formula-edit reference highlighting while preserving the current TextBox-based formula bar and inline cell editor.

## Excel Behavior

While editing a formula, Excel assigns each cell or range reference a color. The same color is applied to the reference text in the formula and to the referenced range on the worksheet. Highlights update as the formula text changes, as the user clicks or drags ranges, and as keyboard range selection changes. They clear when editing is committed or canceled.

## Chosen Approach

Use a lightweight highlight layer around the existing editors instead of replacing them with RichTextBox. This keeps current caret movement, F4 reference cycling, formula range entry, commit/cancel, and keyboard navigation intact.

The implementation has three pieces:

1. A pure planner that scans formula text and returns reference text spans plus same-sheet grid ranges.
2. A grid overlay rendered on `EditOverlay` for the referenced ranges.
3. Text highlight overlays for the formula bar and inline editor, fed by the same planner.

## Scope

The first pass supports normal A1 references, absolute references, ranges, and sheet-qualified references. Same-sheet references draw grid highlights. Cross-sheet references color formula text but do not draw a grid highlight unless the referenced sheet is active. String literals are ignored so text like `"A1"` does not become a highlight.

R1C1 formulas remain compatible with formula entry, but colored reference detection starts with A1 syntax because existing displayed formulas are converted for the formula bar and the current lexer/parser is A1-first. R1C1 coloring can be added behind the same planner interface later.

## UX Details

The palette cycles through Excel-like colors: blue, red, purple, green, orange, teal. Grid highlights use a border plus a faint fill. Formula text highlights use the same foreground color for reference spans while leaving other formula text in the normal editor color.

Highlights refresh on:

- entering inline edit or focusing the formula bar for formula editing
- editor `TextChanged`
- range selection through mouse, drag, or keyboard
- viewport changes while editing
- commit, cancel, focus exit, and sheet changes

## Testing

Planner tests cover reference extraction, ranges, absolute references, sheet-qualified references, color assignment, string-literal exclusion, and graceful handling of malformed formulas. UI integration is verified through build plus manual app testing because caret/text overlay alignment is visual and interaction-sensitive.
