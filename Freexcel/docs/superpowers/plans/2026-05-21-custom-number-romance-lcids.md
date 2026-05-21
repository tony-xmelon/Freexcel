# Custom Number Romance LCIDs Plan

- [x] Identify that Freexcel preserves LCID currency symbols for Spanish and Italian format tokens but still used invariant decimal/group separators.
- [x] Add failing formatter coverage for Spanish Spain `C0A` and Italian `410` Euro number formats.
- [x] Map `C0A` and `410` to deterministic comma decimal and dot group separators without depending on the OS culture.
- [x] Update architecture and parity docs.

## Verification

- Red: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators -v minimal` failed for the new `C0A` and `410` cases before implementation.
- Green: `dotnet test Freexcel\tests\Freexcel.Core.Calc.Tests\Freexcel.Core.Calc.Tests.csproj --no-restore -p:UseSharedCompilation=false -p:NodeReuse=false -m:1 --filter FullyQualifiedName~NumberFormatterTests.CustomNumberSubset_UsesKnownLcidDecimalAndGroupSeparators --logger "console;verbosity=minimal"` passed 7 tests.
