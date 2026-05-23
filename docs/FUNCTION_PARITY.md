# Freexcel Formula Function Parity

**Last updated:** 2026-05-23
**Total implemented:** 345
**Status:** All in-scope functions implemented

## Status Legend

| Status | Meaning |
|---|---|
| Implemented | Works with Excel-matching semantics; covered by tests |
| Partial | Core behavior works; some edge cases or overloads missing |
| Not Implemented | Not yet implemented; returns #NAME? |
| Excluded from scope | Requires Microsoft services or proprietary runtime |

---

## Coverage Summary

| Category | Implemented | Partial | Not Implemented | Excluded | In-scope Total | **Coverage** |
|---|---:|---:|---:|---:|---:|---:|
| Math / Trig | 50 | 0 | 0 | 0 | 50 | **100%** |
| Statistical | 83 | 0 | 0 | 0 | 83 | **100%** |
| Logical | 11 | 0 | 0 | 0 | 11 | **100%** |
| Lookup / Reference | 36 | 0 | 0 | 0 | 36 | **100%** |
| Text | 33 | 0 | 0 | 0 | 33 | **100%** |
| Date / Time | 25 | 0 | 0 | 0 | 25 | **100%** |
| Financial | 53 | 0 | 0 | 0 | 53 | **100%** |
| Information | 15 | 0 | 0 | 0 | 15 | **100%** |
| Lambda / Advanced | 8 | 0 | 0 | 0 | 8 | **100%** |
| Database | 12 | 0 | 0 | 0 | 12 | **100%** |
| Engineering / Cube / Cloud | 19 | 0 | 0 | 7 | 19 | **100%** |
| **TOTAL** | **345** | **0** | **0** | **7** | **345** | **100%** |

Coverage = (Implemented + Partial) / In-scope Total. Excluded functions are not counted in the in-scope total.

The former [remaining formula parity plan](superpowers/plans/2026-05-18-remaining-formula-parity.md) is now historical: its in-scope implementation phases are complete. Current formula work is parity proof and hardening rather than broad function addition:

- Excel-authored cached-result fixture workbooks now cover high-risk financial, statistical, date/time, dynamic-array, lookup/reference, engineering, `LET`, and text-join cases; continue adding targeted edge-case workbooks as parity bugs are found.
- Fuzz/property tests cover inverse and round-trip families such as distribution/inverse pairs, price/yield pairs, XIRR/XNPV, and engineering base conversions.
- Evaluator edge-case audits cover Excel coercion, error precedence, blank/empty handling, range flattening vs. structured range arguments, array expressions, spills, volatility, and date serial behavior.
- Structured-reference formula tests cover current-row, `#This Row`, multi-column, spaced-column, and case-insensitive header resolution through formula evaluation.

## Parity Test Sweep

The 2026-05-19 function parity sweep added a catalog guard and category-focused Excel parity suites:

| Area | Coverage added |
|---|---|
| Catalog integrity | Verifies every documented in-scope function is registered, every registered function is documented, and excluded functions remain outside the runtime. |
| Math / Trig | Exhaustive direct coverage for all 50 documented functions, including numeric coercion, domain errors, ranges, matrix outputs, random bounds, subtotals, and conditional aggregates. |
| Statistical | Direct coverage for previously unpinned aliases and modern names: DEVSQ, GAMMALN.PRECISE, MODE.SNGL, PERCENTILE.INC, PERCENTRANK.INC, QUARTILE.INC, RANK.AVG, and RANK.EQ. |
| Logical | Direct coverage for all logical functions, including IF short-circuiting and Excel-style error handling for IFERROR, IFNA, AND, and OR. |
| Information | Direct coverage for CELL, ERROR.TYPE, INFO, IS* predicates, N, NA, and TYPE. |
| Database | Direct coverage for DSTDEV, DSTDEVP, DVAR, and DVARP sample/population semantics, OR/AND criteria behavior, nonnumeric value handling, and empty-match errors. |
| Financial odd-coupon | ODDFPRICE, ODDFYIELD, ODDLPRICE, and ODDLYIELD now match Microsoft Excel documented examples and enforce Excel date-order/frequency/domain errors. |

