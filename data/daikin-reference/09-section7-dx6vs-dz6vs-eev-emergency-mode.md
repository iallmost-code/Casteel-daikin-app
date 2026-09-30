# SECTION 7 — MANUAL EXTRACTION: DX6VS/DZ6VS INVERTER OUTDOOR UNIT, EEV INDOOR CODES, EMERGENCY MODE

# PART 4 — DX6VS/DZ6VS Inverter EEV Outdoor Unit Full Fault Code Table, EEV Indoor Codes, Emergency Mode DIP Switches
Source manual: SiUS612209EA / SiUS612209EB — Daikin DX6VS/DZ6VS inverter outdoor units, DV**FEC/DFVE** EEV air handlers, CAPE(A)*/CHPE* EEV cased coils, R-410A (2022/2023 — EB is a later revision of the same manual as EA, content identical for all sections reviewed). This manual mainly covers the outdoor unit and EEV air handler/cased coil — for gas furnace or modular blower info, refer to that unit's own service manual.

### Testing Capacitor DC Voltage (safety procedure before servicing control board)
Shut down power, leave control box for 10 min. Touch Earth ground terminal to discharge body static (protects control board). Measure residual voltage at specified C+/C- test points using a VOM (DC voltage range) — must confirm 50V or less before touching charged area. Immediately after measuring, disconnect the outdoor fan motor's connectors (if fan blade rotates from wind, the capacitor WILL recharge — shock hazard). Separate diagrams exist for 1.5-3.0 ton boards (C+ at C7/C8 area, near L804) and 3.5-5.0 ton boards (C+ near C701/C+ pin, larger board layout).
Notice: Inverter control board has small current flowing even when powered off/not running, to keep components cooled — outdoor fan may run at any time including winter months. Avoid obstructing the fan whenever the unit is powered.

