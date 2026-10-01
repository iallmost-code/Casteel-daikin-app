# DR80SN Gas Furnace — Full F01–F09 Blower Speed Tap Airflow Data

**Source:** IM-IOD-2035A, pages 24–25 (Daikin/Goodman/Amana DR80SN gas furnace install manual, airflow tables). Pulled directly from the PDF via text extraction — every number below is transcribed, not estimated.

**Thermostat call wiring (same for all 8 models):** Y/Y1, Y2, and G all land on this table — it's a single-stage-IFC-style combined cooling/fan table covering every tap F01–F09.

**Defaults, per the manual's own note block:**
- F01 = default speed for **G** (continuous fan / circulation)
- F04 = default speed for **Y/Y1** (single-stage cooling, or 1st stage on a 2-stage outdoor unit)
- F05 = default speed for **Y2** (2nd stage cooling) — *except* on 0805C* and 1205D*, see the 2-stage table below

**2-stage outdoor unit override (only applies to DR80SN0805C* and DR80SN1205D*):**

| Furnace Model | Y2 (2nd stage) | Y1 (1st stage) |
|---|---|---|
| DR80SN0805C* | F08 | F02 |
| DR80SN1205D* | F06 | F05 |

For a single-stage outdoor unit, Y can be landed on either Y/Y1 or Y2 on the board — just make sure the tap you pick matches whichever terminal you used.

---

## Cooling / Fan Airflow — CFM by Tap, All 8 Models

ESP columns are CFM at 0.1–0.4" (no watts listed), then CFM + Watts at 0.5"–0.8". `^` = default tap for Y/Y1 per the manual (F04 on every model in this family).

### DR80SN0403A* (TEMP RANGE 25–55°, see heating table)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 658 | 585 | 545 | 495 | 444 | 83 | 390 | 88 | 332 | 94 | 151 | 49 |
| F02 | 749 | 697 | 652 | 607 | 554 | 102 | 509 | 108 | 459 | 113 | 406 | 120 |
| F03 | 925 | 881 | 840 | 800 | 760 | 150 | 721 | 157 | 681 | 162 | 645 | 169 |
| F04^ | 882 | 841 | 800 | 760 | 719 | 138 | 678 | 144 | 641 | 151 | 602 | 157 |
| F05 | 1330 | 1295 | 1273 | 1251 | 1223 | 358 | 1195 | 366 | 1168 | 375 | 1142 | 385 |
| F06 | 1130 | 1090 | 1059 | 1022 | 991 | 230 | 957 | 237 | 926 | 246 | 895 | 255 |
| F07 | 1158 | 1113 | 1090 | 1057 | 1024 | 247 | 996 | 258 | 964 | 264 | 935 | 271 |
| F08 | 1270 | 1235 | 1208 | 1179 | 1147 | 304 | 1119 | 312 | 1088 | 322 | 1060 | 329 |
| F09 | 1417 | 1380 | 1359 | 1336 | 1314 | 408 | 1288 | 419 | 1261 | 430 | 1238 | 440 |

### DR80SN0603A* (TEMP RANGE 20–50°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 659 | 599 | 542 | 490 | 437 | 89 | 383 | 95 | 320 | 102 | N/A | N/A |
| F02 | 1268 | 1221 | 1188 | 1154 | 1122 | 336 | 1091 | 344 | 1060 | 353 | 1029 | 361 |
| F03 | 1087 | 1044 | 1008 | 973 | 938 | 234 | 905 | 242 | 871 | 249 | 841 | 257 |
| F04^ | 1118 | 1070 | 1033 | 997 | 963 | 243 | 929 | 251 | 896 | 260 | 865 | 267 |
| F05 | 1308 | 1262 | 1224 | 1197 | 1167 | 332 | 1141 | 341 | 1117 | 352 | 1089 | 361 |
| F06 | 868 | 823 | 780 | 741 | 699 | 148 | 662 | 154 | 624 | 160 | 584 | 167 |
| F07 | 922 | 877 | 835 | 795 | 757 | 165 | 718 | 173 | 679 | 180 | 642 | 187 |
| F08 | 1382 | 1341 | 1311 | 1291 | 1263 | 435 | 1234 | 443 | 1206 | 453 | 1177 | 464 |
| F09 | 1492 | 1448 | 1409 | 1381 | 1354 | 460 | 1332 | 470 | 1310 | 481 | 1288 | 491 |

