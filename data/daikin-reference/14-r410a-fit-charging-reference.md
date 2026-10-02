# DAIKIN FIT R-410A CHARGING REFERENCE (DX6VS / DZ6VS inverter outdoor units)
Compiled for James Ford (Casteel Heating and Air). Source documents: Daikin Installation & Service Reference for DX6VS***1*A* / DZ6VS***1*A* / DZ6VSA***1EA* (the Fit AC/HP install manual, 60 pages, dated 2023, page numbers below are that manual's printed pages) and Daikin service manual SiUS612209EB (same family, R-410A, with EA as the earlier revision, content the same for the sections used).
Rules for whoever reads this: do NOT guess or fill gaps. If a value is not in this file, say so and send the tech to the unit nameplate or the install manual. Items marked CONFIRM are flagged.
The R-32 Fit units (DC6VS, DH6VS, DC9VS, DH7VS, DH9VS) are a different refrigerant with different charge numbers. See the separate R-32 charging file. Do not mix them.

---
## 1. HOW THE CHARGE IS FIGURED (manual pp.23, 29)
Total Refrigerant Charge (A) = Factory Charge (B) + Additional Charge for line set (C).
- The charge tables (section 6) show (A) total oz and (C) additional oz for each line set length, tonnage, indoor unit type, and liquid/suction pipe size. Charge amounts for lengths in between the printed rows are found by linear approximation between rows.
- Factory Charge (B) may differ from the number on the nameplate. If so, calculate Additional Charge (C) so the Total Charge (A) in the table is kept.
- The unit ships with the charge for the matching indoor unit and a standard line set. Add charge only when the liquid line exceeds the factory charge length. The factory charge (B) is the (A) value in the "15 or less" row (the CHPE tables use a "12 or less" row) minus its (C); see section 5.
- Charge units are ounces (oz).
- Equivalent length of the elbows/bends on the suction line counts toward length. The manual's table prints 90 deg short radius 1.7 / 2 / 2.3, 90 deg long radius 1.5 / 1.7 / 1.6, 45 deg 0.7 / 0.8 / 1 for 3/4, 7/8, 1-1/8 suction ID, labeled "unit: inch" in the manual (that unit may be a misprint for feet, CONFIRM on p.15 before using it).

## 2. LINE SET LIMITS (pp.12, 15)
- Maximum line set EQUIVALENT length: 125 ft (includes elbows and bends). Maximum ACTUAL length: 100 ft.
- Maximum vertical elevation: 90 ft with the outdoor unit BELOW the indoor unit; 100 ft with the outdoor unit ABOVE the indoor unit (verified on the page diagram).
- Outdoor unit below indoor: an inverted loop is required in the suction line near the indoor connection; the top of the loop must be slightly higher than the top of the unit. The trap helps prevent liquid compression at the compressor on start-up.
- Allowable line set diameters, FIT (x = allowed; * = if normal ambient operating temperature is below 14 F, limit the line set to 50 ft max):
  - 1.5 ton: liquid 1/4, 5/16, 3/8; suction 5/8*, 3/4.
  - 2.0 ton: liquid 5/16, 3/8; suction 5/8*, 3/4.
  - 2.5 ton: liquid 5/16, 3/8; suction 3/4*, 7/8.
  - 3.0 ton: liquid 5/16, 3/8; suction 3/4*, 7/8.
  - 3.5, 4.0, 5.0 ton: liquid 3/8; suction 7/8, 1-1/8.
- Allowable line set diameters, ENHANCED CAPACITY FIT: 2.0 ton: liquid 5/16, 3/8; suction 3/4*, 7/8. 3.0, 3.5, 4.0 ton: liquid 3/8; suction 7/8, 1-1/8.
- Liquid line must be insulated if more than 50 ft of liquid line passes through an area that may reach 30 F or more above outdoor ambient in cooling, or if the conditioned space may be cooler than outdoor ambient in heating. Never attach a liquid line to an uninsulated portion of the suction line. Insulate the suction line.
- Reusing an old line set: flush with an HVAC flushing solvent to clean out oil and debris. Do not mix conventional refrigerant/oil with R-410A.
- Compressor PVE oil absorbs moisture fast. Do not leave the system open to atmosphere longer than necessary.
- Design pressure is 450 PSIG. Use refrigerant-grade copper only.

## 3. BRAZING, LEAK TEST, EVACUATION (pp.16-19)
- Remove Schrader valves from service valves before brazing. Braze with 2% minimum silver alloy, no flux. Wrap valves, sensors and the filter drier with a wet rag or heat trap compound; quench joints during and after brazing.
- Purge with nitrogen at 2 to 3 PSIG while brazing.
- A bi-flow filter drier ships separately and must be brazed in by the installer, recommended location before the expansion device at the indoor unit.
- Never use oxygen, high-pressure air or flammable gas for leak testing. The nitrogen line needs a regulator and a relief valve set to open at no more than 450 psig.
- Leak check with leak detector: charge to 10 PSIG with refrigerant, then finish to working pressure with nitrogen.
- Standing pressure test best practice: 450 PSIG nitrogen for a minimum of 4 hours.
- Recommended 3-step nitrogen test (printed with the 3.5-5.0 ton and enhanced 3.0-4.0 ton notes): 150 PSIG for 3 min; 325 PSIG for 5 min; 450 PSIG for 4 hours. Any pressure drop, find the leak, fix it, and repeat from step 1.
- Outdoor unit liquid and suction valves ship CLOSED to hold the charge. Do not open them until the indoor unit and line set are evacuated. All units should have high-voltage power connected 2 hours before startup.
- Standard evacuation: use a vacuum pump with 250 micron capability. Evacuate to 500 microns or less using BOTH the suction and liquid service valves. Close the pump valve and hold for 10 minutes. If pressure rises to 500 microns or less and stays steady, the system is leak-free. If it rises above 500 microns, there may be moisture, noncondensables or a small leak: return to the evacuation step, check for leaks, and repeat.
- Triple evacuation (recommended): (1) evacuate to 4000 microns, hold 15 min, break with dry nitrogen up to 2-3 PSIG, hold 20 min, release nitrogen. (2) Evacuate to 1500 microns, hold 20 min, break with nitrogen to 2-3 PSIG, hold 20 min. (3) Evacuate below 500 microns and hold for 60 min.
- Do not operate the unit in a vacuum or at negative pressure. Do not run suction pressure below 20 psig for more than 5 seconds (compressor overheats). Operating with the suction valve closed damages the compressor and is not covered by warranty.
- Use refrigerant certified to AHRI standards (used refrigerant can damage the compressor and void the warranty).
- Stop valve: ships closed. Open by turning counterclockwise with a hex wrench until the shaft stops, then (3.5-5.0 ton FIT and 3.0-4.0 ton Enhanced Capacity only, back-sealing type) turn to the specified torque, then replace the valve lid. Close by turning clockwise until the shaft stops, then to the torque. Torques as printed (p.17): FIT 1.5-2.0 ton: liquid 3/8" 4-6 lb-ft (3/16" wrench), gas 3/4" 14-16 lb-ft (5/16"), front sealing. FIT 2.5-3.0 ton: liquid 3/8" 4-6 lb-ft (3/16"), gas 7/8" 14-16 lb-ft (5/16"), front sealing. FIT 3.5-5.0 ton: liquid 3/8" 4-5 lb-ft (4 mm), gas 7/8" 14-16 lb-ft (8 mm), front and back sealing. ENHANCED CAPACITY FIT 2.0 ton: liquid 3/8" 4-6 lb-ft (3/16"), gas 7/8" 14-16 lb-ft (5/16"), front sealing; 3.0-4.0 ton: liquid 3/8" 4-5 lb-ft (4 mm), gas 7/8" 14-16 lb-ft (8 mm), front and back sealing. Service port torque 7.9-10.8 lb-ft (3.5-5.0 ton FIT and 3.0-4.0 ton Enhanced only). Valve cap: finger-tight plus 1/6 turn, with refrigerant oil on the threads and sealing surface.

