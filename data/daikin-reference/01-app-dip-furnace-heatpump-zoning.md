## DIP SWITCHES
### READ THIS FIRST

Daikin says the wiring diagram on the unit is the most up-to-date wiring, and it marks the factory switch settings. Check it before you touch anything.

- **BEFORE YOU CHANGE A SINGLE SWITCH:** Photograph or write down the as-found switch positions. On a board swap, set the new board to match, but leave any switch Daikin marks "prohibited to change" at factory, even if the old board had it moved.

- **WHERE THE SETUP LIVES (BOTH FIT GENERATIONS):** On both the R-410A and R-32 Fit, airflow trim, cool profiles, dehumidification and zoning are set in the outdoor unit's 7-segment menu (Setting Mode 1 and 2), not on switches. The DIP switches cover comm termination and emergency mode.

### R-410A GENERATION — SWITCH TABLE

DZ6VS/DX6VS outdoor + DV**FEC/DFVE EEV air handler + CAPE(A)/CHPE EEV cased coil. From Daikin service instructions SiUS612209EA/EB p.34–35.

- **DS-1 (outdoor), switches 1&2:** Both ON — factory default. Termination resistor.

- **DS-2 (outdoor), switches 1&2:** Both OFF — factory default. Cooling emergency level: ON/OFF = Low, OFF/ON = Medium, ON/ON = High. Must be at factory setting for normal operation.

- **DS-3 (indoor, S9–S12):** All OFF — factory default. Heater kit selection, EEV air handler only. Full kW table on the Heat Pump & Air Handler tab.

- **DS-4 (indoor), switches 13&14:** Fan-only speed, EEV air handler only: OFF/OFF = 25%, ON/OFF = 50% (factory default*), OFF/ON = 75%, ON/ON = 100%.

- **DS-4, switch 15:** ON = factory default**. EEV Enable.

- **DS-4, switch 16:** OFF — No Use.

- **DS-5, switches 17&18:** 17 ON / 18 OFF = factory default**. Emergency EEV Opening.

- **DS-5, switch 19:** OFF = factory default**. EEV Emergency Mode.

- **DS-5, switch 20:** OFF — No Use.