### DR80SN0604B* (TEMP RANGE 20–50°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 764 | 695 | 630 | 559 | 485 | 95 | 415 | 102 | 358 | 109 | N/A | N/A |
| F02 | 1287 | 1235 | 1191 | 1147 | 1104 | 244 | 1062 | 252 | 1020 | 263 | 979 | 272 |
| F03 | 1339 | 1301 | 1258 | 1217 | 1174 | 270 | 1131 | 279 | 1090 | 289 | 1048 | 299 |
| F04^ | 1396 | 1346 | 1298 | 1257 | 1217 | 289 | 1175 | 299 | 1135 | 308 | 1098 | 319 |
| F05 | 1185 | 1135 | 1088 | 1040 | 992 | 203 | 947 | 211 | 901 | 219 | 855 | 227 |
| F06 | 1500 | 1460 | 1420 | 1360 | 1380 | 337 | 1294 | 353 | 1256 | 365 | 1219 | 380 |
| F07 | 1591 | 1539 | 1493 | 1454 | 1416 | 391 | 1379 | 402 | 1347 | 412 | 1311 | 424 |
| F08 | 1675 | 1622 | 1583 | 1545 | 1510 | 447 | 1474 | 459 | 1440 | 473 | 1402 | 482 |
| F09 | 1790 | 1741 | 1701 | 1668 | 1631 | 531 | 1599 | 546 | 1567 | 560 | 1532 | 570 |

