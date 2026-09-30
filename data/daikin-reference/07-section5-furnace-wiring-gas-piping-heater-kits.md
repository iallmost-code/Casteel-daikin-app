# SECTION 5 — MANUAL EXTRACTION: FURNACE THERMOSTAT WIRING, GAS PIPING, HEATER KIT DIP TABLES

---
name: daikin-goodman-manuals-reference-2
description: Part 2 of James's saved Daikin/Goodman manual reference data — continues [[daikin-goodman-manuals-reference]] (part 1 was near its size cap). Covers furnace wiring/thermostat diagrams, gas piping and pressure data, and DFVE/DMVE heater kit DIP switch tables pulled from the same 11 official manuals. Read both files together for full Daikin/Goodman equipment reference.
sources: [chat]
aliases: [daikin manuals part 2, goodman manuals part 2, furnace wiring, gas piping data]
---

**DAIKIN/GOODMAN REFERENCE SET — read together for any Daikin/Goodman task (troubleshooting, equipment lookup, AHRI matching for job write-ups):**
- [[daikin-goodman-manuals-reference]] — part 1: cased coils (CHPE/CAPEA), AMST air handler, all 4 gas furnace fault code tables, DMVE/DFVE and DMVT air handlers: fault codes, wiring diagrams, CFM/dip switch tables
- [[daikin-goodman-manuals-reference-2]] (this file) — continuation: furnace thermostat wiring, gas piping/pressure specs, DFVE/DMVE heater kit DIP tables
- [[daikin-goodman-manuals-reference-3]] — Amana/Goodman condenser CoreSense diagnostics, R-32 A2L PCB codes, ComfortNet DX/DZ 7TC-18TC air handler diagnostic codes
- [[daikin-goodman-manuals-reference-4]] — DX6VS/DZ6VS inverter EEV outdoor unit full E-code table, EEV cased coil/air handler indoor error codes, emergency mode DIP switch setup
- [[daikin-ahri-lookup]] — AHRI number lookups, combo matching workflow, distributor catalog data/gaps — use this file's model spec data to confirm exact SKUs before searching ahridirectory.org
- [[hvac-pro-field-guide-app]] — the toolkit app this data feeds into (hvactoolkit.netlify.app)
For fastest field troubleshooting: search all four manuals-reference files first for the exact fault code/wiring/CFM data on the model in hand. For quoting/selling a job: cross-check exact model specs/dimensions/electrical data here against [[daikin-ahri-lookup]]'s combo-matching workflow before finalizing an AHRI number.