## 4. CHARGING PROCEDURE (pp.29-30)
Step 2, charge by line set length: add the additional refrigerant calculated in Step 1 from the tables. Valves must be open and additional charge added per the chart before applying power. After the charge bleeds into the indoor unit, open the liquid service valve. Break vacuum by fully opening the liquid and suction base valves.
Step 3, system start-up test: on first power-up the outdoor unit displays E11, meaning the initial SYSTEM TEST must be run from the Daikin communicating thermostat setup. The test checks the equipment for about 10-15 minutes (longer if there is an error). Turn OFF the electric heater or gas furnace before the test. Thermostat must be OFF before choosing "CHARGE MODE."
Step 4, measure subcooling to verify charge:
1. Set the thermostat to CHARGE MODE. Use it if the required additional charge cannot be put in without running, and whenever adjusting subcooling. CHARGE MODE runs the equipment at full capacity for about two hours, then ends and the system returns to normal thermostat operation.
2. Turn off the electric heater and finish the SYSTEM START-UP TEST first. Charging equipment must use dedicated PVE oil gauges and hoses.
3. Purge the gauge lines. Connect the manifold to the liquid base valve service port. Convert liquid pressure to saturated temperature with a temperature/pressure chart. Install a thermometer on the liquid line at the liquid service valve (good contact, insulated). SUBCOOLING = saturated liquid temp minus liquid line temp.
4. Before adjusting, make sure outdoor ambient is within the charging table range and the unit is running at 100% capacity. When ready, the 7-segment display alternates "cha" and the current subcooling value. At 65-105 F ambient the display shows the current subcooling value.
5. If subcooling is not in range: LOW subcooling, add charge; HIGH subcooling, remove charge.
6. Not more than 8 oz may be added to reach target. Recommended: add 1 oz at a time, then wait 10 minutes to stabilize.
7. The "cha" display can keep flashing if the system is not in condition. Subcool adjustment is not available then; complete charging per Steps 1 and 2 first.
8. Subcooling info is valid only while "cha" and the current subcooling value alternate on the board.
9. Do NOT adjust the charge based on suction pressure.
10. Check the Schrader ports for leaks and tighten valve cores if needed; install caps finger-tight.
11. To achieve rated performance, measure subcooling with a pressure gauge and a temperature sensor.

**Target subcooling, +/- 1 F, valid at 65 F to 105 F outdoor ambient. Below 65 F or above 105 F: WEIGH IN the charge (the subcooling target does not apply).**
FIT (p.29):
| Tonnage | DX6VSA | DX6VSS | DZ6VSA |
|---|---|---|---|
| 1.5 ton | 10 | 10 | 10 |
| 2.0 ton | 12 | 12 | 12 |
| 2.5 ton | 14 | 14 | 14 |
| 3.0 ton | 13 | 15 | 15 |
| 3.5 ton | not listed | 8 | 8 |
| 4.0 ton | not listed | 9 | 9 |
| 5.0 ton | not listed | 9 | 9 |
ENHANCED CAPACITY FIT, DZ6VSA***E (p.30): 2.0 ton 14; 3.0 ton 8; 3.5 ton 9; 4.0 ton 9 (all +/- 1 F).
The FIT table's column headings and the "-" cells were read from the printed table text; if a tech is charging a 3.0 ton, check the model prefix against the column before trusting 13 vs 15.

**R-410A saturated liquid pressure to temperature (p.30, as printed):**
PSIG:F  200:70, 205:72, 210:73, 215:75, 220:76, 225:77, 230:79, 235:80, 240:81, 245:83, 250:84, 255:85, 260:87, 265:88, 270:89, 275:90, 280:91, 285:92, 290:94, 295:95, 300:96, 305:97, 310:98, 320:100, 330:102, 340:105, 350:107, 360:109, 370:111, 380:113, 390:115, 400:117, 410:118, 420:120, 430:122, 440:124, 450:126, 460:127, 470:129, 480:131, 490:133, 500:134, 510:136, 520:137.