### Outdoor Unit Error Codes (Thermostat display / Control board LED display) — full table
| T-stat # | LED | Description | Probable Causes (key) | Corrective Actions (key) |
|---|---|---|---|---|
| 12 | E12 | General memory error | High electrical noise; faulty control board | Replace control board if necessary |
| 13 | E13 | Frequent high pressure faults (CRITICAL) | Blocked/restricted OD coil or lines; stop valve not fully open; overcharge; OD fan not running; HPS inoperable; faulty indoor/outdoor EEV or EEV coil; faulty control board | Clean coil/lines; open stop valve; adjust charge; check OD fan motor/wiring; replace EEV/coil; replace control board if necessary |
| 14 | (none) | Same as E13 but MINOR — continued operation acceptable | Same as E13 | Same as E13 |
| 15 | E15 | Frequent low pressure faults (CRITICAL) | Stop valve not fully open; restriction in refrigerant lines; low charge; refrigerant leak; pressure sensor issue; indoor fan not functioning; faulty EEV/coil; faulty control board | Open stop valve; check for restrictions; check refrigerant charge; leak test; check pressure sensor connection; check indoor blower; replace EEV/coil/board as needed |
| 16 | (none) | Same as E15 but MINOR | Same as E15 | Same as E15 |
| 17 | E17 | Frequent compressor faults | Stop valve not fully open; faulty solenoid valve coil/valve; compressor wire lost phase; compressor motor failure | Open stop valve; check/replace solenoid valve; check wire between board and compressor; inspect compressor motor, replace if necessary |
| 18 | E18 | Control board may need replacement | Outdoor fan motor not connected properly; faulty control board; electrical noise | Check wiring from OD fan motor to board; replace board if necessary |
| 19 | E19 | Frequent OD unit control board/motor faults | Obstruction in fan rotation; fan motor not connected properly; OD fan not running; faulty control board; electrical noise | Check/clean grille of debris; check wiring from OD fan motor to board; replace fan motor & wiring or board if necessary |
| 20 | E20 | Outdoor EEV fault | Outdoor EEV coil not connected; faulty outdoor EEV coil; faulty control board | Check outdoor EEV coil connection, repair/replace as needed; replace board if necessary |
| 21 | E21 | Frequent low discharge superheat faults | Thermistors inoperable/improperly connected; faulty indoor/outdoor EEV or coil; over charge; faulty pressure sensor; faulty control board | Check thermistor connections; replace EEV/coil; check refrigerant charge; check pressure sensor; replace board if necessary |
| 22 | E22 | Frequent high discharge temp faults; discharge thermistor not in correct position | Faulty solenoid valve coil/valve; discharge thermistor inoperable/improperly connected or wrong position; compressor enclosure too high temp; low charge; overcharge; faulty compressor | Check/replace solenoid valve; check discharge thermistor resistance/connections/position; check refrigerant charge; check compressor, replace if necessary |
| 23 | E23 | Discharge thermistor out of range | Discharge thermistor inoperable/improperly connected | Check thermistor resistance & connections; repair/replace as needed |
| 24 | E24 | High pressure switch is open | HPS inoperable | Check resistance on HPS to verify operation; replace if needed |
| 25 | E25 | Outdoor air thermistor open or shorted | Faulty thermistor or connection | Check connection, repair/replace if needed |
| 26 | E26 | Pressure sensor not reacting properly | Pressure sensor inoperable/improperly connected | Check connection, repair/replace if needed |
| 27 | E27 | Outdoor Coil Defrost thermistor out of range | Coil defrost thermistor inoperable/improperly connected | Check connection, repair/replace if needed |
| 28 | E28 | Outdoor Coil thermistor out of range | Coil thermistor inoperable/improperly connected | Check connection, repair/replace if needed |
| 29 | E29 | Liquid thermistor out of range | Liquid thermistor inoperable/improperly connected | Check connection, repair/replace if needed |
| 30 | E30 | Control board may need replacement | Wiring to control board disconnected; faulty control board; electrical noise | Check wiring, repair as needed; replace board if necessary |
| 32 | E32 | High temp faults on OD control board (1.5-3.0 ton) | Ambient too high; stop valve not fully open; cooling bracket screws missing/not properly fastened (3.5-5.0 ton only); poor grease coating between cooling plumbing and bracket (3.5-5.0 ton only); restriction in line; limited refrigerant flow through cooling circuit | Cycle power, re-try in usable ambient range; check grease condition (3.5-5.0 ton); check screw tightening (3.5-5.0 ton); check for restriction; adjust refrigerant charge; open stop valve if needed |
| 33 | (none) | Same as E32 but MINOR | Same as E32 | Same as E32 |
| 34 | E34 | High current condition — potential short circuit | Current spike in supply; stop valve not fully open; compressor wire lost phase; faulty control board; faulty compressor | Check power supply for in-rush current; open stop valve if needed; check refrigerant charge; check wire between board and compressor; check compressor, replace if necessary |
| 35 | E35 | High current condition detected | Short circuit condition; stop valve not fully open; overcharge; faulty control board; faulty compressor | Check installation clearances; open stop valve if needed; adjust refrigerant charge; check/replace board or compressor |
| 36 | E36 | Abnormal condition during startup procedure | Faulty solenoid valve coil/valve; blocked/restricted OD unit coil/lines; compressor wire lost phase; inconsistent compressor load; faulty control board | Check/replace solenoid valve; clean OD coil/lines; check wire between board and compressor; replace board if necessary |
| 37 | E37 | Control board may need replacement | Outdoor fan motor not connected properly; faulty control board | Check wiring from OD fan motor to board; replace board if necessary |
| 38 | E38 | Voltage related issue with compressor | High or low line voltage; compressor wire lost phase; faulty control board | Correct low/high line voltage condition, contact utility if needed; check wire between board and compressor; replace board if necessary |
| 39 | E39 | Control board may need replacement | Thermistors inoperable/improperly connected; faulty control board | Check thermistor connections, repair/replace if needed; replace board if necessary |
| 40 | E40 | Compressor requirement differs from compressor capability | Memory card not correct; control board mismatch | Check memory card data vs. outdoor unit model; verify control board size vs. outdoor unit model; replace board if necessary |
| 41 | E41 | Low refrigerant condition | Refrigerant leak; low charge; thermistors inoperable/improperly connected; faulty outdoor solenoid valve coil/valve | Leak test using leak test procedure; check refrigerant charge; check thermistor connection; check/replace outdoor solenoid valve |
| 42 | E42 | Low power supply voltage condition | Low line voltage supply | Check circuit breakers/fuses; verify unit connected to power per rating plate; correct low line voltage, contact utility if needed |
| 43 | E43 | High power supply voltage condition | High line voltage supply | Verify unit connected per rating plate; correct high line voltage, contact utility if needed |
| 44 | E44 | Outdoor temperature outside recommended operational range | Ambient air conditions too high or low | Cycle power, re-try during usable ambient temp range |
| 47 | E47 | Unable to start System Verification test — indoor heat turned on by secondary heating source | Heat provided by secondary heating source | Turn off Furnace or heater using thermostat before operation |
| 49 | E49 | Unable to enter Charging Mode — indoor heat turned on by secondary source | Heat provided by secondary heating source | Turn off heater using thermostat before operation |
| 50 | E50 | Voltage issue on control board | High/low voltage from supply, or frequency issue; faulty control board | Correct low/high line voltage/frequency issue, contact utility if needed; replace board if necessary |
| 51 | E51 | Communication issues detected by outdoor control board (Network communication error) | Communication wiring disconnected | Check communication wiring, repair as needed |
| 52 | (none) | Frequent compressor faults (MINOR, continued operation acceptable) | Stop valve not fully open; compressor wire lost phase; compressor motor failure | Open stop valve if needed; check wire; inspect compressor motor, replace if necessary |
| 53 | (none) | Frequent OD unit control board/motor faults (MINOR) | Obstruction in fan rotation; fan motor not connected properly; OD fan not running; faulty board; electrical noise | Check/clean grille; check wiring/fan motor; replace board if necessary |
| 54 | (none) | Frequent low discharge superheat faults (MINOR) | Thermistors inoperable/improperly connected; faulty indoor/outdoor EEV or coil; faulty control board | Check thermistor connection; replace EEV/coil; replace board if necessary |
| 55 | (none) | Frequent high discharge temp faults (MINOR) | Discharge thermistor inoperable/wrong position; low charge; overcharge; faulty compressor | Check thermistor resistance/connections/position; check refrigerant charge; check compressor |
| 56 | E56 | Outdoor Suction thermistor out of range | Suction thermistor inoperable/improperly connected; faulty reversing valve | Check connection, repair/replace if needed; check reversing valve, replace if needed |
| -- | E57 | Refrigerant cooling sweat error (3.5-5.0 ton only) — sensing sweat on cooling loop | Refrigerant leak; low charge; faulty indoor EEV/coil; thermistors inoperable/improperly connected | Leak test; check refrigerant charge; check indoor EEV; check indoor EEV coil; check thermistor connections |
| 58 | E58 | Overload Protection sensor for compressor opened | OL sensor (X33A) inoperable or in incorrect position | Check resistance on OL sensor, replace if needed; check OL sensor position/connection |
| B0 | Eb0 | Estimated airflow from indoor subsystem near 0 CFM | Failed indoor blower motor; indoor fan motor not properly connected; too much static pressure | Check ID fan motor wiring/connectors; check ID fan motor, replace if needed; check for ductwork obstruction |
| B9 | Eb9 | Estimated airflow from motor lower than requirement | Same as B0 | Same as B0 |
| D0 | Ed0 | Control board doesn't have necessary shared data | Outdoor unit wired as part of communicating system, integrated control module doesn't contain shared data | Replace control board if necessary |
| D1 | Ed1 | Control board doesn't have appropriate data needed | Outdoor unit wired as part of communicating system, invalid shared/network data | Replace control board if necessary |
| D2 | Ed2 | Airflow requirement greater than indoor subsystem capability (SYSTEM MISMATCH) | Communicating system requires airflow greater than indoor unit's airflow capability, or type of indoor unit without EEV connected; shared data incompatible/missing; comm wiring loose; airflow trim setting out of range | Check combination matched with rating list; verify shared data correct, repopulate; check comm wiring/power supply wiring; verify airflow trim setting, adjust if needed |
| D3 | Ed3 | Mismatch between shared data and control physical hardware | Shared data sent doesn't match hardware config | Verify shared data correct for specific model, repopulate if required |
| D4 | Ed4 | Memory card data has been rejected | Shared data on memory card rejected | Verify shared data correct for specific model, repopulate if required |
| 11 (thermostat-only) | E11 | SYSTEM START-UP TEST incomplete/running | Incomplete or in-progress test | Run the SYSTEM START-UP TEST per outdoor unit installation manual "STEP3. SYSTEM START-UP TEST" |

