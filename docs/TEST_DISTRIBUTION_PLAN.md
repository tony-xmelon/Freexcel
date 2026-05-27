# Freexcel Test Distribution Plan

## Phase Status

| Phase | Status | Scope |
| --- | --- | --- |
| 1. Shareable builds | Complete | Framework-dependent user-test builds publish into `artifacts/releases` with version, timestamp, commit, runtime, and mode in the file name. |
| 2. Feedback intake | Complete | User testing findings are tracked in `docs/USER_TESTING_REPORT_2026-05-24.md`; GitHub issues now include a structured user-test report template. |
| 3. Local diagnostics | Complete | Test builds record local JSONL usage events and crash reports under `%LOCALAPPDATA%\Freexcel\Diagnostics`. No network upload is performed. |
| 4. Hosted release channel | Complete | GitHub Actions publishes latest builds through GitHub Releases with versioned artifacts, a stable latest test build link, and an unsigned local MSIX package for packaging validation. |
| 5. Crash analytics | Complete | Opt-in Sentry crash upload is wired behind tester consent and `FREEXCEL_SENTRY_DSN`; local diagnostics remain available without network upload. |
| 6. Lightweight usage analytics | Complete | Stabilization-only app usage events are recorded through the existing diagnostics pipeline and safe crash breadcrumbs. |
| 7. Auto-update readiness | Complete | Help now exposes the stable latest release page while full in-app update packaging remains deferred. |

## Phase 4 Release Channel

Latest tester download:

https://github.com/tony-xmelon/Freexcel/releases/latest/download/Freexcel-latest-win-x64.exe

The `Tester Release` GitHub Actions workflow runs restore, build, and test before publishing a framework-dependent single-file Windows x64 `.exe` plus an unsigned local MSIX package. It uploads both versioned artifacts produced by `tools/Publish-UserTestBuild.ps1` and stable latest assets:

- `Freexcel-latest-win-x64.exe`
- `Freexcel-latest-win-x64.msix`

The MSIX package is for local packaging validation. Signing, installer trust validation, and Store-style submission remain release-gate work.

Default tester versions come from `release/progress.json`: the current `overallCompletion` value maps to a minor-version band, and the GitHub run number becomes the patch number. At 93% completion, default tester releases use the `v0.6.<run>` stream. Manual `release_version` overrides remain available for special validation builds.

Current release gate: do not treat a new tester release as available until the workflow completes successfully through restore, build, test, release metadata, artifact upload, and GitHub release publication.

## Phase 3 Diagnostics Contract

Freexcel writes tester diagnostics locally only. Files stay on the tester machine unless the tester attaches them to an issue.

- `events.jsonl` records app lifecycle events such as `app_start`, `app_ready`, `app_exit`, and `crash`.
- `CrashReports/*.json` records unhandled WPF dispatcher, AppDomain, and unobserved task exceptions.
- Crash exception messages and stack traces can occasionally contain sensitive values; review files before attaching them to an issue.
- Event properties are allowlisted so workbook paths and workbook contents are not written as analytics properties.
- Set `FREEXCEL_DIAGNOSTICS=0` before launching Freexcel to disable local diagnostics for that run.

## Phase 5 Crash Analytics Contract

Remote crash analytics are off by default. They activate only when all of these are true:

- The tester build is launched with `FREEXCEL_SENTRY_DSN` set to the Sentry DSN.
- The tester opts in from the first-launch crash report prompt or later through `Options > Trust Center`.
- `FREEXCEL_CRASH_ANALYTICS` is not set to `0`.

Remote crash reports include app version, runtime, operating system, process architecture, session ID, exception type, message, stack trace, and safe breadcrumbs from allowlisted app events. They do not intentionally collect workbook contents, formulas, filenames, or paths, but exception messages and stack traces can occasionally contain sensitive values.

## Phase 6 Lightweight Usage Analytics Contract

Lightweight usage analytics reuse the same local diagnostics pipeline and, when crash analytics is enabled, the same safe Sentry breadcrumb path. They are meant only to help stabilize tester builds.

- Recorded categories are app lifecycle, command/dialog opened, file import/export type, and crash/session linkage.
- Event properties are allowlisted to include coarse labels such as command name, dialog type, file type, format, scope, status, reason, source, and worksheet count.
- These events do not intentionally collect workbook contents, formulas, filenames, or paths.
- Crash-linked exception messages and stack traces can occasionally contain sensitive values; review local crash reports before sharing them.
- Set `FREEXCEL_DIAGNOSTICS=0` before launching Freexcel to disable local usage diagnostics for that run. Remote crash breadcrumbs remain gated by Phase 5 crash analytics consent and `FREEXCEL_SENTRY_DSN`.

## Phase 7 Auto-Update Readiness Contract

`Help > Check for Updates` opens the stable latest release page so testers can manually compare or download the newest build without hunting through GitHub. It records a safe `update_check_opened` diagnostics event with source `help`.

Full in-app updates remain deferred until the manual latest-download loop is proven. The intended implementation path is Velopack, which requires early startup initialization through a custom `Main`, release packaging with the `vpk` tooling, and hosted update packages. Until that packaging work is added there is no background update download, no automatic install, and no restart-on-update behavior.

## Future Velopack auto-update work

When tester adoption justifies automatic update prompts, add Velopack packaging as a new distribution phase. That work should package `.nupkg`/release metadata alongside the tester `.exe`, initialize Velopack before WPF startup, check for updates only after user-visible consent, and keep the manual latest-release fallback in Help.

## Tester Report Flow

1. Download the latest user-test build.
2. Run the `.exe`; install the Microsoft .NET Desktop Runtime if Windows prompts for it.
3. Report issues through the GitHub "Freexcel user test report" template.
4. Attach `%LOCALAPPDATA%\Freexcel\Diagnostics\events.jsonl` or `CrashReports/*.json` only when useful, after checking that the attachment contains no private information.
