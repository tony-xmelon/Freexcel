# Freexcel Formula Function Parity

**Last updated:** 2026-05-18  
**Total implemented:** 214
**Status:** covers the full day-to-day Excel function surface plus the first long-tail parity batch; statistical distributions, financial bond math, volatile reference helpers, and Lambda runtime functions remain outstanding

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
| Math / Trig | 48 | 0 | 2 | 0 | 50 | **96%** |
| Statistical | 38 | 0 | 34 | 0 | 72 | **53%** |
| Logical | 11 | 0 | 0 | 0 | 11 | **100%** |
| Lookup / Reference | 32 | 0 | 2 | 1 | 34 | **94%** |
| Text | 29 | 0 | 0 | 4 | 29 | **100%** |
| Date / Time | 25 | 0 | 0 | 0 | 25 | **100%** |
| Financial | 8 | 0 | 45 | 0 | 53 | **15%** |
| Information | 11 | 0 | 4 | 0 | 15 | **73%** |
| Lambda / Advanced | 0 | 0 | 8 | 0 | 8 | **0%** |
| Database | 12 | 0 | 0 | 0 | 12 | **100%** |
| Engineering / Cube / Cloud | 0 | 0 | 0 | 10 | — | **Excluded** |
| **TOTAL** | **214** | **0** | **95** | **15** | **309** | **69%** |

Coverage = (Implemented + Partial) / In-scope Total. Excluded functions are not counted in the in-scope total. Engineering/Cube/Cloud is entirely excluded.

Remaining formula work is tracked in [2026-05-18-remaining-formula-parity.md](superpowers/plans/2026-05-18-remaining-formula-parity.md).

---

## Math / Trig

**Coverage: 48/50 (96%)**

| Function | Status |
|---|---|
| ABS | Implemented |
| ACOS | Implemented |
| ASIN | Implemented |
| ATAN | Implemented |
| ATAN2 | Implemented |
| CEILING | Implemented |
| COMBIN | Implemented |
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
| MOD | Implemented |
| MROUND | Implemented |
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
| SIGN | Implemented |
| SIN | Implemented |
| SQRT | Implemented |
| SUBTOTAL | Implemented |
| SUM | Implemented |
| SUMIF | Implemented |
| SUMIFS | Implemented |
| SUMPRODUCT | Implemented |
| TAN | Implemented |
| TRUNC | Implemented |
| MDETERM | Implemented |
| MINVERSE | Implemented |
| MMULT | Implemented |
| MULTINOMIAL | Implemented |
| SERIESSUM | Implemented |
| SQRTPI | Implemented |
| AGGREGATE | Not Implemented |
| CONVERT | Not Implemented |

---

## Statistical

**Coverage: 38/72 (53%)**

| Function | Status |
|---|---|
| AVEDEV | Implemented |
| AVERAGE | Implemented |
| AVERAGEIF | Implemented |
| AVERAGEIFS | Implemented |
| CORREL | Implemented |
| COUNT | Implemented |
| COUNTA | Implemented |
| COUNTBLANK | Implemented |
| COUNTIF | Implemented |
| COUNTIFS | Implemented |
| FORECAST | Implemented |
| FORECAST.LINEAR | Implemented |
| GEOMEAN | Implemented |
| HARMEAN | Implemented |
| LARGE | Implemented |
| MAX | Implemented |
| MEDIAN | Implemented |
| MIN | Implemented |
| MODE | Implemented |
| MODE.SNGL | Implemented |
| PERCENTILE | Implemented |
| PERCENTILE.EXC | Implemented |
| PERCENTILE.INC | Implemented |
| PERCENTRANK | Implemented |
| PERCENTRANK.INC | Implemented |
| QUARTILE | Implemented |
| QUARTILE.INC | Implemented |
| RANK | Implemented |
| SMALL | Implemented |
| STDEV | Implemented |
| STDEV.P | Implemented |
| STDEV.S | Implemented |
| VAR | Implemented |
| VAR.P | Implemented |
| VAR.S | Implemented |
| BETA.DIST | Not Implemented |
| BETA.INV | Not Implemented |
| BINOM.DIST | Not Implemented |
| BINOM.INV | Not Implemented |
| CHISQ.DIST | Not Implemented |
| CHISQ.INV | Not Implemented |
| CHISQ.TEST | Not Implemented |
| CONFIDENCE | Not Implemented |
| CONFIDENCE.NORM | Not Implemented |
| CONFIDENCE.T | Not Implemented |
| DEVSQ | Implemented |
| EXPON.DIST | Not Implemented |
| F.DIST | Not Implemented |
| F.INV | Not Implemented |
| F.TEST | Not Implemented |
| FREQUENCY | Not Implemented |
| GAMMA.DIST | Not Implemented |
| GAMMA.INV | Not Implemented |
| HYPERGEOM.DIST | Not Implemented |
| KURT | Not Implemented |
| LOGNORM.DIST | Not Implemented |
| LOGNORM.INV | Not Implemented |
| NEGBINOM.DIST | Not Implemented |
| NORM.DIST | Not Implemented |
| NORM.INV | Not Implemented |
| NORM.S.DIST | Not Implemented |
| NORM.S.INV | Not Implemented |
| POISSON.DIST | Not Implemented |
| RANK.AVG | Implemented |
| RANK.EQ | Implemented |
| SKEW | Not Implemented |
| SKEW.P | Not Implemented |
| STANDARDIZE | Not Implemented |
| T.DIST | Not Implemented |
| T.INV | Not Implemented |
| T.TEST | Not Implemented |
| WEIBULL.DIST | Not Implemented |

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