Verification: `Freexcel.Core.Formula.Tests` passes 1,672/1,672 tests. Formula scalar array coercion parity was hardened across six batches (statistical, financial, range-argument, ChiSq, percentrank, higher-order, and rank functions) since the 2026-05-19 sweep, with broader inverse/round-trip tests for distribution and engineering conversion families, direct volatile registry guards, formula serializer/rewriter guards for modern error literals plus omitted dynamic-array arguments, omitted optional lookup-argument parity guards, database blank-criteria-row parity coverage, engineering base-conversion optional-argument error precedence, financial basis-domain guards, `UNICODE` scalar text coercion, `LEN`/`LEFT`/`RIGHT`/`FIND`/`SEARCH`/`MID`/`REPLACE` surrogate-pair text positions, empty-search scalar end-boundary guards, wildcard matching over surrogate-pair text elements, date serial bounds, modern lookup-array error precedence guards including exact, wildcard, and approximate `XLOOKUP`/`XMATCH` scans, legacy lookup index-domain errors, dynamic-array cell-level error precedence and empty-array `#CALC!` guards, finite integer-domain guards for `TAKE`/`DROP` slice counts, `WRAPROWS`/`WRAPCOLS` wrap counts, `SEQUENCE` dimensions, and `CHOOSECOLS`/`CHOOSEROWS` indexes, `EXPAND` spill-size caps, spilled-index-array handling for `CHOOSECOLS`/`CHOOSEROWS`, volatile `RANDARRAY` bounds, structured-reference current-row and spaced-header coverage, East Asian/Thai text function coverage, local `ENCODEURL`/secure `FILTERXML` coverage, higher-order `REDUCE`/`SCAN` nested-array rejection, `SORTBY` omitted-order handling, `XLOOKUP` omitted-mode defaults, omitted dynamic-array padding defaults, `ADDRESS` sheet-name escaping, and cached Excel-result fixtures for lookup/dynamic-array/LET/text cases including cached `#CALC!` formula errors.

---

## Math / Trig

**Coverage: 50/50 (100%)**

| Function | Status |
|---|---|
| ABS | Implemented |
| ACOS | Implemented |
| AGGREGATE | Implemented |
| ASIN | Implemented |
| ATAN | Implemented |
| ATAN2 | Implemented |
| CEILING | Implemented |
| COMBIN | Implemented |
| CONVERT | Implemented |
| COS | Implemented |
| DEGREES | Implemented |
| EVEN | Implemented |
| EXP | Implemented |
| FACT | Implemented |
| FLOOR | Implemented |
| GCD | Implemented |
| INT | Implemented |
| LCM | Implemented |
| LN | Implemented |
| LOG | Implemented |
| MDETERM | Implemented |
| MINVERSE | Implemented |
| MMULT | Implemented |
| MOD | Implemented |
| MROUND | Implemented |
| MULTINOMIAL | Implemented |
| ODD | Implemented |
| PERMUT | Implemented |
| PI | Implemented |
| POWER | Implemented |
| PRODUCT | Implemented |
| QUOTIENT | Implemented |
| RADIANS | Implemented |
| RAND | Implemented |
| RANDBETWEEN | Implemented |
| ROUND | Implemented |
| ROUNDDOWN | Implemented |
| ROUNDUP | Implemented |
| SERIESSUM | Implemented |
| SIGN | Implemented |
| SIN | Implemented |
| SQRT | Implemented |
| SQRTPI | Implemented |
| SUBTOTAL | Implemented |
| SUM | Implemented |
| SUMIF | Implemented |
| SUMIFS | Implemented |
| SUMPRODUCT | Implemented |
| TAN | Implemented |
| TRUNC | Implemented |

---

## Statistical

**Coverage: 83/83 (100%)**

