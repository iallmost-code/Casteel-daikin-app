## FAULT CODES

### General / unitary systems
These are Daikin's self-diagnosis codes for ductless (mini-split), SkyAir and VRV equipment, from Daikin's own code list (SM-TS3) and the One+ Phase Two error code list. Daikin's ducted equipment (Fit, EEV air handlers and coils, communicating furnaces) uses the ClimateTalk codes in the groups below instead. A few codes mean something different on VRV (for example H3, L3, E2, E6, J7, J9, UH), so check the unit's own service manual when it matters.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| A0 | External protection device activated | External protection device wired to the indoor unit T1-T2 terminals has activated; improper field setting; defective indoor PCB. | Check the external device wired to T1-T2 and what tripped it, then field settings, then the indoor PCB. |
| A1 | Indoor unit PCB malfunction | Defective indoor PCB; external noise; wrong models connected together; low supply voltage; disconnected connector. | Check model match, supply voltage and connectors; replace the indoor PCB if it repeats. |
| A3 | Drain level control abnormality (float switch) | Clogged drain or upward drain slope; defective drain pump; defective float switch or short-circuit connector. | Clear the drain and check its slope, test the drain pump and float switch. |
| A5 | Freeze-up protection (cooling) / high pressure control (heating) — indoor | Short-circuited air; clogged air filter; dirty indoor coil; defective indoor coil thermistor or PCB. | Clean the filter and coil, check for short-circuited air, check the coil thermistor. |
| A6 | Indoor fan motor fault | Blocked blower wheel, locked rotor, or failed fan motor. | Clear any obstruction, spin the wheel by hand, then ohm/replace the motor if seized. |
| A7 | Swing flap motor error | Jammed louver or faulty swing flap motor. | Clear the louver path and linkage; replace the motor if it still won't home. |
| A9 | Indoor EEV drive malfunction | Expansion valve coil or driver PCB defect. | Check EEV coil resistance and its connector; replace the valve or board as needed. |
| C4 | Indoor heat exchanger LIQUID-pipe thermistor fault | Loose or broken thermistor wires; defective thermistor; defective indoor PCB. (C5 is the gas pipe.) | Check the connection and resistance against the chart; replace the thermistor or PCB. |
| C9 | Suction/intake air thermistor fault | Failed sensor or bad connector. | Verify resistance vs. chart, reseat the connector, replace if faulty. |
| E1 | Outdoor unit PCB malfunction | Defective outdoor PCB; bad indoor/outdoor relay-wire connection; noise, a momentary voltage drop or power loss. | Cycle power to the outdoor unit; replace the outdoor PCB if the error doesn't clear. |
| E3 | High-pressure switch tripped | Dirty condenser coil, blocked airflow, overcharge, or a closed service valve. | Clean the coil, confirm the outdoor fan runs, verify charge, confirm valves are open. |
| E4 | Low-pressure switch tripped | Refrigerant shortage/leak, restricted metering device, or closed valve. | Leak-check, verify charge by weight/subcool, confirm valves are open and the drier isn't plugged. |
| E5 | Inverter compressor lock / overload (OL) | Compressor lock; high differential pressure; UVW wiring error; defective inverter PCB; stop valve closed; charge problem. | Open the stop valves, check charge and the 4-way valve, check UVW wiring, check the inverter PCB/power transistor, megohm the compressor. (Inverter compressor — no start cap or contactor.) |
| E6 | Compressor overcurrent / lock (VRV: compressor damage alarm) | Defective compressor; compressor harness disconnected; defective control or inverter PCB; stop valve not opened. | Open the stop valves, check the compressor harness and pressure sensors, check the PCB/inverter PCB, then the compressor. |
| E7 | Outdoor fan motor malfunction | Obstruction, failed motor, or fan driver PCB fault. | Clear debris, spin the blade by hand, check motor windings and the driver board. |
| E9 | Outdoor EEV malfunction | Expansion valve or driver fault on the outdoor unit. | Check EEV coil resistance/connector; replace the valve or board. |
| F3 | High discharge pipe temperature | Defective discharge pipe thermistor; stop valve closed; low refrigerant charge; EEV or 4-way valve problem. | Check the stop valves and charge, then the EEV, 4-way valve and discharge thermistor. |
| H0 | Compressor sensor system fault | General sensor/circuit issue in compressor control. | Check compressor sensor wiring and connectors at the board. |
| H3 | High-pressure switch fault (open circuit) | Wiring or sensor issue, distinct from an E3 pressure trip. | Check continuity and wiring to the switch itself. |
| H6 | Compressor position-detection / startup failure | Compressor relay cable disconnected; stop valve closed; input voltage out of spec; defective compressor or inverter PCB. | Check the compressor wiring and stop valves, verify input voltage, then the inverter PCB and compressor. |
| H8 | Compressor current sensor fault | Sensor or wiring fault on compressor current feedback. | Check the current sensor's wiring and connector at the board. |
| H9 | Outdoor air thermistor fault | Failed or disconnected outdoor ambient sensor. | Verify resistance vs. chart, reseat or replace the sensor. |
| J3 | Discharge pipe thermistor fault | Failed sensor or bad connection at the discharge line. | Verify resistance, reseat the connector, replace if out of range. |
| J5 | Suction pipe thermistor fault | Failed sensor or bad connection at the suction line. | Verify resistance, reseat the connector, replace if out of range. |
| J6 | Outdoor heat exchanger thermistor fault | Failed coil sensor on the outdoor unit. | Verify resistance vs. chart, replace if faulty. |
| J8 | Liquid pipe thermistor fault | Failed sensor on the liquid line. | Verify resistance vs. chart, reseat or replace. |
| L3 | Electrical box temperature rise (VRV IV: reactor temperature rise) | Fin temperature rise from a short circuit; defective outdoor fan motor; defective power transistor; defective outdoor PCB. | Check the outdoor fan motor, power transistor and outdoor PCB. |
| L4 | Inverter radiation fin (heat sink) temperature rise | Defective outdoor fan motor; short circuit; defective fin thermistor; silicone grease not applied properly; defective inverter PCB. | Check the outdoor fan, the fin thermistor and the heat-sink grease; replace the inverter PCB if needed. |
| L5 | Inverter instantaneous overcurrent (DC output) | Defective compressor coil or mechanical lock; defective inverter PCB/power module; stop valve closed; wiring or supply voltage problem. | Check the stop valves, wiring and supply voltage; megohm the compressor; check the inverter PCB. |
| L8 | Inverter overcurrent (compressor overloaded) | Compressor overloaded; broken wire in the compressor coil or wiring; defective inverter PCB. (Compressor stall is L9.) | Verify incoming voltage and phase balance, test the diode bridge and power transistors, megohm the compressor. |
| L9 | Compressor startup malfunction | Stall on startup — pressure equalization time or a wiring fault. | Allow standard off-time for pressure equalization before restart; check wiring. |
| P1 | Power supply voltage imbalance | Uneven phases on a 3-phase supply. | Measure all three legs and correct the imbalance at the source. |
| P4 | Radiating fin thermistor fault | Failed sensor on the inverter heat sink. | Verify resistance vs. chart, replace if faulty. |
| U0 | Refrigerant shortage | Refrigerant shortage or clogging (wrong piping); defective thermistor; defective low pressure sensor. | Leak-search and check piping before adding charge; check the thermistors and low pressure sensor. |
| U2 | Power supply voltage abnormal | Brownout, undervoltage, or a wiring/supply issue. | Check the breaker, incoming voltage, and supply wiring. |
| U4 | Indoor–outdoor transmission error | Short or wrong wiring on the transmission wiring (F1/F2); outdoor power off; system address mismatch. | Check F1/F2 wiring (look for 16 VDC across F1-F2), confirm outdoor power and addresses. |
| U7 | Transmission error between outdoor units (VRV) / outdoor PCB signal error (ductless) | VRV: transmission wiring error between outdoor units or an external control adaptor. Ductless: signal transmission error on the outdoor PCB. | VRV: check the outdoor-to-outdoor transmission wiring. Ductless: check/replace the outdoor PCB. |
| UA | Capacity/model mismatch | Incompatible indoor/outdoor pairing or a field-setting error. | Verify the combo is approved and the field-set switches/dip settings match. |
| UF | System not set up / wiring and piping conflict | Wiring and piping don't match; check operation not run; stop valve not opened. | Verify wiring matches piping, open the stop valves, run the check operation. |
| UH | System malfunction — transmission wiring (RA multi: anti-icing in another room) | Improper transmission wiring connection; refrigerant system address undefined. On RA multi units it means anti-icing control in another room. | Re-check the transmission wiring against the install diagram. |
| A4 | Freeze protection (water side) | Shortage of water volume; low WATER temperature setting; defective water temperature thermistor. | Check water flow, the water temperature setting and the thermistor. |
| A8 | Power supply voltage error | Bad voltage, loose wiring, or a supply-side connection issue. | Verify voltage, check wiring and connections at the disconnect and board. |
| C1 | PCB communication error | Loose or damaged wiring between boards, or a lost-power event. | Check connections and wiring between boards; test both boards if it persists. |
| C5 | Gas pipe thermistor fault | Failed or corroded gas-line temperature sensor, or a PCB issue. | Check resistance vs. chart, inspect the connector, replace if faulty. |
| C6 | Indoor PCB / fan PCB combination error | Wrong indoor fan motor for the board, a field-setting error, or a loose adaptor connector. | Verify the motor matches the model, check capacity/field settings, reseat the adaptor harness. |
| E0 | Protection device activated | Outdoor unit PCB safety device tripped, or a broken wire to it. | Inspect the safety device and its wiring; check for the underlying trip cause before resetting. |
| E2 | Ground leakage detected | Ground fault, improper sensor wiring, or a compressor insulation issue. | Test the ground-fault sensor and wiring, then megohm the compressor. |
| E8 | Compressor overcurrent (inverter) | Defective compressor; defective inverter main-circuit capacitor; defective outdoor PCB or power transistor. | Check the compressor, the inverter PCB and its power transistor. (The capacitor here is the inverter main-circuit capacitor, not a run/start cap.) |
| EA | Reversing valve / cool-heat switch fault | Stuck or defective 4-way valve, low charge, or a PCB/solenoid issue. | Check valve operation and solenoid coil, verify charge, inspect the board. |
| H4 | Low-pressure switch fault (open circuit) | Wiring or sensor issue on the low side, distinct from an E4 pressure trip. | Check continuity and wiring to the low-pressure switch itself. |
| H5 | Compressor motor overload thermistor fault | Defective overload thermistor; defective connector contact. (The CT sensor fault is H8.) | Check the overload thermistor and its connector. |
| H7 | Outdoor fan feedback fault | Short in the fan motor leads, an abnormal feedback signal, or a driver PCB issue. | Check the fan connector and wiring, test motor resistance, verify signal at the board. |
| F0 | No.1 / No.2 system common protection device activation (dual-system units) | Daikin's code list gives the name only — no cause or fix is published. | Look for a more specific code and check the unit's own service manual. |
| F4 | Compressor suction temperature abnormal (VRV: wet alarm, liquid returning to the compressor) | Defective suction pipe thermistor; defective indoor EEV; dirty indoor air filter. | Check the suction thermistor and the indoor EEV, clean the air filter. |
| F6 | Refrigerant overcharge detected | System overcharged, or a sensor giving a false high reading. | Verify charge by weight against the nameplate; recover excess if confirmed overcharged. |
| J1 | Pressure sensor fault | Faulty transducer, wiring, or a PCB issue. | Check the sensor's wiring and connector; verify voltage output against spec. |
| J2 | Current sensor (CT) fault | Failed sensor or a compressor-side wiring issue. | Check the CT sensor and inspect the compressor circuit it monitors. |
| J4 | Heat exchanger gas temperature sensor fault | Bad connection or a failed thermistor. | Check the connector, verify resistance vs. chart, replace if faulty. |
| J7 | Subcooling heat exchanger liquid thermistor fault | Failed sensor, bad connector, or a broken wire. | Check resistance vs. chart, inspect the connector and wiring. |
| J9 | Gas pipe purge / subcooling heat exchanger gas pipe thermistor fault | Defective thermistor or wiring (VRV, SkyAir and RA units). | Check the thermistor resistance and wiring. |
| JA | High-pressure sensor fault | Faulty transducer or a miswired connection. | Test the sensor and confirm it's wired to the correct port. |
| JC | Low-pressure sensor fault | Faulty transducer, a miswired connection, or a PCB issue. | Test the sensor with gauges and verify its output voltage. |

