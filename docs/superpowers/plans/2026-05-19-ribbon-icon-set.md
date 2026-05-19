# Ribbon Icon Set Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every ribbon/menu tab a consistent, Excel-like icon system with aligned large, small, and compact command glyphs.

**Architecture:** Add a runtime ribbon icon catalog/decorator that maps command titles to glyphs and decorates text-only ribbon buttons across all tabs. Keep command handlers and existing layout intact. Add shared XAML styles for icon sizing and use targeted Home-tab cleanup where icons already exist but need consistent alignment.

**Tech Stack:** WPF XAML, C# code-behind/helper classes, xUnit source hygiene tests.

---

### Task 1: Add Source Guards

**Files:**
- Modify: `tests/Freexcel.App.Host.Tests/MainWindowSourceHygieneTests.cs`

- [ ] Add tests that require a ribbon icon catalog/decorator.
- [ ] Guard for representative command mappings across Home, Insert, Draw, Page Layout, Formulas, Data, Review, View, PivotTable, and Help.
- [ ] Guard that `MainWindow` applies the decorator after ribbon visual tree creation.

### Task 2: Add Shared Icon System

**Files:**
- Create: `src/Freexcel.App.Host/RibbonIconCatalog.cs`
- Create: `src/Freexcel.App.Host/RibbonIconDecorator.cs`
- Modify: `src/Freexcel.App.Host/Resources/IconResources.xaml`

- [ ] Define command icon records with glyph, category, and accent metadata.
- [ ] Add size/typography styles for large, small, and color-swatch icon content.
- [ ] Decorate string-content ribbon buttons into consistent icon+label content.

### Task 3: Wire Ribbon Decoration

**Files:**
- Modify: `src/Freexcel.App.Host/MainWindow.xaml.cs`

- [ ] Apply the decorator on load and after ribbon tab selection/layout refresh.
- [ ] Keep existing click handlers, context menus, tooltips, and key tips unchanged.

### Task 4: Verify And Review Visually

- [ ] Run source hygiene tests.
- [ ] Build the app host.
- [ ] Launch the app, capture representative screenshots from several tabs, and iterate until the new icons are visible and aligned.
