# DAIKIN R-32 CHARGING REFERENCE
Compiled for Casteel Heating and Air from Daikin spec sheets (SS) and installation manuals (IM/IOD). Every number below is as printed in those documents. Rules for whoever reads this: do NOT guess or fill gaps. If a value is not here, say it is not in this file and tell the tech to check the unit nameplate / installation manual. Items marked CONFIRM have a mapping issue noted.

Everything in this file is R-32 equipment. There is NO R-410A charging chart in this collection.

---
## 1. GENERAL RULES (from the manuals)
- Units are factory charged for a 15 ft line set of 3/8" liquid line (spec sheet note). Add charge for line length beyond that.
- Daikin's manual says the Factory Charge on the install manual's charge table may differ from the nameplate. If so, calculate the Additional Charge so the Total Refrigerant Charge in the table is kept (3P761829-1B p27).
- Nameplate is the final authority on factory charge amount.
- Spec sheets for DC7TC, DC5SE, DC4SE, DC4SQ, DH5SE and DH4SE print the factory charge with NO unit of measure. Other Daikin R-32 sheets use ounces. The unit is not confirmed. Check the nameplate.
- Complete charging info for the SE/SQ units is said to be in Service Manual RS6200006, which we never found on an official site. RS6200301 (the service manual Daikin links) agrees with the install manuals on the TXV superheat/subcool tables.

---
## 2. INVERTER FIT UNITS: DC9VS, DC6VS, DH6VS, DH7VS, DH9VS
Docs: IM 3P761829-1B (DC6VS/DH6VS/DC9VS 24-48/DH7VS 24-48) and IM 3P679063-5L (DH9VS, DH7VS 60, DC9VS 60). Spec sheets SS-xxVS-R32 p.3-4.

**Method (3P761829-1B p30-31; 3P679063-5L p24-26):**
1. Weigh in the charge using the IM line-set total-charge table (Step 1).
2. Then verify subcooling with the thermostat's CHARGE VERIFICATION TEST.
3. The test only works at 65-105 F outdoor ambient, and only while the control board alternates "cha" and the subcool value on its display.
4. Outside 65-105 F: weigh in the charge. Do not rely on the verification test.
5. Do not add more than 8 oz to reach the target.
6. If heat is on at the thermostat, the control cannot enter charging mode (code 49 / E49, "Please set thermostat to off position"). Turn the heat off at the thermostat first.
No single oz/ft number is printed for these. Use the IM total-charge tables (oz per 5 ft of line, by liquid/suction size): 3P761829-1B pp27-29 and 3P679063-5L p24. Those tables are NOT transcribed in this file. Use the manual pages.

**Factory charge by model.** SS = spec sheet, IM = install manual table. They differ by 1-2 oz in many cases, as printed.
| Model | Tons | Liquid | Suction (rated line) | SS charge | IM factory charge |
|---|---|---|---|---|---|
| DC9VSA2410A* | 2 | 3/8" | 7/8" | 76 oz | 75 oz |
| DC9VSA3610A* | 3 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DC9VSA4810A* | 4 | 3/8" | 1-1/8" | 118 oz | 118 oz |
| DC9VSA6010A* | 5 | 3/8" | 1-1/8" | 162 oz | 162 oz |
| DC6VSS1810A* / DC6VSA181WA* | 1.5 | 3/8" | 3/4" | 74 oz | 73 oz |
| DC6VSS2410A* / DC6VSA241WA* | 2 | 3/8" | 3/4" | 74 oz | 73 oz |
| DC6VSS3010A* / DC6VSA301WA* | 2.5 | 3/8" | 7/8" | 76 oz | 75 oz |
| DC6VSS3610A* / DC6VSA361WA* | 3 | 3/8" | 7/8" | 83 oz | 81 oz |
| DC6VSS4210A* | 3.5 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DC6VSS4810A* | 4 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DC6VSS6010A* | 5 | 3/8" | 1-1/8" | 118 oz | 118 oz |
| DH6VSA1810A* | 1.5 | 3/8" | 3/4" | 74 oz | 73 oz |
| DH6VSA2410A* | 2 | 3/8" | 3/4" | 74 oz | 73 oz |
| DH6VSA3010A* | 2.5 | 3/8" | 7/8" | 76 oz | 75 oz |
| DH6VSA3610A* | 3 | 3/8" | 7/8" | 83 oz | 81 oz |
| DH6VSA4210A* | 3.5 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DH6VSA4810A* | 4 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DH6VSA6010A* | 5 | 3/8" | 1-1/8" | 118 oz | 118 oz |
| DH7VSA2410A* | 2 | 3/8" | 7/8" | 76 oz | 75 oz |
| DH7VSA3610A* | 3 | 3/8" | 1-1/8" | 100 oz | 99 oz |
| DH7VSA4210A* | 3.5 | 3/8" | 1-1/8" | 118 oz | 118 oz |
| DH7VSA4810A* | 4 | 3/8" | 1-1/8" | 118 oz | 118 oz |
| DH7VSA6010A* | 5 | 3/8" | 1-1/8" | 162 oz | 162 oz |
| DH9VSA241CA* | 2 | 3/8" | 7/8" | 162 oz | 162 oz |
| DH9VSA361CA* | 3 | 3/8" | 7/8" | 162 oz | 162 oz |
| DH9VSA4810A* | 4 | 3/8" | 1-1/8" | 162 oz | 162 oz (4-ton appears only on the spec sheet; the IM does not list it) |
| DH9VSA6010A* | 5 | 3/8" | 1-1/8" | 162 oz | 162 oz |
The spec sheet suction size is the AHRI-rated line size. The unit's actual suction valve connection is different; the spec sheet says the installer supplies adapters for 7/8" to 1-1/8".