## 5. FACTORY CHARGE (B) BY MODEL FAMILY, computed from the "15 or less" / "12 or less" row of each table as A minus C
Only combinations the manual prints a value for are listed. Nameplate is the final authority.
- AC (DX6VS), 1.5 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.23 (row "15 or less"): 3/8" liq x 3/4" suc = 76 oz
- AC (DX6VS), 2.0 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.23 (row "15 or less"): 3/8" liq x 3/4" suc = 76 oz
- AC (DX6VS), 2.5 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.24 (row "15 or less"): 3/8" liq x 7/8" suc = 79 oz
- AC (DX6VS), 3.0 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.24 (row "15 or less"): 3/8" liq x 7/8" suc = 85 oz
- AC (DX6VS), 3.5 - 4.0 ton FIT, indoor DFVE, DV**FEC, p.24 (row "15 or less"): 3/8" liq x 1-1/8" suc = 111 oz
- AC (DX6VS), 5.0 ton FIT, indoor DFVE, DV**FEC, p.24 (row "15 or less"): 3/8" liq x 1-1/8" suc = 131 oz
- AC (DX6VS), 1.5 ton FIT, indoor CHPE, p.25 (row "12 or less"): 3/8" liq x 3/4" suc = 76 oz
- AC (DX6VS), 2.0 ton FIT, indoor CHPE, p.25 (row "12 or less"): 3/8" liq x 3/4" suc = 76 oz
- AC (DX6VS), 2.5 ton FIT, indoor CHPE, p.25 (row "12 or less"): 3/8" liq x 3/4" suc = 79 oz
- AC (DX6VS), 3.0 ton FIT, indoor CHPE, p.25 (row "12 or less"): 3/8" liq x 7/8" suc = 85 oz
- AC (DX6VS), 3.5 - 4.0 ton FIT, indoor CAPE, CHPE, p.26 (row "12 or less"): 3/8" liq x 7/8" suc = 111 oz; 3/8" liq x 1-1/8" suc = 111 oz
- AC (DX6VS), 5.0 ton FIT, indoor CAPE, CHPE, p.26 (row "12 or less"): 3/8" liq x 7/8" suc = 131 oz; 3/8" liq x 1-1/8" suc = 131 oz
- HP (DZ6VS), 1.5 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.26 (row "15 or less"): 3/8" liq x 5/8" suc = 81 oz; 3/8" liq x 3/4" suc = 81 oz
- HP (DZ6VS), 2.0 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.26 (row "15 or less"): 3/8" liq x 5/8" suc = 81 oz; 3/8" liq x 3/4" suc = 81 oz
- HP (DZ6VS), 2.5 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.27 (row "15 or less"): 3/8" liq x 3/4" suc = 88 oz; 3/8" liq x 7/8" suc = 88 oz
- HP (DZ6VS), 3.0 ton FIT, indoor CAPEA, DFVE, DV**FEC, p.27 (row "15 or less"): 3/8" liq x 3/4" suc = 88 oz; 3/8" liq x 7/8" suc = 88 oz
- HP (DZ6VS), 2.0 ton Enhanced Capacity FIT, indoor CAPEA, DFVE, DV**FEC, p.27 (row "15 or less"): 3/8" liq x 3/4" suc = 88 oz; 3/8" liq x 7/8" suc = 88 oz
- HP (DZ6VS), 3.0 ton Enhanced Capacity FIT, indoor DFVE, DV**FEC, p.27 (row "15 or less"): 3/8" liq x 1-1/8" suc = 118 oz
- HP (DZ6VS), 3.5 - 4.0 ton FIT, indoor DFVE, DV**FEC, p.28 (row "15 or less"): 3/8" liq x 1-1/8" suc = 118 oz
- HP (DZ6VS), 5.0 ton FIT, indoor DFVE, DV**FEC, p.28 (row "15 or less"): 3/8" liq x 1-1/8" suc = 127 oz
- HP (DZ6VS), 3.5 ton Enhanced Capacity FIT, indoor DFVE, DV**FEC, p.28 (row "15 or less"): 3/8" liq x 1-1/8" suc = 127 oz
- HP (DZ6VS), 4.0 ton Enhanced Capacity FIT, indoor DFVE, DV**FEC, p.28 (row "15 or less"): 3/8" liq x 1-1/8" suc = 127 oz

## 6. LINE SET CHARGE TABLES (pp.23-28, extracted from the manual's tables by cell; "A / C" = total oz / additional oz; "n/a" = not allowed or not printed for that combo)
AC pages 23-26 are the DX6VS (cooling only). HP pages 26-28 are the DZ6VS heat pump. Indoor type matters: CAPEA/DFVE/DV**FEC tables differ from CHPE tables (CHPE rows start at "12 or less").

**AC (DX6VS, cooling only) | 1.5 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 23 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 1/4" liq x 5/8" suc | 1/4" liq x 3/4" suc | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|---|---|
| 15 or less | n/a | n/a | n/a | n/a | n/a | 76 / 0 |
| 20 | n/a | n/a | n/a | 76 / 0 | 77 / 1 | 79 / 3 |
| 25 | n/a | 77 / 1 | 76 / 0 | 78 / 2 | 80 / 4 | 82 / 6 |
| 30 | n/a | 78 / 2 | 77 / 1 | 80 / 4 | 83 / 7 | 85 / 9 |
| 35 | n/a | 79 / 3 | 79 / 3 | 82 / 6 | 85 / 9 | 88 / 12 |
| 40 | 77 / 1 | 81 / 5 | 80 / 4 | 84 / 8 | 88 / 12 | 92 / 16 |
| 45 | 78 / 2 | 82 / 6 | 82 / 6 | 86 / 10 | 91 / 15 | 95 / 19 |
| 50 | 78 / 2 | 83 / 7 | 83 / 7 | 88 / 12 | 93 / 17 | 98 / 22 |
| 55 | 79 / 3 | 84 / 8 | 85 / 9 | 89 / 13 | 96 / 20 | 101 / 25 |
| 60 | 80 / 4 | 85 / 9 | 86 / 10 | 91 / 15 | 99 / 23 | 104 / 28 |
| 65 | 81 / 5 | 86 / 10 | 88 / 12 | 93 / 17 | 101 / 25 | 107 / 31 |
| 70 | 81 / 5 | 87 / 11 | 89 / 13 | 95 / 19 | 104 / 28 | 110 / 34 |
| 75 | 82 / 6 | 88 / 12 | 91 / 15 | 97 / 21 | 107 / 31 | 113 / 37 |
| 80 | 83 / 7 | 90 / 14 | 92 / 16 | 99 / 23 | 109 / 33 | 116 / 40 |
| 85 | 83 / 7 | 91 / 15 | 94 / 18 | 101 / 25 | 112 / 36 | 119 / 43 |
| 90 | 84 / 8 | 92 / 16 | 95 / 19 | 103 / 27 | 115 / 39 | 123 / 47 |
| 95 | 85 / 9 | 93 / 17 | 97 / 21 | 105 / 29 | 117 / 41 | 126 / 50 |
| 100 | 85 / 9 | 94 / 18 | 98 / 22 | 107 / 31 | 120 / 44 | 129 / 53 |

**AC (DX6VS, cooling only) | 2.0 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 23 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | n/a | 76 / 0 |
| 20 | n/a | 78 / 2 | 77 / 1 | 79 / 3 |
| 25 | 78 / 2 | 80 / 4 | 80 / 4 | 82 / 6 |
| 30 | 79 / 3 | 82 / 6 | 83 / 7 | 85 / 9 |
| 35 | 81 / 5 | 84 / 8 | 85 / 9 | 88 / 12 |
| 40 | 82 / 6 | 86 / 10 | 88 / 12 | 92 / 16 |
| 45 | 84 / 8 | 88 / 12 | 91 / 15 | 95 / 19 |
| 50 | 85 / 9 | 89 / 13 | 93 / 17 | 98 / 22 |
| 55 | 87 / 11 | 91 / 15 | 96 / 20 | 101 / 25 |
| 60 | 88 / 12 | 93 / 17 | 99 / 23 | 104 / 28 |
| 65 | 90 / 14 | 95 / 19 | 101 / 25 | 107 / 31 |
| 70 | 91 / 15 | 97 / 21 | 104 / 28 | 110 / 34 |
| 75 | n/a | n/a | 107 / 31 | 113 / 37 |
| 80 | n/a | n/a | 109 / 33 | 116 / 40 |
| 85 | n/a | n/a | 112 / 36 | 119 / 43 |
| 90 | n/a | n/a | 115 / 39 | 123 / 47 |
| 95 | n/a | n/a | 117 / 41 | 126 / 50 |
| 100 | n/a | n/a | 120 / 44 | 129 / 53 |

