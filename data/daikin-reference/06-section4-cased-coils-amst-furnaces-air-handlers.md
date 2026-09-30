# SECTION 4 — MANUAL EXTRACTION: CASED COILS, AMST AIR HANDLER, GAS FURNACES, DMVE/DFVE/DMVT AIR HANDLERS

---
name: daikin-goodman-manuals-reference
description: James's saved reference data from 11 official Daikin/Goodman install & service manuals (cased coils, air handlers, gas furnaces) — fault code tables, airflow/CFM tap tables, dip switch settings, heat kit charts, wiring/network troubleshooting. Read this before answering Daikin/Goodman fault code or airflow questions.
sources: [chat]
aliases: [daikin manuals, goodman manuals, install manuals, service manuals, fault code tables]
---

**DAIKIN/GOODMAN REFERENCE SET — read together for any Daikin/Goodman task (troubleshooting, equipment lookup, AHRI matching for job write-ups):**
- [[daikin-goodman-manuals-reference]] (this file) — cased coils (CHPE/CAPEA), AMST air handler, all 4 gas furnace fault code tables, DMVE/DFVE and DMVT air handlers: fault codes, wiring diagrams, CFM/dip switch tables
- [[daikin-goodman-manuals-reference-2]] — continuation: furnace thermostat wiring, gas piping/pressure specs, DFVE/DMVE heater kit DIP tables
- [[daikin-goodman-manuals-reference-3]] — Amana/Goodman condenser CoreSense diagnostics, R-32 A2L PCB codes, ComfortNet DX/DZ 7TC-18TC air handler diagnostic codes
- [[daikin-goodman-manuals-reference-4]] — DX6VS/DZ6VS inverter EEV outdoor unit full E-code table, EEV cased coil/air handler indoor error codes, emergency mode DIP switch setup
- [[daikin-ahri-lookup]] — AHRI number lookups, combo matching workflow, distributor catalog data/gaps — use this file's model spec data to confirm exact SKUs before searching ahridirectory.org
- [[hvac-pro-field-guide-app]] — the toolkit app this data feeds into (hvactoolkit.netlify.app)
For fastest field troubleshooting: search all four manuals-reference files first for the exact fault code/wiring/CFM data on the model in hand. For quoting/selling a job: cross-check exact model specs/dimensions/electrical data here against [[daikin-ahri-lookup]]'s combo-matching workflow before finalizing an AHRI number.

- [stated] uploaded 11 official Daikin Comfort Technologies install & service reference manuals and said "i want to save all this info" / "i want it all" / "all of our daikin info should be linked to help me faster trouble shoot or look up info on equipment or match ahri to write the jobs up that sell" — this file is the saved extraction, organized by equipment type
- [stated] wants this saved as reference data for the field guide toolkit's Daikin/Goodman coverage, alongside [[daikin-ahri-lookup]] and the outdoor unit fault code work already in toolkit.html (see [[hvac-pro-field-guide-app]])

## Source manuals (11 total)
1. IO-454F — CHPE cased coil (R-32), copyright 2022-2024
2. IO-457 — CAPEA/CAPE cased coil (R-32) — uploaded twice (duplicate file, same content)
3. IO-4003C — two-way coil (R-32)
4. IO-4011B — AMST air handler (ECM, R-32, A2L leak detection)
5. IO-2035A — DR80SN/DD80SN 80% single-stage gas furnace (R-32 compatible)
6. IO-2037A — DR92SN/DR96SN/DD96SN 90%+ single-stage gas furnace (R-32 compatible)
7. IO-2043 — DR80TC/DD80TC 80% two-stage gas furnace (R-32 compatible, CoolCloud app)
8. IO-2044 — DR96TC/DD96TC 90%+ two-stage gas furnace (R-32 compatible, CoolCloud app)
9. IO-4039A — DMVE/DFVE EEV air handler (R-410A factory charge, communicating PCB)
10. IO-4040B — DMVT P1400 air handler (ECM, Emerson ClimateTalk board, legacy/non-communicating, R-410A)