| Function | Status |
|---|---|
| AVEDEV | Implemented |
| AVERAGE | Implemented |
| AVERAGEIF | Implemented |
| AVERAGEIFS | Implemented |
| BETA.DIST | Implemented |
| BETA.INV | Implemented |
| BINOM.DIST | Implemented |
| BINOM.DIST.RANGE | Implemented |
| BINOM.INV | Implemented |
| CHISQ.DIST | Implemented |
| CHISQ.DIST.RT | Implemented |
| CHISQ.INV | Implemented |
| CHISQ.INV.RT | Implemented |
| CHISQ.TEST | Implemented |
| CONFIDENCE | Implemented |
| CONFIDENCE.NORM | Implemented |
| CONFIDENCE.T | Implemented |
| CORREL | Implemented |
| COUNT | Implemented |
| COUNTA | Implemented |
| COUNTBLANK | Implemented |
| COUNTIF | Implemented |
| COUNTIFS | Implemented |
| DEVSQ | Implemented |
| EXPON.DIST | Implemented |
| F.DIST | Implemented |
| F.DIST.RT | Implemented |
| F.INV | Implemented |
| F.INV.RT | Implemented |
| F.TEST | Implemented |
| FORECAST | Implemented |
| FORECAST.LINEAR | Implemented |
| FREQUENCY | Implemented |
| GAMMA | Implemented |
| GAMMA.DIST | Implemented |
| GAMMA.INV | Implemented |
| GAMMALN | Implemented |
| GAMMALN.PRECISE | Implemented |
| GEOMEAN | Implemented |
| HARMEAN | Implemented |
| HYPERGEOM.DIST | Implemented |
| KURT | Implemented |
| LARGE | Implemented |
| LOGNORM.DIST | Implemented |
| LOGNORM.INV | Implemented |
| MAX | Implemented |
| MEDIAN | Implemented |
| MIN | Implemented |
| MODE | Implemented |
| MODE.SNGL | Implemented |
| NEGBINOM.DIST | Implemented |
| NORM.DIST | Implemented |
| NORM.INV | Implemented |
| NORM.S.DIST | Implemented |
| NORM.S.INV | Implemented |
| PERCENTILE | Implemented |
| PERCENTILE.EXC | Implemented |
| PERCENTILE.INC | Implemented |
| PERCENTRANK | Implemented |
| PERCENTRANK.INC | Implemented |
| POISSON.DIST | Implemented |
| QUARTILE | Implemented |
| QUARTILE.INC | Implemented |
| RANK | Implemented |
| RANK.AVG | Implemented |
| RANK.EQ | Implemented |
| SKEW | Implemented |
| SKEW.P | Implemented |
| SMALL | Implemented |
| STANDARDIZE | Implemented |
| STDEV | Implemented |
| STDEV.P | Implemented |
| STDEV.S | Implemented |
| T.DIST | Implemented |
| T.DIST.2T | Implemented |
| T.DIST.RT | Implemented |
| T.INV | Implemented |
| T.INV.2T | Implemented |
| T.TEST | Implemented |
| VAR | Implemented |
| VAR.P | Implemented |
| VAR.S | Implemented |
| WEIBULL.DIST | Implemented |

---

## Logical

**Coverage: 11/11 (100%)**

| Function | Status |
|---|---|
| AND | Implemented |
| FALSE | Implemented |
| IF | Implemented |
| IFERROR | Implemented |
| IFNA | Implemented |
| IFS | Implemented |
| NOT | Implemented |
| OR | Implemented |
| SWITCH | Implemented |
| TRUE | Implemented |
| XOR | Implemented |

---

## Lookup / Reference

**Coverage: 36/36 (100%)**