**AC (DX6VS, cooling only) | 2.5 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 24 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | n/a | 79 / 0 |
| 20 | n/a | 81 / 2 | 80 / 1 | 82 / 3 |
| 25 | 80 / 1 | 83 / 4 | 83 / 4 | 85 / 6 |
| 30 | 82 / 3 | 85 / 6 | 86 / 7 | 89 / 10 |
| 35 | 84 / 5 | 87 / 8 | 89 / 10 | 92 / 13 |
| 40 | 85 / 6 | 89 / 10 | 92 / 13 | 95 / 16 |
| 45 | 87 / 8 | 91 / 12 | 94 / 15 | 99 / 20 |
| 50 | 88 / 9 | 93 / 14 | 97 / 18 | 102 / 23 |
| 55 | 90 / 11 | 95 / 16 | 100 / 21 | 105 / 26 |
| 60 | 92 / 13 | 97 / 18 | 103 / 24 | 108 / 29 |
| 65 | 93 / 14 | 99 / 20 | 105 / 26 | 112 / 33 |
| 70 | 95 / 16 | 101 / 22 | 108 / 29 | 115 / 36 |
| 75 | n/a | n/a | 111 / 32 | 118 / 39 |
| 80 | n/a | n/a | 114 / 35 | 121 / 42 |
| 85 | n/a | n/a | 117 / 38 | 125 / 46 |
| 90 | n/a | n/a | 119 / 40 | 128 / 49 |
| 95 | n/a | n/a | 122 / 43 | 131 / 52 |
| 100 | n/a | n/a | 125 / 46 | 134 / 55 |

**AC (DX6VS, cooling only) | 3.0 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 24 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | n/a | 85 / 0 |
| 20 | n/a | 87 / 2 | 86 / 1 | 88 / 3 |
| 25 | 86 / 1 | 89 / 4 | 89 / 4 | 91 / 6 |
| 30 | 88 / 3 | 91 / 6 | 92 / 7 | 95 / 10 |
| 35 | 90 / 5 | 93 / 8 | 95 / 10 | 98 / 13 |
| 40 | 91 / 6 | 95 / 10 | 98 / 13 | 101 / 16 |
| 45 | 93 / 8 | 97 / 12 | 100 / 15 | 105 / 20 |
| 50 | 94 / 9 | 99 / 14 | 103 / 18 | 108 / 23 |
| 55 | 96 / 11 | 101 / 16 | 106 / 21 | 111 / 26 |
| 60 | 98 / 13 | 103 / 18 | 109 / 24 | 114 / 29 |
| 65 | 99 / 14 | 105 / 20 | 111 / 26 | 118 / 33 |
| 70 | 101 / 16 | 107 / 22 | 114 / 29 | 121 / 36 |
| 75 | n/a | n/a | 117 / 32 | 124 / 39 |
| 80 | n/a | n/a | 120 / 35 | 127 / 42 |
| 85 | n/a | n/a | 123 / 38 | 131 / 46 |
| 90 | n/a | n/a | 125 / 40 | 134 / 49 |
| 95 | n/a | n/a | 128 / 43 | 137 / 52 |
| 100 | n/a | n/a | 131 / 46 | 140 / 55 |

**AC (DX6VS, cooling only) | 3.5 - 4.0 ton FIT | indoor: DFVE, DV**FEC | page 24 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 111 / 0 |
| 20 | 111 / 0 | 114 / 3 |
| 25 | 112 / 1 | 117 / 6 |
| 30 | 114 / 3 | 120 / 9 |
| 35 | 117 / 6 | 123 / 12 |
| 40 | 119 / 8 | 126 / 15 |
| 45 | 121 / 10 | 129 / 18 |
| 50 | 123 / 12 | 132 / 21 |
| 55 | 125 / 14 | 135 / 24 |
| 60 | 127 / 16 | 138 / 27 |
| 65 | 129 / 18 | 141 / 30 |
| 70 | 131 / 20 | 144 / 33 |
| 75 | 133 / 22 | 147 / 36 |
| 80 | 135 / 24 | 150 / 39 |
| 85 | 137 / 26 | 153 / 42 |
| 90 | 139 / 28 | 156 / 45 |
| 95 | 142 / 31 | 159 / 48 |
| 100 | 144 / 33 | 162 / 51 |

**AC (DX6VS, cooling only) | 5.0 ton FIT | indoor: DFVE, DV**FEC | page 24 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 131 / 0 |
| 20 | 131 / 0 | 134 / 3 |
| 25 | 132 / 1 | 137 / 6 |
| 30 | 134 / 3 | 140 / 9 |
| 35 | 137 / 6 | 143 / 12 |
| 40 | 139 / 8 | 146 / 15 |
| 45 | 141 / 10 | 149 / 18 |
| 50 | 143 / 12 | 152 / 21 |
| 55 | 145 / 14 | 155 / 24 |
| 60 | 147 / 16 | 158 / 27 |
| 65 | 149 / 18 | 161 / 30 |
| 70 | 151 / 20 | 164 / 33 |
| 75 | 153 / 22 | 167 / 36 |
| 80 | 155 / 24 | 170 / 39 |
| 85 | 157 / 26 | 173 / 42 |
| 90 | 159 / 28 | 176 / 45 |
| 95 | 162 / 31 | 179 / 48 |
| 100 | 164 / 33 | 182 / 51 |