- **DS-6 (indoor), switches 21&22:** OFF/OFF = Normal (factory default*). ON/OFF = Cooling emergency. OFF/ON = Heating emergency High. ON/ON = Heating emergency Low (air handler only — the EEV cased coil doesn't have this).

- **DS-6, switches 23&24:** OFF — No Use.

- **FOOTNOTES (DAIKIN'S WORDING):** * Must be set at factory setting to operate the normal mode. ** Must be set at factory setting in indoor unit with EEV. It's prohibited to change setting. Switches 15, 17, 18 and 19 have no field procedure — leave them alone.

### R-32 GENERATION — OUTDOOR UNIT (DH6VS/DH7VS/DC6VS/DC9VS)

- **DS1 (OUTDOOR) + DS7 (INDOOR) = COMM TERMINATION:** They set the termination resistance on the communication circuit. Factory default is combination 1. On a comm error, try each combination one at a time and apply power after each change (3P761829-1B p.47).

| Combination | DS1 outdoor | DS7 indoor |
|---|---|---|
| 1 (factory default) | Both ON | Both ON |
| 2 | OFF | ON |
| 3 | ON | OFF |
| 4 | OFF | OFF |

- **CHECK FOR DS7 FIRST:** Daikin says to check the indoor unit's install manual to see whether that indoor unit has a DS7 switch.

- **MOST SETUP IS IN THE 7-SEGMENT MENU:** Cool airflow trim, cool profiles, dehumidification and zoning are in Setting Mode 1 and 2 on the outdoor display (3P761829-1B p.48, 55). The wiring diagram also shows a DS2 bank; its function isn't published.

### R-32 GENERATION — AIR HANDLER (DFVE) / EEV COIL (CAPEA/CHPEA)

- **DS7 = INDOOR HALF OF THE TERMINATION PAIR:** Paired with outdoor DS1 — see the combination table on the R-32 outdoor card.

- **208/230V DFVE (P1300):** Takes 3–25 kW heater kits. "Do not change any other dip switches other than S9 to S12" (IOD-4054B p.17). Set the heater size in both the thermostat and S9–S12.

- **115V DFVE (P0300):** No heater kit: "Heater kit is not compatible with this model." Daikin says do not change any dip switches.

- **CAPEA/CHPEA EEV COIL:** No R-32 coil switch table has been verified yet. Go by the wiring diagram on the unit.

### EMERGENCY MODE — WHAT IT ACTUALLY DOES

R-410A Fit EEV equipment, from SiUS612209EB p.32–34. Only for when broken comm wires or a failed thermostat can't be fixed right away. Daikin: "must be limited to a minimum… This is only a temporary solution." It does not hold a set point, and the thermostat and outdoor display won't show status. The indoor board shows "EE".

- **WHEN IT'S ALLOWED:** Outdoor showing E51 or Ed2, or the EEV indoor unit showing E76, E77 or E78, and it can't be fixed right away.

- **COOLING — EEV AIR HANDLER:** Power off. Set fan speed on DS-4 (13/14: 25/50/75/100%). Set DS-6 21 ON / 22 OFF. Pick the cooling level on outdoor DS-2 (Low ON/OFF, Medium OFF/ON, High ON/ON). Compressor speed follows outdoor temp: 100% above 95°F, 50% below 70°F. The indoor unit keeps running the EEV for superheat control.

- **COOLING — EEV CASED COIL:** Power off. Remove the 1, 2, R, C comm wires from all equipment. Jumper the furnace or modular blower's comm terminals per its own service manual. Set the coil's DS-6 21 ON / 22 OFF, then pick the level on outdoor DS-2. Do the furnace/blower jumper before setting DS-2 — Daikin warns the compressor may be damaged otherwise.

- **HEATING — EEV AIR HANDLER:** Runs the heat strips with no thermostat. DS-6 OFF/ON = High (8 min on / 8 off), ON/ON = Low (7 min on / 15 off). S9–S12 must match the installed heater kit, or it may show "Ed". The outdoor unit must stop.

- **HEATING — EEV CASED COIL:** Uses the gas furnace or modular blower. Remove the comm wires, jumper the furnace/blower per its manual, set the coil's DS-6 21 OFF / 22 ON. No outdoor switch needed — the outdoor unit must stop.

- **PUT IT BACK:** Once comm is fixed: DS-6 back to OFF/OFF, outdoor DS-2 back to OFF/OFF, and reconnect all the thermostat comm wiring. Never touch switches 15, 17, 18, 19 — Daikin marks them prohibited to change.

### COMMON MISTAKES & TROUBLESHOOTING

- **CHANGED A SWITCH, NOW IT WON'T COMM:** Put every switch back to as-found. The comm switches are DS1 (outdoor) and DS7 (indoor). Change one thing at a time. After a change, restart outdoor unit first, then the indoor unit (SiUS612209EB p.71).

- **REPLACED THE BOARD:** Match the old board's as-found positions before applying power, except switches marked prohibited to change — those stay at factory.

- **ONE DEVICE KEEPS DISAPPEARING:** Check the wiring at that device's 1 and 2 terminals first, then run the DS1/DS7 combinations on the R-32 outdoor card.

## FURNACE & AC
### DAIKIN FIT LINEUP

| Outdoor | Type | Refrigerant | Pairs with |
|---|---|---|---|
| DZ17VSA / DZ6VS | Heat pump | R-410A | DV**FEC / DFVE air handler, CAPE(A) / CHPE EEV coil |
| DX17VSS / DX6VS | AC | R-410A | DV**FEC / DFVE air handler, CAPE(A) / CHPE EEV coil |
| DH6VS / DH7VSA | Heat pump | R-32 | DFVE air handler, CAPEA / CHPEA EEV coil |
| DC6VS / DC9VSA | AC | R-32 | DFVE air handler, CAPEA / CHPEA EEV coil |

DH7VSA and DC9VSA are the Enhanced Capacity / High Efficiency models. R-32 Fit needs a Daikin-approved communicating thermostat (Daikin One+). Fit also connects with any Daikin communicating gas furnace.

### GAS FURNACE PAIRING

A Fit heat pump pairs with a Daikin communicating gas furnace through an EEV cased coil (SiUS612209EB shows "EEV Cased Coil + Gas Furnace").

- **DUAL-FUEL BALANCE POINT:** Where the switchover between the gas furnace and the heat pump is set — see AUX / SUPPLEMENTAL HEAT SET-UP on the Heat Pump & Air Handler tab.

- **COMMUNICATING WIRING:** Terminal map for a communicating 2-stage furnace paired with a legacy 24V air conditioner is on the Heat Pump & Air Handler tab's WIRING — TERMINAL MAPS card.

### EEV COIL BASICS

- **WHAT IT IS:** Electronic Expansion Valve — a stepper-motor-driven metering device that replaces a fixed orifice or mechanical TXV. The indoor board drives it directly.

- **WHY FIT USES IT:** The variable-speed compressor modulates capacity across a wide range; only an electronically controlled valve can keep up with metering refrigerant correctly at every step instead of just at full load.

- **SUPERHEAT CONTROL:** The indoor board reads the coil thermistors and pressure sensor and steps the valve itself. There's no field adjustment. A bad reading points to a sensor, wiring or board check (codes 70–75).

- **EMERGENCY MODE:** There's no field procedure for forcing the EEV to a position — Daikin marks the EEV switches "prohibited to change." Coil emergency mode is DS-6 plus jumpering the furnace's comm terminals. See the Emergency Mode card on the DIP Switches tab.

### FIELD CONFIGURATION — R-32 EEV COIL (CAPEA/CHPEA)

- **SWITCHES:** No R-32 coil switch table has been verified yet. Go by the wiring diagram on the unit. If the coil has a DS7, it's the indoor half of the comm termination pair (see the R-32 outdoor card on the DIP Switches tab).

- **EMERGENCY MODE:** On the R-410A coil (the only one with a published procedure): DS-6 21 ON / 22 OFF = cooling, 21 OFF / 22 ON = heating via the furnace. Full steps on the DIP Switches tab.

### AC-ONLY OUTDOOR UNITS

The AC and heat pump models share one install manual per generation. A few settings are heat-pump only (marked "HP only" in the Setting Mode menu).

- **R-410A GENERATION:** Fit: DX6VS (AC) and DZ6VS (heat pump) share service instructions SiUS612209EA/EB. ComfortNet: DX7TC/DX16TC/DX18TC (AC) and DZ7TC/DZ16TC/DZ18TC (heat pump) share RSD6200007.

- **R-32 GENERATION:** DC6VS / DC9VSA (AC) and DH6VS / DH7VSA (heat pump) share install manual 3P761829-1B.

### COPELAND CORESENSE™ MODULE — AMANA ALXS/ALZS, DAIKIN DC/DH SINGLE & TWO-STAGE

Self-contained diagnostic module on any residential condensing unit with a Copeland Scroll compressor — no external sensors needed. Full ALERT/LOCK flash-code tables for both the 3-wire and 2-wire "Comfort Alert" versions are in the FAULT CODE REFERENCE card on the CODES & MANUALS tab — this card is wiring/hardware context only. Source: Amana RS6200301r1 / Daikin RSD6200301 (identical servicing content, different brand cover).

- **3-WIRE MODULE:** Amana ALXS/ALZS; Daikin DC4SEA/DC5SEA/DH4SEA/DH5SEA. Status LEDs: Solid Yellow "RUN" = normal operation. Solid Red "TRIP" = thermostat demand (Y) present but compressor not running.

- **2-WIRE "COMFORT ALERT" MODULE:** The manual's "Applies to" line for this module is blank, so the model list isn't published. Same self-contained design. Wiring: indoor unit C/Y terminals → CoreSense module C/Y → contactor coil, with HPCO (high-pressure cutout) and LPCO (low-pressure cutout) switches in the circuit. Green power LED = voltage present. Yellow alert LED flashes the fault code. Red trip LED = compressor tripped or has no power.

- **READING THE FLASH PATTERN:** Flash code = number of LED flashes, pause, repeat. TRIP and ALERT LEDs flashing together = control circuit voltage too low for operation — check line voltage and transformer output before condemning the module.

### HIGH/LOW PRESSURE CONTROL TEST & CAPACITOR TESTING — AMANA/DAIKIN CONDENSERS

Source: Amana RS6200301r1 / Daikin RSD6200301.

- **HIGH PRESSURE SWITCH:** Should open at 610 PSIG ±10, close at 420 PSIG ±25. Test in cooling: disconnect power, disconnect the condenser fan motor's black wire (single-stage) or unplug it from the board (2-stage), apply power, set thermostat to cool. Test in heating: disconnect the evaporator fan motor's black wire instead, set thermostat to heat.

- **LOW PRESSURE SWITCH:** Should open at 21 PSIG, auto-reset (close) at ~50 PSIG. Test is the opposite of the high-pressure test: in cooling disconnect the EVAPORATOR fan, in heating disconnect the CONDENSER fan, run a call and verify open/close pressures.

- **RUN CAPACITOR FORMULA:** Start Winding Amps × 2,652 ÷ capacitor voltage = microfarads. Measure amp draw from Herm to the start terminal, and voltage across the HERM–C terminals.

- **DIGITAL METER (CAPACITANCE MODE):** Discharge the cap first (Daikin: through a 200–300 Ω resistor). Remove it from the circuit, select capacitance mode, connect leads, compare to the printed value — actual reading slightly under printed is fine; significantly lower or zero means replace.

- **ANALOG METER:** Good = swings to zero then slowly returns to infinity. Shorted = swings to zero and stays. Open = no reading at all.

- **HARD START KITS:** In most cases not required on Scroll compressor units — a non-replaceable check valve in the discharge line prevents high-side pressure buildup and needs only ~½ sec to equalize. If used in low-voltage/low-lock-rotor situations, only Amana-brand or Copeland-approved kits are permitted. "Kick Start" / "Super Boost" kits are NOT approved.

## HEAT PUMP & AIR HANDLER
### SWITCH TABLES

The R-32 outdoor DS1/DS7 termination table, the R-410A switch table and emergency mode are on the DIP Switches tab.

### COMM BUS BIAS VOLTAGE TROUBLESHOOTING

Straight from Daikin's own reference guide — the field procedure for a "not discovering equipment" complaint on a communicating system.

1. Power off first: check every connected component for loose, disconnected, broken, or shorted wires. Confirm no short between Data1 or Data2 and R (24VAC) or C (24VAC common). Confirm Data1/Data2 aren't reversed at the indoor unit, thermostat, or outdoor unit.

1. Apply power. Confirm 24VAC across R and C at each block.

1. If equipment still isn't discovering, check the comm bus bias: with the thermostat OFF and the system idle, measure DC voltage from 24VAC common to Data1 (= D1 VDC) and from 24VAC common to Data2 (= D2 VDC). Bias = D1 − D2, target 0.6 VDC (Daikin's own worked example: 0.61 VDC).

1. Measure Data1-to-Data2 directly — it should equal the bias value from the previous step. Check bias at the indoor unit and at any EEV coil the same way; all readings should match across every terminal block.

1. If bias reads below 0.6 VDC, move the outdoor board's TERM DIP switch (DS1) to OFF. This should bring the bias up to 0.6 VDC.

1. After any wiring or DIP-switch change, fully power down the system, wait a few minutes, then power back up. Allow 3–5 minutes for the thermostat to rediscover the indoor and outdoor equipment.

### AUX / SUPPLEMENTAL HEAT SET-UP

- **HP LOCKOUT TEMPERATURE:** Compressor won't run below this outdoor temp. Range −40°F to 65°F in 5°F steps, default −5°F. Must be at least 10°F below the aux heat lockout temperature.

- **AUX HEAT LOCKOUT TEMPERATURE:** Electric strip/aux heat won't run above this outdoor temp. Range −10°F to 75°F in 5°F steps, default 50°F. Must be at least 10°F above the HP lockout temperature.

- **BACKUP HEAT TRIGGER:** Between the HP lockout and aux lockout temps, backup heat is requested immediately if the gap between setpoint and indoor temp exceeds 4°F; otherwise the thermostat waits and only calls for backup if the heat pump alone isn't tracking the setpoint in a reasonable time.

- **DUAL-FUEL BALANCE POINT:** Range −10°F to 75°F in 5°F steps, default 50°F. Only the gas furnace runs below the balance point. With software v2.7 and higher, the furnace also turns on above it if the heat pump can't hold the heat setpoint.

- **T ON / T OFF:** Lets the thermostat control the aux heat source with its own PI algorithm. Heat pump as primary: T on −7°F to −3°F (default −3°F), T off −4°F to 1°F (default 1°F), and T off must be 3 or 4°F above T on. Aux as primary: T on −1 or −2°F, T off fixed at 1°F. T on/T off is also the only control option on AC-only units.

- **AUX1 / AUX2 WIRING:** Dry-contact outputs, not switched 24VAC directly — route a 24VAC signal through an SPST relay to the field device, same as any other Aux accessory (see wiring card above). Minimum 18-gauge wire, 125 ft max.

Setup path: Installer Wizard > equipment setup > heat pump > heat pump settings (lockouts, balance point) — or add equipment > aux heat source (T on/T off, connection, indoor fan behavior) for a straight aux/AC-only setup.

### FIELD CONFIGURATION — R-32 AIR HANDLER (DFVE)

- **DS7 = INDOOR HALF OF THE TERMINATION PAIR:** Paired with outdoor DS1. Factory default is both ON on both boards; the combination table is on the DIP Switches tab.

- **208/230V DFVE (P1300):** Takes 3–25 kW field heater kits. "Do not change any other dip switches other than S9 to S12" (IOD-4054B p.17). Set the heater size in both the thermostat and S9–S12 — Daikin says both places.

- **115V DFVE (P0300):** "Heater kit is not compatible with this model." Don't change any dip switches. If it gets an electric heat call, Daikin's fix is S9–S12 all OFF and heating emergency mode OFF (IOD-4055).

### DMVT AIR HANDLER — HEATER kW SWITCHES

Daikin files the DMVT manual (IOD-4040B) under R-32, but its text says "factory-shipped with R410A." Check the nameplate refrigerant.

- **SWITCH LAYOUT:** Flat S1–S13: S1/S2 cooling tap, S3/S4 and S8 trim, S5/S6 profile, S7 dehumidification, S9/S10/S11 heater kW, S12/S13 continuous fan. (The DMVE uses DS banks with S9–S12 instead.)

| Heater kW | S9 | S10 | S11 |
|---|---|---|---|
| 3 | ON | ON | ON |
| 5 | ON | ON | OFF |
| 6 | ON | OFF | ON |
| 8 | ON | OFF | OFF |
| 10 | OFF | ON | ON |
| 15 | OFF | ON | OFF |
| 19 / 20 | OFF | OFF | ON |
| 25 | OFF | OFF | OFF |

19 kW and 20 kW share a pattern because they apply to different models (IOD-4040B p.19).

- **Eb ON A DMVT:** "No heater kit installed — system calling for auxiliary heat." Do NOT set S9–S11 all OFF on a DMVT — that selects 25 kW. Set the switches to the kit that's actually installed.

### R-410A HEATER KIT SELECTION (S9–S12, EEV AIR HANDLERS)

DMVE*/DFVE* (P1400) R-410A EEV air handlers (IOD-4039B, SiUS612209EB). Set the heater capacity in both the thermostat and S9–S12. "Do not change any other dip switches other than S9 to S12," per the manual — incorrect settings elsewhere can cause a fault. Which specific kW rating maps to "1st/2nd/3rd… valid heater kit" is model-specific — the ordinal position is universal on this board, the kW label behind each position isn't, so check that model's own airflow/heater table for the actual kW value.

- **No heater kit — FACTORY DEFAULT:** S9 OFF, S10 OFF, S11 OFF, S12 OFF.

- **1st valid heater kit:** S9 ON, S10 ON, S11 ON, S12 ON.

- **2nd valid heater kit:** S9 ON, S10 ON, S11 ON, S12 OFF.

- **3rd valid heater kit:** S9 ON, S10 ON, S11 OFF, S12 ON.

- **4th valid heater kit:** S9 ON, S10 ON, S11 OFF, S12 OFF.

- **5th valid heater kit:** S9 ON, S10 OFF, S11 ON, S12 ON.

- **6th valid heater kit:** S9 ON, S10 OFF, S11 ON, S12 OFF.

- **7th valid heater kit:** S9 ON, S10 OFF, S11 OFF, S12 ON.

### WHAT THIS TAB IS

Daikin One+/One Touch communicating thermostat setup for regular unitary ClimateTalk systems (Fit, DX6VS, 2-stage, and legacy-paired communicating equipment) — wiring, DIP switches, aux heat, calibration, and how to get back into commissioning mode. This is the everyday communicating platform underneath most Daikin installs, separate from the DAIKIN ZONE tab's dedicated zoning panel. Everything below is sourced directly from Daikin's own wiring diagrams, service manuals, and thermostat reference guide.

### WIRING — TERMINAL MAPS BY SYSTEM TYPE

From the Daikin One+ wiring diagram (v1.0). Indoor to thermostat: 1→1, 2→2, R→R, C→C. The thermostat's terminal order is 1, 2, C, R, so the red and black wires cross over — but R still lands on R and C on C. Outdoor to indoor is 1 and 2 only. 18-gauge minimum, 125 ft max run.

**COMMUNICATING 2-STAGE HEAT PUMP OR A/C**

| Outdoor unit | Indoor unit | Wire | Thermostat |
|---|---|---|---|
| 1 | 1 | White | 1 |
| 2 | 2 | Green | 2 |
| R / C to the outdoor transformer | R | Red | R |
| — | C | Black | C |

Transformer is normally factory-installed in the outdoor unit; if not, a field transformer kit is required.

**COMMUNICATING FIT SYSTEM WITH AHU (DX17VSS-class outdoor)**

Outdoor 1/2 to the air handler, then 1/2/R/C from the air handler to the thermostat (R→R, C→C).

**COMMUNICATING FIT SYSTEM WITH EEV COIL**

Outdoor 1/2 to the indoor unit and EEV coil; 1/2/R/C from the indoor unit to the thermostat, R→R and C→C.

**COMMUNICATING FURNACE WITH 24V LEGACY AIR CONDITIONER**

| 24V outdoor condenser | Communicating 2-stage furnace | Wire | Thermostat |
|---|---|---|---|
| Y | Y1 | — | — |
| — | 1 | White | 1 |
| — | 2 | Green | 2 |
| — | R | Red | R |
| C | C | Black | C |

Only two wires (Y/C) run to the legacy 24V AC condenser; the furnace side still carries the full 4-wire comm run to the thermostat.

**COMMUNICATING INVERTER HEAT PUMP OR A/C**

Two wires (1/2) connect outdoor to the air handler or furnace; the indoor unit then carries the 4-wire run to the thermostat (White 1→1, Green 2→2, Red R→R, Black C→C), same as the 2-stage diagram above.

**ACCESSORY HOOKUP (HUMIDIFIER / DEHUMIDIFIER / OTHER FIELD DEVICE)**

Two accessories max, wired to either Aux 1/1c or Aux 2/2c — picked in the Daikin One+ installer wizard. The thermostat's aux outputs are dry contacts; route a 24VAC control signal through an SPST relay (normally open) to actually switch the field device's line-voltage circuit.

### DIP SWITCHES

The full R-410A switch table (DS-1 to DS-6) and emergency mode are on the DIP Switches tab. On DFVE/DMVE boards set the heater size in both the thermostat and S9–S12.

### HEATER KIT CONFIGURATION

Which method you use depends on the indoor board family — check which one you're looking at before reaching for a screwdriver or the thermostat menu.

- **DFVE / DMVE BOARDS:** Set the heater capacity in two places: the thermostat (Installer Wizard > equipment setup > air handler > heater kit > size) AND the S9–S12 DIP switches (IOD-4039B p.14–15). Airflow trim for electric heat is a separate menu one level down.

- **DMVT / MBVC BOARDS:** Heater kit size is set with DIP switches on the board (DMVT table above). Then check "heater kit installed" in the thermostat's air handler menu.

| Air handler family | Available heater kit sizes |
|---|---|
| DV25PEC, DV24FEC, DFVE24, DMVE24 | 0, 3, 5, 6, 8, 10 kW |
| DV35FEC, DV36FEC, DV37PEC, DV42FEC, DFVE35/36/42, DMVE36 | 0, 5, 6, 8, 10, 15, 19 kW |
| DV47FEC, DV48FEC, DV59PEC, DFVE47/48, DMVE48 | 0, 5, 6, 8, 10, 15, 20 kW |
| DV61PEC, DV59FEC, DV60FEC, DFVE59/60, DMVE60 | 0, 5, 6, 8, 10, 15, 20, 25 kW |
| MBVK16CH1X | 0, 3, 5, 15 kW |
| MBVK20CH1X | 0, 5, 15, 20, 25 kW |
| AWVE30, AWVE36 | 0, 3 kW |

### COMFORTNET DX/DZ 7TC–18TC — NOMINAL AIRFLOW BY OUTDOOR MODEL

R-410A ComfortNet communicating platform. The SZC models below are ComfortNet outdoor air conditioners and heat pumps. Uses CTK0* thermostats, two-way digital comms over Data1/Data2 (up to 4 wires total to the thermostat, 150 ft max, 18 AWG). Source: Daikin RSD6200007r24.

- **CTK04 STANDARD WIRING (2-wire indoor–outdoor):** Only Data1/Data2 required between indoor and outdoor units. A 40VA 208/230VAC-to-24VAC transformer (included with the CTK0* kit) powers the outdoor unit's electronic control; outdoor "C" 24V common should be grounded to equipment (earth) ground.

- **CTK04 ALTERNATE WIRING (3-wire indoor–outdoor):** Data1/Data2 plus a common "C" wire connecting both units' commons, for a better communication reference — still 4 wires total to the thermostat.

| Model | Cooling High | Cooling Low | Heating High | Heating Low |
|---|---|---|---|---|
| SZC160241 | 800 | 600 | 800 | 600 |
| SZC160361 | 1200 | 800 | 1200 | 800 |
| SZC160481 | 1550 | 1100 | 1550 | 1100 |
| SZC160601 | 1800 | 1210 | 1800 | 1210 |
| SZC180361 | 1250 | 850 | 1250 | 850 |
| SZC180481 | 1750 | 1210 | 1750 | 1210 |
| SZC180601 | 1750 | 1210 | 1750 | 1210 |
| SZC70241 | 800 | 560 | 800 | 560 |
| SZC70361 | 1200 | 840 | 1200 | 840 |
| SZC70481 | 1600 | 1120 | 1600 | 1120 |
| SZC70601 | 1890 | 1323 | 1890 | 1323 |

Full PCBJA101/102/104 air handler diagnostic codes (motor faults, heater mismatch, network data faults) are in the FAULT CODE REFERENCE card on the CODES & MANUALS tab.

### CALIBRATION PROCEDURE

Daikin's documented steps for correcting a thermostat's displayed temperature/humidity against a known-good reference.

1. Set the system mode to OFF.

1. Wait 30 minutes for the thermostat to settle and read ambient temperature.

1. Read the room temperature with a calibrated meter near the thermostat and record it.

1. In the installer settings, go to system optimization > calibration and enter the offset needed to match the meter. (Setpoint offsets is a different, demand-response setting.)

Ranges: temperature calibration −10°F to 10°F in 1°F steps (default 0°F); humidity calibration −15% to 15% in 1% steps (default 0%). Remote wireless sensors (see below) have their own, narrower calibration range: −7°F to 7°F temp, −15% to 15% humidity.

### RETURNING TO DEALER/INSTALLER MODE

For adjusting equipment settings after initial commissioning is already complete — you don't need to factory-reset the stat to get back into the setup wizard.

1. Tap the settings (hamburger) menu icon, top left of the home screen.

1. Scroll to the bottom of the settings list and select "dealer edit."

1. Select "continue" on the warning screen, then enter the 4-digit installer PIN.

1. Don't know the PIN? The dealer-edit screen has an info icon that displays the installer code.

This drops you back into the same 5-step smart thermostat setup (communication / personalization / equipment setup / system optimization / preferences) used during original commissioning — any change here can affect system operation, so know what you're changing before you change it.

### FIRMWARE / OTA UPDATES

- **AUTO-UPDATE ON SETUP:** Thermostats running software 1.6.x or older, or 2.1.x and newer, auto-update as soon as they connect to a network during the setup wizard — no separate update step needed on a fresh install with working wifi.

- **MANUAL CHECK:** Settings > thermostat > check for update. Returns either "software update found" (with an install option) or "no update available."

- **BENCH TESTING / PRE-CONFIGURING OFF-SITE:** Each thermostat needs its own 24VAC/DC power source to power up and update off-wall — a baseplate wired to a dedicated 24V adapter works fine for pre-staging stats before a job.

### WIRELESS RHT SENSOR (DSEN-TH-BWS-A)

Compatible with DTST-CWBSA-NI-A and -NI-B (Daikin One+) thermostats.

- MAX PER STAT: 8

- BATTERY: CR2450

- OPERATING RANGE: 35–104°F

- HUMIDITY RANGE: 5–95%

1.64"L × 1.64"W × 0.69"H, 3.3oz. Storage temperature −22°F to 122°F. FCC-compliant sub-gig ISM radio. Pair from the installer menu: Add Equipment > Remote Sensor > pair sensor.

### OTHER FIELD-RELEVANT DEFAULTS

| Setting | Range | Default |
|---|---|---|
| Min/max setpoints | 50°F–90°F, 1°F steps | 50°F–90°F |
| Setpoint deadband (heat/cool) | 2°F–9°F, 1°F steps | 4°F |
| Overcool to dehumidify | 0, 1, 2, or 3°F | 0°F |
| Heat pump defrost interval (R410A) | 30, 60, 90, 120 min | — |
| Heat pump defrost interval (R32, mid-2025+) | 2, 6, 12, 24 hr | — |
| Quiet mode sound suppression | Off / Quiet / Quieter / Quietest | varies by event |

The 2024 R-32 outdoor install manual (3P761829-1B) still lists 30–120 min defrost. Quiet mode / sound suppression scheduling is side-discharge outdoor units only. Defrost interval options split by refrigerant/software generation — confirm which the installed unit uses before assuming a setting exists.

## ZONING
### ZONING PLATFORM
Two platforms below: the Daikin DOZP-6-A zone panel first, then the EWC UT3000.

### WHAT THIS IS

Daikin's own proprietary communicating zoning system — not EWC, not a third-party bypass panel. Pulled straight from Daikin's TRC-15 technical training module and the DOZP-6-ADA-A install manual, current as of 2026. This is new enough that most of what's below won't be in any manual your guys can find on their own — that's the point of this tab.

- **KIT:** DOZP-6-ADA-A — ships as the DOZP-6-A zone controller + DOZA-DPS-A differential pressure sensor, 2 pitot tubes, 16ft silicone tubing, mounting screws.

- **COMPATIBLE EQUIPMENT:** Unitary R-32 inverter-driven communicating HVAC systems (Daikin, Goodman, Amana).

- **COMPATIBLE THERMOSTATS:** Daikin One+, Daikin One Touch, Amana Smart Thermostat. Requires firmware revision 4.0.10 or higher on every thermostat connected to the panel. Set up Wi-Fi in the thermostat's communication menu and it updates automatically.

- **WIRELESS RHT SENSORS:** Can be used as a zone device in place of a wired thermostat. Up to 8 RHT sensors per Daikin One+. Only pairs with a One+ — not One Touch or the Amana stat.

- **UP TO 6 ZONES — NO BYPASS:** Do not install a bypass damper. Daikin: "No bypass needed." The panel handles excess static with the differential pressure sensor — see the pressure sensor card below.

### MOUNTING & TERMINALS

- **MOUNTING LOCATION:** Return duct, a nearby wall, or studs where you can back it with plywood. Do NOT mount on the supply duct, the air handler, furnace housing, evaporator housing, or any hot water coil.

- **ZONE TERMINALS (×6):** Each zone block carries R / C / 1 / 2 (thermostat/sensor) plus C / PO / PC (damper). Up to 3 sets of damper wires can be daisy-chained into one zone's damper terminal.

- **DAMPER COMPATIBILITY:** Any 24VAC Power-Open/Power-Close damper actuator with a 35-second travel time. You cannot connect an RSD or any competitor's spring-return damper to this panel.

- **AUX 1 / AUX 2:** Two dry-contact relays (AC or DC controlled) for a whole-house humidifier, dehumidifier, or an aux heat source. Configured from the thermostat's equipment setup menu, not on the board itself.

- **A2L ALARM INPUT:** Terminals C and Alarm (IOD-7195 p.3), fed from the air handler's alarm contacts or the furnace's Alarm terminal. On a refrigerant alarm, the panel opens all zone dampers to mitigate the leak — see the fault table below for the code (0x81).

- **DAMPER TEST BUTTON:** Press once: opens all dampers, then closes them one at a time while the front-panel "test" LED blinks green. Hold 5 seconds: forces all dampers open and holds them (LED solid green) — hold 5 seconds again to exit. The install manual (IOD-7195) says the board checks every zone automatically every 10 minutes (the TRC-15 training says 5).

### TRANSFORMER & POWER SIZING

A dedicated, field-supplied 24VAC transformer is required — this panel is not powered off the equipment's own transformer. Size it off the worst-case total VA.

| Component | VA each |
|---|---|
| Daikin One+ / One Touch / Amana stat | 6 |
| Zone panel (DOZP-6-A) | 2.5 |
| Each damper (typical) | 1.5–2.5 |
| Transformer | Max dampers | Max wired stats |
| 40VA (min allowed) | up to 6 | up to 3 |
| 100VA (max allowed) | up to 24 | up to 6 |

Add up every thermostat, the panel itself, and every damper on the job, then pick the transformer that clears the total. Example: 2 stats (12VA) + panel (2.5VA) + 4×1.5VA dampers (6VA) = 20.5VA total — a 40VA transformer covers it. A bigger job (4 stats + 10 dampers at 2.5VA) can clear 51.5VA, which needs the 100VA unit.

### DIFFERENTIAL PRESSURE SENSOR (DOZA-DPS-A)

- **MOUNTING:** Pitot tubes go in the supply and return plenums (5/32" holes, arrow aligned with airflow); the sensor body mounts between the two pitot locations. Wire GND→GND, SIGNAL→SIGNAL, 5V OUT→5V IN. Confirm the green PWR LED is lit after power-up, then enable the sensor on the thermostat.

- **DEFAULT THRESHOLDS:** Min 0.6" w.c. / Max 0.8" w.c. — same defaults recommended for both a furnace+coil setup and an air handler, so leave them unless a specific job calls for a change.

- **NORMAL RELEASE (LESS AGGRESSIVE):** Thermostat compares indoor blower CFM to the max zone CFM continuously. If blower CFM is too high, it modulates only the specific dampers that need it — not a blanket response.

- **AGGRESSIVE RELEASE:** Triggers only when the sensor reads above max pressure (0.8" default): opens ALL dampers to 100% for 5 minutes. After 5 minutes it checks whether pressure has dropped below the min threshold (0.6" default) — if so, it exits and resumes normal operation; if not, it holds high-airflow relief for another 5 minutes.

If the pressure transducer's sensed path includes a media filter, subtract that filter's rated pressure drop from both the max and min pressure settings — the media filter's own spec sheet has that number.

### COMMUNICATION WIRING PRACTICE

- **BIAS VOLTAGE:** Maintain 0.6–0.9VDC across Data 1/Data 2. This is wider than the tolerance floating around in some secondhand notes — don't condemn a bus reading inside this range.

- **BUS TERM SWITCH:** Leave it in the OFF position. Do not switch it.

- **TERMINATIONS:** Never land three or more wires in one communication terminal. Landing two is fine, but twist the exposed copper together first, then insert — a one-to-one connection is always the goal when it's achievable. Avoid mixing wire gauges on the same run.

- **WIRE CAPS:** Insert the wires into the cap first and let the cap do the twisting. Twisting the wires by hand before capping weakens the connection.

### COMMISSIONING FLOW

1. Firmware upgrade on every thermostat connected to the panel — done from the "communication" menu on each stat. Do this before anything else; more than 3 stats updating at once can take longer, wait for all to finish.

1. Setup name for each thermostat (personalization menu) — an unnamed stat defaults to "main room" and makes zone assignment confusing later.

1. Setup thermostat role — one stat must be set Primary (always zone 1), the rest Additional. No primary selected throws a critical alert on the thermostat and an indoor-unit comm fault until one is set.

1. Start the zoning wizard from the zone board menu (equipment setup → zone board → start zoning wizard) — walks through every remaining step below in order.

1. Setup wired sensors — enable the diff pressure sensor and, if wanted, high airflow relief; set min/max pressure.

1. Enable zones — the board detects connected dampers automatically; check the box for each zone you want active.

1. Assign zone devices — assign every thermostat and wireless RHT sensor to its zone. Primary stat is locked to zone 1.

1. Zone settings per zone — enable voting (checked = that zone can independently call for heat/cool; unchecked = it only runs while another zone is calling), setpoint limits (set at the local stat for wired zones), overcool (for dehumidification) and deadband (the gap between heat and cool setpoints).

1. Zone weight / auto-weight — run auto-weight to measure and assign each zone's percentage of the outdoor unit's max CFM. Daikin's times: 2 zones 10–15 min, up to 30–35 min for 6 zones. Can be hand-tuned afterward.

1. Zone test — manually open/close individual zones to verify damper operation and airflow. It stops if you leave the zoning commissioning screen.

1. Complete zone board installation, then continue on into the rest of that equipment's normal system commissioning per its install manual.

Can be done entirely on the thermostat itself, or remotely through the SkyportCare app (Tools → select thermostat model → Quality Install → add job → scan the thermostat's QR/DKN code → grant 3.5-hour temporary remote access → same wizard steps as above).

### DEALER EDIT / INSTALLER CODE

To get back into the setup wizard after initial commissioning: thermostat menu → settings → dealer edit → continue past the warning. Tap the info icon (top right) to reveal a 4-character installer code, close that popup, then type the code back in and press "unlock thermostat."

### FAULT CODES — THERMOSTAT SIDE

These show as an alert on the connected thermostat itself, not on the zone panel.

| Code | Meaning | Status | Fix |
|---|---|---|---|
| 25 | Zone board communication loss | Critical | Verify voltages and check all wiring connections. |
| 31–35 | Additional zone thermostat 1–5 disconnected | Minor | Verify proper setup and all wire connections for that thermostat. |
| 36 | No primary thermostat detected | Critical | Set a primary thermostat (zone 1); verify all wire connections. |

Worth knowing cold: with no primary thermostat set, the thermostat itself shows this as error 36 — but Daikin's own training material separately notes the indoor unit will show an E77 ("not finding thermostat") at the same time. Same underlying cause, two different displays reporting it under two different numbers — check which device you're actually reading before you go hunting the wrong code.

### FAULT CODES — ZONE PANEL (HEX)

These are panel-side codes, distinct from the thermostat-side table above.

| Code | Meaning | Status | Fix |
|---|---|---|---|
| 0x81 | Refrigerant (A2L) alarm activated | Critical | Follow the A2L flow chart in the installation manual. |
| 0x82–0x87 | Zone 1–6 damper not connected | Critical | LED on the panel is solid: check that zone's damper wiring. LED flashing: check the wiring on the damper or at the zone board connector for that zone. |
| 0x88–0x8D | Zone 1–6 wired temperature sensor short-circuited | Critical | Incorrect wiring or connection — check resistance between the wiring pins and the sensor for a short on that zone. |
| 0x90 | Pressure sensor open or short-circuited | Minor | Check zone board settings and wiring. Check for 5V between C and 5V. If 5V is present and LED is off, check wiring/sensor. If 5V present and LED on, check resistance between C and Signal at the sensor connector — open reading means wiring or sensor failure. |
| 0x91 | Firmware upgrade critical data corrupted | Minor | OTA update was interrupted (e.g. power drop). Zone board restarts the OTA process automatically — no action needed. |
| 0x92 | Firmware upgrade checksum mismatched | Minor | Wrong firmware image or corrupted data received. The upgrade restarts automatically (the install manual says the zone board restarts it; TRC-15 says the thermostat) — no action needed. |
| 0x93 | External flash initialization failed | Minor | Doesn't affect zone operation, but the board won't get the latest firmware. Power-cycle; replace the zone board if it persists. |
| 0x94 | External flash read/write failed | Minor | External flash hardware fault. Power-cycle; replace the zone board if it persists. |
| 0x95 | Firmware internal flash update failed | Minor | MCU internal flash issue; board won't get the latest firmware. Power-cycle; replace the zone board if it persists. |

### ======== EWC UT3000 ZONE PANEL (everything below is EWC, not DOZP) ========

### WHAT THIS IS

The UT3000 is an EWC Controls zone panel (EWC bulletin TB-241). Goodman trained on it in TRC-2. It works with ClimateTalk communicating systems or any 24V 2-heat/1-cool system.

### COMPATIBLE SYSTEMS

- **SUPPORTED EQUIPMENT:** ClimateTalk™ communicating equipment: up to 4 stages of heat (including modulating gas) and 2 stages of cooling. Or any 24V 2-heat/1-cool system.

- **THERMOSTATS:** Any ClimateTalk-based communicating thermostat, or standard 24V thermostats.

- **ZONE CAPACITY:** 2–3 zones per panel; twin two panels to expand to 5 zones.

- **DAMPERS:** EWC URD, ND, RSD and SID, or any 24VAC 2-wire or 3-wire power-open/power-close damper. Spring-type dampers are supported: only 1 spring-type damper per zone (400 mA).

### POWER & SENSORS

- **POWER:** 24VAC, 40 VA min / 60 VA max, 50/60 Hz. EWC "always recommends" a separate transformer. 2.5 A main board protection; if F1 trips, let it cool and find the short.

- **SUPPLY AIR SENSOR (SAS):** Included. If it's disconnected or fails, the panel falls back to timed-mode staging.

- **OUTDOOR AIR SENSOR (OAS):** Optional. Communicating systems provide the outdoor temperature.

### FEATURES

- **LCD + 4 BUTTONS:** Menus, settings, live status and messages.

- **PROPORTIONAL MODE:** Operates in proportional mode at all times. On communicating systems allow at least 1–2 minutes for it to recognize the equipment (TRC-2 says 2–4).

- **DUAL FUEL:** Built in.

- **IAQ RELAY:** SPDT indoor air quality relay with an input trigger.

- **DAMPERS AT IDLE:** All dampers are open when the HVAC system is idle (TRC-2).

### WIRING & LEDs

- **DATA BUS COLORS (TRC-2):** Green = 1 (Data 1), Yellow = 2 (Data 2), White = C.

- **LEDs:** 5 colored LEDs show status and mode. Zone LEDs show which dampers are energized to open. Rapid, random pulses on the comm LEDs mean a good link.

### TROUBLESHOOTING

- **NO POWER / BLANK DISPLAY:** Check 24VAC at the transformer. If F1 tripped, let it cool, then find and repair the short.

- **DAMPER WON'T OPEN:** Check 24V at the damper motor and its 500 mA breaker.

- **COMM PROBLEMS:** Never move the termination switches on the zone controller — they stay OFF (TRC-2). Check the data wiring and bias voltage instead.

### FIELD NOTES — NOT IN ANY MANUAL

From installs, not from EWC or Daikin documentation.

- **MOLEX CONNECTOR CORROSION:** If the UT3000 has Molex push-on connectors instead of a screw terminal block, they corrode in the field, especially after being unplugged during troubleshooting. Intermittent faults 6–12 months after install: suspect those connectors.

- **MATCH DAMPER ACTUATORS:** When replacing an actuator on an existing UT3000 system, use the same model as the rest so travel times match across zones.
