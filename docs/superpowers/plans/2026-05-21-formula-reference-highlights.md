# Formula Reference Highlights Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Excel-style colored formula reference text and grid range highlights while editing formulas.

**Architecture:** Build a pure `FormulaReferenceHighlightPlanner` that returns spans and ranges, then wire those results into WPF overlays owned by `MainWindow.Editing.cs`. Keep the current `TextBox` editors as the behavioral source of truth and make the highlight layers disposable UI.

**Tech Stack:** C# 13, WPF, xUnit, FluentAssertions, existing Freexcel App.Host/App.UI projects.

---

### Task 1: Reference Highlight Planner

**Files:**
- Create: `Freexcel/src/Freexcel.App.Host/FormulaReferenceHighlightPlanner.cs`
- Test: `Freexcel/tests/Freexcel.App.Host.Tests/FormulaReferenceHighlightPlannerTests.cs`

- [ ] **Step 1: Write failing planner tests**

Add tests for `=SUM(A1:B2,C3)`, `$A$1`, `Sheet2!B4`, quoted sheet names, and `"A1"` inside string literals.

- [ ] **Step 2: Run tests to verify failure**

Run: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter FormulaReferenceHighlightPlannerTests -m:1 /nodeReuse:false -p:UseSharedCompilation=false`

Expected: compile failure because the planner type does not exist.

- [ ] **Step 3: Implement planner**

Implement records for reference highlights and a scanner that returns text span start/length, palette index, display text, sheet name if present, and same-sheet `GridRange?`.

- [ ] **Step 4: Run tests to verify pass**

Run the same filtered test command.

Expected: all planner tests pass.

### Task 2: Grid Highlight Overlay

**Files:**
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.xaml.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.Editing.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.Viewport.cs`

- [ ] **Step 1: Add failing host-facing test where practical**

Add planner-backed tests for visible same-sheet ranges and skipped cross-sheet ranges if UI geometry can stay pure. If geometry is too coupled to WPF controls, rely on build plus manual app verification for this task.

- [ ] **Step 2: Implement overlay lifecycle**

Add fields for reference highlight elements, recompute on editor changes, draw colored borders/fills on `EditOverlay`, refresh after viewport changes, and clear on commit/cancel/non-formula state.

- [ ] **Step 3: Run focused tests**

Run planner tests and existing formula range entry tests.

### Task 3: Formula Text Highlight Overlay

**Files:**
- Create: `Freexcel/src/Freexcel.App.Host/FormulaReferenceTextOverlay.cs`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.xaml`
- Modify: `Freexcel/src/Freexcel.App.Host/MainWindow.Editing.cs`

- [ ] **Step 1: Implement formula bar overlay**

Wrap the formula bar in a grid, add a transparent hit-test-free text overlay, and keep the TextBox as the real editor.

- [ ] **Step 2: Implement inline editor overlay**

Create and position a matching overlay beside the inline editor, using the same font, padding, size, and highlight spans.

- [ ] **Step 3: Verify visually**

Run the app and test editing formulas with multiple references, mouse range selection, drag selection, and Shift+arrow selection.

### Task 4: Final Verification And Merge Prep

**Files:**
- All changed files

- [ ] **Step 1: Run focused tests**

Run: `dotnet test Freexcel\tests\Freexcel.App.Host.Tests\Freexcel.App.Host.Tests.csproj --filter "FormulaReferenceHighlightPlannerTests|FormulaRangeEntryPlannerTests|ExcelEditKeyPlannerTests" -m:1 /nodeReuse:false -p:UseSharedCompilation=false`

- [ ] **Step 2: Run app build**

Run: `dotnet build Freexcel\src\Freexcel.App.Host\Freexcel.App.Host.csproj -m:1 /nodeReuse:false -p:UseSharedCompilation=false`

- [ ] **Step 3: Manual app smoke test**

Run the app and verify formula references are colored in the formula bar and inline editor, matching grid highlights, while commit/cancel still works.

- [ ] **Step 4: Commit**

Commit the implementation as `feat: highlight formula references while editing`.