| Function | Status |
|---|---|
| ADDRESS | Implemented |
| CHOOSE | Implemented |
| CHOOSECOLS | Implemented |
| CHOOSEROWS | Implemented |
| COLUMN | Implemented |
| COLUMNS | Implemented |
| DROP | Implemented |
| EXPAND | Implemented |
| FILTER | Implemented |
| FORMULATEXT | Implemented |
| HLOOKUP | Implemented |
| HSTACK | Implemented |
| HYPERLINK | Implemented |
| INDEX | Implemented |
| INDIRECT | Implemented |
| LOOKUP | Implemented |
| MATCH | Implemented |
| OFFSET | Implemented |
| RANDARRAY | Implemented |
| ROW | Implemented |
| ROWS | Implemented |
| SEQUENCE | Implemented |
| SORT | Implemented |
| SORTBY | Implemented |
| TAKE | Implemented |
| TOCOL | Implemented |
| TOROW | Implemented |
| TRANSPOSE | Implemented |
| UNIQUE | Implemented |
| VLOOKUP | Implemented |
| VSTACK | Implemented |
| WRAPCOLS | Implemented |
| WRAPROWS | Implemented |
| XLOOKUP | Implemented |
| XMATCH | Implemented |
| GETPIVOTDATA | Implemented for worksheet-range PivotTables; OLAP/Data Model/Power Pivot semantics excluded with those subsystems |

---

## Text

**Coverage: 33/33 (100%)**

| Function | Status |
|---|---|
| CHAR | Implemented |
| CLEAN | Implemented |
| CODE | Implemented |
| CONCAT | Implemented |
| CONCATENATE | Implemented |
| DOLLAR | Implemented |
| EXACT | Implemented |
| FIND | Implemented |
| FIXED | Implemented |
| LEFT | Implemented |
| LEN | Implemented |
| LOWER | Implemented |
| MID | Implemented |
| N | Implemented |
| NUMBERVALUE | Implemented |
| PROPER | Implemented |
| REPLACE | Implemented |
| REPT | Implemented |
| RIGHT | Implemented |
| SEARCH | Implemented |
| SUBSTITUTE | Implemented |
| T | Implemented |
| TEXT | Implemented |
| TEXTJOIN | Implemented |
| TRIM | Implemented |
| UNICHAR | Implemented |
| UNICODE | Implemented |
| UPPER | Implemented |
| VALUE | Implemented |
| ASC | Implemented |
| BAHTTEXT | Implemented |
| DBCS | Implemented |
| PHONETIC | Implemented |

---

## Date / Time

**Coverage: 25/25 (100%)**

| Function | Status |
|---|---|
| DATE | Implemented |
| DATEDIF | Implemented |
| DATEVALUE | Implemented |
| DAY | Implemented |
| DAYS | Implemented |
| DAYS360 | Implemented |
| EDATE | Implemented |
| EOMONTH | Implemented |
| HOUR | Implemented |
| ISOWEEKNUM | Implemented |
| MINUTE | Implemented |
| MONTH | Implemented |
| NETWORKDAYS | Implemented |
| NETWORKDAYS.INTL | Implemented |
| NOW | Implemented |
| SECOND | Implemented |
| TIME | Implemented |
| TIMEVALUE | Implemented |
| TODAY | Implemented |
| WEEKDAY | Implemented |
| WEEKNUM | Implemented |
| WORKDAY | Implemented |
| WORKDAY.INTL | Implemented |
| YEAR | Implemented |
| YEARFRAC | Implemented |

---

## Financial

**Coverage: 53/53 (100%)**