Ed2 (System Mismatch) — airflow trim limits table (critical for AHRI-legal combos):
- DX6VS*361*A*/DZ6VS*361*A* outdoor with D*96VC0403B*/D*96VC0603B*/D*80VC0603B*/D*80VC0803B*/D*97MC0603B*/D*96SC0603BU*/MBVC1200* indoor: trim settings more than 10% invalid — trimmed-up CFM causes mismatch error.
- DX6VS*601*A*/DZ6VS*601*A* outdoor with D*96VC0804C*/D*97MC0804C*/D*80VC0804C* indoor: trim settings more than 5% invalid — trimmed-up CFM causes mismatch error.
- Always verify the outdoor+indoor combination is a certified match on the AHRI website before troubleshooting further; replace with certified combination if not matched.

### Outdoor Unit Diagnostic Flowchart Detail (selected key codes)
E13 High Pressure Error — trips above 4.2 MPa (605 PSIG). Diagnosis path: compare manifold gauge to D-checker reading → check overcharge/subcooling → check OD hex mid thermistor (cooling)/ID pressure sensor (heating) → check stop valve for clog → check OD coil dirty (cooling) → check OD fan failure (cooling) → check static pressure high (heating) → check ID blower failure (heating) → check HPS wiring to PCB → check HPS failure → check E24 code → replace OD PCB if nothing else resolves.
E15 Low Pressure Error — trips below 0.12 MPa (17 PSIG) sustained 5 min. Diagnosis: compare manifold gauge to D-checker → check OD pressure sensor failure → check stop valve clog → check undercharge/leak → check thermistor failure (ID gas temp cooling / suction temp heating) → check EEV coil temp differential before/after (both OD and ID) → check refrigerant filter/dryer clogging → check fan failure (ID cooling / OD heating, static pressure) → replace OD PCB if nothing resolves.
E21 EEV Control Error — detected by discharge pipe superheat + EEV pulse; triggers when discharge superheat becomes excessively low and EEV pulse is at minimum. Diagnosis: check refrigerant charge correct → check indoor/outdoor EEV coils connected to PCB properly → check EEV coils attached to EEV body properly (protrusion on coil must click into dimple on EEV body) → check EEV coil resistance normal → check thermistors connected/normal → check pressure sensor normal → replace PCB if nothing resolves.
E22 High Discharge Temp Error — trips above 120°C (248°F) discharge temp. Similar diagnosis chain: check discharge thermistor connection/position/resistance → check EEV coils/resistance → replace PCB.
E32 Outdoor PCB High Temp Error — 1.5-3.0 ton: trips at 95°C (203°F) inverter cooling fin temp (check fin dirty, obstruction around coil/grille, short circuit, suction air temp >46°C/115°F, cycle power, replace PCB). 3.5-5.0 ton: trips at 110°C (230°F) cooling plate temp (check liquid tubing contact to cooling plate, cooling plate cover nails/screw torque 1.59±0.20 N·m / 1.17±0.15 lb·ft, grease replacement, R7T thermistor connection, refrigerant circuit clogging, charge/superheat, short circuit, replace PCB).
E41 Refrigerant Shortage — cooling: checks charge/SH, clogging. Heating: checks compressor wiring phase/terminal, charge/SH, clogging, D-checker data (disch temp − cond temp > 65°C/117°F triggers sensor check), OD air temp sensor check, liquid tubing temp sensor check (3.5-5.0 ton: OD air temp − 2°C/4°F > liquid pipe temp), or install thermal insulation on exposed outdoor liquid tubing if nothing else found.
E44 Outdoor Temp Outside Range — Cooling: OD temp > 55°C(131°F) or < -21°C(-6°F). Heating: OD temp > 27°C(81°F) or < -32°C(-26°F). System cannot run in that condition by design; verify actual temp against D-checker, check for false readings (short circuit of discharge air, thermistor touching coil or exposed to sunlight), replace thermistor or OD PCB if needed.
E57 Refrigerant Cooling Sweat Error (3.5-5.0 ton HP only) — detected by outdoor liquid thermistor temp becoming excessively low during heating operation. Same EEV/thermistor diagnosis chain as E21/E22.
E58 Overload Protection Sensor Open — detected by no continuity in OL switch at start of compressor operation. Check OL connected to PCB properly → check OL switch opened → replace PCB or OL switch.
Ed2 System Mismatch — check combination certified on AHRI website; check airflow trim setting not set to prohibited value (see trim limits table above).