**AC (DX6VS, cooling only) | 1.5 ton FIT | indoor: CHPE | page 25 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 1/4" liq x 5/8" suc | 1/4" liq x 3/4" suc | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|---|---|
| 12 or less | n/a | n/a | n/a | n/a | n/a | 76 / 0 |
| 15 | n/a | n/a | n/a | 76 / 0 | 76 / 0 | 76 / 0 |
| 20 | n/a | 77 / 1 | 76 / 0 | 77 / 1 | 79 / 3 | 81 / 5 |
| 25 | n/a | 78 / 2 | 77 / 1 | 79 / 3 | 82 / 6 | 84 / 8 |
| 30 | n/a | 79 / 3 | 78 / 2 | 81 / 5 | 85 / 9 | 87 / 11 |
| 35 | 77 / 1 | 80 / 4 | 80 / 4 | 83 / 7 | 87 / 11 | 90 / 14 |
| 40 | 78 / 2 | 81 / 5 | 81 / 5 | 85 / 9 | 90 / 14 | 93 / 17 |
| 45 | 78 / 2 | 82 / 6 | 83 / 7 | 87 / 11 | 93 / 17 | 96 / 20 |
| 50 | 79 / 3 | 83 / 7 | 84 / 8 | 89 / 13 | 95 / 19 | 100 / 24 |
| 55 | 80 / 4 | 85 / 9 | 86 / 10 | 91 / 15 | 98 / 22 | 103 / 27 |
| 60 | 81 / 5 | 86 / 10 | 87 / 11 | 93 / 17 | 101 / 25 | 106 / 30 |
| 65 | 81 / 5 | 87 / 11 | 89 / 13 | 94 / 18 | 103 / 27 | 109 / 33 |
| 70 | 82 / 6 | 88 / 12 | 90 / 14 | 96 / 20 | 106 / 30 | 112 / 36 |
| 75 | 83 / 7 | 89 / 13 | 92 / 16 | 98 / 22 | 109 / 33 | 115 / 39 |
| 80 | 83 / 7 | 90 / 14 | 93 / 17 | 100 / 24 | 111 / 35 | 118 / 42 |
| 85 | 84 / 8 | 91 / 15 | 95 / 19 | 102 / 26 | 114 / 38 | 121 / 45 |
| 90 | 85 / 9 | 92 / 16 | 96 / 20 | 104 / 28 | 117 / 41 | 124 / 48 |
| 95 | 85 / 9 | 94 / 18 | 98 / 22 | 106 / 30 | 119 / 43 | 127 / 51 |
| 100 | 86 / 10 | 95 / 19 | 99 / 23 | 108 / 32 | 122 / 46 | 131 / 55 |

**AC (DX6VS, cooling only) | 2.0 ton FIT | indoor: CHPE | page 25 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|
| 12 or less | n/a | n/a | n/a | 76 / 0 |
| 15 | n/a | 76 / 0 | 76 / 0 | 76 / 0 |
| 20 | 77 / 1 | 79 / 3 | 79 / 3 | 81 / 5 |
| 25 | 79 / 3 | 81 / 5 | 82 / 6 | 84 / 8 |
| 30 | 80 / 4 | 83 / 7 | 85 / 9 | 87 / 11 |
| 35 | 82 / 6 | 85 / 9 | 87 / 11 | 90 / 14 |
| 40 | 83 / 7 | 87 / 11 | 90 / 14 | 93 / 17 |
| 45 | 85 / 9 | 89 / 13 | 93 / 17 | 96 / 20 |
| 50 | 86 / 10 | 91 / 15 | 95 / 19 | 100 / 24 |
| 55 | 88 / 12 | 93 / 17 | 98 / 22 | 103 / 27 |
| 60 | 89 / 13 | 94 / 18 | 101 / 25 | 106 / 30 |
| 65 | 91 / 15 | 96 / 20 | 103 / 27 | 109 / 33 |
| 70 | 92 / 16 | 98 / 22 | 106 / 30 | 112 / 36 |
| 75 | n/a | n/a | 109 / 33 | 115 / 39 |
| 80 | n/a | n/a | 111 / 35 | 118 / 42 |
| 85 | n/a | n/a | 114 / 38 | 121 / 45 |
| 90 | n/a | n/a | 117 / 41 | 124 / 48 |
| 95 | n/a | n/a | 119 / 43 | 127 / 51 |
| 100 | n/a | n/a | 122 / 46 | 131 / 55 |

**AC (DX6VS, cooling only) | 2.5 ton FIT | indoor: CHPE | page 25 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|
| 12 or less | n/a | n/a | n/a | 79 / 0 |
| 15 | n/a | 79 / 0 | 79 / 0 | 79 / 0 |
| 20 | 80 / 1 | 82 / 3 | 82 / 3 | 84 / 5 |
| 25 | 82 / 3 | 84 / 5 | 84 / 5 | 87 / 8 |
| 30 | 83 / 4 | 86 / 7 | 88 / 9 | 91 / 12 |
| 35 | 85 / 6 | 88 / 9 | 91 / 12 | 94 / 15 |
| 40 | 87 / 8 | 90 / 11 | 93 / 14 | 97 / 18 |
| 45 | 88 / 9 | 92 / 13 | 96 / 17 | 100 / 21 |
| 50 | 90 / 11 | 94 / 15 | 99 / 20 | 104 / 25 |
| 55 | 91 / 12 | 96 / 17 | 102 / 23 | 107 / 28 |
| 60 | 93 / 14 | 98 / 19 | 105 / 26 | 110 / 31 |
| 65 | 94 / 15 | 100 / 21 | 107 / 28 | 113 / 34 |
| 70 | 96 / 17 | 102 / 23 | 110 / 31 | 117 / 38 |
| 75 | n/a | n/a | 113 / 34 | 120 / 41 |
| 80 | n/a | n/a | 116 / 37 | 123 / 44 |
| 85 | n/a | n/a | 119 / 40 | 126 / 47 |
| 90 | n/a | n/a | 121 / 42 | 130 / 51 |
| 95 | n/a | n/a | 124 / 45 | 133 / 54 |
| 100 | n/a | n/a | 127 / 48 | 136 / 57 |

**AC (DX6VS, cooling only) | 3.0 ton FIT | indoor: CHPE | page 25 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 12 or less | n/a | n/a | n/a | 85 / 0 |
| 15 | n/a | 85 / 0 | 85 / 0 | 85 / 0 |
| 20 | 86 / 1 | 88 / 3 | 88 / 3 | 90 / 5 |
| 25 | 88 / 3 | 90 / 5 | 90 / 5 | 93 / 8 |
| 30 | 89 / 4 | 92 / 7 | 94 / 9 | 97 / 12 |
| 35 | 91 / 6 | 94 / 9 | 97 / 12 | 100 / 15 |
| 40 | 93 / 8 | 96 / 11 | 99 / 14 | 103 / 18 |
| 45 | 94 / 9 | 98 / 13 | 102 / 17 | 106 / 21 |
| 50 | 96 / 11 | 100 / 15 | 105 / 20 | 110 / 25 |
| 55 | 97 / 12 | 102 / 17 | 108 / 23 | 113 / 28 |
| 60 | 99 / 14 | 104 / 19 | 111 / 26 | 116 / 31 |
| 65 | 100 / 15 | 106 / 21 | 113 / 28 | 119 / 34 |
| 70 | 102 / 17 | 108 / 23 | 116 / 31 | 123 / 38 |
| 75 | n/a | n/a | 119 / 34 | 126 / 41 |
| 80 | n/a | n/a | 122 / 37 | 129 / 44 |
| 85 | n/a | n/a | 125 / 40 | 132 / 47 |
| 90 | n/a | n/a | 127 / 42 | 136 / 51 |
| 95 | n/a | n/a | 130 / 45 | 139 / 54 |
| 100 | n/a | n/a | 133 / 48 | 142 / 57 |

