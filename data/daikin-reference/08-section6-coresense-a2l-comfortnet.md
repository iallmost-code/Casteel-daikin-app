# SECTION 6 — MANUAL EXTRACTION: CORESENSE DIAGNOSTICS, R-32 A2L PCB CODES, COMFORTNET AIR HANDLER CODES

# PART 3 — Amana/Daikin CoreSense Diagnostics, R-32 A2L PCB Codes, ComfortNet Air Handler Codes
Source manuals: RS6200301r1 (Amana ALXS/GLXS/ALZS/GLZS), RSD6200301 (Daikin DC3SQN/DC3SEN/DC4SQA/DC4SEA/DC5SEA/DH4SQA/DH4SEA/DH5SEA, R-32, July 2024), RSD6200007r24 (Daikin ComfortNet DX7TC/DX16TC/DX18TC/DZ7TC/DZ16TC/DZ18TC, R-410A, May 2023)

## 1. Amana ALXS/GLXS/ALZS/GLZS and Daikin DC/DH — same architecture, different brand covers
These two manuals are functionally identical in servicing/diagnostics content — same CoreSense 3-wire/2-wire diagnostics, same troubleshooting flowcharts, same R-32 A2L PCB fault table.

### Copeland CoreSense™ Diagnostics — 3-Wire Module
Applies to: Amana ALXS/ALZS units; Daikin DC4SEA/DC5SEA/DH4SEA/DH5SEA. Self-contained module, no external sensors, works with any residential condensing unit with a Copeland Scroll compressor. LED indicator flashes alert codes.

Status LEDs: Solid Yellow "RUN" = module powered, operating normally. Solid Red "TRIP" = thermostat demand (Y) present but compressor not running (check: compressor protector open/high head pressure/low supply voltage; outdoor disconnect open; breaker/fuse open; broken wire/connector; high pressure switch open; contactor failed open).

"ALERT" Flash Codes (Yellow):
- Flash Code 1 — Long Run Time (low-side fault): low refrigerant charge; evaporator blower not running (relay/capacitor/motor/wiring/board/thermostat wiring); evaporator coil frozen (low suction pressure, low thermostat setting, airflow blockage, ductwork/filter blockage); faulty metering device (TXV bulb, stuck/defective TXV or fixed orifice); liquid line restriction (blocked filter drier); thermostat malfunctioning (sub-base short, installation).
- Flash Code 2 — Compressor (Pressure) Trip, discharge pressure out of limits or compressor overloaded: condenser fan not running (capacitor/wiring/motor); high head pressure (high pressure switch, overcharge, non-condensables); condenser coil poor air circulation (dirty/blocked/damaged).
- Flash Code 3 — Short Cycling: thermostat demand signal intermittent; time delay relay or control board defective; low or high pressure switch cycling.
- Flash Code 4 — Locked Rotor: run capacitor failed; low line voltage; excessive liquid refrigerant in compressor; compressor bearings seized (measure compressor oil level).
- Flash Code 5 — Compressor (Moderate Run) Trip: same causes as Flash Code 1 (evaporator blower, metering device, condenser coil circulation, low charge).

"LOCK" Flash Codes (Red, Yellow off) — compressor locked out after repeated trip events:
- Red Flash 2, Yellow Off — Compressor (Pressure) Trip lockout after 4 consecutive or 10 total pressure trips.
- Red Flash 3, Yellow Off — Short Cycling lockout after 10 consecutive short-cycling events.
- Red Flash 4, Yellow Off — Locked Rotor lockout after 10 consecutive locked rotor events.
- Red Flash 5, Yellow Off — Compressor (Moderate Run) Trip lockout after 4 consecutive or 10 total moderate run trips.

Flash code = number of LED flashes, pause, repeat. TRIP and ALERT LEDs flashing together = control circuit voltage too low for operation.

### CoreSense 2-Wire "Comfort Alert" Module (Diagnostics)
Applies to base-tier units without the 3-wire module. Same self-contained design, no external sensors. Green power LED = voltage present at power connection. Yellow alert LED flashes to indicate fault code. Red trip LED indicates if compressor is tripped or has no power. Wiring: Indoor unit C/Y terminals → CoreSense module C/Y → Contactor Coil, with HPCO (high pressure cutout) and LPCO (low pressure cutout) switches in the circuit.