### Indoor Unit Error Codes (EEV Cased Coil, EEV Air Handler — DV**FEC/DFVE**, CAPE(A)*/CHPE*)
Control board 2-digit 7-segment display shows State (2 sec) → blank (0.5 sec) → Error code if present → Airflow (estimated CFM, e.g. "A" then upper 2 digits then lower 2 digits, e.g. 1240 CFM shows A...12...40). EEV cased coil does NOT display airflow (coil has no blower).

State codes (normal operation): On=Standby/Normal Mode; FC=Cooling Mode*; FH=Heat Pump Heating Mode*; _F=Fan Only*; H1=Electric Heat Low*; H2=Electric Heat High*; dF=Defrost Mode*; Hu=Humidifier Running with No Heating*; EE=Emergency Mode. (*EEV cased coil does not indicate these state codes, only error codes.)

Full Error Code Table:
| Code | Description | Possible Causes (key) | Corrective Actions (key) |
|---|---|---|---|
| EE | No 24V power to control board; blown fuse/breaker; internal control board fault | Manual disconnect switch OFF; 24V no power to control board; blown F2U fuse or circuit breaker; control board internal fault | Assure 208/230V and 24V power; check fuse F2U on control board; check for possible shorts; replace control board |
| Eb | Selecting "no heater kit" and receiving electric heat demand | No heater kit selected | Select the valid heater kit on thermostat |
| Ed | Heater kit dip switches not set properly | Invalid heater kit selected | Set correct dip switches |
| E5 | Fuse open | Fuse (F1U) is blown | Replace fuse |
| EF | Auxiliary switch open | High water level in evaporation coil drain pan; connected alarm device activated; auxiliary alarm terminals (TB4, TB5) open | Check water level in drain pan; check alarm device |
| d0 | Data not on network | No shared data on the network | Populate shared data set using memory card |
| d1 | Invalid data on network | Wrong shared data on network | Populate shared data set using memory card |
| d4 | Invalid memory card data | Wrong memory card data | Replace memory card |
| b0 | Blower motor not running | Fan/motor obstruction; power interruption (low voltage); high loading conditions; blocked filters; blockage in ductwork | Check for obstruction; verify input voltage; check filters/grilles/ductwork; check obstruction on fan/motor/ductwork; replace motor |
| b1 | Blower motor communication error | High/low AC line voltage; incorrect wiring; locked motor rotor | Verify line voltage; check locked rotor condition; check control board or motor |
| b2 | Blower motor HP mismatch | Wrong/no shared data; locked motor rotor | Check control board or motor |
| b3 | Blower motor operating in power/temp/speed limit | Blocked filters, restrictive/undersized ductwork, high ambient temp | Check filters/ductwork, resize/replace if needed |
| b4 | Blower motor current trip or lost rotor | Fan/motor obstruction, abnormal loading, high loading, blocked filters, restrictive ductwork | Check for obstruction, verify voltage, check filters/ductwork, resize if needed, replace motor |
| b6 | Over/under voltage trip or over temp trip | High AC line voltage to ID blower; low AC line voltage; high ambient temp | Verify line voltage, check ID blower motor condition |
| b7 | Incomplete parameter sent to motor | Wrong/no shared data; locked motor rotor | Check control board or motor |
| b9 | Low indoor airflow (electric heat mode) | Fan/motor obstruction or blocked filters; power interruption; blockage in airflow/ductwork undersized | Check for obstruction, verify voltage, check filters/duct system, resize/replace if needed |
| 70 | EEV disconnection detected | Indoor EEV coil not connected | Check indoor EEV coil connection (control board and junction connector) |
| 73 | Liquid side thermistor abnormality | Open/short circuit of liquid thermistor (X5A); reading incorrect or out of range | Check thermistor connection; check resistance value; replace thermistor; replace control board |
| 74 | Gas side thermistor abnormality | Open/short circuit of gas thermistor (X5A); reading incorrect or out of range | Check thermistor connection; check resistance value; replace thermistor; replace control board |
| 75 | Pressure sensor abnormality | Open/short circuit of pressure sensor (X15A); reading incorrect or out of range | Check pressure sensor connection; check resistance; replace pressure sensor; replace control board |
| 76 | Indoor unit - outdoor unit, gas furnace or modular blower communication error (during operation) | Fan/motor obstruction (low voltage); power interruption; high loading; blocked filters; blockage in ductwork/airflow | Check for obstruction on fan/motor; verify input voltage; check filters/ductwork; check obstruction |
| 77 | Indoor unit - thermostat communication error (during startup & operation) | Open/short circuit on network; incorrect wiring between indoor unit and thermostat/thermostat failure; power interruption (low voltage) | Check open/short circuit; check indoor unit and thermostat wiring; check power supply; press "LEARN" button >5 sec to re-establish network |
| 78 | Indoor unit - outdoor unit, gas furnace or modular blower communication error (during startup) | Open communication circuit; no power supply to OD unit/gas furnace/modular blower | Check for indoor unit and other unit wiring; check power supply to OD unit/gas furnace/modular blower |
| 9b | Low indoor airflow (without electric heat mode) | Fan/motor obstruction or blocked filters; restrictive/undersized ductwork; wrong outdoor/indoor combination; ID motor failure | Check ductwork/filter blockage; resize/replace ductwork; check for combination match; replace ID motor if necessary |