**AC (DX6VS, cooling only) | 3.5 - 4.0 ton FIT | indoor: CAPE, CHPE | page 26 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 12 or less | 112 / 1 | 114 / 3 |
| 15 | 113 / 2 | 116 / 5 |
| 20 | 115 / 4 | 119 / 8 |
| 25 | 117 / 6 | 122 / 11 |
| 30 | 119 / 8 | 125 / 14 |
| 35 | 121 / 10 | 128 / 17 |
| 40 | 123 / 12 | 131 / 20 |
| 45 | 126 / 15 | 134 / 23 |
| 50 | 128 / 17 | 137 / 26 |
| 55 | 130 / 19 | 140 / 29 |
| 60 | 132 / 21 | 143 / 32 |
| 65 | 134 / 23 | 146 / 35 |
| 70 | 136 / 25 | 149 / 38 |
| 75 | 138 / 27 | 152 / 41 |
| 80 | 140 / 29 | 155 / 44 |
| 85 | 142 / 31 | 158 / 47 |
| 90 | 144 / 33 | 161 / 50 |
| 95 | 146 / 35 | 164 / 53 |
| 100 | 148 / 37 | 167 / 56 |

**AC (DX6VS, cooling only) | 5.0 ton FIT | indoor: CAPE, CHPE | page 26 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 12 or less | 135 / 4 | 137 / 6 |
| 15 | 136 / 5 | 139 / 8 |
| 20 | 138 / 7 | 142 / 11 |
| 25 | 140 / 9 | 145 / 14 |
| 30 | 142 / 11 | 148 / 17 |
| 35 | 144 / 13 | 151 / 20 |
| 40 | 146 / 15 | 154 / 23 |
| 45 | 149 / 18 | 157 / 26 |
| 50 | 151 / 20 | 160 / 29 |
| 55 | 153 / 22 | 163 / 32 |
| 60 | 155 / 24 | 166 / 35 |
| 65 | 157 / 26 | 169 / 38 |
| 70 | 159 / 28 | 172 / 41 |
| 75 | 161 / 30 | 175 / 44 |
| 80 | 163 / 32 | 178 / 47 |
| 85 | 165 / 34 | 181 / 50 |
| 90 | 167 / 36 | 184 / 53 |
| 95 | 169 / 38 | 187 / 56 |
| 100 | 171 / 40 | 190 / 59 |

**HP (DZ6VS, heat pump) | 1.5 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 26 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 1/4" liq x 5/8" suc | 1/4" liq x 3/4" suc | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|---|---|
| 15 or less | n/a | n/a | n/a | n/a | 81 / 0 | 81 / 0 |
| 20 | n/a | 81 / 0 | n/a | 81 / 0 | 82 / 1 | 84 / 3 |
| 25 | n/a | 82 / 1 | 81 / 0 | 83 / 2 | 85 / 4 | 87 / 6 |
| 30 | 81 / 0 | 83 / 2 | 82 / 1 | 85 / 4 | 88 / 7 | 90 / 9 |
| 35 | 81 / 0 | 84 / 3 | 84 / 3 | 87 / 6 | 90 / 9 | 93 / 12 |
| 40 | 82 / 1 | 86 / 5 | 85 / 4 | 89 / 8 | 93 / 12 | 97 / 16 |
| 45 | 83 / 2 | 87 / 6 | 87 / 6 | 91 / 10 | 96 / 15 | 100 / 19 |
| 50 | 83 / 2 | 88 / 7 | 88 / 7 | 93 / 12 | 98 / 17 | 103 / 22 |
| 55 | 84 / 3 | 89 / 8 | 90 / 9 | 94 / 13 | 101 / 20 | 106 / 25 |
| 60 | 85 / 4 | 90 / 9 | 91 / 10 | 96 / 15 | 104 / 23 | 109 / 28 |
| 65 | 86 / 5 | 91 / 10 | 93 / 12 | 98 / 17 | 106 / 25 | 112 / 31 |
| 70 | 86 / 5 | 92 / 11 | 94 / 13 | 100 / 19 | 109 / 28 | 115 / 34 |
| 75 | 87 / 6 | 93 / 12 | 96 / 15 | 102 / 21 | 112 / 31 | 118 / 37 |
| 80 | 88 / 7 | 95 / 14 | 97 / 16 | 104 / 23 | 114 / 33 | 121 / 40 |
| 85 | 88 / 7 | 96 / 15 | 99 / 18 | 106 / 25 | 117 / 36 | 124 / 43 |
| 90 | 89 / 8 | 97 / 16 | 100 / 19 | 108 / 27 | 120 / 39 | 128 / 47 |
| 95 | 90 / 9 | 98 / 17 | 102 / 21 | 110 / 29 | 122 / 41 | 131 / 50 |
| 100 | 90 / 9 | 99 / 18 | 103 / 22 | 112 / 31 | 125 / 44 | 134 / 53 |

**HP (DZ6VS, heat pump) | 2.0 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 26 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 5/8" suc | 5/16" liq x 3/4" suc | 3/8" liq x 5/8" suc | 3/8" liq x 3/4" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | 81 / 0 | 81 / 0 |
| 20 | n/a | 83 / 2 | 82 / 1 | 84 / 3 |
| 25 | 83 / 2 | 85 / 4 | 85 / 4 | 87 / 6 |
| 30 | 84 / 3 | 87 / 6 | 88 / 7 | 90 / 9 |
| 35 | 86 / 5 | 89 / 8 | 90 / 9 | 93 / 12 |
| 40 | 87 / 6 | 91 / 10 | 93 / 12 | 97 / 16 |
| 45 | 89 / 8 | 93 / 12 | 96 / 15 | 100 / 19 |
| 50 | 90 / 9 | 94 / 13 | 98 / 17 | 103 / 22 |
| 55 | 92 / 11 | 96 / 15 | 101 / 20 | 106 / 25 |
| 60 | 93 / 12 | 98 / 17 | 104 / 23 | 109 / 28 |
| 65 | 95 / 14 | 100 / 19 | 106 / 25 | 112 / 31 |
| 70 | 96 / 15 | 102 / 21 | 109 / 28 | 115 / 34 |
| 75 | n/a | n/a | 112 / 31 | 118 / 37 |
| 80 | n/a | n/a | 114 / 33 | 121 / 40 |
| 85 | n/a | n/a | 117 / 36 | 124 / 43 |
| 90 | n/a | n/a | 120 / 39 | 128 / 47 |
| 95 | n/a | n/a | 122 / 41 | 131 / 50 |
| 100 | n/a | n/a | 125 / 44 | 134 / 53 |