### Daikin Fit / ClimateTalk communication
ClimateTalk is the communicating protocol linking a Daikin Fit outdoor unit, air handler/furnace, EEV coil, and a Daikin One+ thermostat. Codes below show on the thermostat — cross-checked against Daikin's own One+ Pro dealer error-code references.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| 02 | Thermostat internal comm error | ClimateTalk coprocessor failed to start. | Warm-start (power-cycle) the thermostat; replace it if this repeats. |
| 03 | Thermostat internal comm error | Coprocessor unresponsive to commands. | Warm-start; call Daikin support; replace if it persists. |
| 04 | Thermostat software upgrade error | Firmware update failed to complete. | Warm-start and retry the update; replace if it won't finish. |
| 05 | Thermostat internal comm error | General ClimateTalk fault. | Check 24VAC power to the thermostat, then warm-start. |
| 06 | Piezo speaker hardware error | Speaker driver failed to start. | Verify 24VAC power to the thermostat, then warm-start; call support if it repeats. |
| 07 | LED hardware error | LED driver failed to start. | Verify power, warm-start, contact support if it repeats. |
| 08 | Software upgrade error — signature mismatch | OTA download signature didn't verify; thermostat reverted to previous firmware. | Verify power, warm-start and retry; contact support if it won't take. |
| 09 | Software upgrade error | OTA upgrade process failed to complete. | Verify power, warm-start and retry; contact support if it persists. |
| 0A | Proximity sensor hardware error | Proximity sensor driver could not start. | Check 24 VAC and warm-start the thermostat; if it repeats, call Daikin support. |
| 0B | Temp/humidity sensor hardware error | Sensor driver failed to start. | Warm-start, contact support, replace the thermostat if needed. |
| 0C | Temperature sensor failed in operation | Sensor faulted after startup rather than at power-up. | Warm-start; replace the thermostat if it recurs. |
| 0D | Humidity sensor failed in operation | Sensor faulted after startup. | Warm-start; replace the thermostat if it recurs. |
| 0E | Wi-Fi hardware error | Wi-Fi driver failed to start. | Verify power, warm-start, contact support if it repeats. |
| 0F | Wi-Fi hardware error | Wi-Fi driver communication issue. | Warm-start the thermostat; if it repeats, call Daikin support. |
| 10 | Thermostat reboot logged | Power loss, an OTA update, or a manual reboot. | Informational only — no action needed unless it keeps repeating. |
| 1E | Heat pump communication loss | Reversed Data1/Data2 polarity, lost power, or damaged wiring to the heat pump. | Check polarity at both ends, verify power, inspect the run for damage. |
| 1F | Air conditioner communication loss | Reversed data polarity, lost power, or damaged wiring to the AC unit. | Same checks as heat pump comm loss, at the AC unit. |
| 20 | EEV coil communication loss | Reversed data polarity, power loss, or wire damage at the expansion valve. | Check polarity and continuity to the EEV driver. |
| 21 | Air handler communication loss | Reversed data polarity, power loss, or damaged wiring to the air handler. | Check polarity, power, and the wiring run to the air handler. |
| 22 | Furnace communication loss | Reversed data polarity, power loss, or damaged wiring to the furnace. | Check polarity, power, and the wiring run to the furnace. |
| 51 | No ClimateTalk equipment discovered | Nothing responding on the communicating bus. | Check wiring, polarity, and power at every node on the bus, one at a time. |
| 70 | EEV open circuit | EEV coil disconnected at the indoor unit, or wired incorrectly. | Check the EEV coil connection, verify winding resistance, replace the coil or board. |
| 73 | EEV liquid-side temperature fault | Liquid thermistor open, shorted, or reading abnormally. | Check the thermistor connection and resistance; replace the thermistor or board. |
| 74 | EEV gas-side temperature fault | Gas-side thermistor open, shorted, or reading abnormally. | Check the thermistor connection and resistance; replace as needed. |
| 75 | EEV pressure sensor fault | Pressure sensor open, shorted, or out of range. | Check the connection, verify output voltage, replace the sensor or board. |
| 76 | Equipment communication loss during operation | Open circuit, wiring fault, or a power loss mid-run. | Check the equipment's wiring and power supply; replace the board if wiring checks out. |
| 77 | Thermostat communication loss (startup or operation) | Wiring fault, thermostat failure, or a voltage issue. | Check wiring and 24V supply; press the equipment's LEARN button to re-pair if applicable; may need a board replacement. |
| 78 | Equipment communication loss during startup | Open circuit, wiring error, or power interruption at startup. | Check wiring and power supply before assuming a bad board. |
| D0 | EEV data not yet on network | Board hasn't received its shared configuration data. | Populate the shared data set using the memory card per the install manual. |
| D4 | EEV invalid memory card data | Memory card data rejected by the board. | Verify the card has the correct data for that model; replace the board if it still won't take. |

