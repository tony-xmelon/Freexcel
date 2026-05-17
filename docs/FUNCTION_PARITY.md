# Freexcel Formula Function Parity

**Last updated:** 2026-05-18  
**Total implemented:** 165  
**Status:** covers the full day-to-day Excel function surface; statistical distributions and financial bond math remain outstanding

## Status Legend

| Status | Meaning |
|---|---|
| Implemented | Works with Excel-matching semantics; covered by tests |
| Partial | Core behavior works; some edge cases or overloads missing |
| Needs Implementation | Not yet implemented; returns #NAME? |
| Excluded from scope | Requires Microsoft services or proprietary runtime |

---

## Math / Trig

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
| AGGREGATE | Needs Implementation |
| CONVERT | Needs Implementation |
| MDETERM | Needs Implementation |
| MINVERSE | Needs Implementation |
| MMULT | Needs Implementation |
| MULTINOMIAL | Needs Implementation |
| SERIESSUM | Needs Implementation |
| SQRTPI | Needs Implementation |

---

## Statistical

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
| BETA.DIST | Needs Implementation |
| BETA.INV | Needs Implementation |
| BINOM.DIST | Needs Implementation |
| BINOM.INV | Needs Implementation |
| CHISQ.DIST | Needs Implementation |
| CHISQ.INV | Needs Implementation |
| CHISQ.TEST | Needs Implementation |
| CONFIDENCE | Needs Implementation |
| CONFIDENCE.NORM | Needs Implementation |
| CONFIDENCE.T | Needs Implementation |
| DEVSQ | Needs Implementation |
| EXPON.DIST | Needs Implementation |
| F.DIST | Needs Implementation |
| F.INV | Needs Implementation |
| F.TEST | Needs Implementation |
| FREQUENCY | Needs Implementation |
| GAMMA.DIST | Needs Implementation |
| GAMMA.INV | Needs Implementation |
| HYPERGEOM.DIST | Needs Implementation |
| KURT | Needs Implementation |
| LOGNORM.DIST | Needs Implementation |
| LOGNORM.INV | Needs Implementation |
| NEGBINOM.DIST | Needs Implementation |
| NORM.DIST | Needs Implementation |
| NORM.INV | Needs Implementation |
| NORM.S.DIST | Needs Implementation |
| NORM.S.INV | Needs Implementation |
| POISSON.DIST | Needs Implementation |
| RANK.AVG | Needs Implementation |
| RANK.EQ | Needs Implementation |
| SKEW | Needs Implementation |
| SKEW.P | Needs Implementation |
| STANDARDIZE | Needs Implementation |
| T.DIST | Needs Implementation |
| T.INV | Needs Implementation |
| T.TEST | Needs Implementation |
| WEIBULL.DIST | Needs Implementation |

---

## Logical

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
| FORMULATEXT | Needs Implementation |
| OFFSET | Needs Implementation |
| TRANSPOSE (function) | Needs Implementation |
| GETPIVOTDATA | Excluded from scope |

---

## Text

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
| NUMBERVALUE | Needs Implementation |
| UNICHAR | Needs Implementation |
| UNICODE | Needs Implementation |
| ASC | Excluded from scope |
| BAHTTEXT | Excluded from scope |
| DBCS | Excluded from scope |
| PHONETIC | Excluded from scope |

---

## Date / Time

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
| NETWORKDAYS.INTL | Needs Implementation |
| WORKDAY.INTL | Needs Implementation |

---

## Financial

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
| ACCRINT | Needs Implementation |
| AMORDEGRC | Needs Implementation |
| AMORLINC | Needs Implementation |
| COUPDAYBS | Needs Implementation |
| COUPDAYS | Needs Implementation |
| COUPDAYSNC | Needs Implementation |
| COUPNCD | Needs Implementation |
| COUPNUM | Needs Implementation |
| COUPPCD | Needs Implementation |
| CUMIPMT | Needs Implementation |
| CUMPRINC | Needs Implementation |
| DB | Needs Implementation |
| DDB | Needs Implementation |
| DISC | Needs Implementation |
| DOLLARDE | Needs Implementation |
| DOLLARFR | Needs Implementation |
| DURATION | Needs Implementation |
| EFFECT | Needs Implementation |
| FVSCHEDULE | Needs Implementation |
| INTRATE | Needs Implementation |
| IPMT | Needs Implementation |
| MDURATION | Needs Implementation |
| MIRR | Needs Implementation |
| NOMINAL | Needs Implementation |
| ODDFPRICE | Needs Implementation |
| ODDFYIELD | Needs Implementation |
| ODDLPRICE | Needs Implementation |
| ODDLYIELD | Needs Implementation |
| PDURATION | Needs Implementation |
| PPMT | Needs Implementation |
| PRICE | Needs Implementation |
| PRICEDISC | Needs Implementation |
| PRICEMAT | Needs Implementation |
| RECEIVED | Needs Implementation |
| RRI | Needs Implementation |
| SYD | Needs Implementation |
| TBILLEQ | Needs Implementation |
| TBILLPRICE | Needs Implementation |
| TBILLYIELD | Needs Implementation |
| VDB | Needs Implementation |
| XIRR | Needs Implementation |
| XNPV | Needs Implementation |
| YIELD | Needs Implementation |
| YIELDDISC | Needs Implementation |
| YIELDMAT | Needs Implementation |

---

## Information

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
| CELL | Needs Implementation |
| ERROR.TYPE | Needs Implementation |
| INFO | Needs Implementation |
| ISFORMULA | Needs Implementation |
| ISREF | Needs Implementation |
| TYPE | Needs Implementation |

---

## Lambda / Advanced Calculation

| Function | Status |
|---|---|
| LAMBDA | Needs Implementation |
| LET | Needs Implementation |
| BYROW | Needs Implementation |
| BYCOL | Needs Implementation |
| MAKEARRAY | Needs Implementation |
| MAP | Needs Implementation |
| REDUCE | Needs Implementation |
| SCAN | Needs Implementation |

---

## Database

| Function | Status |
|---|---|
| DAVERAGE | Needs Implementation |
| DCOUNT | Needs Implementation |
| DCOUNTA | Needs Implementation |
| DGET | Needs Implementation |
| DMAX | Needs Implementation |
| DMIN | Needs Implementation |
| DPRODUCT | Needs Implementation |
| DSTDEV | Needs Implementation |
| DSTDEVP | Needs Implementation |
| DSUM | Needs Implementation |
| DVAR | Needs Implementation |
| DVARP | Needs Implementation |

---

## Engineering / Cube / Cloud

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
