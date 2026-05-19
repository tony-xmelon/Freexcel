# Keyboard Interaction Parity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring Freexcel keyboard interaction into Excel-for-Windows parity through small red/green batches.

**Architecture:** Put shortcut recognition and edit-mode key intent in small host-level helpers with direct unit tests. Keep `MainWindow` responsible for WPF wiring, command execution, selection changes, dialogs, and viewport refresh.

**Tech Stack:** C#/.NET 10, WPF, xUnit, FluentAssertions.

---

### Task 1: Entry/Edit And Paste Shortcut Batch

**Files:**
- Modify: `src/Freexcel.App.Host/KeyboardShortcutMatcher.cs`
- Create: `src/Freexcel.App.Host/ExcelEditKeyPlanner.cs`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`
- Modify: `tests/Freexcel.App.Host.Tests/KeyboardShortcutMatcherTests.cs`
- Create: `tests/Freexcel.App.Host.Tests/ExcelEditKeyPlannerTests.cs`

- [ ] Write failing tests for `Ctrl+Alt+V`, edit-mode arrow behavior, `Alt+Enter`, `Ctrl+Enter`, `Shift+Enter`, and `Shift+Tab`.
- [ ] Run focused host tests and confirm the new tests fail for missing APIs or wrong behavior.
- [ ] Implement the minimal matcher/planner code.
- [ ] Wire `MainWindow` to open Paste Special for `Ctrl+Alt+V` and use the planner in inline editor/formula bar handlers.
- [ ] Run focused host tests.
- [ ] Commit this batch if it can be isolated from pre-existing dirty changes.

### Task 2: Selection Shortcut Batch

**Files:**
- Modify: `src/Freexcel.App.Host/KeyboardShortcutMatcher.cs`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`
- Modify: `tests/Freexcel.App.Host.Tests/KeyboardShortcutMatcherTests.cs`

- [ ] Add tests for `Ctrl+Shift+Space` and `Ctrl+Shift+*`.
- [ ] Implement whole-sheet/current-region routing.
- [ ] Run focused host tests.
- [ ] Commit the batch.

### Task 3: Remaining Common Shortcut Batch

**Files:**
- Modify: `src/Freexcel.App.Host/KeyboardShortcutMatcher.cs`
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`
- Modify: `docs/SHORTCUT_PARITY_MATRIX.md`
- Modify: host tests for command routing helpers.

- [ ] Add tests and implementations for create table (`Ctrl+L`/`Ctrl+T`), Insert Function (`Shift+F3`), spell check (`F7`), calculation keys (`F9` variants), formula bar expand/collapse (`Ctrl+Shift+U`), Quick Analysis unsupported/disabled behavior (`Ctrl+Q`), and chart shortcuts (`Alt+F1`, `F11`).
- [ ] Update the shortcut matrix as each shortcut becomes implemented, partial, deferred, or excluded.
- [ ] Run focused host tests and commit each independent shortcut family.