### Air handler / furnace — ClimateTalk blower & heater kit codes
Blower and heater-kit codes for communicating air handlers (DFVE, DMVT, DMVE) and communicating furnaces, from Daikin's One+ unitary error code list and the air handler service instructions. The thermostat logs them under Error history. Eb, Ed and EC apply to air handlers only. On an EEV air handler board, "EE" on the board's own LED can also mean it's in Emergency mode.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| B0 | Blower motor not running | Loose wiring connection or a failed motor. | Check and tighten wiring connections first, then test/replace the motor. |
| B1 | Blower motor communication error | Loose wiring, a failed motor, or a bad control module. | Check connections, then test the motor and control module. |
| B2 | Blower motor horsepower mismatch | Wrong motor installed, or incorrect shared data on the board. | Verify the motor matches the model spec; repopulate shared data if needed. |
| B3 | Blower operating in a limiting condition | Blocked filters or airflow blockage; restrictive or undersized ductwork; low voltage; incorrect wiring; high ambient temperature. | Clear the filter and airflow path, verify supply voltage and wiring, check duct sizing. |
| B4 | Blower current trip / lost rotor position | Abnormal load or a blockage on the blower wheel or housing. | Check filters, registers, and ductwork for obstructions before replacing the motor. |
| B5 | Blower motor locked rotor | Obstruction in the housing or seized bearings. | Clear any obstruction, check the wheel spins freely by hand, replace the motor if seized. |
| B6 | Blower motor voltage or temperature trip | Supply voltage out of range, or ambient temperature exceeding motor rating. | Verify line voltage matches nameplate, check the installation environment. |
| B7 | Blower motor missing required parameters | Control module data error, or a locked rotor confusing the parameter check. | Verify the shared data set, check rotor condition, reprogram if needed. |
| B9 | Low indoor airflow | Blocked filter or restrictive ductwork. | Clean/replace the filter, inspect ductwork sizing, confirm registers are open. |
| D0 | No shared data on network | The board hasn't received its configuration data set yet. | Populate the shared data set using the memory card per the install manual. |
| D1 | Incorrect shared data on network | Data set on the board doesn't match this specific unit. | Repopulate the correct shared data set using the memory card. |
| D4 | Invalid memory card data | Memory card data rejected by the board. | Verify the card has the correct data, repopulate, or replace the board. |
| Eb | Heat called with no heater kit selected | No heater kit selected. | Select the valid heater kit on the thermostat. |
| Ed | Invalid heater kit selected | Heater kit DIP switches set wrong. | Set the correct DIP switches for the installed kit. |
| EC | Heater kit size mismatch | Selected kit doesn't match what's actually installed — oversized, undersized, or wrong data. | Verify the dip switches against the installed kit and the nameplate. |
| EE | Internal control fault | Disconnect switch left off, a blown fuse, or a board malfunction. | Confirm the unit disconnect is on, check/replace the fuse, replace the board if it persists. |
| EF | Auxiliary alarm open — high water | High water level in the evaporator coil drain pan; auxiliary alarm terminals TB4/TB5 open. | Service the drain and pan. If nothing is wired to TB4/TB5, close those terminals. |
| E5 | Control board fuse blown (air handler) | Fuse F1U blown; connector TB10 open. | Check wiring to the aux alarm, heater kit and communication connection, then replace the fuse. |

