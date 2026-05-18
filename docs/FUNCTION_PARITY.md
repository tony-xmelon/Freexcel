# Freexcel Formula Function Parity

**Last updated:** 2026-05-18  
**Total implemented:** 184  
**Status:** covers the full day-to-day Excel function surface; statistical distributions and financial bond math remain outstanding

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
| Math / Trig | 42 | 0 | 8 | 0 | 50 | **84%** |
| Statistical | 35 | 0 | 37 | 0 | 72 | **49%** |
| Logical | 11 | 0 | 0 | 0 | 11 | **100%** |
| Lookup / Reference | 30 | 0 | 3 | 1 | 33 | **91%** |
| Text | 26 | 0 | 3 | 4 | 29 | **90%** |
| Date / Time | 23 | 0 | 2 | 0 | 25 | **92%** |
| Financial | 8 | 0 | 45 | 0 | 53 | **15%** |
| Information | 9 | 0 | 4 | 2 | 13 | **69%** |
| Lambda / Advanced | 0 | 0 | 8 | 0 | 8 | **0%** |
| Database | 0 | 0 | 12 | 0 | 12 | **0%** |
| Engineering / Cube / Cloud | 0 | 0 | 0 | 10 | — | **Excluded** |
| **TOTAL** | **184** | **0** | **122** | **17** | **306** | **60%** |

Coverage = (Implemented + Partial) / In-scope Total. Excluded functions are not counted in the in-scope total. Engineering/Cube/Cloud is entirely excluded.

---

## Math / Trig

**Coverage: 42/50 (84%)**

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
| AGGREGATE | Not Implemented |
| CONVERT | Not Implemented |
| MDETERM | Not Implemented |
| MINVERSE | Not Implemented |
| MMULT | Not Implemented |
| MULTINOMIAL | Not Implemented |
| SERIESSUM | Not Implemented |
| SQRTPI | Not Implemented |

---

## Statistical

**Coverage: 35/72 (49%)**

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
| DEVSQ | Not Implemented |
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
| RANK.AVG | Not Implemented |
| RANK.EQ | Not Implemented |
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

**Coverage: 30/33 (91%); 1 Excluded**

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
| TRANSPOSE (function) | Not Implemented |
| GETPIVOTDATA | Excluded from scope |

---

## Text

**Coverage: 26/29 (90%); 4 Excluded**

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
| NUMBERVALUE | Not Implemented |
| UNICHAR | Not Implemented |
| UNICODE | Not Implemented |
| ASC | Excluded from scope |
| BAHTTEXT | Excluded from scope |
| DBCS | Excluded from scope |
| PHONETIC | Excluded from scope |

---

## Date / Time

**Coverage: 23/25 (92%)**

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
| NETWORKDAYS.INTL | Not Implemented |
| WORKDAY.INTL | Not Implemented |

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

**Coverage: 9/15 (60%)**

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
| CELL | Excluded from scope | Too complex; ~30 display-tied properties; rarely used |
| ERROR.TYPE | Not Implemented |
| INFO | Excluded from scope | Returns system info irrelevant to calculation |
| ISFORMULA | Not Implemented |
| ISREF | Not Implemented |
| TYPE | Not Implemented |

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

**Coverage: 0/12 (0%)**

| Function | Status |
|---|---|
| DAVERAGE | Not Implemented |
| DCOUNT | Not Implemented |
| DCOUNTA | Not Implemented |
| DGET | Not Implemented |
| DMAX | Not Implemented |
| DMIN | Not Implemented |
| DPRODUCT | Not Implemented |
| DSTDEV | Not Implemented |
| DSTDEVP | Not Implemented |
| DSUM | Not Implemented |
| DVAR | Not Implemented |
| DVARP | Not Implemented |

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