**Target subcooling, as printed (+/- 1 F each).** SS = spec sheet "Subcooling at Service Valve". TEST = CHARGE VERIFICATION TEST table (IM p31). FULL = Full-capacity charging table (IM p31).
- DC9VS (clean 1:1 match by tonnage): 2T = SS 14, TEST 8, FULL 14. 3T = SS 8, TEST 8, FULL 8. 4T = SS 9, TEST 10, FULL 9. 5T = 11 (IM 3P679063-5L p26 charging table, 65-105 F OD).
- DH7VS: 2T = SS 14, TEST 8, FULL 14. 3T = SS 9, TEST 8, FULL 8 (Daikin's own documents disagree here: SS says 9, IM says 8). 3.5T and 4T = SS 9, TEST 10, FULL 9. 5T = 11 (3P679063-5L p26).
- DH9VS (all sizes): 11 (3P679063-5L p26, 65-105 F OD).
- DH6VS, in row order 1.5T / 2T / 2.5T / 3T / 3.5T / 4T / 5T (CONFIRM against IM p31 for the exact tonnage, mapped by order from our extraction):
  1.5T: SS 10, TEST 7, FULL 10
  2T: SS 12, TEST 8 (see note), FULL 12
  2.5T: SS 14, TEST 8, FULL 14
  3T: SS 15, TEST 9, FULL 15
  3.5T: SS 8, TEST 8, FULL 8
  4T: SS 9, TEST 8, FULL 9
  5T: SS 9, TEST 10, FULL 9
  Note from the IM: the 2-ton DC6VSA/DC6VSS/DH6VSA target is 10 +/- 1 F when OD ambient is below 80 F.
- DC6VS: same values as DH6VS for the same tonnages (CONFIRM). The DC6VSA361WA (3T) row shows 13 (TEST 9, FULL 13) in our extraction, a different value from DC6VSS3610A. CONFIRM on IM p31.

---
## 3. SINGLE-STAGE / TWO-STAGE SE/SQ UNITS: DC5SE, DC4SE, DC4SQ, DH5SE, DH4SE
Docs: IOD-4048C (DC5SE/DC4SQ/DC4SE), IOD-4047A (DH4SE), IOD-4064A (DH5SE), RS6200301 p40, spec sheets.

**Cooling method (DC5SE/DC4SE/DC4SQ, IOD-4048C p9):**
- TXV indoor coil: charge by SUBCOOLING only.
- Piston (fixed orifice) indoor coil: use the superheat table (IOD-4048C p9).
- Outdoor temperature must be 60 F or higher.
- Two-stage units: charge at LOW stage.
**Heat pumps (DH4SE IOD-4047A p11, DH5SE IOD-4064A p11):** TXV systems charge by subcooling (8 +/- 1 F). Heating mode charge is by weight with line adjustments. Make final adjustments in cooling.

**Additional charge per foot beyond 15 ft (IOD-4048C p8, IOD-4047A p8, IOD-4064A p8, "Initial Charge Addition per Foot (oz)"):**
| Liquid line | Suction line | oz per ft |
|---|---|---|
| 3/8" | 5/8" | 0.53 |
| 3/8" | 3/4" | 0.55 |
| 3/8" | 7/8" | 0.58 |
| 3/8" | 1-1/8" | 0.64 |
| 1/4" | 5/8" | 0.23 |

**Target values as printed:**
- DC5SE (IOD-4048C p11, table printed as an image, read visually; matches RS6200301 p40): 1.5T-4.0T: subcool 7-9 F at OD liquid, superheat 10-12 F at compressor. 5.0T: subcool 5-7 F, superheat 10-12 F. The older revision IOD-4048B printed the first row as 1.5T-2.5T only.
- DC4SE / DC4SQ (IOD-4048C p11): text says subcool 8 +/- 1 F. The TXV table has two rows: subcool 7-9 F with superheat 10-14 F, and subcool 7-9 F with superheat 9-11 F. Which tonnages go with which row is NOT clear in our extraction. CONFIRM on IOD-4048C p11. (RS6200301 labels the same tables as the GLXS4B/ALXS4B family and the GLXS3B/ALXS3B family; values agree.)
- DH4SE (IOD-4047A p11): subcool at liquid valve 8 +/- 1 F (cooling). Superheat at compressor in the four rows as printed: 19, 17, 15, 16 F (+/- 1) in cooling; 8 F (+/- 1) in heating. Only the 3.0-ton is confirmed: 15 F in IOD-4047A (Aug 2024); the older IOD-4047 (Dec 2023) printed 16 F. Both revisions are still posted, the newer one presumably governs. The other tonnage mappings are CONFIRM.
- DH5SE (IOD-4064A p11): subcool at liquid valve 8 +/- 1 F (cooling). Superheat at compressor in the four rows as printed: 19, 18, 15, 16 F (+/- 1) in cooling (tonnage mapping CONFIRM). Heating superheat is 8 +/- 1 F in the table, but the running text on the same page says 5 +/- 1 F at 4-6" from the compressor for TXV outdoor units. Daikin's own page disagrees with itself, so look at the nameplate/manual. Two-stage 5-ton: superheat 16 +/- 1 F (low stage, cooling), subcool 6 +/- 1 F (low stage, cooling), heating superheat 5 +/- 1 F (high stage).

**Factory charge by model (spec sheet, NO UNIT PRINTED, probably oz, confirm on nameplate):**
| Model | Tons | Liquid | Suction |  Charge |
|---|---|---|---|---|
| DC5SEA1810A* | 1.5 | 3/8" | 3/4" | 54 |
| DC5SEA2410A* | 2 | 3/8" | 3/4" | 65 |
| DC5SEA3010A* | 2.5 | 3/8" | 3/4" | 87 |
| DC5SEA3610A* | 3 | 3/8" | 7/8" | 88 |
| DC5SEA4210A* | 3.5 | 3/8" | 1-1/8" | 141 |
| DC5SEA4810A* | 4 | 3/8" | 1-1/8" | 138 |
| DC5SEA6010A* | 5 | 3/8" | 1-1/8" | 167 |
| DC4SEA1810A* | 1.5 | 3/8" | 3/4" | 54 |
| DC4SEA2410A* | 2 | 3/8" | 3/4" | 58 |
| DC4SEA3010A* | 2.5 | 3/8" | 3/4" | 64 |
| DC4SEA3610A* | 3 | 3/8" | 7/8" | 69 |
| DC4SEA4210A* | 3.5 | 3/8" | 1-1/8" | 83 |
| DC4SEA4810A* | 4 | 3/8" | 1-1/8" | 91 |
| DC4SEA6010A* | 5 | 3/8" | 1-1/8" | 94 |
| DC4SQA1810A* | 1.5 | 3/8" | 3/4" | 53 |
| DC4SQA2410A* | 2 | 3/8" | 3/4" | 53 |
| DC4SQA3010A* | 2.5 | 3/8" | 3/4" | 63 |
| DC4SQA3610A* | 3 | 3/8" | 7/8" | 69 |
| DC4SQA4210A* | 3.5 | 3/8" | 1-1/8" | 83 |
| DC4SQA4810A* | 4 | 3/8" | 1-1/8" | 91 |
| DC4SQA6010A* | 5 | 3/8" | 1-1/8" | 94 |
| DH5SEA1810A* | 1.5 | 3/8" | 3/4" | 88 |
| DH5SEA2410A* | 2 | 3/8" | 3/4" | 83 |
| DH5SEA3010A* | 2.5 | 3/8" | 3/4" | 94 |
| DH5SEA3610A* | 3 | 3/8" | 7/8" | 95 |
| DH5SEA4210A* | 3.5 | 3/8" | 1-1/8" | 139 |
| DH5SEA4810A* | 4 | 3/8" | 1-1/8" | 174 |
| DH5SEA6010A* | 5 | 3/8" | 1-1/8" | 185 |
| DH4SEA1810* | 1.5 | 3/8" | 3/4" | 71 |
| DH4SEA2410* | 2 | 3/8" | 3/4" | 70 |
| DH4SEA3010* | 2.5 | 3/8" | 3/4" | 78 |
| DH4SEA3610* | 3 | 3/8" | 7/8" | 83 |
| DH4SEA4210* | 3.5 | 3/8" | 1-1/8" | 139 |
| DH4SEA4810* | 4 | 3/8" | 1-1/8" | 174 |
| DH4SEA6010* | 5 | 3/8" | 1-1/8" | 194 |

---
## 4. TWO-STAGE TC UNITS: DC7TC, DH7TC (GAP)
- No installation manual or service manual was found for these. Missing: charge per foot, charging procedure, target subcool, fault codes.
- DH7TC spec sheet says a specified TXV kit is required on the indoor coil (the outdoor unit determines the TXV). It prints "Design Subcooling 5-7 F at the liquid service valve, ARI 95 test conditions." That is a PERFORMANCE RATING CONDITION, not a field charging target.
- Factory charge (spec sheet): DC7TC (NO UNIT PRINTED): 2T 104, 3T 92, 4T 180, 5T 167. DH7TC (oz): 2T 103, 3T 129, 4T 229, 5T 198.
- Tell the tech to use the manual that ships with the unit.

---
## 5. CHARGE-RELATED FAULT CODES AND CHECKS
- E3: high-pressure switch tripped. Dirty condenser coil, blocked airflow, overcharge, or closed service valve. Clean coil, confirm outdoor fan runs, verify charge, confirm valves open.
- E4: low-pressure switch tripped. Refrigerant shortage/leak, restricted metering device, or closed valve. Leak-check, verify charge by weight/subcool, confirm valves open, check drier not plugged.
- F6: refrigerant overcharge detected. Overcharged, or a sensor giving a false high reading. Verify charge by weight against the nameplate; recover excess if confirmed.
- J7: subcooling heat exchanger liquid thermistor fault. J9: gas pipe purge / subcooling heat exchanger gas pipe thermistor fault. Check resistance vs chart, connector, wiring.
- 49 / E49: control cannot enter Charging Mode because indoor heat is on. Turn heat off at the thermostat.
- CoreSense (Amana ALXS/ALZS, Daikin DC/DH) alert flash 1, long run time (compressor running over 18 hrs): low charge, evaporator blower not running, frozen coil, bad metering device, liquid line restriction, thermostat problem.
- Pressure controls (Amana/Daikin condensers): high pressure opens 610 psig +/- 10, closes 420 +/- 25. Low pressure opens 21 psig, closes about 50.
- EEV coils/air handlers: indoor board controls superheat itself with thermistors and a pressure sensor; no field adjustment. A bad reading points to a sensor, wiring, or board (codes 70-75).

---
## 6. WHAT IS NOT IN THIS FILE
- The IM total-charge tables by line length (3P761829-1B pp27-29, 3P679063-5L p24) are not transcribed.
- No R-410A charging charts, no superheat table for piston-metered units (IOD-4048C p9 has it, not transcribed), no evacuation/micron/nitrogen procedures, no R-32 handling or A2L charging safety procedures beyond the leak-detection codes.
- No service manual for the R-32 inverter units. The SiUS612209EA/EB manual we have is for the R-410A DX6VS/DZ6VS.