### Furnace — ClimateTalk / communicating codes
Codes for Daikin communicating furnaces (DR80TC, DR96TC and similar), from the One+ unitary error code list and the furnace install manuals IOD-2043 / IOD-2044. The furnace board itself shows 7-segment codes. It works with or without a Fit outdoor unit. On the DR80TC board the gas-valve letters are the reverse of the thermostat list: board EEb = external valve, EEC = internal.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| E0 | Lockout — excessive ignition attempts | Furnace failed to establish flame across repeated tries. | Check gas supply, pressure switch, igniter, and flame sensor in that order. |
| E1 | Low-stage pressure switch closed at startup | Switch contacts stuck closed before the inducer even starts. | Check the switch for stuck/welded contacts; replace if it won't open with power off. |
| E2 | Low-stage pressure switch open during heating | Blocked hose, restricted flue, or a failing inducer. | Inspect the pressure switch hose and flue for blockage; check inducer operation. |
| E3 | High-limit switch open | Insufficient airflow or flame rollout. | Check the filter, blower operation, burner alignment, and flue for blockage. |
| E4 | Flame detected with no call for heat | Flame-sense signal short, or a slow/leaking gas valve. | Correct any sensor short, verify the gas valve fully closes. |
| E5 | Blown fuse on the board | Short in the low-voltage wiring. | Locate and correct the short before replacing the fuse. |
| E6 | Low flame signal | Coated/corroded flame sensor, or the sensor out of position. | Clean the sensor, verify its position and gas pressure. |
| E7 | Igniter fault or poor grounding | Wiring or grounding issue at the igniter. | Check igniter wiring, connections, and the unit's equipment ground. |
| E8 | High-stage pressure switch stuck closed | Contacts sticking closed. | Replace the switch or repair the wiring holding it closed. |
| E9 | High-stage pressure switch stuck open | Blocked hose or a pressure/flue issue. | Inspect the hose, flue, and switch operation. |
| EA | Reversed 115VAC polarity | Hot/neutral reversed at the disconnect. | Correct wiring polarity and verify the equipment ground. |
| EB | Internal gas valve error | Gas valve energized when it should not be; internal gas valve error. | Check wiring in the gas valve circuit; if it's correct, replace the integrated control board. |
| EC | External gas valve error / inducer current fault | Model-dependent — an external valve failure on some boards, an inducer overcurrent on others. | Check the gas valve first on ULN models; check inducer motor draw on others. |
| Ed | Flame rollout switch open | Burner orifice misaligned or a blocked heat exchanger. | Align the orifice and burners, clear any blockage, inspect the heat exchanger. |
| EE | Internal control fault | Daikin's code list gives no cause. | No fix is published beyond the control itself — check the furnace install manual for the model. |
| EF | Auxiliary input open — high condensate | High water level tripped a float switch. | Check the overflow pan and condensate drain. |
| 15 / 16 | Return-air temp (RAT) sensor open / short | Failed or disconnected return-air sensor. | Check the sensor and its wiring; verify resistance against spec. |
| E19 | Onboard return air temperature sensor (R311) is unplugged | Sensor disconnected, damaged, or not yet detected by the control after a power event. | Power cycle the furnace — the control can take up to 90 seconds to detect sensors. Check the PCB for visible damage to sensor R311 and replace the PCB if damaged. Turn power OFF before servicing. (IOD-2043 p.35, IOD-2044 p.49.) Note: E15/E16 are the EXTERNAL return air probe; E19/E1A are the onboard sensor R311 — two different sensors. |
| 17 / 18 | Supply-air temp (SAT) sensor open / short | Failed or disconnected supply-air sensor. | Check the sensor and its wiring; verify resistance against spec. |
| 19 / 1A | Board temperature sensor open / short | Onboard temp sensor failed. | Replace the board if the sensor itself is confirmed bad. |
| 1B–1F | Air pressure switch (APS) sensor errors — reference / null / span / pressure / input | Daikin's code list gives the names only. | No cause or fix is published — check the furnace install manual for the model. |
| 76 / 77 / 78 | 76 equipment communication loss / 77 thermostat communication loss / 78 need to connect outdoor unit | 76 and 77 are communication losses. 78 is not a comm loss — the system is asking for the outdoor unit to be connected. | 76/77: check wiring and power on the affected run. 78: connect/commission the outdoor unit. |