## 1. CHPE / CAPEA-CAPE cased coils (IO-454F, IO-457) — R-32
**[stated] James's correction: CAPE is an EEV (electronic expansion valve) coil; CAPT is a TXV (thermal/thermostatic expansion valve) coil — different metering device, different model line. Don't confuse the two on a lookup.**
**[stated] James's correction: CHP-prefix coils are dedicated horizontal cased coils only. CAPT/CAPE-prefix coils are upflow/downflow only (NOT horizontal). This matters for AHRI matchups — a horizontal application needs CHP specifically; a horizontal-only site can't use a CAP-prefix coil regardless of which shows a better SEER2/EER2 number on the combo table.**
Both CHPE and CAPEA/CAPE use nearly identical PCB architecture and fault code tables (full table below — pulled verbatim from both manuals' Troubleshooting section, page 18 CHPE / page 18 CAPEA). CAPEA/CAPE is the EEV-equipped cased coil covered by manual IO-457.

### Fault code table (verbatim, both CHPE and CAPEA/CAPE)
| Error Code | PCB LED Display | ClimateTalk Message | Description | Possible Causes | Corrective Actions |
|---|---|---|---|---|---|
| EE | No display (EE display is EMG mode) | INTERNAL FAULT | — | No 24 volt power to PCB; blown fuse or circuit breaker; PCB has an internal fault | Assure 24 volt power to blower and control board. Check fuse F2U on control board; check for possible short in 115/230 volt and 24 volt circuits, repair as necessary; replace the control board |
| d0 | E_d0 | Data Not Yet On Network (NO NET DATA) | Data Not Yet On Network | No shared data on the network | Populate shared data set using memory card |
| d4 | E_d4 | Invalid Memory Card Data (INVALID MC DATA) | Invalid Memory Card Data | Wrong memory card data | Replace circuit board; rewrite data using the correct memory card |
| 70 | E_70 | EEV OPEN CKT | EEV disconnection detected | Indoor EEV coil not connected; incorrect wiring to EEV | Check Indoor EEV coil connection (PCB and junction connector); replace EEV coil; check the resistance value of EEV coil (refer service manual); replace control board |
| 73 | E_73 | LIQ TEMP FLT | Liquid side thermistor abnormality | Open (or) short circuit of the liquid thermistor (X5A); liquid thermistor reading incorrect or values outside the normal range | Check connection to liquid thermistor (PCB and junction connector); check resistance value of thermistor (refer service manual); replace thermistor; replace control board |
| 74 | E_74 | GAS TEMP FLT | Gas side thermistor abnormality | Open (or) short circuit of the gas thermistor (X5A); gas thermistor reading incorrect or values outside the normal range | Check connection to gas thermistor (PCB and junction connector); check resistance value of thermistor; replace thermistor; replace control board |
| 75 | E_75 | PRESSURE FLT | Pressure sensor abnormality | Open (or) short circuit of the Pressure Sensor (X15A); pressure sensor reading incorrect or values outside normal range | Check connection to pressure sensor (PCB and junction connector); check output voltage of pressure sensor (refer service manual); replace pressure sensor; replace control board |
| 76 | E_76 | EQUIP COMM LOSS | Outdoor unit - Gas furnace or Blower unit communication error (during operation) | Open communication circuit; incorrect wiring between OD unit, Gas furnace or Modular blower; no power supply to OD unit, Gas furnace or Modular blower | Check for cased coil and other unit wiring; replace the control board; check power supply to OD unit, Gas furnace or Modular blower |
| 77 | E_77 | TSTAT ID NO COM | Indoor Unit Thermostat communication error (start-up & during operation) | Incorrect wiring between ID unit and thermostat; the system may have the communication error without error code 77 on the indoor PCB; thermostat failure; power interruption (low voltage) | Check for thermostat and indoor unit wiring; verify the input voltage at the ID unit and thermostat; after recovering the system with power supply, TSTAT ID NO COM will continue to be displayed on the thermostat within 2 minutes; the error code will be cleared automatically; replace control board or thermostat; press "LEARN" button on PCB for more than 5 seconds to reestablish network |
| 78 | E_78 | CONNECT EQUIP | Outdoor unit - Gas furnace or Blower unit communication error (Startup operation) | Open communication circuit; incorrect wiring between OD unit, Gas furnace or Modular blower; no power supply to OD unit, Gas furnace or Modular blower | Check for cased coil and other unit wiring; replace the control board; check power supply to OD unit, Gas furnace or Modular blower |

### Wiring diagram (CHPE — IO-454F page 21, and CAPEA/CAPE — IO-457 page 22; both diagrams are functionally identical)
**Color codes:** BL=Blue, RD=Red, YL=Yellow, OR=Orange, BK=Black, GY=Grey, BR=Brown, GR=Green, WH=White, PU=Purple
**Component codes:** TR1 = Coil transformer; F1U, F2U = Fuse link; DS1-DS6 = Selector switch
**Key connections:** EEV wiring → X3A; Pressure sensor → X15A; Thermistor (heat exchanger 1,2) → X5A; DS1-DS6 dip switch bank sets selector switches (factory-set default — do not alter unless directed); SEG1/SEG2 = 7-segment display; CPU LED, Status LED, RX LED (network status: red = network status, green RX = network traffic — use Learn button to reset network); BS1/BS2 = fault recall/learn buttons; low voltage terminals (BL/RD/GY/BK) run TO THERMOSTAT; transmission wiring (BL/RD/GY/BK) runs to EEV coil inside the coil cabinet, which has its own thermistor and pressure sensor; 120/208/230V supply comes into TR1 coil transformer producing 24VAC output (PU/YL leads) to power the PCB — COM/120/208/230 taps let you match the transformer to the actual gas furnace/blower supply voltage.
**Transformer bracket selection (Table 1, from IO-454F/CHPE — same logic applies to CAPEA):** based on furnace type/cabinet width, use Bracket A, B, or C: Upflow 80% (any width) = Bracket A; Upflow 96%/97% (any width) = Bracket B; Counterflow 80% (any width) = Bracket C; Counterflow 96% at 17.5" width = Bracket C, at 21.0" width = Bracket B; Counterflow 97% at 17.5" width = Bracket C, at 24.5" width = Bracket B; Modular Blower (MBVC*, any width) = Bracket C.
**Notes from the diagram:** manufacturer's specified replacement parts must be used when servicing; if any of the original wires supplied with the unit must be replaced, use wiring material rated at least 105°C, copper conductors only; unit must be permanently grounded per NEC/local codes; to recall the last 6 faults, hold Fault Recall button >5 seconds while in standby (no thermostat inputs); selection of correct supply voltage for transformer depends on power supply voltage to gas furnace or blower unit; use N.E.C. Class 2 wire.

- 2-wire and 4-wire communicating wiring specs documented (matches the thermostat wiring conventions used across the Daikin Fit communicating family)
- CAPEA/CAPE (IO-457) additionally has a Maximum Allowed CFM table by model — not yet transcribed row-by-row; ask if a specific model's number is needed

## 2. Two-way coil (IO-4003C)
- Standard install/service reference; braze, leak test, evacuation, and drain line procedures documented (P-trap 2" min / 2.75" min dimensions same as other coils)
- No separate fault code table (coil, not a controlled device) — faults come from whichever air handler/furnace it's paired with

## 3. AMST air handler (IO-4011B) — ECM, R-32, ships with A2L refrigerant leak detection
**A2L PCB Fault Code table (Table 17) — RED LED status on the leak-detection PCB:**
- Normal Operation: slow flash (2 sec on/2 sec off) — no action
- R-32 Leak Alarm: fast flash — identify leak source, address it; unit turns off thermostat call, runs blower for air circulation, switches off electric heater
- Delay Mode: solid ON — after alarm/leak clears, unit stays in this mode 5 min before returning to normal; check HVAC performance and re-check for leaks
- System Verification Mode: fast flash (contractor-run test, simulates R-32 leak alarm for max 5 min) — no action needed; enter by pressing PCB button 2x within 5 sec
- Control Board Internal Fault: 2 flashes then 5 sec off — unplug/replug R32 sensor, cycle power; if persists, replace control board
- R-32 Sensor Communication Fault: 3 flashes then 5 sec off — control can't talk to sensor; unplug/replug sensor, cycle power; if persists replace both sensor and PCB (connector issue can't be isolated further in field)
- R-32 Sensor Fault: 4 flashes then 5 sec off — sensor itself reports internal fault; unplug/replug, cycle power; if persists replace the sensor
- A2L sensor bracket "FRONT" label must face away from equipment on both sensor bracket and gaskets during reassembly
- UV coil purifier kits available: UVPK01 (AMST24B) through UVPK07 (AMST60D) — kit determines drain pan main/side/ext and condensate collector front/back parts
- Heater kit compatibility and speed tap defaults documented; downflow requires L-shaped sheet metal duct with no registers directly below heater