### Fault Recall (EEV Indoor Units) — reviewing last 6 faults on control board
Press FAULT RECALL button 2-5 seconds → display shows solid "--" → release → shows most recent fault. Subsequent presses recall previous faults (up to 6 stored). Consecutively repeated faults displayed max 3 times. If left untouched >3 min, control returns to Standby. To clear error code history: press and hold FAULT RECALL until display blinks "--" (longer hold than the 2-5 sec recall press), release, display shows "88" and clears the faults. If held >15 sec, control goes back to Standby without clearing.

### Mode Display Navigation (2-digit display backup tool, hold-time state machine)
From "No Display" (Screen Zero): hold Fault Recall >2 sec → Solid Display. Release between 2-5 sec → enters error code list (First Error Code → press Fault Recall for next → Second Error Code → ... → Last Error Code → flashing display 0.5s on/0.25s off, idle 3 min then returns to No Display). Hold >5 sec from Solid Display → No Display (2nd level). Release between 5-10 sec → back to No Display (Screen Zero). Hold >10 sec → Flashing Display (0.2s on/0.2s off). Release between 10-15 sec → Solid "88" for 3 sec then ERASES ALL diagnostic codes. Release after 15 sec → back to Screen Zero, nothing erased.

### Emergency Mode Setup (EEV Cased Coil, EEV Air Handler, Gas Furnace/Modular Blower combos)
Used when communication between equipment is broken or a thermostat has failed and can't be immediately fixed. Does NOT control to a specific room temperature setpoint — only a temporary solution based on building load at time of activation. In emergency mode, the 7-segment display on the EEV indoor unit control board shows "EE"; status is not shown on the thermostat or outdoor unit 7-segment display.