### AC / heat pump outdoor unit — extended diagnostics (communicating)
Thermostat and control-board codes for Daikin Fit outdoor units, from Daikin's Installation & Service Reference tables: 3P761829-1B (R-32 DC6VS/DH6VS/DC9VSA/DH7VSA) and 3P731493-1 (R-410A DX6VS/DZ6VS/DZ6VSA). The two manuals list the same codes and meanings; the size notes on codes 32, 33 and 57 and the network pages differ. Where the board column shows a hyphen, the code shows on the thermostat and there is no code on the board display.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| 11 / E11 | System start-up test required (thermostat-only message) | Installer needs to run the SYSTEM START-UP TEST from the thermostat menu, or that test is currently running. | Run the SYSTEM START-UP TEST from the thermostat (see the outdoor unit installation manual, STEP 3 System Start-Up Test). Code clears automatically once testing completes. |
| 12 / E12 | General memory error. | High electrical noise, or a faulty control board. | Replace control board if necessary. |
| 13 / E13 | Frequent high-pressure faults (CRITICAL). | Blocked/restricted outdoor unit coil and/or lines; stop valve not completely open; overcharge; outdoor fan not running; high-pressure switch (HPS) inoperable; faulty indoor and outdoor EEV coil; faulty indoor and outdoor EEV; faulty control board. | Check and clean outdoor unit coil and/or lines. Check the opening of stop valve — should be full open; repair/replace if needed. Check refrigerant charge level; adjust if needed. Check outdoor fan motor and wiring; repair/replace if needed. Check indoor and outdoor EEV; replace if needed. Check indoor and outdoor EEV coil; replace if needed. Replace control board if necessary. |
| 14 / (dash) | Same as 13, but MINOR — equipment is experiencing frequent high-pressure faults; control has determined continued operation is acceptable. | Same causes as code 13. | Same corrective actions as code 13. |
| 15 / E15 | Frequent low-pressure faults (CRITICAL). | Stop valve not completely open; restriction in refrigerant line; low refrigerant charge; refrigerant leak; pressure sensor inoperable or not properly connected; indoor fan motor not functioning correctly; faulty indoor and outdoor EEV coil; faulty indoor and outdoor EEV; faulty control board. | Check the opening of stop valve; repair/replace if needed. Check for restrictions in refrigerant line; repair/replace if needed. Check refrigerant charge level; adjust if needed. Test for system leaks using leak test procedure. Check the connection to pressure sensor; repair/replace if needed. Check indoor and outdoor EEV; replace if needed. Check indoor and outdoor EEV coil; replace if needed. Check indoor blower motor and wiring; repair/replace if needed. Replace control board if necessary. |
| 16 / (dash) | Same as 15, but MINOR — continued operation acceptable. | Same causes as code 15. | Same corrective actions as code 15. |
| 17 / E17 | Frequent compressor faults. | Stop valve not completely open; compressor wire is lost phase; compressor motor failure. | Check the opening of stop valve; repair/replace if needed. Check the wire between control board and compressor. Inspect compressor motor for proper function; replace if necessary. |
| 18 / E18 | Control board may need to be replaced. | Outdoor fan motor not connected properly; faulty control board; electrical noise. | Check wiring from outdoor fan motor to control board; repair if needed. Replace control board if necessary. |
| 19 / E19 | Frequent outdoor unit control board and/or motor faults. | Obstruction in fan rotation; outdoor fan motor not connected properly; outdoor fan not running; faulty control board; electrical noise. | Check and clean grille of any debris. Check wiring from outdoor fan motor to control board; repair if needed. Check outdoor fan motor and wiring; replace if needed. Replace control board if necessary. Note: this is the OUTDOOR-board version of "E19" — a furnace/indoor control board showing E19 is a different fault (onboard return-air sensor R311 unplugged; see the furnace ClimateTalk table above). Same code number, two different boards, two different meanings — confirm which board is actually displaying it before diagnosing. |
| 20 / E20 | Outdoor EEV fault. | Outdoor EEV coil is not connected; faulty outdoor EEV coil; faulty control board. | Check outdoor EEV coil connection; repair/replace as needed. Replace control board if necessary. |
| 21 / E21 | Frequent low discharge superheat faults. | Thermistors inoperable or improperly connected; faulty indoor and outdoor EEV coil; faulty indoor and outdoor EEV; over charge; faulty pressure sensor; faulty control board. | Check the connection to thermistors; repair/replace if needed. Check indoor and outdoor EEV coil; replace if needed. Check indoor and outdoor EEV; replace/repair if needed. Check refrigerant charge level; adjust if needed. Check pressure sensor; replace/repair if needed. Replace control board if necessary. |
| 22 / E22 | Frequent high discharge temperature faults. Discharge thermistor is not put in correct position. | Discharge thermistor inoperable or improperly connected; discharge thermistor is put in incorrect position or off; the compressor enclosure temperature is too high; low refrigerant charge; overcharge; faulty compressor. | Check discharge thermistor resistance and connections; repair/replace as needed. Check discharge thermistor position. Check refrigerant charge level; adjust if needed. Check the compressor; repair/replace if needed. |
| 23 / E23 | The control has detected that the Discharge Temperature Sensor is out of range. | Discharge thermistor inoperable or improperly connected. | Check discharge thermistor resistance and connections; repair/replace as needed. |
| 24 / E24 | The high pressure switch is open. | High pressure switch (HPS) inoperable. | Check resistance on HPS to verify operation; replace if needed. |
| 25 / E25 | The outdoor air temperature sensor is open or shorted. | Faulty outdoor thermistor sensor or disconnect. | Inspect and test sensor; replace sensor if needed. |
| 26 / E26 | The control determines that the pressure sensor is not reacting properly. | Pressure sensor inoperable or not properly connected. | Check the connection to pressure sensor; repair/replace if needed. |
| 27 / E27 | The control has detected that the Outdoor Coil Defrost Temperature Sensor is out of range. | Outdoor defrost thermistor inoperable or not properly connected. | Check the connection to OD defrost thermistor; repair/replace if needed. |
| 28 / E28 | The control has detected that the Outdoor Coil Temperature Sensor is out of range. | Outdoor coil thermistor inoperable or not properly connected. | Check the connection to OD coil thermistor; repair/replace if needed. |
| 29 / E29 | The control has detected that the Liquid Temperature Sensor is out of range. | Liquid thermistor inoperable or not properly connected. | Check the connection to liquid thermistor; repair/replace if needed. |
| 30 / E30 | Indicates the control board may need to be replaced. | Wiring to control board disconnected; faulty control board; electrical noise. | Check wiring to control board; repair as needed. Replace control board if necessary. |
| 32 / E32 | Frequent high-temperature faults on the outdoor unit control board. | Ambient air conditions too high; stop valve not completely open; cooling bracket screw(s) missing or not properly fastened ; no or poor thermal grease coating between cooling plumbing and cooling bracket on control board ; no flow or limited flow through control board cooling circuit (potential restriction in line or low refrigerant) . | Cycle power; re-try during usable ambient temperature range. Check grease applying condition . Check screw tightening condition . Check for restriction in line. Check refrigerant charge level; adjust if needed. Check the opening of stop valve — should be full open; repair/replace if needed. |
| 33 / (dash) | Same as 32, but MINOR — control has determined continued operation is acceptable. | Same causes as code 32. | Same corrective actions as code 32. |
| 34 / E34 | Control board detected a high current condition. This indicates the potential for a short circuit. | Current spike in supply; stop valve not completely open; the compressor wire is lost phase; faulty control board; faulty compressor. | Check power supply for in-rush current during start-up or steady state operation. Check the opening of stop valve; repair/replace if needed. Check the wire between control board and compressor. Replace control board if necessary. Check the compressor; repair/replace if needed. |
| 35 / E35 | Control board detected a high current condition. | Short circuit condition; stop valve not completely open; overcharge; faulty control board; faulty compressor. | Check installation clearances. Check the opening of stop valve; repair/replace if needed. Check refrigerant charge level; adjust if needed. Replace control board if necessary. Check the compressor; repair/replace if needed. |
| 36 / E36 | The control encountered an abnormal condition during the startup procedure. | Blocked/restricted outdoor unit coil and/or lines; the compressor wire is lost phase; inconsistent compressor load; faulty control board. | Check and clean outdoor unit coil and/or lines. Check the wire between control board and compressor. Replace control board if necessary. |
| 37 / E37 | Indicates the control board may need to be replaced. | Outdoor fan motor not connected properly; faulty control board. | Check wiring from outdoor fan motor to control board; repair if needed. Replace control board if necessary. |
| 38 / E38 | The control has detected a voltage related issue with the compressor. | High or low voltage from supply; the compressor wire is lost phase; faulty control board. | Correct low/high line voltage condition; contact local utility if needed. Check the wire between control board and compressor. Replace control board if necessary. |
| 39 / E39 | Indicates the control board may need to be replaced. | Thermistors inoperable or improperly connected; faulty control board. | Check the connection to thermistors; repair/replace if needed. Replace control board if necessary. |
| 40 / E40 | Control determines that its compressor requirement is different than the compressor capability. | Memory card not correct; control board mismatch. | Check memory card data vs. outdoor unit model. Verify control board size vs. outdoor unit model; replace control board if necessary. |
| 41 / E41 | The control has detected a low refrigerant condition. | Refrigerant leak; low refrigerant charge; thermistors inoperable or not properly connected. | Test for system leaks using leak test procedure. Check refrigerant charge level; adjust if needed. Check the connection to thermistor; repair/replace if needed. |
| 42 / E42 | Control detects a low power supply voltage condition. | Low line voltage supply. | Check circuit breakers and fuses; replace if needed. Verify unit is connected to power supply as specified on rating plate. Correct low line voltage condition; contact local utility if needed. |
| 43 / E43 | Control detects a high power supply voltage condition. | High line voltage supply. | Verify unit is connected to power supply as specified on rating plate. Correct high line voltage condition; contact local utility if needed. |
| 44 / E44 | The control detects the outdoor temperature outside recommended operational range. Unit may continue to operate normally. | Ambient air conditions too high or low. | Cycle power; re-try during usable ambient temperature range. |
| 47 / E47 | The control is unable to start the System Verification test because indoor heat has been turned on by thermostat. Please set thermostat to off position. | Heat provided by secondary heating source. | Turn off Furnace or heater using thermostat before operation. |
| 49 / E49 | The control is unable to enter Charging Mode because indoor heat has been turned on by thermostat. Please set thermostat to off position. | Heat provided by secondary heating source. | Turn off heater using thermostat before operation. |
| 50 / E50 | This indicates there is a voltage issue on the control board. See service manual for troubleshooting information. | High or low voltage from supply voltage or frequency; faulty control board; noise. | Correct low/high line voltage condition; contact local utility if needed. Replace control board if necessary. Contact local utility if needed. |
| 51 / E51 | This indicates potential communication issues have been detected by the outdoor unit control board. (Network communication error — see Network Troubleshooting.) | Communication wiring disconnected. | Check communication wiring; repair as needed. |
| 52 / (dash) | Frequent compressor faults (companion of 17), continued operation acceptable — control has determined this may be a problem with the equipment. | Stop valve not completely open; the compressor wire is lost phase; compressor motor failure. | Same corrective actions as code 17. |
| 53 / (dash) | Frequent outdoor unit control board and/or motor faults (companion of 19), continued operation acceptable. | Obstruction in fan rotation; outdoor fan motor not connected properly; outdoor fan not running; faulty control board; noise. | Same corrective actions as code 19. |
| 54 / (dash) | Frequent low discharge superheat faults (companion of 21), continued operation acceptable. | Thermistors inoperable or improperly connected; faulty indoor EEV or indoor EEV coil (when cooling); faulty control board; faulty outdoor EEV or outdoor EEV coil (when heating). | Check the connection to thermistors; repair/replace if needed. Check indoor EEV; replace if needed. Check indoor EEV coil; replace if needed. Replace control board if necessary. Check outdoor EEV; replace if needed. Check outdoor EEV coil; replace if needed. |
| 55 / (dash) | Frequent high discharge temperature faults (companion of 22), continued operation acceptable. | Discharge thermistor inoperable or improperly connected; discharge thermistor is put in incorrect position or off; low refrigerant charge; overcharge; faulty compressor. | Check discharge thermistor resistance and connections; repair/replace as needed. Check discharge thermistor position. Check refrigerant charge level; adjust if needed. Check the compressor; repair/replace if needed. |
| 56 / E56 | The control has detected if the Outdoor Suction Temperature Sensor is out of range. | Suction thermistor inoperable or not properly connected; faulty reversing valve. | Check the connection to suction thermistor; repair/replace if needed. Check reversing valve; replace if needed. |
| 57 / (dash) | This indicates the control is sensing sweating on the cooling loop.  | Refrigerant leak; low refrigerant charge; faulty indoor EEV or indoor EEV coil; thermistors inoperable or improperly connected. | Test for system leaks using leak test procedure. Check refrigerant charge level; adjust if needed. Check indoor EEV; replace if needed. Check indoor EEV coil; replace if needed. Check the connection to thermistors; repair/replace if needed. |
| 58 / E58 | The Overload Protection sensor for Compressor is opened. | Overload protection (OL) sensor inoperable; jumper wire (X33A) is put in incorrect position or off. | Check resistance on OL sensor to verify operation; replace if needed. Check OL sensor position on compressor body. Check jumper wire position (X33A). |
| B0 / Eb0 | The estimated airflow from indoor subsystem is near to 0 CFM. | Failed indoor blower motor; indoor fan motor not properly connected; too much static pressure. | Check ID fan motor wiring and connectors; repair/replace if needed. Check ID fan motor; replace if needed. Check the obstruction inside duct work. |
| B9 / Eb9 | Estimated airflow from motor is lower than the airflow requirement. | Failed indoor blower motor; indoor fan motor not properly connected; too much static pressure. | Check ID fan motor wiring and connectors; repair/replace if needed. Check ID fan motor; replace if needed. |
| D0 / Ed0 | Control board does not have the necessary data for it to properly perform its functions. | Outdoor unit is wired as part of a communicating system and integrated control module does not contain any shared data. | Replace control board if necessary. |
| D1 / Ed1 | Control board does not have the appropriate data needed to properly perform its functions. | Outdoor unit is wired as part of a communicating system and integrated control module contains invalid shared data or network data is invalid for the integrated control module. | Replace control board if necessary. |
| D2 / Ed2 | The airflow requirement is greater than the airflow capability of the indoor subsystem. | Outdoor unit is wired as part of a communicating system and outdoor unit requires airflow greater than indoor unit's airflow capability, or a type of indoor unit without EEV is connected to the system; shared data is incompatible the system or missing parameters; communication wiring with indoor unit has loose connection; airflow trim setting is out of range. | Check combination to be matched with rating list; correct if needed. Verify shared data is correct for your specific model; repopulate data if required. Check communication wiring and power supply wiring of indoor unit. Verify trim setting and adjust if needed. See "SET THERMOSTAT TO ADJUST INDOOR AIR CFM TRIM" section. |
| D3 / Ed3 | There is a mismatch between the shared data and the control physical hardware. | Shared data sent to integrated control module does not match hardware configuration. | Verify shared data is correct for your specific model; repopulate data if required. |
| D4 / Ed4 | The memory card data has been rejected. | Shared data on memory card has been rejected. | Verify shared data is correct for your specific model; repopulate data if required. |

