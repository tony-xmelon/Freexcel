# Freexcel Test Distribution Plan

## Phase Status

| Phase | Status | Scope |
| --- | --- | --- |
| 1. Shareable builds | Complete | Framework-dependent user-test builds publish into `artifacts/releases` with version, timestamp, commit, runtime, and mode in the file name. |
| 2. Feedback intake | Complete | User testing findings are tracked in `docs/USER_TESTING_REPORT_2026-05-24.md`; GitHub issues now include a structured user-test report template. |
| 3. Local diagnostics | Complete | Test builds record local JSONL usage events and crash reports under `%LOCALAPPDATA%\Freexcel\Diagnostics`. No network upload is performed. |
| 4. Hosted release channel | Next | Publish latest builds through GitHub Releases with checksums, release notes, and a stable "latest test build" link. |
| 5. Hosted telemetry | Later | Decide whether to add opt-in remote crash/usage upload after the local diagnostics format has stabilized. |

## Phase 3 Diagnostics Contract

Freexcel writes tester diagnostics locally only. Files stay on the tester machine unless the tester attaches them to an issue.

- `events.jsonl` records app lifecycle events such as `app_start`, `app_ready`, `app_exit`, and `crash`.
- `CrashReports/*.json` records unhandled WPF dispatcher, AppDomain, and unobserved task exceptions.
- Event properties are allowlisted so workbook paths and workbook contents are not written as analytics properties.
- Set `FREEXCEL_DIAGNOSTICS=0` before launching Freexcel to disable local diagnostics for that run.

## Tester Report Flow

1. Download the latest user-test build.
2. Run the `.exe`; install the Microsoft .NET Desktop Runtime if Windows prompts for it.
3. Report issues through the GitHub "Freexcel user test report" template.
4. Attach `%LOCALAPPDATA%\Freexcel\Diagnostics\events.jsonl` or `CrashReports/*.json` only when useful, after checking that the attachment contains no private information.