**HP (DZ6VS, heat pump) | 2.5 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 27 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | 88 / 0 | 88 / 0 |
| 20 | n/a | 90 / 2 | 89 / 1 | 91 / 3 |
| 25 | 89 / 1 | 92 / 4 | 92 / 4 | 94 / 6 |
| 30 | 91 / 3 | 94 / 6 | 95 / 7 | 98 / 10 |
| 35 | 93 / 5 | 96 / 8 | 98 / 10 | 101 / 13 |
| 40 | 94 / 6 | 98 / 10 | 101 / 13 | 104 / 16 |
| 45 | 96 / 8 | 100 / 12 | 103 / 15 | 108 / 20 |
| 50 | 97 / 9 | 102 / 14 | 106 / 18 | 111 / 23 |
| 55 | 99 / 11 | 104 / 16 | 109 / 21 | 114 / 26 |
| 60 | 101 / 13 | 106 / 18 | 112 / 24 | 117 / 29 |
| 65 | 102 / 14 | 108 / 20 | 114 / 26 | 121 / 33 |
| 70 | 104 / 16 | 110 / 22 | 117 / 29 | 124 / 36 |
| 75 | n/a | n/a | 120 / 32 | 127 / 39 |
| 80 | n/a | n/a | 123 / 35 | 130 / 42 |
| 85 | n/a | n/a | 126 / 38 | 134 / 46 |
| 90 | n/a | n/a | 128 / 40 | 137 / 49 |
| 95 | n/a | n/a | 131 / 43 | 140 / 52 |
| 100 | n/a | n/a | 134 / 46 | 143 / 55 |

**HP (DZ6VS, heat pump) | 3.0 ton FIT | indoor: CAPEA, DFVE, DV**FEC | page 27 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | 88 / 0 | 88 / 0 |
| 20 | n/a | 90 / 2 | 89 / 1 | 91 / 3 |
| 25 | 89 / 1 | 92 / 4 | 92 / 4 | 94 / 6 |
| 30 | 91 / 3 | 94 / 6 | 95 / 7 | 98 / 10 |
| 35 | 93 / 5 | 96 / 8 | 98 / 10 | 101 / 13 |
| 40 | 94 / 6 | 98 / 10 | 101 / 13 | 104 / 16 |
| 45 | 96 / 8 | 100 / 12 | 103 / 15 | 108 / 20 |
| 50 | 97 / 9 | 102 / 14 | 106 / 18 | 111 / 23 |
| 55 | 99 / 11 | 104 / 16 | 109 / 21 | 114 / 26 |
| 60 | 101 / 13 | 106 / 18 | 112 / 24 | 117 / 29 |
| 65 | 102 / 14 | 108 / 20 | 114 / 26 | 121 / 33 |
| 70 | 104 / 16 | 110 / 22 | 117 / 29 | 124 / 36 |
| 75 | n/a | n/a | 120 / 32 | 127 / 39 |
| 80 | n/a | n/a | 123 / 35 | 130 / 42 |
| 85 | n/a | n/a | 126 / 38 | 134 / 46 |
| 90 | n/a | n/a | 128 / 40 | 137 / 49 |
| 95 | n/a | n/a | 131 / 43 | 140 / 52 |
| 100 | n/a | n/a | 134 / 46 | 143 / 55 |

**HP (DZ6VS, heat pump) | 2.0 ton Enhanced Capacity FIT | indoor: CAPEA, DFVE, DV**FEC | page 27 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 5/16" liq x 3/4" suc | 5/16" liq x 7/8" suc | 3/8" liq x 3/4" suc | 3/8" liq x 7/8" suc |
|---|---|---|---|---|
| 15 or less | n/a | n/a | 88 / 0 | 88 / 0 |
| 20 | n/a | 90 / 2 | 89 / 1 | 91 / 3 |
| 25 | 89 / 1 | 92 / 4 | 92 / 4 | 94 / 6 |
| 30 | 91 / 3 | 94 / 6 | 95 / 7 | 98 / 10 |
| 35 | 93 / 5 | 96 / 8 | 98 / 10 | 101 / 13 |
| 40 | 94 / 6 | 98 / 10 | 101 / 13 | 104 / 16 |
| 45 | 96 / 8 | 100 / 12 | 103 / 15 | 108 / 20 |
| 50 | 97 / 9 | 102 / 14 | 106 / 18 | 111 / 23 |
| 55 | 99 / 11 | 104 / 16 | 109 / 21 | 114 / 26 |
| 60 | 101 / 13 | 106 / 18 | 112 / 24 | 117 / 29 |
| 65 | 102 / 14 | 108 / 20 | 114 / 26 | 121 / 33 |
| 70 | 104 / 16 | 110 / 22 | 117 / 29 | 124 / 36 |
| 75 | n/a | n/a | 120 / 32 | 127 / 39 |
| 80 | n/a | n/a | 123 / 35 | 130 / 42 |
| 85 | n/a | n/a | 126 / 38 | 134 / 46 |
| 90 | n/a | n/a | 128 / 40 | 137 / 49 |
| 95 | n/a | n/a | 131 / 43 | 140 / 52 |
| 100 | n/a | n/a | 134 / 46 | 143 / 55 |

**HP (DZ6VS, heat pump) | 3.0 ton Enhanced Capacity FIT | indoor: DFVE, DV**FEC | page 27 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 118 / 0 |
| 20 | 118 / 0 | 121 / 3 |
| 25 | 120 / 2 | 124 / 6 |
| 30 | 124 / 6 | 129 / 11 |
| 35 | 127 / 9 | 133 / 15 |
| 40 | 130 / 12 | 137 / 19 |
| 45 | 134 / 16 | 140 / 22 |
| 50 | 137 / 19 | 144 / 26 |
| 55 | 140 / 22 | 148 / 30 |
| 60 | 144 / 26 | 152 / 34 |
| 65 | 147 / 29 | 155 / 37 |
| 70 | 150 / 32 | 159 / 41 |
| 75 | 154 / 36 | 163 / 45 |
| 80 | 157 / 39 | 166 / 48 |
| 85 | 160 / 42 | 170 / 52 |
| 90 | 164 / 46 | 174 / 56 |
| 95 | 167 / 49 | 178 / 60 |
| 100 | 170 / 52 | 181 / 63 |

**HP (DZ6VS, heat pump) | 3.5 - 4.0 ton FIT | indoor: DFVE, DV**FEC | page 28 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 118 / 0 |
| 20 | 118 / 0 | 121 / 3 |
| 25 | 120 / 2 | 124 / 6 |
| 30 | 124 / 6 | 129 / 11 |
| 35 | 127 / 9 | 133 / 15 |
| 40 | 130 / 12 | 137 / 19 |
| 45 | 134 / 16 | 140 / 22 |
| 50 | 137 / 19 | 144 / 26 |
| 55 | 140 / 22 | 148 / 30 |
| 60 | 144 / 26 | 152 / 34 |
| 65 | 147 / 29 | 155 / 37 |
| 70 | 150 / 32 | 159 / 41 |
| 75 | 154 / 36 | 163 / 45 |
| 80 | 157 / 39 | 166 / 48 |
| 85 | 160 / 42 | 170 / 52 |
| 90 | 164 / 46 | 174 / 56 |
| 95 | 167 / 49 | 178 / 60 |
| 100 | 170 / 52 | 181 / 63 |