### Daikin Fit outdoor unit — network troubleshooting (communication faults)
From the Daikin Fit Installation & Service Reference (3P761829-1B p.47; the R-410A manual 3P731493-1 has the same LED table). On the R-410A Fit the fix is to flip both DS1 switches; the R-32 family pairs outdoor DS1 with indoor DS7.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| DS1 / DS7 termination combinations | Outdoor DS1 and indoor DS7 set the comm circuit termination resistance. | Factory default is combination 1: DS1 both ON, DS7 both ON. | On a comm error, try the combinations one at a time: 1 = DS1 ON / DS7 ON (default), 2 = OFF / ON, 3 = ON / OFF, 4 = OFF / OFF. Apply power after each change and see if the error clears. |
| LEARN button | Resets the network. | — | Press and hold about 5 seconds to reset the network. |
| Red LED — Off | Normal condition. | — | None. |
| Red LED — 1 Flash | Communications failure. | An unknown packet was received. | Press the LEARN button; verify wiring. |
| Red LED — 2 Flash | Out-of-box reset. | Control just powered up, or LEARN was pressed. | None. |
| Green LED — Off | No power / communications error. | No power to the unit, or an open fuse. | Check breakers and fuses, press LEARN, check for shorts. |
| Green LED — 1 Steady Flash | No network found. | — | Check the comm wiring and connections. |
| Green LED — Rapid Flashing | Normal network traffic. | Control is talking on the network as expected. | None. |
| Green LED — On Solid | Terminal 1 / Terminal 2 miswire. | Terminals 1 and 2 reversed, or shorted to each other or to C/R. | Correct the 1/2 wiring. |

### CoreSense™ 3-Wire Module — Amana ALXS/ALZS, Daikin DC4SEA/DC5SEA/DH4SEA/DH5SEA
Copeland CoreSense diagnostics — self-contained module on any residential condensing unit with a Copeland Scroll compressor, no external sensors. LED flash count = fault. Source: Amana RS6200301r1 / Daikin RSD6200301 service manuals (functionally identical content).

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| RUN (Solid Yellow) | Normal operation | Module powered, compressor running normally. | No action. |
| TRIP (Solid Red) | Thermostat demand (Y) present but compressor not running | Compressor protector open/high head pressure/low supply voltage; outdoor disconnect open; breaker/fuse open; broken wire/connector; high pressure switch open; contactor failed open. | Check each item in order — protector, disconnect, breaker, wiring, HPS, contactor. |
| TRIP + ALERT together | Control circuit voltage too low for operation | Low incoming voltage to the module. | Check line voltage and low-voltage transformer output before condemning the module. |
| ALERT Flash 1 (Yellow) | Long Run Time (low-side fault) | Low refrigerant charge; evaporator blower not running (relay/capacitor/motor/wiring/board/thermostat wiring); evaporator coil frozen (low suction pressure, low t-stat setting, airflow blockage, duct/filter blockage); faulty metering device (TXV bulb/stuck TXV/fixed orifice); liquid line restriction (blocked filter drier); thermostat malfunction. | Check each cause listed. |
| ALERT Flash 2 (Yellow) | Compressor (Pressure) Trip — runs 12sec–15min then trips, off >7min | Condenser fan not running (capacitor/wiring/motor); high head pressure (HPS, overcharge, non-condensables); condenser coil poor air circulation (dirty/blocked/damaged). | Check condenser fan first, then head pressure/charge, then coil airflow. |
| ALERT Flash 3 (Yellow) | Short Cycling — runs 12sec–15min then trips 35sec–7min | Thermostat demand signal intermittent; time delay relay or control board defective; low or high pressure switch cycling. | Check t-stat wiring/signal, then the delay relay/board, then pressure switches. |
| ALERT Flash 4 (Yellow) | Locked Rotor — trips within 12sec run, doesn't restart within 35sec | Run capacitor failed; low line voltage; excessive liquid refrigerant in compressor; compressor bearings seized. | Check capacitor and line voltage first; measure compressor oil level before condemning the compressor. |
| ALERT Flash 5 (Yellow) | Compressor (Moderate Run) Trip — runs 15min–18hrs then trips >7min | 1. Evaporator blower not running; 2. faulty metering device (TXV bulb, TXV/fixed orifice stuck closed); 3. condenser coil poor air circulation (dirty, blocked, damaged); 4. low refrigerant charge. | Check the evaporator blower, the metering device, condenser coil airflow and the charge. |
| LOCK Red Flash 2, Yellow Off | Compressor (Pressure) Trip lockout — 4 consecutive or 10 total pressure trips | Same causes as Alert Flash 2. | Same fixes as Flash 2. |
| LOCK Red Flash 3, Yellow Off | Short Cycling lockout — 10 consecutive short-cycling events | Same causes as Alert Flash 3; if HPS present, treat as Flash 2 (pressure) instead. | Same fixes as Flash 3, or Flash 2 if HPS-related. |
| LOCK Red Flash 4, Yellow Off | Locked Rotor lockout — 10 consecutive locked rotor events | Same causes as Alert Flash 4. | Same fixes as Flash 4. |
| LOCK Red Flash 5, Yellow Off | Compressor (Moderate Run) Trip lockout — 4 consecutive or 10 total moderate run trips | Same causes as Alert Flash 5. | Same fixes as Flash 5. |