### Table 1 — Quick Reference (Amana/Daikin DC/DH CoreSense Alert Codes)
| Alert Code | Alert Condition | Lock Level | Lock Indication |
|---|---|---|---|
| Normal Run (Solid Yellow) | Normal operation, no trip | N/A | N/A |
| Code1 (Yellow Flash 1) | Long run time — compressor running >18 hrs (disabled in Heat Pump mode) | N/A | N/A |
| Code2 (Yellow Flash 2) | Compressor (pressure) trip — runs 12sec-15min then trips >7min | 4x consecutive | Red: Flash 2, Yellow: Off |
| Code3 (Yellow Flash 3) | Pressure switch cycling — runs 12sec-15min then trips 35sec-7min | 4x consecutive or 10x total | Red: Flash 3, Yellow: Off |
| Code4 (Yellow Flash 4) | Locked rotor — trips within 12sec run, doesn't restart within 35sec | 10x consecutive | Red: Flash 4, Yellow: Off |
| Code5 (Yellow Flash 5) | Compressor (moderate run) trip — runs 15min-18hrs then trips >7min | 4x consecutive or 10x total | Red: Flash 5, Yellow: Off |
| Code9 (Red Flash 9) | Current to PROT terminal >2A for 40ms | Current > 2A for 40ms | Red: Flash 9, Yellow: Off |
| Trip (Solid Red) | Demand present, compressor not running | N/A | N/A |

### R-32 A2L PCB Fault Code (leak detection system, red LED on PCB seen through round glass view panel)
| Mode | LED Flashing Pattern | Recommended Action |
|---|---|---|
| Normal Operation | Slow (2 sec on / 2 sec off) | No action |
| R-32 Leak Alarm | Fast flashing | Controls/sensor working properly — identify leak source and address it. If observed, do NOT open the unit or turn it off. |
| Delay Mode | LED on continuously | After leak/alarm clears, unit stays in alarm mode 5 min before returning to normal. Check HVAC performance, re-check for leaks after any alarm. |
| System Verification Mode | Fast flashing (same as leak alarm) | Contractor-run test simulating R-32 leak (max 5 min) — press button 2x within 5 sec to enter; no action needed; auto-exits after 5 min or press button once to end early |
| Control Board Internal Fault | LED flashes 2x, off 5 sec, repeat | Unplug/replug R32 sensor, cycle power. If persists, replace control board. If then shows 3-flash pattern, replace sensor instead. |
| R-32 Sensor Communication Fault | LED flashes 3x, off 5 sec, repeat | Unplug/replug sensor, cycle power. If persists, replace both sensor and PCB (connector issue can't be isolated further in field). |
| R-32 Sensor Fault | LED flashes 4x, off 5 sec, repeat | Unplug/replug, cycle power. If persists, replace the sensor only (comms to sensor are fine, sensor itself reports internal fault). |

A2L PCB/sensor replacement: Take off blower access panel, disconnect PCB harness and R32 sensor wire, detach PCB from 4 plastic standoffs, install new PCB, reconnect harness/sensor wire per wiring instructions on unit, reassemble. For sensor replacement: also remove drain port gasket on drain pan, remove push pins, install new sensor+gaskets with "FRONT" label facing away from equipment on both sensor bracket and gaskets. R-32 sensor must only be replaced with manufacturer-specified sensors.

### EEM Blower Replacement (New AWST/AWSF R32 Air Handlers)
Disconnect power → remove front access panel → remove 2 screws each side holding lower control box, move aside → loosen/remove set screw on blower wheel hub, ensure wheel slides freely on motor shaft → protect coil with cardboard → remove 3 screws holding blower assembly, let rest on coil → slide blower assembly all the way left in cabinet → remove bolts holding motor bracket to blower, slide motor out of blower shell.

### High Efficiency Motor Check (3-phase brushless DC, single-phase AC input, one-piece encapsulated, ball bearing)
Terminal layout: C-L-G-N (high voltage, 3/16" spade) and 1-2-3-4-5 (low voltage, 1/4" spade, speed taps). 1) Check 230V across motor L and N — if present, proceed; if not, check line voltage circuit. 2) Check 24V from C to whichever tap (1-5) is in use — if present, motor has failed and needs replacement; if not, check 24V circuit to motor. Note when replacing: belly band must sit between the vents on the motor, and wiring needs proper drip loop to prevent condensate entry.