**HP (DZ6VS, heat pump) | 5.0 ton FIT | indoor: DFVE, DV**FEC | page 28 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 127 / 0 |
| 20 | 127 / 0 | 130 / 3 |
| 25 | 128 / 1 | 133 / 6 |
| 30 | 133 / 6 | 138 / 11 |
| 35 | 136 / 9 | 142 / 15 |
| 40 | 139 / 12 | 146 / 19 |
| 45 | 142 / 15 | 149 / 22 |
| 50 | 146 / 19 | 153 / 26 |
| 55 | 149 / 22 | 157 / 30 |
| 60 | 152 / 25 | 160 / 33 |
| 65 | 156 / 29 | 164 / 37 |
| 70 | 159 / 32 | 168 / 41 |
| 75 | 162 / 35 | 172 / 45 |
| 80 | 166 / 39 | 175 / 48 |
| 85 | 169 / 42 | 179 / 52 |
| 90 | 172 / 45 | 183 / 56 |
| 95 | 176 / 49 | 186 / 59 |
| 100 | 179 / 52 | 190 / 63 |

**HP (DZ6VS, heat pump) | 3.5 ton Enhanced Capacity FIT | indoor: DFVE, DV**FEC | page 28 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 127 / 0 |
| 20 | 127 / 0 | 130 / 3 |
| 25 | 128 / 1 | 133 / 6 |
| 30 | 133 / 6 | 138 / 11 |
| 35 | 136 / 9 | 142 / 15 |
| 40 | 139 / 12 | 146 / 19 |
| 45 | 142 / 15 | 149 / 22 |
| 50 | 146 / 19 | 153 / 26 |
| 55 | 149 / 22 | 157 / 30 |
| 60 | 152 / 25 | 160 / 33 |
| 65 | 156 / 29 | 164 / 37 |
| 70 | 159 / 32 | 168 / 41 |
| 75 | 162 / 35 | 172 / 45 |
| 80 | 166 / 39 | 175 / 48 |
| 85 | 169 / 42 | 179 / 52 |
| 90 | 172 / 45 | 183 / 56 |
| 95 | 176 / 49 | 186 / 59 |
| 100 | 179 / 52 | 190 / 63 |

**HP (DZ6VS, heat pump) | 4.0 ton Enhanced Capacity FIT | indoor: DFVE, DV**FEC | page 28 (A = total charge oz, C = additional oz vs factory)**

| Line length (ft) | 3/8" liq x 7/8" suc | 3/8" liq x 1-1/8" suc |
|---|---|---|
| 15 or less | n/a | 127 / 0 |
| 20 | 127 / 0 | 130 / 3 |
| 25 | 128 / 1 | 133 / 6 |
| 30 | 133 / 6 | 138 / 11 |
| 35 | 136 / 9 | 142 / 15 |
| 40 | 139 / 12 | 146 / 19 |
| 45 | 142 / 15 | 149 / 22 |
| 50 | 146 / 19 | 153 / 26 |
| 55 | 149 / 22 | 157 / 30 |
| 60 | 152 / 25 | 160 / 33 |
| 65 | 156 / 29 | 164 / 37 |
| 70 | 159 / 32 | 168 / 41 |
| 75 | 162 / 35 | 172 / 45 |
| 80 | 166 / 39 | 175 / 48 |
| 85 | 169 / 42 | 179 / 52 |
| 90 | 172 / 45 | 183 / 56 |
| 95 | 176 / 49 | 186 / 59 |
| 100 | 179 / 52 | 190 / 63 |

---
## 7. R-410A FIT SERVICE-MANUAL CHARGE-RELATED NOTES (SiUS612209EB)
- E13 high pressure error: trips above 4.2 MPa (605 PSIG). Check overcharge/subcooling, stop valve, OD coil (cooling), OD fan, HPS, E24. E15 low pressure error: trips below 0.12 MPa (17 PSIG) sustained 5 minutes. Check pressure sensor, stop valve, undercharge or leak, thermistors, EEV, drier clog, fans. In the E15 flow, when undercharged: adjust subcooling with the manifold gauge, then check for a refrigerant leak.
- E21 low discharge superheat: first check the refrigerant charge is correct, then EEV coils and connections (coil protrusion clicks into the EEV body dimple), coil resistance, thermistors, pressure sensor.
- E22 high discharge temperature (trips above 120 C / 248 F): check discharge thermistor, EEV coils, charge. E41 low refrigerant: leak test, check charge, thermistors, outdoor solenoid valve.
- E57 refrigerant cooling sweat error (3.5-5.0 ton only): leak test, check charge, indoor EEV and coil, thermistors.
- Compressor efficiency check (S-104): attach gauges, run CHARGE MODE. If high-side pressure is below normal, low-side pressure is above normal, coil temperature difference is low and compressor amps are low, and the charge is correct, the compressor is faulty.
- Repairs: after any open-system repair, replace the liquid line drier, evacuate and charge. Never open a system that is under vacuum. Sweep tubing with dry nitrogen when brazing. There is no pump-down function; recover all refrigerant from both service ports on the stop valves.
- Mixture of noncondensable gas: recover refrigerant, evacuate the pipe, re-charge. Overcharge: recover part of the charge. Undercharge: test for leaks, add refrigerant (service-manual analysis chart).
- Charge Mode and the thermostat's Charge Mode setting are also in the board's serviceman menu (item 9, 0 = ON, 1 = OFF in the service manual's menu table). The outdoor display alternates "cha" with subcooling when ready.
- Emergency mode cooling on these systems: compressor speed follows outdoor temp (below 70 F = 50%, above 95 F = 100%), indoor EEV keeps controlling superheat. Not for charging.

## 8. NOT IN THIS FILE
- The manual's Cooling Analysis Chart (p.41) and Heating Analysis Chart (p.42) are printed rotated; they were not transcribed. Use the manual pages.
- No separate heating-mode charge procedure for the DZ6VS heat pump; the manual's charge steps cover both with the same tables. CHARGE MODE is a cooling-mode verification.
- No superheat targets: the Fit inverter units charge by subcooling with CHARGE MODE; the EEV controls superheat itself.
- Old (non-Fit) R-410A single/two-stage condensers (DX/DZ 7TC-18TC ComfortNet, DX3SE etc.) are not covered here. We have only their airflow tables and fault codes.
- Other tonnage/indoor combinations not printed in the tables are not allowed or not available.