### CoreSense™ "Comfort Alert" 2-Wire Module — base-tier units without the 3-wire module
Same self-contained design, no external sensors. From the Amana RS6200301r1 / Daikin RSD6200301 service manuals, whose "Applies to" line for this module is blank — the model list isn't published. The schematic shows indoor C/Y, the HPCO (high pressure cutout) and LPCO (low pressure cutout) switches, the contactor coil and the module.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| Normal Run — Solid Yellow | Normal operation, no trip | — | No action. |
| Code1 — Yellow Flash 1 | Long run time: compressor running >18 hrs (disabled in Heat Pump mode) | Same low-side causes as the 3-wire module's Flash 1. | Same fixes as 3-wire Flash 1. |
| Code2 — Yellow Flash 2 | Compressor (pressure) trip: runs 12sec–15min then trips >7min | Same as 3-wire Flash 2. Locks out after 4x consecutive (Red Flash 2, Yellow Off). | Same fixes as 3-wire Flash 2. |
| Code3 — Yellow Flash 3 | Pressure switch cycling: runs 12sec–15min then trips 35sec–7min | Same as 3-wire Flash 3. Locks out after 4x consecutive or 10x total (Red Flash 3, Yellow Off). | Same fixes as 3-wire Flash 3. |
| Code4 — Yellow Flash 4 | Locked rotor: trips within 12sec run, doesn't restart within 35sec | Same as 3-wire Flash 4. Locks out after 10x consecutive (Red Flash 4, Yellow Off). | Same fixes as 3-wire Flash 4. |
| Code5 — Yellow Flash 5 | Compressor (moderate run) trip: runs 15min–18hrs then trips >7min | Same as 3-wire Flash 5. Locks out after 4x consecutive or 10x total (Red Flash 5, Yellow Off). | Same fixes as 3-wire Flash 5. |
| Code9 — Red Flash 9 | Current to the PROT terminal is greater than 2A for 40ms | Lock indication: Red Flash 9, Yellow Off. | No cause or fix is published in the manual. |
| Trip — Solid Red | Demand present, compressor not running | Same causes as 3-wire TRIP. | Same fixes as 3-wire TRIP. |

### R-32 Refrigerant (A2L) Leak Detection board — indoor coil / blower section, LED label on the blower access panel
From Amana RS6200301r1 / Daikin RSD6200301. The R-32 sensor sits on the indoor coil drain pan and the board is behind the blower access panel — it detects R-32 leaking in the indoor coil, turns on the blower and switches off electric heat.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| Normal Operation | LED: slow flash, 2 sec on / 2 sec off | — | No action. |
| R-32 Leak Alarm | LED: fast flashing | Controls/sensor working properly — a leak has been detected. | Identify the leak source and address it. Do NOT open the unit or turn it off while this is displayed. |
| Delay Mode | LED: on continuously | After the leak/alarm clears, unit stays in alarm mode 5 minutes before returning to normal. | Check HVAC performance and re-check for leaks after any alarm clears. |
| System Verification Mode | LED: fast flashing (same as Leak Alarm) | Contractor-run test simulating an R-32 leak, max 5 minutes — press the button twice within 5 sec to enter. | No action needed; auto-exits after 5 min, or press the button once to end early. |
| Control Board Internal Fault | LED: flashes 2x, off 5 sec, repeat | PCB-side fault. | 1) Unplug and replug the R-32 sensor, cycle power. 2) If still faulted, unplug the sensor and LEAVE it unplugged, cycle power. If it still shows 2 flashes, replace the control; if it now shows 3 flashes, replace the sensor. |
| R-32 Sensor Communication Fault | LED: flashes 3x, off 5 sec, repeat | Connector/comm issue between sensor and PCB. | Unplug/replug the sensor and cycle power. If it persists, replace both the sensor and PCB — the connector issue can't be isolated further in the field. |
| R-32 Sensor Fault | LED: flashes 4x, off 5 sec, repeat | Sensor itself reports an internal fault; comms to the sensor are fine. | Unplug/replug and cycle power. If it persists, replace the sensor only. |

