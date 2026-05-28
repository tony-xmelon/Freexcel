# Freexcel Tester Release Checklist

Use this checklist before promoting a tester build beyond internal validation. Paste the completed gate summary into the `Tester Release` workflow `release_notes` input when the build is intended as a public-preview candidate.

## Required Release Gate

- Restore, build, and test completed in the release workflow.
- Test result artifact was uploaded, even for failed release-gate attempts.
- Versioned `.exe`, latest `.exe`, versioned MSIX, latest MSIX, and checksum artifacts were uploaded.
- GitHub release was published with the expected tester stream from `release/progress.json`.
- Latest download link was checked from the published release.

## Public-Preview Accessibility Gate

- Keyboard-only smoke validation recorded for workbook open/save, grid navigation/editing, ribbon tab traversal, context menus, dialogs, sheet tabs, and Help.
- Screen-reader smoke validation recorded for first launch, workbook grid focus, formula bar edits, dialog titles/default buttons, warning messages, and accessibility checker results.
- UI Automation catalog review recorded for stable names, automation IDs, invoke patterns, and focus order on newly changed controls.
- Known accessibility issues are listed with affected workflow, severity, and planned follow-up.

## Promotion Decision

- If every accessibility gate item is complete, mark the release notes as public-preview eligible.
- If any accessibility gate item is skipped or incomplete, mark the build as internal-only and do not promote it as a public-preview candidate.