### AMST Wiring Diagrams (IO-4011B pages 5-7)
Two separate diagrams: **AMST**U1300** (1.5T-4T models)** and **AMST60DU1300** (5T model, different transformer/wiring layout) — plus a shared 3-Phase Heat Kit diagram.
**Wire code:** BK=Black, BL=Blue, BR=Brown, GR=Green, PU=Purple, WH=White, RD=Red, YL=Yellow, PK=Pink
**Component legend:** CB=Circuit breaker, CR=Control relay, EHK=Electric heater kit, EM=Evaporator motor, GND=Ground, PCB=Control board, PLM=Male plug, REF=Refrigerant, RM=Female plug, TB=Terminal board, TR=Transformer
**Notes from the diagram:** replacement wire must be same size/type of insulation as original; only use copper conductors, use listed connectors; if speed taps are re-wired (adjusting motor speed), see further instructions for details; red wire connects to 240V (24V tap) for factory setup, move red wire to 208V tap to convert; low voltage transformer rated 75VA @ 3.125A output.
Ref PCB connections: EEV_IN / EEV_OUT / CTM_OUT / R_OUT / sensor — 5-pin connector to the refrigerant EEV board.

### AMST Speed Tap / Blower Wiring (IO-4011B pages 9-10)
9-speed ECM blower motor (AMST60DU1300 doesn't support speed tap adjustment — factory set).
**Selecting Speed Taps 1-5** (not applicable to AMST60DU1300): move the Purple (PU) wire lead from the alternate control relay to the desired Speed Tap; terminal block locations T1-T5 correlate to Speed Taps 1-5 (Table 2). **When selecting Speed Tap 1 or 5, the Black (BK) jumper must be removed completely and placed in the literature bag** (BK jumper is used to select speed taps 6-9).
**Selecting Speed Taps 6-9** (not applicable to AMST60DU1300): move the Black (BK) jumper, jumping T1 to any of terminal block locations T2-T5, shifting the motor to the 6-9 taps when the Purple (PU) lead from the blower relay is placed on the same tap as the Black (BK) jumper (Table 3).
**AMST60DU1300 only:** wiring is set up for 2-Stage compressor speed application as default from factory (Table 4 — terminal assignments: R=RD, C=BL, G=(blank), W1=WH, W2=BR, Y1=PU, Y2=YL, O=(blank), DH=(blank); T2=WH, T3=PU, T4=BR, T5=YL for 2-stage; for 1-Stage Applications T9 variant, T2=WH only; for 1-Stage T6 variant, T2=YL, T4=BR, T5=WH). For 1-Stage application, remove the Y1-to-T3 PU jumper (see Figures 5A/5B in source for exact wiring, T1 cooling airflow uses the jumper removal).

### AMST Electric Heat Temperature Rise Tables (IO-4011B page 11, Tables 5-7)
Heat kit nominal kW columns: 3, 5, 6, 8, 10, 15, 19/20, 25. Temp rise (°F) values by CFM (800-2000) and supply voltage:
**230/1/60 supply:** 800 CFM → 12/19/23/31/37°F (3/5/6/8kW); 1200 CFM → 8/12/15/21/25/37/49/62°F (3/5/6/8/10/15/19/25kW); 2000 CFM → 5/7/9/12/15/22/30/37°F.
**220/1/60 supply:** 800 CFM → 11/18/22/30/35°F; 1200 CFM → 7/12/15/20/24/35/47/59°F; 2000 CFM → 4/7/9/12/14/21/28/35°F.
**208/1/60 supply:** 800 CFM → 10/17/21/28/33°F; 1200 CFM → 7/11/14/19/22/33/45/56°F; 2000 CFM → 4/7/8/11/13/20/27/33°F.
Formula for CFM not in table: TR = (kW × 3412) × Voltage Correction / (1.08 × CFM), where Voltage Correction = .96 (230V), .92 (220V), .87 (208V).

### Minimum CFM Required for Heater Kits (Table 8, IO-4011B page 12)
| Model | 3kW | 5kW | 6kW | 8kW | 10kW | 15kW | 19kW | 20kW | 25kW |
|---|---|---|---|---|---|---|---|---|---|
| AMST24BU1300 | 715 | 715 | 715 | 715 | 850 | 850 | — | — | — |
| AMST30BU1300 | 715 | 715 | 715 | 715 | 875 | 1050 | — | — | — |
| AMST36CU1300 | 1170 | 1170 | 1170 | 1170 | 1170 | 1345 | 1345 | — | — |
| AMST42CU1300 | 1170 | 1170 | 1170 | 1170 | 1170 | 1345 | 1345 | — | — |
| AMST48CU1300 | 1170 | 1170 | 1170 | 1170 | 1170 | 1345 | 1345 | — | — |
| AMST60DU1300 | 1590 | 1590 | 1590 | 1590 | 1590 | 1715 | — | 1715 | 1930 |
(These are absolute minimum allowable airflows, not recommended airflow — follow the nameplate's Minimum Blower Setting/speed tap instead.)

### AMST Airflow Data — full CFM-by-static-pressure table (Table 9, IO-4011B page 13)
Format: CFM at 0.1"–0.9" w.c. static pressure, by model and speed tap (T1 lowest to T9 highest, T6-T9 not applicable on all models):
- **AMST24BU1300:** T1: 825/800/745/730/660/645/560/550/460 (0.1-0.9"); T5: 1045/1025/985/970/920/910/850/845/785; T9: 1215/1195/1155/1145/1105/1095/1045/1040/980
- **AMST30BU1300:** T1: 855/830/780/765/705/695/625/615/515; T5: 1185/1165/1125/1115/1070/1060/1015/1010/960; T9: 1185/1165/1125/1115/1070/1060/1015/1010/960
- **AMST36CU1300:** T1: 1070/1035/960/935/830/810/700/690/610; T5: 1560/1530/1470/1455/1390/1380/1310/1300/1235; T9: 1830/1805/1755/1740/1685/1675/1605/1595/1525
- **AMST42CU1300:** T1: 1165/1140/1085/1065/990/975/895/880/765; T5: 1495/1470/1425/1415/1365/1355/1305/1295/1220; T9: 1760/1730/1700/1670/1640/1610/1580/1550/1505
- **AMST48CU1300:** T1: 1420/1390/1330/1310/1235/1220/1135/1125/1050; T5: 1735/1710/1660/1640/1560/1550/1485/1475/1410; T9: 1820/1795/1750/1735/1680/1670/1605/1595/1525
- **AMST60DU1300:** T1: 1215/1175/1095/1070/975/950/790/780/700; T6: 1815/1785/1725/1710/1650/1640/1570/1560/1490; T9: 1970/1945/1895/1880/1815/1805/1740/1730/1660
(Full table has all 9 taps per model in the source PDF — the above shows lowest/mid/highest tap per model as a sample; ask for any specific tap's exact number if needed.)
Notes: airflow data at 230V without air filter in place; static on table includes static from media filter; cooling/heat pump speed tap should be selected based on AHRI rating, otherwise select a tap providing minimum 350 CFM per outdoor ton; use CFM adjustment factors of 0.98 (horizontal left) and 0.96 (horizontal right & downflow orientations); humidistat can adjust cooling airflow to 85%.

### AMST Mitigation Mode Table (Annex GG, Table 10) — R-32 leak minimum room area requirements
| Model | Qmin CFM | Min Room Area (m²) | Min Room Area (ft²) |
|---|---|---|---|
| AMST24BU1300 | 379 | 19.49 | 210 |
| AMST30BU1300 | 380 | 19.58 | 211 |
| AMST36CU1300 | 380 | 19.58 | 211 |
| AMST42CU1300 | 494 | 25.43 | 274 |
| AMST48CU1300 | 593 | 30.53 | 329 |
| AMST60DU1300 | 690 | 35.54 | 383 |
(Qmin = minimum circulation airflow to the conditioned space; TAmin = required minimum area of total conditioned space — this table confirms whether a room is large enough to safely dilute an R-32 leak per code.)

## 4. Gas furnaces — 80%/90%/two-stage families (IO-2035A, IO-2037A, IO-2043, IO-2044)
All four share the same core EE-code troubleshooting architecture (Daikin/Goodman "ClimateTalk"-style integrated control module). The two-stage 2043/2044 manuals add E10/E11/onboard-sensor codes not present in some single-stage docs; the newest 90% two-stage (IO-2044) uses "CoolCloud HVAC App" branding instead of "R-32 Information Section" wording but the codes are the same family.

### Universal 1-Stage / EE Troubleshooting Codes (present across all 4 furnace manuals)
| LED | Fault | Cause | Fix |
|---|---|---|---|
| I dL | Normal operation | — | — |
| EE0 | Furnace fails to operate (lockout, 3 failed ignition retries) | Gas interruption, pressure switch drainage, igniter misalignment, dirty flame sensor, flue blockage, bad induced draft blower | Locate/correct gas interruption; check front cover pressure switch drainage; replace/realign igniter; clean flame sensor; check flue piping; verify induced draft blower |
| EE1 | Furnace fails to operate | Low-stage pressure switch circuit closed at cycle start, stuck contacts, short in wiring | Replace low stage pressure switch; repair short in wiring |
| EE2 | Induced draft blower runs continuously, no furnace operation | Pressure switch circuit not closed, hose blocked/pinched, blocked flue/inlet pipe, weak induced draft blower, wrong switch set point, loose wiring | Inspect/repair pressure switch hose; inspect flue/inlet piping for blockage; check drain system; check induced draft blower performance; check/replace pressure switch; tighten wiring |
| EE3 | Circulator blower runs continuously, no furnace operation | Primary limit circuit open — insufficient conditioned air, blocked filters/restrictive ductwork, improper blower speed, failed blower motor, loose wiring in high limit circuit | Check filters/ductwork for blockage; check circulator blower speed/performance; correct speed or replace motor; tighten wiring |
| EE4 | Induced draft + circulator blower run continuously, no furnace operation | Flame sensed with no call for heat — short to ground in flame sense circuit, lingering burner flame, slow-closing gas valve | Correct short at flame sensor/wiring; check for lingering/lazy flame; verify gas valve operation |
| EE5 | No furnace operation | Open fuse, short in low voltage wiring | Replace fuse; locate and correct short |
| EE6 | Normal furnace operation (informational) | Flame sense micro amp signal minimal/coated/oxidized/misaligned, lazy flame from improper gas pressure/combustion air | Clean flame sensor; inspect alignment; check inlet air piping for blockage; compare/adjust gas pressure to rating plate |
| EEL | Furnace fails to operate | Problem with igniter circuit — improperly connected/shorted igniter, poor unit ground, igniter relay fault | Check/correct wiring from control module to igniter; diagnose/replace shorted igniter; verify unit ground; check igniter output from control |
| EEA | Furnace fails to operate | Polarity of 115V AC reversed, poor unit ground | Correct polarity/wiring; verify proper ground |
| EEb | Furnace fails to operate | Gas valve not energized when it should be (external gas valve error) | Check wiring in gas valve circuit; replace integrated control board |
| EEC | Furnace fails to operate | Gas valve energized when it shouldn't be (internal gas valve error) | Check wiring in gas valve circuit; replace integrated control board |
| None (no LED signal) | Furnace fails to operate, integrated control module LED provides no signal | No 115V power to furnace or no 24V power to module, blown fuse/tripped breaker, non-functional module | Restore power; correct condition that caused fuse to open, replace fuse; replace non-functional module |
| E10 | Furnace fails to operate | Grounding fault, poor neutral connection | Verify neutral wire connection to furnace and continuity to ground source |
| E11 | Furnace fails to operate | Open roll out switch | Check for correct gas pressure; check burner alignment; check/correct burner restriction |
| EEn | Furnace fails to operate | Igniter open | Check for igniter wiring; replace damaged igniter |
| EEJ | Furnace fails to operate | Inducer relay error | Replace integrated control board |
| EEH | Twinning feature not working | TWIN error | Check for wiring connections; replace integrated control board |
| EEE | Furnace fails to operate | Internal faults or IRQ loss in control board | Replace integrated control board |
| EbL | Furnace fails to operate, goes to hard lockout | Main blower motor consuming very little current after heat on delay, below expected value | Check for loose motor wiring; replace blower motor if burnt |
| EbU | Furnace fails to operate, goes to hard lockout | Main blower motor consuming too much current during inducer pre-purge, above expected value | Verify wiring connections to/from motor; verify line voltage wires not reversed at control |
| EAF | Furnace stops heating, only fan runs | Furnace lost communication with R-32 sensor, in mitigation mode | Furnace may not be paired with an R-32 cooling unit — check R-32 Information Section; verify R-32 sensor wire connection not loose/damaged; replace R-32 sensor |
| EAL | Furnace stops heating, only fan runs | R-32 sensor detected refrigerant leak, furnace in mitigation mode | Investigate indoor coil for refrigerant leak; furnace resumes normal operation once leak clears and 5-min delay ends |
| EAS | Furnace stops heating, only fan runs | R-32 sensor detected a fault, furnace in mitigation mode | Investigate the R-32 sensor; replace if needed |
| Ear | Furnace stops heating, only fan runs | A2L relay in furnace control board detected a fault, furnace in mitigation mode | Investigate A2L relay; cycle power on furnace; replace integrated control board |

### Two-stage-specific additional codes (IO-2043, IO-2044 — DR80TC/DD80TC, DR96TC/DD96TC)
| LED | Fault | Cause | Fix |
|---|---|---|---|
| EE7 | Furnace fails to operate | Problem with igniter circuit (poor ground, shorted igniter, relay fault) | Check/correct wiring to igniter; diagnose/replace igniter; verify ground; check igniter output |
| EE8 | Furnace fails to operate on high stage, operates normally on low stage; induced draft blower operating | High stage pressure switch circuit closed at start of heating cycle, contacts sticking, shorts in wiring | Diagnose/replace high stage pressure switch; repair short in wiring |
| EE9 | Furnace fails to operate on high stage, operates normally on low stage; induced draft blower operating | High stage pressure switch circuit not closed | Inspect pressure switch hose; inspect flue/inlet piping; check drain system; check induced draft blower performance; tighten wiring |
| EEd (2043 only) | Furnace fails to operate, integrated control module shows EEd | Aux limit switch open (blower compartment) | Check filters/ductwork for blockage; check circulator blower speed/performance; correct speed or replace motor; tighten wiring |
| EEF (2043 only) | Furnace fails to operate, integrated control module shows EEF | Aux limit switch (condensate switch) open | Check evap drain pan, trap, piping |
| **Ed0** | Furnace fails to operate | Equipment lacks shared data | Populate shared data set using memory card |
| **E I5** | External return air temp reading not visible on CoolCloud app | Return Air Temperature Sensor Circuit is Open (External) | Allow up to 90 sec for sensor detection; verify sensor probe fully plugged in; verify connector crimped properly; verify resistance across probe is 10kΩ at 77°F (lower resistance = higher temp, higher resistance = lower temp); replace PCB if still faulted |
| **E I6** | External return air temp reading not visible on CoolCloud app | Return Air Temperature Sensor Circuit is Shorted (External) | Check sensor probe terminals/conductors for short; check PCB connector for shorts if error shown with probe unplugged; replace PCB |
| **E I7** | Supply air temp reading not visible on CoolCloud app | Supply Air Temperature Sensor Circuit is Open (External) | Same procedure as E I5 for supply sensor; 10kΩ at 77°F; replace PCB |
| **E I8** | Supply air temp reading not visible on CoolCloud app | Supply Air Temperature Sensor Circuit is Shorted (External) | Same as E I6 for supply sensor; replace PCB |
| **E I9 — THE furnace-side E19** | Onboard return air temperature reading not visible on CoolCloud app | Onboard return air temperature sensor (R311) is unplugged | Power cycle furnace (control can take up to 90 sec to detect sensors); check PCB for visible electrical/mechanical damage to onboard sensor R311; replace PCB. **This is the exact furnace-side E19 code confirmed earlier this session via Daikin's dealer app — now cross-confirmed word-for-word from the official IO-2043/IO-2044 manuals.** |
| **E IA** | Onboard return air temp reading not visible on CoolCloud app | Onboard return air temperature sensor is shorted | Power cycle furnace; ensure no foreign objects on PCB causing electrical short at R311; replace PCB |
| Ed1 | Operation different than expected or no operation | Invalid memory card data | Verify shared data set correct for specific model; re-populate using correct memory card |

### Manifold gas pressure spec (from IO-2044, applies broadly to these furnace families)
| Gas | Stage | Range | Nominal |
|---|---|---|---|
| Natural | Low | 1.6–2.2" w.c. | 1.9" w.c. |
| Natural | High | 3.2–3.8" w.c. | 3.5" w.c. |
| Propane | Low | 5.7–6.3" w.c. | 6.0" w.c. |
| Propane | High | 9.7–10.3" w.c. | 10.0" w.c. |

### Temperature rise procedure
Rise = Supply air temp − Return air temp, measured with thermometers placed where NOT subjected to radiant heat off the heat exchanger. Adjust circulator blower speed to hit the rise range on the furnace rating plate/spec sheet (increase blower speed to reduce rise, decrease to increase rise).

### Airflow/CFM tap tables
All four manuals include full Fan & Cooling Airflow and Heating Airflow tables by model/tap/external static pressure (F01-F09 taps, 0.1"-0.8" ESP) for every model size (0403A through 1205D range). These are large data tables — not transcribed row-by-row here to keep this file usable; ask for a specific model's CFM table and it can be pulled from the source PDF or re-read on request.

### Wiring diagram error code quick-reference (matches EE-code table, from wiring diagram page in each furnace manual)
Internal faults/IRQ loss = EE; Lockout due to excessive retries = EE0; Pressure switch stuck closed = EE1; Pressure switch stuck open = EE2; Flame detected when no flame should be = EE4; Open fuse = EE5; Low flame signal = EE6; Ignitor relay fault = EEn/EEJ region; Reversed line polarity/grounding error = EEA; Internal gas valve error = EEC; External gas valve error = EEb; Open rollout switch = E11; Ignitor open = EEn; Twin error = EEH; Low circulator current = Eb-range.

## 5. DMVE/DFVE EEV Air Handler (IO-4039A) — R-410A factory-charged, communicating PCB
### Fault code table (PCB LED Display, error codes E_xx)
| Code | Description | Possible Causes (highlights) | Corrective Actions (highlights) |
|---|---|---|---|
| E_Eb | No heater kit installed, system calling for auxiliary heat | No heater kit selected | Select the valid heater kit on thermostat |
| E_Ed | Heater kit DIP switches not set properly | Wrong DIP switch selection for installed heater kit | Set correct DIP switches |
| E_E5 | Fuse open | Blown fuse (F1U) | Replace fuse |
| E_EF | Auxiliary switch open | High water level in evap coil drain pan, connected alarm device activated, Aux Alarm terminals (TB4, TB5) open | Check water level in drain pan; check alarm device |
| E_d0 | Data not on network | No shared data on network | Populate shared data set using memory card |
| E_d1 | Invalid data on network | Wrong shared data on network | Populate shared data set using memory card |
| E_d4 | Invalid memory card data | Wrong memory card data | Replace memory card |
| E_b0 | Blower motor not running | Fan/motor obstruction, power interruption (low voltage), high loading conditions, blocked filters, blockage in ductwork | Check for obstruction; verify input voltage at motor; check filters/grilles/duct system; check for obstruction on fan/motor/ductwork; replace motor |
| E_b1 | Blower motor communication error | High/low AC line voltage to ID blower, incorrect wiring, locked motor rotor condition | Verify line voltage within spec; check for locked rotor condition; check circuit board or motor |
| E_b2 | Blower motor HP mismatch | Wrong/no shared data on network, locked motor rotor condition | Check circuit board or motor |
| E_b3 (low indoor airflow, without electric heat mode) | Low indoor airflow | Fan/motor obstruction, blocked ductwork/filter undersized, wiring disconnected, wrong outdoor/indoor combination, ID motor failure | Check ductwork/filter blockage; resize/replace ductwork if needed |
| E_9b (low indoor airflow, WITH electric heat mode) | Low indoor airflow | Same as E_b3 but in electric heat mode | Same corrective actions as E_b3 |
| E_70 | EEV disconnection detected | Indoor EEV coil not connected | Check Indoor EEV coil connection (PCB and junction connector) |
| E_73 | Liquid side thermistor abnormality | Open/short circuit of liquid thermistor (X5A), reading/values outside normal range | Check the connection to liquid thermistor (PCB and junction connector); replace thermistor; replace control board |
| E_74 | Gas side thermistor abnormality | Open/short circuit of gas thermistor (X5A), reading/values outside normal range | Check connection to gas thermistor; replace thermistor; replace control board |
| E_75 | Pressure sensor abnormality | Open/short circuit of Pressure Sensor, reading/values outside normal range | Check connection to pressure sensor; replace sensor; replace control board |
| E_77 | Indoor Unit - Thermostat communication error (startup & during operation) | Incorrect wiring between ID unit and thermostat, thermostat failure, power interruption (low voltage) | Verify input voltage at ID unit and thermostat; after recovering comm within 2 min, TSTAT ID NO COM will continue to be displayed and clear automatically within 5 sec; replace control board or thermostat; press LEARN button on PCB for more than 5 sec to reestablish network |

### Blower Motor family (additional codes, page 21 table)
| Code | Description | Cause | Fix |
|---|---|---|---|
| E_b4 | Blower Motor - Current Trip (or) Lost Rotor | Fan/motor obstruction, abnormal motor loading, high loading conditions, blockage in airflow | Check for obstruction on fan/motor; verify input voltage; check filters/grilles/duct system; check for obstruction; resize/replace ductwork; replace motor |
| E_b6 | Blower motor stops for over/under voltage or over heating | High AC line voltage, low AC line voltage, high ambient temperatures | Verify line voltage; check ID blower motor condition |
| E_b7 | ID blower motor does not have required parameters to function | Wrong / no shared data on the network, locked motor rotor condition | Check circuit board or motor |
| E_9b | Low Indoor Airflow (Major Error Code, EH mode only) | Same causes as E_b3 in electric heat mode | Same fixes as E_b3 |

### Diagnostic codes quick table (7-segment LED)
On = Normal Operation; Eb = No HTR kit installed, calling for aux heat (Minor); Ed = Heater kit DIP switches not set properly; E5 = Fuse Open; EF = Aux Switch Open; d0 = Data not on network; d1 = Invalid data on network; d4 = Invalid memory card data; b0 = Blower motor not running; b1 = Blower motor comm error; b2 = Blower motor HP mismatch; b3 = Blower motor operating in power/temp/speed limit; b4 = Blower motor current trip or lost rotor; b6 = Over/under voltage trip or over temp trip; b7 = Incomplete parameter sent to motor; b9 = Low indoor airflow (Minor, without EH mode); 9b = Low indoor airflow (Major, EH mode only); 70 = EEV disconnection detected; 73 = Liquid side thermistor abnormality; 74 = Gas side thermistor abnormality; 75 = Pressure sensor abnormality; 77 = Indoor unit-thermostat comm error; HU = Humidification demand; FC = Fan Cool (comm mode only); FH = Fan Heat (comm mode only); F = Fan only (manual); H1 = Electric Heat Low; H2 = Electric Heat High; dF = Defrost (comm mode only, shown as H1 in legacy setup)

### Communications Troubleshooting Chart (Red Communications LED / Green Receive LED)
- Red LED Off/None: normal
- Red LED 1 Flash: Communications Failure → depress Learn Button, verify wiring connection (depress once quickly for power-up reset, hold 5 sec for out-of-box reset)
- Red LED 2 Flashes: Out-of-box reset (control power up, learn button depressed) — no action needed
- Green LED Off: No power / comm error → check fuses/breakers, replace blown fuse, check for shorts in low voltage wiring, reset network via learn button, check data1/data2 voltages (turn power OFF before repair)
- Green LED 1 Steady Flash: No network found → broken/disconnected data wires, air handler installed as non-communicating/traditional system → check comm wiring, wire connections at terminal block, verify install type, check data1/data2 voltages
- Green LED Rapid Flashing: Normal network traffic — no action
- Green LED On Solid: Data1/Data2 miss-wire → wires reversed at air handler/thermostat/outdoor unit, short between data wires or data-to-R/C → check wiring, verify voltages

### DIP switch heater kit tables (DFVE* and DMVE* models — different tables per model family)
Switches S9/S10/S11/S12 select heater kit; NO Heater Kit = all OFF (factory default). First through Seventh Valid Heater Kit selections vary by exact model (24BP1400 vs 36CP1400 vs 42CP1400 vs 48DP1400 vs 60DP1400) — kW ratings per tap range 3-25kW depending on model. Ask for a specific model's exact DIP table if needed (data is in the source PDF, page 15, Tables 9 & 10).

### Max measured CFM allowed (airflow trim table)
| Model | Up-Flow | Down-Flow | Hz-Flow |
|---|---|---|---|
| DFVE24BP1400 | 910 | 870 | 870 |
| DFVE36CP1400 | 1450 | 1390 | 1390 |
| DFVE42CP1400 | 1520 | 1450 | 1450 |
| DFVE48DP1400 | 1590 | 1520 | 1520 |
| DFVE60DP1400 | 1890 | 1800 | 1800 |

### Heat kit temperature rise tables (240/230/208 volt supply)
Full tables present for 800-2000 CFM range across 3/5/6/8/10/15/20/25 kW heat kits — three separate tables (240V, 230V, 208V supply). Model-specific heat kit kW compatibility table (Table 7) also present: DFVE24BP1400/DMVE24BP1400 up to 10kW; DFVE36CP1400/DMVE36CP1400 up to 19kW (1250 shown at 15kW cap in one column); DFVE48DP1400/DMVE48DP1400 and 60DP1400 support up to 20/25kW. Ask for exact figures if needed — full tables are in source PDF pages 11-13.

## 6. DMVT P1400 Air Handler (IO-4040B) — ECM motor, Emerson ClimateTalk board, LEGACY/non-communicating, R-410A
**This is the exact air handler family James was missing blower tap CFM data for earlier this session (DMVT-R32 lookup gap noted in [[daikin-ahri-lookup]]) — this manual has the full tap table.**

### Speed Selection DIP Switches (Table, page 19 — "Airflow Label")
| TAP | S1 | S2 | S3 | S4 | S5 | S6 | S12 | S13 |
|---|---|---|---|---|---|---|---|---|
| A | OFF | OFF | OFF | OFF | OFF | OFF | OFF | OFF |
| B | ON | OFF | ON | OFF | OFF | OFF | OFF | ON |
| C | OFF | ON | OFF | ON | OFF | OFF | ON | OFF |
| D | ON | ON | ON | ON | OFF | OFF | ON | ON |

S1/S2 = cooling selection switches; S3/S4 = adjust selection switches; S5/S6 = profile selection switches; S12/S13 = continuous fan speed.

### Cooling/Heat Pump Airflow Table (Low Stage Cool / High Stage Cool CFM by Tap)
| Model | Tap A | Tap B | Tap C | Tap D |
|---|---|---|---|---|
| DMVT24BP14 | 370/550 | 440/660 | 525/780 | 655/975 |
| DMVT30BP14 | 395/590 | 480/720 | 575/860 | 705/1050 |
| DMVT36BP14 / DMVT36CP14 | 530/790 | 635/950 | 755/1125 | 805/1200 |
| DMVT42CP14 | 670/1000 | 805/1200 | 870/1300 | 940/1400 |
| DMVT48CP14 / DMVT48DP14 | 805/1200 | 870/1300 | 935/1395 | 1000/1490 |
| DMVT60DP14 | 940/1400 | 1005/1500 | 1165/1740 | 1195/1785 |
(Format: Low Stage Cool CFM / High Stage Cool CFM)

### Electric Heat Airflow Table (by kW and S9/S10/S11 DIP settings)
| Htr kW | S9 | S10 | S11 | DMVT24BP14 | DMVT30/36BP14 | DMVT36CP14 | DMVT42CP14 | DMVT48CP14 | DMVT48DP14 | DMVT60DP14 |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | ON | ON | ON | 550 | 550 | NR | NR | NR | NR | NR |
| 5 | ON | ON | OFF | 650 | 650 | 735 | 735 | 880 | NR | NR |
| 6 | ON | OFF | ON | 700 | 700 | 810 | 810 | 880 | 1170 | 1135 |
| 8 | ON | OFF | OFF | 800 | 800 | 935 | 935 | 1045 | 1260 | 1375 |
| 10 | OFF | ON | ON | 850 | 875 | 1020 | 1020 | 1200 | 1300 | 1455 |
| 15 | OFF | ON | OFF | 875 | 1050 | 1145 | 1145 | 1420 | 1595 | 1815 |
| 19 | OFF | OFF | ON | NR | NR | 1345 | 1345 | 1480 | NR | NR |
| 20 | OFF | OFF | ON | NR | NR | NR | NR | NR | 1595 | 1860 |
| 25 | OFF | OFF | OFF | NR | NR | NR | NR | NR | NR | 1925 |
NR = Not Rated for that model/kW combo.

### Minimum CFM Required for Heater Kits (Table 10, from IO-4040B)
Absolute minimum allowable airflow per model/heat kit kW combo (NOT the recommended airflow — follow the Minimum Blower Setting/speed tap on the unit's nameplate instead):
DMVT24BP14: 3kW=550, 5kW=650, 6kW=700, 8kW=800, 10kW=850, 15kW=875
DMVT30BP14: 3kW=550, 5kW=650, 6kW=700, 8kW=800, 10kW=875, 15kW=1050
DMVT36BP14: 3kW=630, 5kW=650, 6kW=700, 8kW=800, 10kW=875, 15kW=1050
DMVT36CP14/42CP14: 5kW=735, 6kW=810, 8kW=935, 10kW=1020, 15kW=1145, 19kW=1345
DMVT48CP14: 5kW=880, 6kW=880, 8kW=1045, 10kW=1200, 15kW=1420, 19kW=1480
DMVT48DP14: 5kW=1040, 6kW=1170, 8kW=1260, 10kW=1300, 15kW=1595, 20kW=1595
DMVT60DP14: 5kW=1135, 6kW=1265, 8kW=1375, 10kW=1455, 15kW=1815, 20kW=1860, 25kW=1925

### Fault Code Table — Legacy/ComfortNet dual naming (7-segment LED / ComfortNet thermostat message)
| 7-Seg | ComfortNet Msg | Fault | Cause | Fix |
|---|---|---|---|---|
| (No Display) | None | LED display fails to energize on call for W1/Aux/Emergency heat | Normal operation OR heater kit oversized/undersized/mismatched for shared data (see EC below) | Check dip switches / shared data |
| EC | HTR TOO LARGE | Heater kit selected via dipswitches is too large for heater kits specified in shared data set | Verify installed electric heater is valid for the air handler blower model; check nameplate/spec sheet for allowable heater kit(s); verify shared data set is correct, re-populate with correct memory card if required |
| EC (alt) | HTR TOO SMALL | Heater kit selected via dipswitches is too small for heater kits in shared data set | Same corrective actions as HTR TOO LARGE |
| EC (alt) | NO HTR MATCH | Heater kit selected doesn't match heater kits specified in shared data set | Same corrective actions as HTR TOO LARGE |
| EF | Aux Alarm Fault | Aux switch open — high water level in evaporation coil | Check overflow pan and service |
| EE | INTERNAL FAULT | No 208/230V power to air handler blower or no 24V power to control module, blown fuse/breaker, internal fault | Assure 208/230V and 24V power to air handler; check integrated control module fuse (3A); check for possible shorts in 208/230V and 24V circuits, repair as necessary; replace bad integrated control module |
| d0 | NO NET DATA | Data not yet on network | Populate shared data set using memory card |
| d1 | INVALID DATA | Invalid data on network | Populate correct shared data set using memory card |
| d4 | INVALID MC DATA | Invalid memory card data | Verify shared data is correct for specific model; re-populate data using correct memory card if required |
| b0 | MOTOR NOT RUN | Circulator blower motor not running when it should be | Loose wiring connection at circulator motor power leads or circulator motor power leads disconnected; failed circulator blower motor | Tighten or correct wiring connection; check circulator blower motor, replace if necessary |
| b1 | MOTOR COMM | Integrated control module has lost communications with circulator blower motor | Loose wiring connection at circulator motor control leads; failed circulator blower motor | Tighten or correct wiring connection; check circulator blower motor, replace if necessary; check integrated control module, replace if necessary |
| b2 | MOTOR MISMATCH | Circulator blower motor horse power in shared data set does not match circulator blower motor horse power | Incorrect circulator blower motor in air handler, or incorrect shared data set in integrated control module | Verify circulator blower motor is the specified type for the air handler model, replace if necessary; verify shared data set is correct for the specific model, re-populate correct memory card if required |
| b3 | MOTOR LIMITS | Circulator blower motor is operating in a power, temperature, or speed limiting condition | Blocked filters, restrictive ductwork, undersized ductwork, high ambient temperatures | Check filters for blockage, clean/remove obstruction; check ductwork for blockage; verify all registers are fully open; verify ductwork appropriately sized for the system, resize/replace if necessary |
| b4 | MOTOR TRIPS | Circulator blower motor senses a loss of rotor control, or senses high current | Abnormal motor loading, sudden change in speed or torque, sudden blockage of air handler/coil air inlet or outlet, high loading conditions, blocked filters, very restrictive ductwork, blockage of air handler/coil air inlet or outlet | Check filters/registers/duct system and air handler blower/coil air inlet/outlet for blockages; see "Installation Instructions" for installation requirements |
| b5 | MTR LCKD ROTOR | Circulator blower motor fails to start 10 consecutive times | Obstruction in circulator blower housing, seized circulator blower motor bearings, failed circulator blower motor | Check circulator blower for obstructions, remove/repair/replace wheel and/or motor if necessary; check shaft rotation and motor; replace motor if necessary |
| b6 | MOTOR VOLTS | Circulator blower motor shuts down for over/under voltage condition or over-temperature condition on power module | High AC line voltage to air handler blower, low AC line voltage to air handler blower, high ambient temperatures | Check power to air handler blower — verify line voltage is within the range specified on the air handler blower rating plate |
| b7 | MOTOR PARAMS | Circulator blower motor does not have enough information to operate properly; motor fails to start 40 consecutive times | Error with integrated control module, motor has a locked rotor condition | Check integrated control module — verify control is populated with correct shared data (see data set errors above); check for locked rotor condition (see b5 for details) |
| b9 | LOW ID AIRFLOW | Airflow is lower than demanded | Blocked filters, restrictive ductwork, undersized ductwork | Check filters for blockage, clean/remove obstruction; check ductwork for blockage; verify all registers are fully open; verify ductwork appropriately sized, resize/replace if necessary |

### 7-segment LED status quick reference (Diagnostic Codes table, page 29)
(no display) = Internal control fault/no power; On = Standby, waiting for inputs; Ed = Heater kit DIP switches not set properly; Eb = No HTR kit installed, calling for aux heat; E5 = Fuse open; EF = Aux switch open; d0 = Data not on network; d1 = Invalid data on network; d4 = Invalid memory card data; b0-b9 = see table above; C1 = Low stage cool (legacy only); C2 = High stage cool (legacy only); P1 = Low stage HP heat (legacy only); P2 = High stage HP heat (legacy only); h1 = Emergency heat low (comm only); h2 = Emergency heat high (comm only); FC = Fan cool (comm only); FH = Fan heat (comm only); F = Fan only; H1 = Electric heat low; H2 = Electric heat high; dF = Defrost (comm only, shown as H1 in legacy setup). Green CFM LED: each flash = 100 CFM approximation (e.g. 8 flashes = 800 CFM).

### Communications Troubleshooting Chart (same LED architecture as DFVE/DMVE — see section 5 above for full table; DMVT adds "Verify that bus BIAS and TERM dipswitches are in the ON position" as a corrective action for Red LED 1 Flash)

### High Humidity / Condensate Kit tables (DMVT)
- HHK0004: DMVT24B/30B/36B — HHK0005: DMVT36C/42C/48C — HHK0006: DMVT48C — HHK0007: DMVT48D — HHK0008: DMVT48B
- DFKE-02 downflow kit: DMVT24B/30B/36B/36C/42C — DFKE-03: DMVT48C/48D/60D
- CMK0018: DMVT24B/36C — CMK0019: DMVT30B/36B/42C — CMK0020: DMVT48C/48D/60D

## Notes for future use
- All fault code tables above are transcribed as close to verbatim as practical from the official manuals — use these as the authoritative source over any third-party/airintelligence.com reference for these specific models.
- CFM/airflow tap tables for the four gas furnace families (DR80SN, DR92SN/DR96SN/DD96SN, DR80TC/DD80TC, DR96TC/DD96TC) exist in full in the source manuals but were not transcribed row-by-row here due to size — request a specific model's table if needed for the toolkit or a lookup.
- The DFVE/DMVE (IO-4039A) heater kit DIP switch valid-kit tables (which kW maps to which S9-S12 pattern, per exact model) also were not fully transcribed — same reason, request if needed.
