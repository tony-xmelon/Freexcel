# Freexcel Test Distribution Plan

## Phase Status

| Phase | Status | Scope |
| --- | --- | --- |
| 1. Shareable builds | Complete | Framework-dependent user-test builds publish into `artifacts/releases` with version, timestamp, commit, runtime, and mode in the file name. |
| 2. Feedback intake | Complete | User testing findings are tracked in `docs/USER_TESTING_REPORT_2026-05-24.md`; GitHub issues now include a structured user-test report template. |
| 3. Local diagnostics | Complete | Test builds record local JSONL usage events and crash reports under `%LOCALAPPDATA%\Freexcel\Diagnostics`. No network upload is performed. |
| 4. Hosted release channel | In progress | GitHub Actions publishes latest builds through GitHub Releases with versioned artifacts and a stable latest test build link. |
| 5. Crash analytics | In progress | Opt-in Sentry crash upload is wired behind tester consent and `FREEXCEL_SENTRY_DSN`; local diagnostics remain available without network upload. |

## Phase 4 Release Channel

Latest tester download:

https://github.com/tony-xmelon/Freexcel/releases/latest/download/Freexcel-latest-win-x64.exe

The `Tester Release` GitHub Actions workflow runs restore, build, and test before publishing a framework-dependent single-file Windows x64 `.exe`. It uploads both the versioned build produced by `tools/Publish-UserTestBuild.ps1` and the stable `Freexcel-latest-win-x64.exe` release asset.

## Phase 3 Diagnostics Contract

Freexcel writes tester diagnostics locally only. Files stay on the tester machine unless the tester attaches them to an issue.

- `events.jsonl` records app lifecycle events such as `app_start`, `app_ready`, `app_exit`, and `crash`.
- `CrashReports/*.json` records unhandled WPF dispatcher, AppDomain, and unobserved task exceptions.
- Event properties are allowlisted so workbook paths and workbook contents are not written as analytics properties.
- Set `FREEXCEL_DIAGNOSTICS=0` before launching Freexcel to disable local diagnostics for that run.

## Phase 5 Crash Analytics Contract

Remote crash analytics are off by default. They activate only when all of these are true:

- The tester build is launched with `FREEXCEL_SENTRY_DSN` set to the Sentry DSN.
- The tester opts in from the first-launch crash report prompt or later through `Options > Trust Center`.
- `FREEXCEL_CRASH_ANALYTICS` is not set to `0`.

Remote crash reports include app version, runtime, operating system, process architecture, session ID, exception details, and safe breadcrumbs from allowlisted app events. They do not intentionally collect workbook contents, formulas, filenames, or paths.

## Tester Report Flow

1. Download the latest user-test build.
2. Run the `.exe`; install the Microsoft .NET Desktop Runtime if Windows prompts for it.
3. Report issues through the GitHub "Freexcel user test report" template.
4. Attach `%LOCALAPPDATA%\Freexcel\Diagnostics\events.jsonl` or `CrashReports/*.json` only when useful, after checking that the attachment contains no private information.