### High/Low Pressure Control Test Procedures
High pressure: Should open at 610 PSIG ±10, close at 420 PSIG ±25. Test in cooling: disconnect power, disconnect black wire from condenser fan motor (single stage) or unplug from board (2-stage), apply power, set thermostat to cool. Test in heating: disconnect black wire from evaporator fan motor instead, set thermostat to heat.
Low pressure: Should open at 21 PSIG, auto-reset (close) at ~50 PSIG. Same test structure.

### Capacitor testing
Run capacitor formula: Start Winding Amps × 2,652 ÷ capacitor voltage = microfarads (measure amp draw from Herm to start terminal, and voltage across HERM-C terminals). Digital multimeter capacitance mode: remove cap from circuit, select capacitance, connect leads, compare reading to printed value (actual may read less than printed — significantly lower or zero = replace). Analog meter: good = swings to zero then slowly returns to infinity; shorted = swings to zero and stays; open = no reading at all.
Hard start kits: Not required on Scroll compressor units (non-replaceable check valve in discharge line prevents high-side pressure buildup, needs only ~½ sec to equalize). If used in low-voltage/low-lock-rotor situations, only Amana-brand or Copeland-approved hard start kits are permitted — "Kick Start"/"Super Boost" kits are NOT approved.

### Checking Compressor / Resistance Test (from RSD6200301 servicing section)
Each compressor is equipped with an internal overload — a line break device that senses both motor amperage and winding temperature. High motor temp or amperage heats the disc, causing it to open and break the COMMON circuit within the compressor on single phase units. Heat generated inside the shell (from recycling, high amperage, or insufficient gas to cool the motor) is slow to dissipate — allow at least 3-4 hours for it to cool and reset before retesting.
Testing compressor windings: kill power, remove leads from compressor terminals, ohmmeter test continuity between S-R, C-R, and C-S (single phase units) or T1-T2, T2-T3 (3 phase). If either winding does not test continuous, replace the compressor. NOTE: if an open compressor is indicated, allow ample time for the internal overload to reset before replacing — an open-reading C-R/C-S with a good S-R reading can mean a tripped internal overload rather than a dead compressor.

## 2. ComfortNet DX7TC/DX16TC/DX18TC, DZ7TC/DZ16TC/DZ18TC (RSD6200007r24) — R-410A, 4-wire communicating
Uses CTK0* ComfortNet thermostats. Two-way digital comms between thermostat, indoor unit, and outdoor unit over 2 data wires (Data1/Data2) — up to 4 wires total between equipment and thermostat, 150 ft max recommended run, 18 AWG thermostat wire.

### CTK04 Standard Wiring (2-wire between indoor/outdoor)
Only data lines 1 and 2 required between indoor and outdoor units. A 40VA 208/230VAC-to-24VAC transformer (included with CTK0* kit) powers the outdoor unit's electronic control; outdoor "C" 24V common should be grounded to equipment (earth) ground.
### CTK04 Alternate Wiring (3-wire between indoor/outdoor)
Data lines 1 and 2 plus a common "C" wire connecting both units' commons for better communication reference — still 4 wires total to the thermostat.

### Nominal Airflow table (High/Low stage CFM, Cooling & Heating) by model
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

### Network Troubleshooting (Communications Troubleshooting Chart — Red/Green LED, air handler control board)
Red Communications LED: Off = normal. 1 Flash = communications failure (depress Learn button once quickly for power-up reset or hold 2 sec for out-of-box reset; verify bus BIAS/TERM dipswitches ON). 2 Flashes = out-of-box reset (control powered up with learn button held) — no action needed.
Green Receive LED: Off = no power/comms error (check fuses/breakers, replace blown fuse, check low-voltage shorts, reset network via learn button, check Data1/Data2 voltages — power OFF before repair). 1 Steady Flash = no network found (broken/disconnected data wire, or air handler installed as non-communicating/traditional — check wiring, verify install type). Rapid Flashing = normal network traffic, no action. On Solid = Data1/Data2 miswire (reversed wires, short between data wires, or short to R/C — check wiring/connections/voltages, power OFF before repair).