- [stated] this is a continuation of [[daikin-goodman-manuals-reference]] — same 11 manuals, same project (James said "get it all dont skip" / "i want all info pulled out and saved" after the first pass; this file holds wiring diagrams, gas piping specs, and DIP tables that didn't fit in part 1). James: "all of our daikin info should be linked to help me faster trouble shoot or look up info on equipment or match ahri to write the jobs up that sell"

## Gas Furnace Thermostat Wiring Diagrams (from IO-2035A, applies across the DR80SN/DR92SN/DR96SN/DD96SN/DR80TC/DD80TC/DR96TC/DD96TC family — same basic wiring convention)
**Single-stage heating with single-stage cooling:** Thermostat W-R-G-C-Y → Integrated Furnace Control Module W-R-G-C-Y/Y1-Y2 → Remote cooling unit (single stage) C-Y.
**Single-stage heating with two-stage cooling:** Thermostat W-R-G-C-Y1-Y2 → Integrated Furnace Control Module W-R-G-C-Y/Y1-Y2 → Remote cooling unit (two stage) C-Y1-Y2.
**Twinning two furnaces:** Furnace 2 and Furnace 1 each have their own W-R-G-C-Y/Y1-Y2 terminal block wired in parallel to one Room Thermostat W-R-G-C-Y/Y1-Y2, with a TWIN terminal jumper between the two furnace control boards, and separate Cond Unit Contactor connections for each. **Critical twinning note:** each furnace must be connected to its own 115VAC power supply, and the L1 connection to each furnace must be in phase (connected to circuit breakers on the same 115VAC service panel phase leg) — verify by checking voltage from L1 to L1 on each furnace; if in phase, the voltage between both furnaces will be ZERO.
**115V line accessory connections:** furnace integrated control module has line voltage accessory terminals for an optional field-supplied humidifier and/or electronic air cleaner. Humidifier = 1.0 Amp max at 120VAC; Electronic Air Cleaner = 1.0 Amp max at 120VAC. Humidifier hot terminal = HUM H; EAC hot terminal = EAC H; both neutral terminals = NEUTRAL.
**Low voltage humidifier:** furnace control module has a 24V terminal for an optional field-supplied 24V humidifier, energized any time the draft inducer is powered. This is a 24V circuit only — common connection must be on the C terminal of the low voltage strip (where thermostat wires connect); do NOT connect to the line N location where line voltage neutral wires connect.
**Low voltage ventilation:** VT IN / VT OUT dry contact connections on the control board, normally open, energize during an R-32 fault/alarm condition (for field ventilator wiring).
**Low voltage A2L alarm:** provides 24VAC for field alarm wiring connections, normally open, energizes during an R-32 fault/alarm condition.
**R-32 sensor wire:** routes from the indoor evaporator coil into the furnace, connects to the board's R-32 SENSOR terminal. A green LED next to the sensor connection indicates comm status during startup — ON during startup, then blinks (sensor present, communicating) or turns OFF (no signal from sensor). IMPORTANT: wire routing must not interfere with circulator blower operation, filter removal, or routine maintenance; must not be routed near hot surfaces or the outlet flue pipe.

## R-32 A2L Function (furnace-side, from IO-2035A — applies to all 4 furnace families)
The furnace control board can shut off gas heat and turn on the blower fan if it detects an R-32 refrigerant leak signaled by the R-32 sensor on the indoor coil. **R-32 function is ON by default.** If the cooling unit paired with the furnace does NOT use R-32 refrigerant, this function must be disabled or the furnace will not run properly.
**To disable/enable:** enter the A2L Function Enabled menu (press left/right switch until LED displays "A2E", press center switch, LED displays current setting yes/no, press left/right to toggle, press center to confirm).
**On leak detection (Mitigation Mode):** furnace displays A2L Refrigerant Leakage code (EAL), shuts down gas operation, energizes optional ventilation/alarm outputs, runs fan at max CFM airflow. Exits mitigation mode after leak clears and a 5-minute delay expires (or immediately if user turns off A2L verification, or after a fault/alarm resolves).
**A2L Verification (installer test):** simulates the leak process without an actual leak, only usable when no active faults exist — enter via "A2u" menu, select "YES"; the control exits automatically after 5 minutes, on alarm/fault, or manual override.

## Gas Furnace Filter Sizing (from IO-2035A page 17 — Minimum Recommended Filter Size table)
**Upflow models:** 0403A*=1-16x25 side or 1-14x24 bottom; 0603A*=1-16x25 side or 14x24 bottom; 0603B*=1-16x25 side or bottom; 0604B*=1-16x25 side or bottom; 0803B*=1-16x25 side or bottom; 0804B*=1-16x25 side or bottom; 0804C*=1-16x25 side or bottom; 0805C*=1-16x25 side or bottom¹; 1005C*=2-16x25 side or 1-20x25 bottom¹; 1205D*=2-16x25 side or 1-24x24 bottom¹.
**Downflow models:** 0403A*=2-10x20 or 1-14x25 top; 0603A*=2-10x20 or 1-14x25 top; 0804B*=2-14x20 or 1-16x25 top; 0805C*=2-14x20 or 1-20x25 top; 1005C*=2-14x20 or 1-20x25 top.
¹ = use 2-16x25 filters and two side returns or 20x25 filter on bottom return if furnace is connected to a cooling unit over 4 tons nominal capacity. Larger filters may be used; filters may also be centrally located; a combination of one side & bottom may be used instead of both sides.

## Gas Supply & Piping Data (from IO-2035A pages 12-15 — applies across furnace family)
**Inlet gas supply pressure:** Natural Gas: Min 4.5" w.c. / Max 10.0" w.c.; Propane Gas: Min 11.0" w.c. / Max 13.0" w.c.
**Manifold pressure (0-4500 ft altitude):** Natural gas, no kit, #45 orifice, 3.5" w.c. manifold pressure, no pressure switch change needed; Propane, LPT-03 kit, #55 orifice, 10.0" w.c. manifold pressure. (Canada: gas furnaces only certified to 4500 ft.)
**Natural Gas Pipe Capacity (CFH) by length and nominal pipe size** (0.5 psig or less, 0.3" w.c. pressure drop, 0.60 specific gravity gas):
| Length (ft) | 1/2" | 3/4" | 1" | 1-1/4" | 1-1/2" |
|---|---|---|---|---|---|
| 10 | 132 | 278 | 520 | 1050 | 1600 |
| 30 | 73 | 152 | 285 | 590 | 980 |
| 50 | 56 | 115 | 215 | 440 | 670 |
| 100 | 38 | 79 | 150 | 305 | 460 |
CFH formula: BTUH Furnace Input ÷ Heating Value of Gas (BTU/Cubic Foot).
**Propane piping (first-to-second stage regulator, 2 psig drop at 10 psig setting, capacities in 1,000 BTU/hour):**
| Length (ft) | 3/8" | 1/2" | 5/8" | 3/4" | 7/8" |
|---|---|---|---|---|---|
| 10 | 730 | 1,700 | 3,200 | 5,300 | 8,300 |
| 50 | 330 | 770 | 1,500 | 2,400 | 3,700 |
| 100 | 220 | 540 | 1,000 | 1,700 | 2,600 |
| 200 | 150 | 380 | 700 | 1,100 | 1,800 |
**Propane satisfactory operating pressure:** 10" w.c. at the furnace manifold with all gas appliances operating.
**Total external static pressure procedure:** with clean filters, measure return duct static (negative, at furnace inlet) and supply duct static (positive, between furnace and cooling coil, via test hole in the "A" block-off plate) — sum the absolute values for total ESP. Example: return = -.1", supply = .3" → total = .4" w.c. Compare against the furnace rating plate max ESP.
**Gas heat sequence of operation (call for heat):** thermostat closes W → 24VAC on W terminal → control self-check → verify limit switch closed (24VAC Pin 8) → verify pressure switch open (0VAC Pin 5) → gas valve circuitry check → energize induced draft blower → pre-purge begins once pressure switch closes (24VAC Pin 5) → after pre-purge, energize igniter → after igniter warm-up, energize gas valve → igniter de-energized once flame sensed → after 30 sec, indoor blower energizes on heating speed → on satisfied call, gas valve de-energizes, inducer runs 15 sec post-purge, blower runs selected off-delay (90 sec default, adjustable 30-180 sec).
**Blower speed selection:** Heating (1-stage): press left/right until LED shows "gA1", press center, LED shows current speed as Fxx (xx = 01-09); available speeds for W/W1 call: F01, F02 (default), F03, F04. Cooling (1-stage, Y/Y1 call): F01 through F09, default F04. Cooling (2-stage, Y2 call): F01-F09, default F05. Continuous fan/circulation mode: press left/right until LED shows "FSd", press center to select Fxx, F01 is default circulation speed, all 9 speeds available.

## DFVE/DMVE EEV Air Handler — Heater Kit DIP Switch Tables (IO-4039A page 15, Tables 9 & 10)
**DIP Switch Setting logic (Table 10) — Switches S9/S10/S11/S12, default (No Heater Kit) = all OFF:**
| Function | S9 | S10 | S11 | S12 |
|---|---|---|---|---|
| No Heater Kit | OFF* | OFF* | OFF* | OFF* |
| First Valid Heater Kit | ON | ON | ON | ON |
| Second Valid Heater Kit | ON | ON | ON | OFF |
| Third Valid Heater Kit | ON | ON | OFF | ON |
| Fourth Valid Heater Kit | ON | ON | OFF | OFF |
| Fifth Valid Heater Kit | ON | OFF | ON | ON |
| Sixth Valid Heater Kit | ON | OFF | ON | OFF |
| Seventh Valid Heater Kit | ON | OFF | OFF | ON |

**Per-model kW mapping — DFVE\* models (Table 9):**
| Heater Kit Slot | DFVE24BP1400 | DFVE36CP1400 | DFVE42CP1400 | DFVE48DP1400 | DFVE60DP1400 |
|---|---|---|---|---|---|
| First Valid | 3 | 3/5 | 3/5 | 3/5 | 3/5 |
| Second Valid | 5 | 6 | 6 | 6 | 6 |
| Third Valid | 6 | 8 | 8 | 8 | 8 |
| Fourth Valid | 8 | 10 | 10 | 10 | 10 |
| Fifth Valid | 10 | 15 | 15 | 15 | 15 |
| Sixth Valid | — | 19 | 19 | 20 | 20 |
| Seventh Valid | — | — | — | — | 25 |

**Per-model kW mapping — DMVE\* models (Table 9, same structure, mirrored to DMVE naming):**
| Heater Kit Slot | DMVE24BP1400 | DMVE36CP1400 | DMVE48CP1400 | DMVE60DP1400 |
|---|---|---|---|---|
| First Valid | 3 | 3/5 | 3/5 | 3/5 |
| Second Valid | 5 | 6 | 6 | 6 |
| Third Valid | 6 | 8 | 8 | 8 |
| Fourth Valid | 8 | 10 | 10 | 10 |
| Fifth Valid | 10 | 15 | 15 | 15 |
| Sixth Valid | — | 19 | 19 | 20 |
| Seventh Valid | — | — | — | 25 |

NOTE: Do not change any other DIP switches besides S9-S12 — incorrect settings may cause an error. In emergency mode (comm loss), heater kit selection is driven by these same DIP switches (S9/S10/S11/S12).
**Motor orientation:** upflow needs no motor rotation; downflow requires loosening the motor mount and rotating the motor so female connections face down (prevents water collection/premature failure).
**Humidifier accessory relay:** ACC-IN/ACC-OUT 1/4" terminals, normally open. 3 modes: ON (closes only during active heat call + humidification call), OFF (never closes), IND (cycles with any humidification call independent of heat call — allows 4 fan speeds: 25/50/75/100% during idle + humidification).

## Notes for future use
- See [[daikin-goodman-manuals-reference]] (part 1) for: cased coil (CHPE/CAPEA) fault codes + wiring diagram, AMST air handler fault codes + wiring diagrams + full CFM tables, all 4 gas furnace fault code tables, DMVE/DFVE fault codes + communications troubleshooting, DMVT P1400 full fault/CFM/DIP tables.
- Still not transcribed row-by-row anywhere (exists in source PDFs, ask if needed): the four gas furnace families' full Fan & Cooling Airflow / Heating Airflow CFM tables by model/tap/ESP (large matrices, IO-2035A/2037A/2043/2044); the AMST full 9-tap CFM table for every static pressure column (a representative sample is in part 1, full table has more rows per model); CAPEA/CAPE Maximum Allowed CFM table by model.