When to consider emergency mode: outdoor unit showing E51 (comm error), Ed2 (indoor too small/can't communicate with outdoor), or EEV indoor unit showing E76 (no OD/indoor comms), E77 (no thermostat comms), or E78 (no OD/indoor comms during startup) — acceptable to use emergency mode if equipment can't be immediately fixed. Cycling power may temporarily clear error codes without fixing the underlying problem.

1. Heating Emergency Mode setup (EEV Cased Coil):
1) Remove thermostat communication wirings (1, 2, R, C) from ALL connected equipment (cased coil, gas furnace/modular blower, outdoor unit, thermostat) at their communication terminals (inside each unit's control board).
2) Reconnect the Gas Furnace or Modular Blower's communication terminal short-circuited with a jumper wire (so it alone operates in Heating Emergency Mode without the thermostat) — refer to that unit's own service manual for wiring points.
3) Set the EEV cased coil to Heating Emergency Mode: dip switches S-21 OFF and S-22 ON on switch bank DS-6 on the EEV cased coil control board.
4) Operation starts automatically when equipment is powered — no need to set emergency mode on the outdoor unit itself.
Note: during Heating Emergency Mode, the outdoor unit must stop operation. Once comms are restored, settings must be returned to default and all thermostat communication wiring reconnected.

For EEV Air Handler (electric heat strips, not gas): Runs electric heat strips independently of thermostat, in High Heat Level or Low Heat Level. Set via Switch Bank DS-6 dipswitches S-21/S-22 (default OFF/OFF = normal; S-21 OFF + S-22 ON = Low Heat Level; S-21 ON + S-22 ON = High Heat Level). Indoor fan and electric heater cycle on set intervals by level:
| Heat Level | Heating On | Heating Off |
|---|---|---|
| High Heat Level | 8 min | 8 min |
| Low Heat Level | 7 min | 15 min |
(2-stage heat kits energize in stage 2 during this mode.) Emergency airflow: set DIP switches S-9 through S-12 on Switch Bank DS-3 to match the correct heater kit size (see DS-3 table below). Also set switch bank DS-4 dipswitches S-13/S-14 for desired emergency fan speed (25/50/75/100%).
Note: an "Ed" error on startup in emergency mode means DIP switches don't match the Electric Heating Airflow Table — configuring correctly clears the error.