### PCBJA101/PCBJA102 Air Handler Diagnostic Codes (7-segment LED / ComfortNet thermostat message)
| 7-Seg | ComfortNet Msg | Fault | Cause | Fix |
|---|---|---|---|---|
| 1 Flash | HTR TOO LARGE (Ec) | Electric heat dipswitch set larger than for auxiliary heat expected on call for W1/Emergency heat | Heater kit selected via dipswitches too large for spec sheet | Verify electric heat dipswitch settings; verify installed heater valid for air handler model per Spec Sheet; verify shared data correct, repopulate w/ correct memory card if needed |
| 1 Flash | HTR TOO SMALL (Ec) | Electric heat dipswitch set smaller than expected | Same as above, too small | Same corrective actions |
| 1 Flash | NO HTR MATCH (Ec) | Electric heat dipswitch doesn't match heater kits in shared data | Same | Same corrective actions |
| 5 Flashes | INTERNAL FAULT (Not Displayed, EE) | No airflow on call; no air handler operation | Manual disconnect switch OFF or 24V wire improperly connected/disconnected; blown fuse or circuit breaker; integrated control module internal fault | Assure 208/230V and 24V power to air handler; check integrated control module fuse (3A), replace if necessary; check for possible shorts in 208/230V and 24V circuits, repair as necessary; replace bad integrated control module |
| 9 Flashes | NO NET DATA (d0) | Data not yet on network | Air handler does not contain any shared data | Populate shared data set using memory card |
| 11 Flashes | INVALID MC DATA (d4) | Invalid memory card data | Shared data on memory card rejected by integrated control module | Verify shared data correct for specific model, repopulate using correct memory card |
| 6 Flashes | MOTOR NOT RUN (b0) | Circulator blower motor not running when it should be | Loose wiring at motor power leads/disconnected; failed circulator blower motor | Tighten/correct wiring; check circulator blower motor, replace if necessary |
| 6 Flashes | MOTOR COMM (b1) | Integrated control module lost comms with circulator blower motor | Loose wiring at motor control leads; failed motor; failed integrated control module | Tighten/correct wiring; check/replace motor; check/replace integrated control module |
| 6 Flashes | MOTOR MISMATCH (b2) | Circulator blower motor horsepower in shared data doesn't match actual motor | Incorrect motor in air handler, or incorrect shared data set | Verify motor is specified type, replace if necessary; verify/repopulate shared data for specific model |
| 6 Flashes | MOTOR LIMITS (b3) | Motor operating in power/temp/speed limiting condition | Blocked filters, restrictive/undersized ductwork, high ambient temps | Check filters/clean, check/remove ductwork obstruction, verify registers open, verify ductwork sized appropriately, resize/replace if necessary |
| 6 Flashes | MOTOR TRIPS (b4) | Motor senses loss of rotor control or high current | Abnormal motor loading, sudden speed/torque change, sudden blockage of air handler/coil inlet or outlet, high loading, blocked filters, very restrictive ductwork | Check filters/registers/ductwork/inlet/outlet for blockages; see installation instructions for requirements |
| 6 Flashes | MTR LCKD ROTOR (b5) | Motor fails to start 10 consecutive times | Obstruction in blower housing, seized bearings, failed motor | Check for obstruction, repair/replace wheel and/or motor if necessary |
| 6 Flashes | MOTOR VOLTS (b6) | Motor shuts down for over/under voltage or over-temp | High or low AC line voltage to air handler blower, high ambient temps | Check power to air handler blower, verify line voltage within range on rating plate |
| 6 Flashes | MOTOR PARAMS (b7) | Motor doesn't have enough info to operate, or fails to start 40 consecutive times | Error with integrated control module; motor has locked rotor condition | Check integrated control module has correct shared data; check for locked rotor condition |
| 6 Flashes | LOW ID AIRFLOW (b9) | Airflow lower than demanded | Blocked filters, restrictive/undersized ductwork | Check/clean filters, check ductwork blockage/registers/sizing |

### PCBJA104 Air Handler Diagnostic Codes (7-segment LED, legacy & ComfortNet)
Same fault architecture as PCBJA101/102 (EC/HTR TOO LARGE-SMALL-NO MATCH, No Display=INTERNAL FAULT/EE, d0=NO NET DATA, d1=INVALID DATA, d4=INVALID MC DATA, b0-b9 motor codes identical to above) plus:
- EF / Aux Alarm Fault — Aux switch open. Cause: high water level in evaporation coil. Fix: check overflow pan and service.
Notes/cautions: turn power OFF before repair; use memory card specific to the model; insert memory card BEFORE turning power ON; memory card may be removed after data is loaded; error code clears once data is loaded.