**Coverage: 32/34 (94%); 1 Excluded**

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
| HLOOKUP | Implemented |
| HSTACK | Implemented |
| INDEX | Implemented |
| INDIRECT | Implemented |
| LOOKUP | Implemented |
| MATCH | Implemented |
| RANDARRAY | Implemented |
| ROW | Implemented |
| ROWS | Implemented |
| SEQUENCE | Implemented |
| SORT | Implemented |
| SORTBY | Implemented |
| TAKE | Implemented |
| TOCOL | Implemented |
| TOROW | Implemented |
| UNIQUE | Implemented |
| VLOOKUP | Implemented |
| VSTACK | Implemented |
| WRAPCOLS | Implemented |
| WRAPROWS | Implemented |
| XLOOKUP | Implemented |
| XMATCH | Implemented |
| FORMULATEXT | Not Implemented |
| OFFSET | Not Implemented |
| TRANSPOSE (function) | Implemented |
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
| UPPER | Implemented |
| VALUE | Implemented |
| NUMBERVALUE | Implemented |
| UNICHAR | Implemented |
| UNICODE | Implemented |
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
| NOW | Implemented |
| SECOND | Implemented |
| TIME | Implemented |
| TIMEVALUE | Implemented |
| TODAY | Implemented |
| WEEKDAY | Implemented |
| WEEKNUM | Implemented |
| WORKDAY | Implemented |
| YEAR | Implemented |
| YEARFRAC | Implemented |
| NETWORKDAYS.INTL | Implemented |
| WORKDAY.INTL | Implemented |

---

## Financial

**Coverage: 8/53 (15%)**

| Function | Status |
|---|---|
| FV | Implemented |
| IRR | Implemented |
| NPER | Implemented |
| NPV | Implemented |
| PMT | Implemented |
| PV | Implemented |
| RATE | Implemented |
| SLN | Implemented |
| ACCRINT | Not Implemented |
| AMORDEGRC | Not Implemented |
| AMORLINC | Not Implemented |
| COUPDAYBS | Not Implemented |
| COUPDAYS | Not Implemented |
| COUPDAYSNC | Not Implemented |
| COUPNCD | Not Implemented |
| COUPNUM | Not Implemented |
| COUPPCD | Not Implemented |
| CUMIPMT | Not Implemented |
| CUMPRINC | Not Implemented |
| DB | Not Implemented |
| DDB | Not Implemented |
| DISC | Not Implemented |
| DOLLARDE | Not Implemented |
| DOLLARFR | Not Implemented |
| DURATION | Not Implemented |
| EFFECT | Not Implemented |
| FVSCHEDULE | Not Implemented |
| INTRATE | Not Implemented |
| IPMT | Not Implemented |
| MDURATION | Not Implemented |
| MIRR | Not Implemented |
| NOMINAL | Not Implemented |
| ODDFPRICE | Not Implemented |
| ODDFYIELD | Not Implemented |
| ODDLPRICE | Not Implemented |
| ODDLYIELD | Not Implemented |
| PDURATION | Not Implemented |
| PPMT | Not Implemented |
| PRICE | Not Implemented |
| PRICEDISC | Not Implemented |
| PRICEMAT | Not Implemented |
| RECEIVED | Not Implemented |
| RRI | Not Implemented |
| SYD | Not Implemented |
| TBILLEQ | Not Implemented |
| TBILLPRICE | Not Implemented |
| TBILLYIELD | Not Implemented |
| VDB | Not Implemented |
| XIRR | Not Implemented |
| XNPV | Not Implemented |
| YIELD | Not Implemented |
| YIELDDISC | Not Implemented |
| YIELDMAT | Not Implemented |

---

## Information

**Coverage: 11/15 (73%)**

| Function | Status |
|---|---|
| ISBLANK | Implemented |
| ISERROR | Implemented |
| ISEVEN | Implemented |
| ISLOGICAL | Implemented |
| ISNA | Implemented |
| ISNUMBER | Implemented |
| ISODD | Implemented |
| ISTEXT | Implemented |
| NA | Implemented |
| CELL | Not Implemented | |
| ERROR.TYPE | Implemented |
| INFO | Not Implemented | |
| ISFORMULA | Not Implemented |
| ISREF | Not Implemented |
| TYPE | Implemented |

---

## Lambda / Advanced Calculation

**Coverage: 0/8 (0%)**

| Function | Status |
|---|---|
| LAMBDA | Not Implemented |
| LET | Not Implemented |
| BYROW | Not Implemented |
| BYCOL | Not Implemented |
| MAKEARRAY | Not Implemented |
| MAP | Not Implemented |
| REDUCE | Not Implemented |
| SCAN | Not Implemented |

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

> Note: Engineering conversion functions (BIN2DEC, HEX2DEC, CONVERT, etc.) are not yet implemented. Full engineering function suite may be added in a future phase if demand warrants.