2. Cooling Emergency Mode setup: used when indoor/outdoor communication is not functioning. Outdoor and indoor units run independently.
Compressor speed auto-adjusts by outdoor ambient temp: below 70°F = 50% speed; above 95°F = 100% speed; between 70-95°F, linear ramp. Indoor unit provides constant airflow as selected even if compressor stops; EEV continues operating for superheat control, compressor cycles at intervals.
For EEV Cased Coil: 1) Remove thermostat comm wirings from all equipment. 2) Reconnect Gas Furnace/Modular Blower comm terminal short-circuited (same as heating). 3) Set cased coil to Cooling Emergency Mode: DIP S-21 ON, S-22 OFF on DS-6. 4) Select cooling level at outdoor unit: Low/Medium/High via switch bank DS-2 (S-1/S-2). 5) Operation starts on power-up.
Note: reconnect emergency cooling wirings to gas furnace/modular blower BEFORE setting outdoor DS-2 dip switches — otherwise compressor may be damaged.
For EEV Air Handler: two steps — 1) select airflow on indoor unit via DS-4 (S-13/S-14) at 25/50/75/100%, AND set DS-6 S-21 ON / S-22 OFF to enable emergency indoor fan. 2) Select cooling level at outdoor unit via DS-2 (S-1/S-2): Low/Medium/High.

Outdoor unit Switch Bank DS-2 (Cooling Emergency Mode level selection, S-1/S-2): Normal=OFF/OFF*. Cooling Emergency Low=ON/OFF. Cooling Emergency Medium=OFF/ON. Cooling Emergency High=ON/ON.

Switch Bank DS-3 — EEV Air Handler Control Board Heater Kit Selection (S-9 through S-12), by nominal capacity:
| Selection | 24 | 35,36 | 42 | 47,48 | 59,60 | S-9 | S-10 | S-11 | S-12 |
|---|---|---|---|---|---|---|---|---|---|
| No Heater | - | - | - | - | - | OFF* | OFF* | OFF* | OFF* |
| First | 3 | 3/5 | 3/5 | 3/5 | 3/5 | ON | ON | ON | ON |
| Second | 5 | 6 | 6 | 6 | 6 | ON | ON | ON | OFF |
| Third | 6 | 8 | 8 | 8 | 8 | ON | ON | OFF | ON |
| Fourth | 8 | 10 | 10 | 10 | 10 | ON | ON | OFF | OFF |
| Fifth | 10 | 15 | 15 | 15 | 15 | ON | OFF | ON | ON |
| Sixth | -- | 19 | 19 | 20 | 20 | ON | OFF | ON | OFF |
| Seventh | -- | -- | -- | -- | 25 | ON | OFF | OFF | ON |
(* = default factory setting)

Switch Bank DS-4 — EEV Air Handler Fan Only Speed (S-13/S-14): 25%=OFF/OFF. 50%=ON*/OFF*(default). 75%=OFF/ON. 100%=ON/ON.

Switch Bank DS-6 — EEV Air Handler AND Cased Coil Emergency Mode (S-21/S-22): Normal=OFF*/OFF*. Cooling Emergency=ON/OFF. Heating Emergency High=OFF/ON. Heating Emergency Low=ON/ON (*EEV Cased Coil does not have a Low Heat Level function — cased coil has no electric heat strips).

Full DIP Switch Default Factory Settings table (all switch banks, all functions): Indoor unit DS-1 (switches 1-4) = No Use, all OFF. DS-2 (5-8) = No Use, all OFF. DS-3 (9-12) = Heater Kit Selection (Emergency Mode, EEV Air Handler only), all OFF default. DS-4 (13-14) = Emergency Fan Mode (EEV Air Handler only) — 13=ON default, 14=OFF default; (15-16) = EEV Enable (15=ON default), No Use (16). DS-5 (17-20) = Emergency EEV Opening (17=ON, 18=OFF), EEV Emergency Mode (19=OFF), No Use (20) — all must stay at factory setting, prohibited to change with EEV-equipped indoor unit. DS-6 (21-24) = Emergency Mode (21-22, both OFF default), No Use (23-24). Outdoor unit DS-1 (1-2) = Termination Resistor, both ON. DS-2 (1-2) = Cooling Emergency Mode, both OFF default.