*(Note: F06 row for this model shows 0.4"=1360 then 0.5"=1380 in the source — that's not a transcription error on my end, the manual's own table dips and climbs there. Flagging it so you don't think I fat-fingered it.)*

### DR80SN0803B* (TEMP RANGE 35–65°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 710 | 646 | 580 | 515 | 432 | 79 | 367 | 85 | 314 | 90 | 274 | 95 |
| F02 | 1298 | 1255 | 1216 | 1178 | 1140 | 242 | 1102 | 253 | 1067 | 263 | 1028 | 273 |
| F03 | 1209 | 1166 | 1124 | 1083 | 1045 | 208 | 1005 | 217 | 964 | 227 | 923 | 236 |
| F04^ | 1138 | 1091 | 1045 | 1001 | 959 | 181 | 920 | 188 | 876 | 197 | 832 | 208 |
| F05 | 1391 | 1352 | 1314 | 1278 | 1241 | 288 | 1209 | 298 | 1175 | 311 | 1140 | 242* |
| F06 | 977 | 931 | 880 | 836 | 785 | 135 | 734 | 142 | 683 | 151 | 626 | 158 |
| F07 | 1036 | 985 | 940 | 895 | 848 | 150 | 799 | 158 | 751 | 167 | 705 | 175 |
| F08 | 1456 | 1414 | 1376 | 1341 | 1302 | 315 | 1270 | 327 | 1238 | 337 | 1200 | 352 |
| F09 | 1533 | 1488 | 1452 | 1415 | 1383 | 360 | 1350 | 370 | 1317 | 381 | 1286 | 393 |

*(\*F05 @ 0.8" watts = 242 in the source text — that's lower than the 0.7" watts of 311, which doesn't track with every other row's climbing trend. Could be a manual typo (possibly meant 342 or similar). Don't treat that one number as gospel — if you're sizing off F05 at 0.8" ESP on this model, verify against the actual printed page or an amp-draw check in the field rather than trusting that digit.)*

### DR80SN0804B* (TEMP RANGE 35–65°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 841 | 657 | 595 | 522 | 439 | 90 | 367 | 97 | 315 | 102 | N/A | N/A |
| F02 | 1141 | 1089 | 1045 | 1001 | 958 | 192 | 914 | 200 | 869 | 207 | 823 | 214 |
| F03 | 1311 | 1267 | 1226 | 1189 | 1150 | 253 | 1114 | 264 | 1072 | 275 | 1034 | 283 |
| F04^ | 1395 | 1347 | 1309 | 1270 | 1233 | 291 | 1199 | 302 | 1164 | 312 | 1125 | 323 |
| F05 | 1490 | 1447 | 1407 | 1373 | 1336 | 339 | 1303 | 351 | 1269 | 360 | 1237 | 373 |
| F06 | 1553 | 1510 | 1469 | 1435 | 1401 | 372 | 1368 | 384 | 1335 | 395 | 1300 | 408 |
| F07 | 1593 | 1548 | 1508 | 1474 | 1440 | 392 | 1409 | 405 | 1376 | 415 | 1343 | 429 |
| F08 | 1776 | 1735 | 1695 | 1661 | 1628 | 514 | 1601 | 529 | 1570 | 542 | 1542 | 555 |
| F09 | 1853 | 1812 | 1773 | 1739 | 1708 | 569 | 1679 | 585 | 1650 | 599 | 1623 | 614 |

*(F01 @ 0.1" shows 841 in the source, which is oddly close to the F02 value — the table's own trend for F01 on every other model is in the 650–850 range at 0.1", so this is plausible as printed, just flagging it reads a little high next to its own F02.)*

### DR80SN0805C* (TEMP RANGE 35–65°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 837 | 752 | 671 | 576 | 501 | 100 | 426 | 107 | 361 | 113 | 315 | 119 |
| F02 | 1316 | 1270 | 1218 | 1166 | 1114 | 217 | 1061 | 227 | 1000 | 238 | 962 | 251 |
| F03 | 1353 | 1323 | 1286 | 1235 | 1183 | 242 | 1131 | 253 | 1085 | 263 | 1040 | 275 |
| F04^ | 1587 | 1544 | 1506 | 1459 | 1416 | 333 | 1372 | 345 | 1323 | 358 | 1281 | 369 |
| F05 | 1731 | 1673 | 1632 | 1587 | 1546 | 398 | 1506 | 414 | 1463 | 426 | 1421 | 440 |
| F06 | 1794 | 1744 | 1709 | 1671 | 1632 | 444 | 1591 | 459 | 1555 | 474 | 1513 | 489 |
| F07 | 1861 | 1805 | 1761 | 1720 | 1681 | 481 | 1642 | 496 | 1603 | 509 | 1565 | 524 |
| F08 | 1910 | 1873 | 1839 | 1798 | 1761 | 525 | 1723 | 545 | 1686 | 559 | 1648 | 574 |
| F09 | 2110 | 2055 | 2035 | 2003 | 1973 | 700 | 1946 | 724 | 1907 | 731 | 1890 | 750 |

*(2-stage outdoor override applies to this model: Y1 = F02, Y2 = F08 — not the "F04/F05" family default.)*

### DR80SN1005C* (TEMP RANGE 35–65°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 802 | 724 | 637 | 551 | 468 | 87 | 389 | 95 | 342 | 100 | 294 | 106 |
| F02 | 1405 | 1356 | 1308 | 1262 | 1210 | 241 | 1182 | N/A* | 1155 | 252 | 1102 | 264 |
| F03 | 1574 | 1531 | 1484 | 1440 | 1392 | 320 | 1357 | 331 | 1306 | 342 | 1256 | 355 |
| F04^ | 1619 | 1575 | 1526 | 1489 | 1446 | 336 | 1404 | 352 | 1355 | 361 | 1313 | 374 |
| F05 | 1688 | 1641 | 1600 | 1557 | 1513 | 367 | 1477 | 383 | 1428 | 398 | 1381 | 405 |
| F06 | 1811 | 1769 | 1730 | 1686 | 1649 | 443 | 1610 | 456 | 1572 | 468 | 1525 | 482 |
| F07 | 1857 | 1812 | 1774 | 1733 | 1697 | 475 | 1662 | 489 | 1622 | 505 | 1586 | 518 |
| F08 | 1892 | 1850 | 1805 | 1774 | 1735 | 496 | 1692 | 511 | 1658 | 523 | 1621 | 537 |
| F09 | 2116 | 2073 | 2039 | 2005 | 1981 | 675 | 1945 | 688 | 1909 | 707 | 1879 | 728 |

*(\*F02 @ 0.6" watts is printed `#N/A` in the source manual itself — not my extraction choking, the manual actually shows that as a blank/error cell. No watts value available for that one cell.)*

### DR80SN1205D* (TEMP RANGE 40–70°)
| Tap | 0.1 CFM | 0.2 CFM | 0.3 CFM | 0.4 CFM | 0.5 CFM | 0.5 W | 0.6 CFM | 0.6 W | 0.7 CFM | 0.7 W | 0.8 CFM | 0.8 W |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | 851 | 774 | 692 | 615 | 535 | 105 | 470 | 111 | 411 | 118 | 359 | 124 |
| F02 | 1677 | 1629 | 1583 | 1540 | 1498 | 408 | 1449 | 422 | 1399 | 436 | 1349 | 450 |
| F03 | 1537 | 1489 | 1444 | 1404 | 1365 | 335 | 1322 | 348 | 1272 | 360 | 1211 | 372 |
| F04^ | 1416 | 1365 | 1315 | 1267 | 1220 | 277 | 1163 | 285 | 1106 | 296 | 1048 | 306 |
| F05 | 1154 | 1098 | 1043 | 983 | 932 | 177 | 874 | 187 | 819 | 196 | 755 | 205 |
| F06 | 1806 | 1764 | 1729 | 1688 | 1654 | 489 | 1615 | 503 | 1578 | 519 | 1535 | 535 |
| F07 | 1869 | 1816 | 1773 | 1731 | 1693 | 521 | 1661 | 535 | 1629 | 548 | 1589 | 560 |
| F08 | 1947 | 1903 | 1865 | 1833 | 1802 | 604 | 1769 | 621 | 1743 | 640 | 1708 | 654 |
| F09 | 2107 | 2066 | 2030 | 1996 | 1963 | 734 | 1932 | 753 | 1899 | 772 | 1867 | 788 |

*(2-stage outdoor override applies to this model: Y1 = F05, Y2 = F06.)*

---

## Heating Airflow — Taps F01–F04 Only, All 8 Models

Taps F05–F09 are **not used on the heating (W/W1) call** in this furnace family — the manual only publishes heating CFM/rise for F01–F04 because those are the only taps within the family's design temp-rise range for a W/W1 call. `^^` = not recommended for heating (minimum tap, shown for reference). `^` = default & recommended heating tap.

Format below: CFM / °Rise at each ESP, 0.1" through 0.8" (rise only published through 0.5"; CFM continues through 0.8").

### DR80SN0403A* — TEMP RANGE 25–55°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 658 / N/A | 585 / N/A | 545 / N/A | 495 / N/A | 444 / N/A | 390 | 332 | 151 |
| F02^ | 749 / 40 | 697 / 42 | 652 / 45 | 607 / 49 | 554 / 53 | 509 | 459 | 406 |
| F03 | 925 / 32 | 881 / 34 | 840 / 35 | 800 / 37 | 760 / 39 | 721 | 681 | 645 |
| F04 | 882 / 34 | 841 / 35 | 800 / 37 | 760 / 39 | 719 / 41 | 678 | 641 | 602 |

### DR80SN0603A* — TEMP RANGE 20–50°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 659 / N/A | 599 / N/A | 542 / N/A | 490 / N/A | 437 / N/A | 383 | 320 | N/A |
| F02^ | 1268 / 35 | 1221 / 36 | 1188 / 37 | 1154 / 38 | 1122 / 40 | 1091 | 1060 | 1029 |
| F03 | 1087 / 41 | 1044 / 43 | 1008 / 44 | 973 / 46 | 938 / 47 | 905 | 871 | 841 |
| F04 | 1118 / 40 | 1070 / 42 | 1033 / 43 | 997 / 45 | 963 / 46 | 929 | 896 | 865 |

### DR80SN0604B* — TEMP RANGE 20–50°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 764 / N/A | 695 / N/A | 630 / N/A | 559 / N/A | 485 / N/A | 415 | 358 | N/A |
| F02^ | 1287 / 35 | 1235 / 36 | 1191 / 37 | 1147 / 39 | 1104 / 40 | 1062 | 1020 | 979 |
| F03 | 1339 / 33 | 1301 / 34 | 1258 / 35 | 1217 / 37 | 1174 / 38 | 1131 | 1090 | 1048 |
| F04 | 1396 / 32 | 1346 / 33 | 1298 / 34 | 1257 / 35 | 1217 / 37 | 1175 | 1135 | 1098 |

### DR80SN0803B* — TEMP RANGE 35–65°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 710 / N/A | 646 / N/A | 580 / N/A | 515 / N/A | 432 / N/A | 367 | 314 | 274 |
| F02^ | 1298 / 46 | 1255 / 47 | 1216 / 49 | 1178 / 50 | 1140 / 52 | 1102 | 1067 | 1028 |
| F03 | 1209 / 49 | 1166 / 51 | 1124 / 53 | 1083 / 55 | 1045 / 57 | 1005 | 964 | 923 |
| F04 | 1138 / 52 | 1091 / 54 | 1045 / 57 | 1001 / 59 | 959 / 62 | 920 | 876 | 832 |

### DR80SN0804B* — TEMP RANGE 35–65°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 841 / N/A | 657 / N/A | 595 / N/A | 522 / N/A | 439 / N/A | 367 | 315 | N/A |
| F02^ | 1141 / 52 | 1089 / 54 | 1045 / 57 | 1001 / 59 | 958 / 62 | 914 | 869 | 823 |
| F03 | 1311 / 45 | 1267 / 47 | 1226 / 48 | 1189 / 50 | 1150 / 52 | 1114 | 1072 | 1034 |
| F04 | 1395 / 42 | 1347 / 44 | 1309 / 45 | 1270 / 47 | 1233 / 48 | 1199 | 1164 | 1125 |

### DR80SN0805C* — TEMP RANGE 35–65°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 837 / N/A | 752 / N/A | 671 / N/A | 576 / N/A | 501 / N/A | 426 | 361 | 315 |
| F02^ | 1316 / 45 | 1270 / 47 | 1218 / 49 | 1166 / 51 | 1114 / 53 | 1061 | 1000 | 962 |
| F03 | 1353 / 44 | 1323 / 45 | 1286 / 46 | 1235 / 48 | 1183 / 50 | 1131 | 1085 | 1040 |
| F04 | 1587 / 37 | 1544 / 38 | 1506 / 39 | 1459 / 41 | 1416 / 42 | 1372 | 1323 | 1281 |

### DR80SN1005C* — TEMP RANGE 35–65°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01^^ | 802 / N/A | 724 / N/A | 637 / N/A | 551 / N/A | 468 / N/A | 389 | 342 | 294 |
| F02^ | 1405 / 53 | 1356 / 55 | 1308 / 57 | 1262 / 59 | 1210 / 61 | 1155 | 1102 | 1057 |
| F03 | 1574 / 47 | 1531 / 48 | 1484 / 50 | 1440 / 51 | 1392 / 53 | 1357 | 1306 | 1256 |
| F04 | 1619 / 46 | 1575 / 47 | 1526 / 49 | 1489 / 50 | 1446 / 51 | 1404 | 1355 | 1313 |

### DR80SN1205D* — TEMP RANGE 40–70°, call = W/W1
| Tap | 0.1" CFM/Rise | 0.2" CFM/Rise | 0.3" CFM/Rise | 0.4" CFM/Rise | 0.5" CFM/Rise | 0.6" CFM | 0.7" CFM | 0.8" CFM |
|---|---|---|---|---|---|---|---|---|
| F01 | 851 / N/A | 774 / N/A | 692 / N/A | 615 / N/A | 535 / N/A | 470 | 411 | 359 |
| F02^ | 1677 / 53 | 1629 / 55 | 1583 / 56 | 1540 / 58 | 1498 / 59 | 1449 | 1399 | 1349 |
| F03 | 1537 / 58 | 1489 / 60 | 1444 / 62 | 1404 / 63 | 1365 / 65 | 1322 | 1272 | 1211 |
| F04^^ | 1416 / N/A | 1365 / N/A | 1315 / N/A | 1267 / N/A | 1220 / N/A | 1163 | 1106 | 1048 |

*(Note: on the 1205D*, F04 is flagged `^^` not recommended, and F02 is the default/recommended tap — opposite of every other model in the family, where F01 is the not-recommended floor and F02 is still default. Still F02 default across the board, just the "don't use this one for heat" tap flips to F04 on the biggest unit.)*

---

## Heads up — found a second furnace family in this same manual

While pulling this, I found the same PDF (IM-IOD-2035A) also contains a separate airflow table set for a **DD80SN** family, starting right after the DR80SN heating table ends. I haven't pulled that one yet since you asked specifically about F01–F09 and didn't name a model — let me know if you're actually working on a DD80SN unit and I'll pull that table too, same format, verified against the source the same way.