| Function | Status |
|---|---|
| ACCRINT | Implemented |
| AMORDEGRC | Implemented |
| AMORLINC | Implemented |
| COUPDAYBS | Implemented |
| COUPDAYS | Implemented |
| COUPDAYSNC | Implemented |
| COUPNCD | Implemented |
| COUPNUM | Implemented |
| COUPPCD | Implemented |
| CUMIPMT | Implemented |
| CUMPRINC | Implemented |
| DB | Implemented |
| DDB | Implemented |
| DISC | Implemented |
| DOLLARDE | Implemented |
| DOLLARFR | Implemented |
| DURATION | Implemented |
| EFFECT | Implemented |
| FVSCHEDULE | Implemented |
| FV | Implemented |
| INTRATE | Implemented |
| IPMT | Implemented |
| IRR | Implemented |
| MDURATION | Implemented |
| MIRR | Implemented |
| NOMINAL | Implemented |
| NPER | Implemented |
| NPV | Implemented |
| ODDFPRICE | Implemented |
| ODDFYIELD | Implemented |
| ODDLPRICE | Implemented |
| ODDLYIELD | Implemented |
| PDURATION | Implemented |
| PMT | Implemented |
| PPMT | Implemented |
| PRICE | Implemented |
| PRICEDISC | Implemented |
| PRICEMAT | Implemented |
| PV | Implemented |
| RATE | Implemented |
| RECEIVED | Implemented |
| RRI | Implemented |
| SLN | Implemented |
| SYD | Implemented |
| TBILLEQ | Implemented |
| TBILLPRICE | Implemented |
| TBILLYIELD | Implemented |
| VDB | Implemented |
| XIRR | Implemented |
| XNPV | Implemented |
| YIELD | Implemented |
| YIELDDISC | Implemented |
| YIELDMAT | Implemented |

---

## Information

**Coverage: 15/15 (100%)**

| Function | Status |
|---|---|
| CELL | Implemented |
| ERROR.TYPE | Implemented |
| INFO | Implemented |
| ISBLANK | Implemented |
| ISERROR | Implemented |
| ISEVEN | Implemented |
| ISFORMULA | Implemented |
| ISLOGICAL | Implemented |
| ISNA | Implemented |
| ISNUMBER | Implemented |
| ISODD | Implemented |
| ISREF | Implemented |
| ISTEXT | Implemented |
| NA | Implemented |
| TYPE | Implemented |

---

## Lambda / Advanced Calculation

**Coverage: 8/8 (100%)**

| Function | Status |
|---|---|
| LAMBDA | Implemented |
| LET | Implemented |
| BYROW | Implemented |
| BYCOL | Implemented |
| MAKEARRAY | Implemented |
| MAP | Implemented |
| REDUCE | Implemented |
| SCAN | Implemented |

---

## Database

**Coverage: 12/12 (100%)**

| Function | Status |
|---|---|
| DAVERAGE | Implemented |
| DCOUNT | Implemented |
| DCOUNTA | Implemented |
| DGET | Implemented |
| DMAX | Implemented |
| DMIN | Implemented |
| DPRODUCT | Implemented |
| DSTDEV | Implemented |
| DSTDEVP | Implemented |
| DSUM | Implemented |
| DVAR | Implemented |
| DVARP | Implemented |

---

## Engineering / Cube / Cloud

**Coverage: 17/17 in-scope functions (100%); cloud/cube functions excluded**

| Function | Status |
|---|---|
| BIN2DEC | Implemented |
| BIN2HEX | Implemented |
| BIN2OCT | Implemented |
| BITAND | Implemented |
| BITLSHIFT | Implemented |
| BITOR | Implemented |
| BITRSHIFT | Implemented |
| BITXOR | Implemented |
| CUBEKPIMEMBER | Excluded from scope |
| CUBEMEMBER | Excluded from scope |
| CUBESET | Excluded from scope |
| CUBESETCOUNT | Excluded from scope |
| CUBEVALUE | Excluded from scope |
| DEC2BIN | Implemented |
| DEC2HEX | Implemented |
| DEC2OCT | Implemented |
| ENCODEURL | Implemented |
| FILTERXML | Implemented |
| HEX2BIN | Implemented |
| HEX2DEC | Implemented |
| HEX2OCT | Implemented |
| OCT2BIN | Implemented |
| OCT2DEC | Implemented |
| OCT2HEX | Implemented |
| RTD | Excluded from scope |
| WEBSERVICE | Excluded from scope |

> Note: `CONVERT` handles unit conversion. The discrete base-conversion and bit-manipulation engineering functions are implemented separately.