### ComfortNet DX/DZ 7TC–18TC — PCBJA101/102/104 Air Handler Diagnostic Codes
R-410A ComfortNet air handler control boards, from Daikin RSD6200007r24 pp.43-50. PCBJA101/102 use LED flash counts; PCBJA104 uses a 7-segment display and adds d1 and EF (it has no 5-flash row).

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| 1 Flash — HTR TOO LARGE (Ec) | Electric heat dip switch set larger than expected for the call on W1/Emergency heat. | Heater kit selected via dip switches too large per the spec sheet. | Verify electric heat dip switch settings match the installed heater per the spec sheet; verify/repopulate shared data with the correct memory card. |
| 1 Flash — HTR TOO SMALL (Ec) | Electric heat dip switch set smaller than expected. | Same as above, undersized. | Same corrective actions as HTR TOO LARGE. |
| 1 Flash — NO HTR MATCH (Ec) | Electric heat dip switch doesn't match any heater kit in shared data. | Dip switch/shared-data mismatch. | Same corrective actions as HTR TOO LARGE. |
| 5 Flashes — Open fuse (PCBJA101/102) | Open fuse (no thermostat display). | Short in the low voltage wiring. | Replace the fuse with a 3-amp automotive type after finding the short. |
| No flash — INTERNAL FAULT (EE) | No airflow on call; no air handler operation. | Manual disconnect OFF or 24V wire improperly connected/disconnected; blown fuse/breaker; integrated control module internal fault. | Confirm 208/230V and 24V power; check the 3A fuse on the control module, replace if necessary; check for shorts in both circuits; replace the control module if it persists. |
| 9 Flashes — NO NET DATA (d0) | Data not yet on network. | Air handler doesn't contain any shared data. | Populate the shared data set using the memory card. |
| 11 Flashes — INVALID MC DATA (d4) | Invalid memory card data. | Shared data on the card rejected by the control module. | Verify shared data is correct for the specific model, repopulate with the correct memory card. |
| 6 Flashes — MOTOR NOT RUN (b0) | Circulator blower motor not running when it should be. | Loose wiring at motor power leads / disconnected; failed motor. | Tighten/correct wiring; check the motor, replace if necessary. |
| 6 Flashes — MOTOR COMM (b1) | Control module lost comms with the blower motor. | Loose wiring at motor control leads; failed motor; failed control module. | Tighten/correct wiring; check/replace motor; check/replace control module. |
| 6 Flashes — MOTOR MISMATCH (b2) | Blower motor HP in shared data doesn't match the actual motor. | Incorrect motor installed, or incorrect shared data set. | Verify motor type, replace if necessary; verify/repopulate shared data for the specific model. |
| 6 Flashes — MOTOR LIMITS (b3) | Motor operating in a power/temp/speed limiting condition. | Blocked filters, restrictive/undersized ductwork, high ambient temps. | Check/clean filters, check ductwork/registers for obstruction, verify duct sizing, resize/replace if necessary. |
| 6 Flashes — MOTOR TRIPS (b4) | Motor senses loss of rotor control or high current. | Abnormal loading, sudden speed/torque change, sudden blockage at inlet/outlet, high loading, blocked filters, very restrictive ductwork. | Check filters/registers/ductwork/inlet/outlet for blockage; see install instructions for duct requirements. |
| 6 Flashes — MTR LCKD ROTOR (b5) | Motor fails to start 10 consecutive times. | Obstruction in blower housing, seized bearings, failed motor. | Check for obstruction; repair/replace wheel and/or motor if necessary. |
| 6 Flashes — MOTOR VOLTS (b6) | Motor shuts down for over/under voltage or over-temp. | High or low AC line voltage to the blower, high ambient temps. | Check power to the air handler blower; verify line voltage is within nameplate range. |
| 6 Flashes — MOTOR PARAMS (b7) | Motor lacks enough info to operate, or fails to start 40 consecutive times. | Control module error; motor has a locked rotor condition. | Check control module has correct shared data; check for a locked rotor condition. |
| 6 Flashes — LOW ID AIRFLOW (b9) | Airflow lower than demanded. | Blocked filters, restrictive/undersized ductwork. | Check/clean filters; check ductwork blockage/registers/sizing. |
| d1 — Invalid data on network (PCBJA104) | Invalid data on network. | Wrong shared data on the network. | Populate the shared data set using the memory card. |
| EF — Aux Alarm Fault (PCBJA104 only) | Aux switch open. | High water level in the evaporator coil drain pan. | Check overflow pan and service the drain. |

### EEV Cased Coil / EEV Air Handler indoor codes — CAPE(A)*/CHPE*, DV**FEC/DFVE**
R-410A DX6VS/DZ6VS-family EEV indoor units. Control board 2-digit 7-segment display: State (2 sec) → blank (0.5 sec) → Error code if present → Airflow (est. CFM). Cased coil does not display airflow (no blower). Source: Daikin SiUS612209EA/EB.

| Code | Meaning | Cause | Fix |
|---|---|---|---|
| EE | No 24V power to control board; blown fuse/breaker; internal fault | Manual disconnect OFF; no 24V to board; blown F2U fuse or breaker; board internal fault. | Confirm 208/230V and 24V power; check F2U fuse; check for shorts; replace board if necessary. Note: "EE" on the board's own LED display means the unit is in Emergency mode. |
| Eb | “No heater kit” selected but electric heat demand received | No heater kit selected on the thermostat. | Select the valid heater kit on the thermostat. |
| Ed | Heater kit dip switches not set properly | Invalid heater kit dip switch combination. | Set the correct dip switches. |
| E5 | Fuse open | Fuse F1U blown; connector TB10 open. | Check TB10 and the wiring, replace the fuse. |
| EF | Auxiliary switch open | High water level in the evaporator drain pan; alarm device on TB4/TB5 activated; TB4/TB5 left open. | Check the drain pan and the alarm device. If nothing is wired to TB4/TB5, close those terminals. |
| d0 | Data not on network | No shared data on the network. | Populate the shared data set using the memory card. |
| d1 | Invalid data on network | Wrong shared data on the network. | Populate the correct shared data set using the memory card. |
| d4 | Invalid memory card data | Wrong memory card data. | Rewrite the data using the correct memory card, or replace the control board. |
| b0 | Blower motor not running | Fan/motor obstruction; power interruption (low voltage); incorrect/loose wiring. | Check for obstruction; verify input voltage at the motor; check/tighten wiring; replace control board or motor. |
| b1 | Blower motor communication error | Incorrect/loose wiring; power interruption (low voltage). | Check/tighten wiring; verify input voltage at the motor; replace control board or motor. |
| b2 | Blower motor HP mismatch | Incorrect size motor; invalid shared data. | Correct the motor installation; populate the shared data set using the memory card. |
| b3 | Blower motor in power/temp/speed limit | Fan/motor obstruction or blocked filters; power interruption (low voltage); incorrect wiring; ductwork blockage or undersized. | Check for obstruction, clean the filter; verify input voltage; check wiring; replace motor. |
| b4 | Blower motor current trip or lost rotor | Obstruction, abnormal loading, high loading, blocked filters, restrictive ductwork. | Check for obstruction; verify voltage; check filters/ductwork; replace motor if needed. |
| b6 | Over/under voltage trip or over-temp trip | High or low AC line voltage to the blower; high ambient temp. | Verify line voltage; check blower motor condition. |
| b7 | Incomplete parameter sent to motor | Wrong/no shared data; locked motor rotor. | Check control board or motor. |
| b9 | Low indoor airflow (WITHOUT electric heat mode) | Fan/motor obstruction or blocked filters; restrictive or undersized ductwork; indoor motor failure. | Check for obstruction and filter/duct blockage; check motor connections and rotation; verify input voltage; verify duct sizing; replace motor. |
| 70 | EEV disconnection detected | Indoor EEV coil not connected. | Check the indoor EEV coil connection at the control board and junction connector. |
| 73 | Liquid side thermistor abnormality | Open/short circuit of liquid thermistor X5A; reading out of range. | Check thermistor connection and resistance; replace thermistor or control board. |
| 74 | Gas side thermistor abnormality | Open/short circuit of gas thermistor X5A; reading out of range. | Check thermistor connection and resistance; replace thermistor or control board. |
| 75 | Pressure sensor abnormality | Open/short circuit of pressure sensor X15A; reading out of range. | Check pressure sensor connection and resistance; replace sensor or control board. |
| 76 | Comms error with outdoor unit/furnace/modular blower (during operation) | Open communication circuit; incorrect wiring between OD unit, gas furnace or modular blower; no power to the OD unit, gas furnace or modular blower. | Check the wiring between units; check power to the other unit; replace the control board. |
| 77 | Comms error with thermostat (startup & operation) | Incorrect wiring between indoor unit and thermostat; thermostat failure; power interruption (low voltage). | Check thermostat and indoor unit wiring; verify input voltage; press LEARN on the control board for more than 5 sec; replace the control board or thermostat. |
| 78 | Comms error with outdoor unit/furnace/modular blower (during startup) | Open communication circuit; no power to the other unit. | Check wiring between units; check power supply to the other unit. |
| 9b | Low indoor airflow (WITH electric heat mode) | Fan/motor obstruction or blocked filters; restrictive or undersized ductwork; indoor motor failure; wrong outdoor/indoor unit combination. | Check for obstruction and filter/duct blockage; check motor connections and rotation; verify input voltage; verify duct sizing; replace motor. |
