# Freexcel Formula Function Parity

**Last updated:** 2026-05-18  
**Total implemented:** 319  
**Status:** All categories complete; only legacy CONFIDENCE alias remains outstanding

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
| Statistical | 82 | 0 | 1 | 0 | 83 | **99%** |
| Logical | 11 | 0 | 0 | 0 | 11 | **100%** |
| Lookup / Reference | 34 | 0 | 0 | 1 | 34 | **100%** |
| Text | 29 | 0 | 0 | 4 | 29 | **100%** |
| Date / Time | 25 | 0 | 0 | 0 | 25 | **100%** |
| Financial | 53 | 0 | 0 | 0 | 53 | **100%** |
| Information | 15 | 0 | 0 | 0 | 15 | **100%** |
| Lambda / Advanced | 8 | 0 | 0 | 0 | 8 | **100%** |
| Database | 12 | 0 | 0 | 0 | 12 | **100%** |
| Engineering / Cube / Cloud | 0 | 0 | 0 | 10 | — | **Excluded** |
| **TOTAL** | **319** | **0** | **1** | **15** | **320** | **99.7%** |

Coverage = (Implemented + Partial) / In-scope Total. Excluded functions are not counted in the in-scope total. Engineering/Cube/Cloud is entirely excluded.

Remaining formula work is tracked in [2026-05-18-remaining-formula-parity.md](superpowers/plans/2026-05-18-remaining-formula-parity.md).

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

**Coverage: 82/83 (99%)**

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
| CONFIDENCE | Not Implemented |
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

**Coverage: 34/34 (100%); 1 Excluded**

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
| GETPIVOTDATA | Excluded from scope |

---

## Text

**Coverage: 29/29 (100%); 4 Excluded**

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
| ASC | Excluded from scope |
| BAHTTEXT | Excluded from scope |
| DBCS | Excluded from scope |
| PHONETIC | Excluded from scope |

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

**Coverage: Entirely Excluded (10 functions)**

| Function | Status |
|---|---|
| CUBEKPIMEMBER | Excluded from scope |
| CUBEMEMBER | Excluded from scope |
| CUBESET | Excluded from scope |
| CUBESETCOUNT | Excluded from scope |
| CUBEVALUE | Excluded from scope |
| ENCODEURL | Excluded from scope |
| FILTERXML | Excluded from scope |
| HYPERLINK | Excluded from scope |
| RTD | Excluded from scope |
| WEBSERVICE | Excluded from scope |

> Note: Engineering conversion functions (BIN2DEC, HEX2DEC, etc.) are covered by CONVERT. Full discrete engineering bit-manipulation functions (BITAND, BITOR, BITRSHIFT, etc.) are not yet implemented and may be added in a future phase.
