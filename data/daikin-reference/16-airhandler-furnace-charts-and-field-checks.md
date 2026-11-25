# 16. Air handler / furnace troubleshooting charts and outdoor field checks (added to Error Codes)

Copied as printed from official Daikin / Goodman PDFs. The DFVE and DMVT charts are printed sideways; they were read with the page rotation applied and checked against the page images. The RSD6200301 field checks were checked word for word against the PDF text (75 of 75 pieces matched).

Sources:
- IOD-4054 (DFVE P1300, R-32) pp.22-23: https://cdn.daikincloud.io/PIM/Assets/Documents/IM-IOD-4054%20FINAL%206.20.2024.pdf
- IOD-4053 (DMVT) pp.31-34: https://daikincomfort.com/docs/default-source/dmvt/im-iod-4053.pdf
- RS6612301 (Goodman GR9S92 / GR9S96 / GD9S96 family, May 2024) pp.34-37: https://mobile.goodmanmfg.com/mobileapp/stellent/pdf/infoPdf/Lit/RS6612301.pdf
- RSD6200301 (Daikin SE/SQ service manual) pp.17, 29-31: https://daikincomfort.com/docs/default-source/dc4se/sm-rsd6200301.pdf

## DFVE (208-230V, DFVE***P1300**, R-32) — Troubleshooting Chart (Error Code / PCB LED Display / Description / Possible Causes / Corrective Actions) (Doc IOD-4054 p.22-23)

Source: Daikin IOD-4054, Troubleshooting, pp.22-23 (printed sideways in the manual). Text as printed.

| Error Code | PCB LED Display | Description | Possible Causes | Corrective Actions |
|---|---|---|---|---|
| EE | No display (EE display is EMG mode) | • No power supply to ID blower / no 24 volt power to PCB / • Blown fuse or circuit breaker / • PCB has an internal fault | • Manual disconnect switch OFF / • No power supply to ID blower / no 24 volt power to PCB / • Blown fuse or faulty circuit breaker / • Control board has internal fault | • Assure 208/230 volt and 24 volt power to blower and control board. / • Check fuse F2U on control board / • Check for possible short in 208/230 volt and 24 volt circuits. Repair as necessary. / • Replace the control board. |
| Eb | E_Eb | Selecting "no heater kit" and receiving electric heat demand | • No heater kit selected | • Select the valid heater kit on thermostat / • Valid dip switch selection (heater kit selection out of range of the unit configuration) |
| Ed | E_Ed | Heater Kit dip switches not set properly | • Invalid heater kit selected | • Set correct dip switches |
| E5 | E_E5 | Fuse Open | • Fuse (F1U) is blown / • Connector TB10 is open | • Replace fuse / • Check wiring to AUX alarm, heater kit, communication connection. / • Replace the control board / After recovering the system, E5 will still be displayed on the indoor PCB (about 30 seconds). BLOWN FUSE will still be displayed on the thermostat within 45 seconds. They will be cleared automatically. |
| EF | E_EF | Auxiliary Switch Open | • High water level in the evaporation coil / • The connected alarm device is activated / • Auxiliary Alarm terminals (TB4, TB5) are open | • Check water level in drain pan / • Check alarm device. / • Close Auxiliary terminals TB4 and TB5 if not used / After recovering the system, EF will still be displayed on the indoor PCB (about 30 seconds). AUXILIARY CONTACTS OPEN will still be displayed on the thermostat within 45 seconds. They will be cleared automatically. |
| d0 | E_d0 | Data not on Network | • No shared data on the network | • Populate shared data set using memory card. |
| d1 | E_d1 | Invalid Data on Network | • Wrong shared data on the network | • Populate shared data set using memory card. |
| d4 | E_d4 | Invalid Memory Card Data | • Wrong memory card data | • Replace circuit board / • Rewrite data using the correct memory card |
| b0 | E_b0 | Blower Motor not running | • Fan/motor obstruction / • Power interruption (low voltage) / • Incorrect / loose wiring | • Check for obstruction on the fan/motor / • Verify the input voltage at the motor / • Check wiring or tighten wiring connections if needed / • Replace circuit board or motor |
| b1 | E_b1 | Blower Motor Communication error | • Incorrect / loose wiring / • Power interruption (low voltage) | • Check wiring or tighten wiring connections if needed / • Verify the input voltage at the motor / • Replace circuit board or motor |
| b2 | E_b2 | Blower Motor HP Mismatch | • Incorrect size motor / • Invalid shared data | • Correct motor installation / • Populate shared data set using memory card. |
| b3 | E_b3 | Blower Motor operating in Power, Temp or Speed Limiting conditions | • Fan/motor obstruction or blocked filters / • Power interruption (low voltage) / • Incorrect wiring / • Blockage in the airflow (ductwork) or ductwork undersized | • Check for obstruction on the fan/motor/ductwork, clean filters / • Verify the input voltage at the motor / • Check wiring / • Replace motor |
| b9 | E_b9 | Low Indoor Airflow (without Electric Heat mode) | • Fan/motor obstruction or blocked filters / • Restrictive ductwork or ductwork undersized / • Wiring disconnected / • Wrong outdoor/indoor combination / • ID motor failure | • Check for obstruction on the fan/motor / • Check ductwork/filter for blockage, clean filters / • Remove obstruction. Verify all registers are fully open / • Check the connections and the rotation of the motor / • Verify the input voltage at the motor / • Verify ductwork is appropriately sized for system. Resize/replace ductwork if needed / • Replace motor |
| 9b | E_9b | Low Indoor Airflow (with Electric Heat mode) | • Fan/motor obstruction or blocked filters / • Restrictive ductwork or ductwork undersized / • ID motor failure / • Wiring disconnected | • Check for obstruction on the fan/motor / • Check ductwork/filter for blockage, clean filters / • Remove obstruction. Verify all registers are fully open / • Check the connections and the rotation of the motor / • Verify the input voltage at the motor / • Verify ductwork is appropriately sized for system. Resize/replace ductwork if needed / • Replace motor |
| 70 | E_70 | EEV disconnection detected | • Indoor EEV coil not connected / • Incorrect wiring to EEV | • Check Indoor EEV coil connection (PCB and junction connector) / • Replace EEV coil / • Check the resistance value of EEV coil (refer service manual) / • Replace the control board |
| 73 | E_73 | Liquid side thermistor abnormality | • Open (or) short circuit of the liquid thermistor (X5A) / • Liquid thermistor reading incorrect or values outside the normal range | • Check the connection to liquid thermistor (PCB and junction connector) / • Check the resistance value of the thermistor (refer service manual) / • Replace thermistor / • Replace the control board |
| 74 | E_74 | Gas side thermistor abnormality | • Open (or) short circuit of the gas thermistor (X5A) / • Gas thermistor reading incorrect or values outside the normal range | • Check the connection to gas thermistor (PCB and junction connector) / • Check the resistance value of the thermistor (refer service manual) / • Replace thermistor / • Replace the control board |
| 75 | E_75 | Pressure sensor abnormality | • Open (or) short circuit of the Pressure sensor (X15A) / • Pressure sensor reading incorrect or values outside the normal range | • Check the connection to pressure sensor (PCB and junction connector) / • Check the output voltage of the pressure sensor (refer service manual) / • Replace pressure sensor / • Replace the control board |
| 77 | E_77 | Indoor Unit - Thermostat communication error (start-up & during operation) | • Incorrect wiring between ID unit and thermostat. The system may have the communication error without error code 77 on the indoor PCB. Follow section 17.5 SYSTEM TROUBLESHOOTING / • Thermostat failure / • Power interruption (low voltage) | • Check for thermostat and indoor unit wiring / • Verify the input voltage at the ID unit and thermostat / • Replace control board or thermostat / • Press "LEARN" button on PCB for more than 5 seconds to reestablish network / After recovering the system with power supply, TSTAT ID NO COM will continue to be displayed on the thermostat within 2 minutes. The error code will be cleared automatically. |
| A0 | E_A0 | Refrigerant Leak Alarm | • Refrigerant Leak / • A2L sensor failure | • Ventilate the room before conducting any actions / • Check coil leakage / • Remove refrigerant from system and replace coil |
| AF | E_AF | A2L Sensor Communication Error | • A2L sensor not connected / • Incorrect wiring of A2L sensor | • Check the connection of A2L sensor / • Replace A2L sensor |
| A1 | E_A1 | A2L Sensor Internal Alarm | • A2L sensor failure | • Replace A2L sensor / • Replace control board |

## DMVT — Troubleshooting Chart (Symptoms / 7-Segment LED Codes / Fault Description / ComfortNet™ Thermostat Message / Possible Causes / Corrective Actions / Notes & Cautions) (Doc IOD-4053 p.31-34)

Source: Daikin IOD-4053, 19 Troubleshooting Chart, pp.31-34 (printed sideways in the manual). Text as printed. 7-segment LED code characters alternate. The ComfortNet™ thermostat code column is printed as display characters; the thermostat message is listed here. *“your model” refers to the unit’s Serial & Rating Plate or Specification Sheet.

| Symptoms of Abnormal Operation (Legacy &amp; ComfortNet™ Thermostat) | 7-Segment LED Code | Fault Description | ComfortNet™ Thermostat Message | Possible Causes | Corrective Actions | Notes &amp; Cautions |
|---|---|---|---|---|---|---|
| LED display is ON continuously | ON | Normal operation | None | Normal operation | None | Normal operation |
| Electric heaters fail to energize on a call for W1 or Auxiliary/Emergency heat Integrated control module LED display provides the indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated ComfortNet™ thermostat scrolls “Check Air Handler” message | EC | Heater kit selected via dipswitches is too large for heater kits specified in shared data set | HTR TOO LARGE | Heater kit selected via dipswitches is too large for heater kits in shared data set | Verify electric heat dipswitch settings Verify the installed electric heater is valid for the air handler blower. Check Serial & Rating Plate or Specification Sheet applicable to your model* for allowable heater kit(s). Verify shared data set is correct for the specific model. Re-populate data using correct memory card if required. | Turn power OFF prior to repair. Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Turn power off before removing memory card. |
| Electric heat airflow is higher than expected on a call for W1 or Auxiliary/Emergency heat Integrated control module LED display provides the indicated error code. | EC | Heater kit selected via dipswitches is too small for heater kits specified in shared data set | HTR TOO SMALL | Heater kit selected via dipswitches is too small for heater kits in shared data set | Verify electric heat dipswitch settings Verify the installed electric heater is valid for the air handler blower. Check Serial & Rating Plate or Specification Sheet applicable to your model* for allowable heater kit(s). Verify shared data set is correct for the specific model. Re-populate data using correct memory card if required. | Turn power OFF prior to repair. Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Turn power off before removing memory card. |
| Electric heat airflow is higher than expected on a call for W1 or Auxiliary/Emergency heat Integrated control module LED display provides the indicated error code. | EC | Heater kit selected via dipswitches does not heater kits specified in shared data set | NO HTR MATCH | Heater kit selected via dipswitches is doesn’t match heater kits in shared data set | Verify electric heat dipswitch settings Verify the installed electric heater is valid for the air handler blower. Check Serial & Rating Plate or Specification Sheet applicable to your model* for allowable heater kit(s). Verify shared data set is correct for the specific model. Re-populate data using correct memory card if required. | Turn power OFF prior to repair. Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Turn power off before removing memory card. |
| Integrated control module LED display EF error code. ComfortNet™ thermostat “Call for Service”. | EF | Aux switch open | Aux Alarm Fault | High water level in the evaporation coil. | Check overflow pan and service | Turn power OFF prior to service. |
| Air handler blower fails to operate Integrated control module LED display provides no signal. ComfortNet™ thermostat “Call for Service” icon illuminated ComfortNet™ thermostat scrolls “Check Air Handler” message | No Display | No 208/230 volt power to air handler blower or no 24 volt power to integrated control module Blown fuse or circuit breaker Integrated control module has an internal fault. | INTERNAL FAULT | Manual disconnect switch OFF or 24 volt wire improperly connected or loose Blown fuse or circuit breaker Integrated control module has an internal fault | Assure 208/230 volt and 24 volt power to air handler blower and integrated control module. Check integrated control module fuse (3A). Replace if necessary. Check for possible shorts in 208/230 volt and 24 volt circuits. Repair as necessary. Replace integrated control module. | Turn power OFF prior to repair. Replace integrated control module fuse with 3A automotive fuse. Replace integrated control module with correct replacement part Read precautions in “Electrostatic Discharge” section of manual. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | d0 | Data not yet on network. | NO NET DATA | Air handler blower does not contain any shared data. | Populate shared data set using memory card. | Turn power OFF prior to repair Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Error code will be cleared once data is loaded. Turn power off before removing memory card |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | d1 | Invalid data on network. | INVALID DATA | Air handler blower does not contain an appropriate shared data set. | Populate correct shared data set using memory card. | Turn power OFF prior to repair Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Error code will be cleared once data is loaded. |
| Operation different than expected or no operation. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | d4 | Invalid memory card data. | INVALID MC DATA | Shared data set on memory card has been rejected by integrated control module | Verify shared data set is correct for the specific model. Re-populate data using correct memory card if required. | Turn power OFF prior to repair Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Error code will be cleared once data is loaded. Turn power off before removing memory card |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b0 | Circulator blower motor is not running when it should be running. | MOTOR NOT RUN | Loose wiring connection at circulator motor power leads or circulator motor power leads disconnected. Failed circulator blower motor. | Tighten or correct wiring connection. Check circulator blower motor. Replace if necessary. | Turn power OFF prior to repair Replace circulator motor with correct replacement part. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b1 | Integrated control module has lost communications with circulator blower motor. | MOTOR COMM | Loose wiring connection at circulator motor control leads. Failed circulator blower motor. Failed integrated control module. | Tighten or correct wiring connection. Check circulator blower motor. Replace if necessary. Check integrated control module. Replace if necessary. | Turn power OFF prior to repair Replace circulator motor with correct replacement part. Replace integrated control module with correct replacement part. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b2 | Circulator blower motor horse power in shared data set does not match circulator blower motor horse power. | MOTOR MISMATCH | Incorrect circulator blower motor in air handler blower. Incorrect shared data set in integrated control module. | Verify circulator blower motor horse power is the same specified for the specific air handler blower model. Replace if necessary. Verify shared data set is correct for the specific model. Re-populate data using correct memory card if required. | Turn power OFF prior to repair Replace motor with correct replacement part. Use memory card for the specific model Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded. Error code will be cleared once shared data and motor horse power match. Turn power off before removing memory card |
| Air handler blower operates at reduced performance. Airflow delivered is less than expected. Integrated control module LED display provides b3 error code. | b3 | Circulator blower motor is operating in a power, temperature, or speed limiting condition. | MOTOR LIMITS | Blocked filters. Restrictive ductwork. Undersized ductwork. High ambient temperatures. | Check filters for blockage. Clean filters or remove obstruction. Check ductwork for blockage. Remove obstruction. Verify all registers are fully open. Verify ductwork is appropriately sized for system. Resize/replace ductwork if necessary. See "Installation Instructions" for installation requirements. | Turn power OFF prior to repair. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b4 | Circulator blower motor senses a loss rotor control. Circulator blower motor senses high current. | MOTOR TRIPS | Abnormal motor loading, sudden change in speed or torque, sudden blockage of air handler blower/coil air inlet or outlet. High loading conditions, blocked filters, very restrictive ductwork, blockage of air handler blower/coil air inlet or outlet. | Check filters, filter grills/registers, duct system, and air handler blower/coil air inlet/outlet for blockages. | Turn power OFF prior to repair. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b5 | Circulator blower motor fails to start 10 consecutive times. | MTR LCKD ROTOR | Obstruction in circulator blower housing. Seized circulator blower motor bearings. Failed circulator blower motor. | Check circulator blower for obstructions. Remove and repair/replace wheel/motor if necessary. Check circulator blower motor shaft rotation and motor. Replace motor if necessary. | Turn power OFF prior to repair Replace motor with correct replacement part. Replace wheel with correct replacement part. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b6 | Circulator blower motor shuts down for over or under voltage condition. Circulator blower motor shuts down due to over temperature condition on power module. | MOTOR VOLTS | High AC line voltage to air handler blower. Low AC line voltage to air hander blower. High ambient temperatures. | Check power to air handler blower. Verify line voltage to blower is within the range specified on the air handler blower rating plate. See "Installation Instructions" for installation requirements. | Turn power OFF prior to repair. |
| Air handler blower fails to operate. Integrated control module LED display provides indicated error code. ComfortNet™ thermostat “Call for Service” icon illuminated. ComfortNet™ thermostat scrolls “Check Air Handler” message. | b7 | Circulator blower motor does not have enough information to operate properly. Motor fails to start 40 consecutive times. | MOTOR PARAMS | Error with integrated control module. Motor has a locked rotor condition. | Check integrated control module. Verify control is populated with correct shared data set. See data errors above for details. Check for locked rotor condition (see error code above for details). | Turn power OFF prior to repair. Replace with correct replacement part(s). Use memory card for the specific model. Insert memory card BEFORE turning power ON. Memory card may be removed after data is loaded Turn power off before removing memory card. |
| Air handler blower operates at reduced performance or operates on low stage when high stage is expected. Integrated control module LED display provides indicated error code. | b9 | Airflow is lower than demanded. | LOW ID AIRFLOW | Blocked filters. Restrictive ductwork. Undersized ductwork. | Check filters for blockage. Clean filters or remove obstruction. Check ductwork for blockage. Remove obstruction. Verify all registers are fully open. Verify ductwork is appropriately sized for system. Resize/replace ductwork if necessary. | Turn power OFF prior to repair. |

## GR9S92 / GR9S96 / GD9S96 (also AR9S92 / AR9S96 / AD9S96 / VM9S96 / VC9S96) — 1 Stage Troubleshooting Codes (Symptom / LED Status / Fault Description / Corrective Actions) (Doc RS6612301 p.34-37)

Source: Goodman / Daikin service manual RS6612301 (May 2024), “Service and Troubleshooting GR9S92 / GR9S96 / GD9S96 / AR9S92 / AR9S96 / AD9S96 / VM9S96 / VC9S96 Single Stage Gas Furnaces”, from goodmanmfg.com. Text as printed. The step-by-step troubleshooting flowcharts (90% Heating, E0, E1/E2, Eb/EC) are drawings on pp.38-42; open the manual for those.

| Symptom | LED Status | Fault Description | Corrective Actions |
|---|---|---|---|
| Normal operation | IdL | Normal operation | None |
| Furnace fails to operate | EE0 | Furnace lockout due to an excessive number of ignition “retries” (3 total) Failure to establish flame Loss of flame after establishment | Locate and correct gas interruption / Check front cover pressure switch operation and verify proper drainage (hose, wiring, contact operation), correct if necessary / Replace or realign igniter / Check flame sense signal, clean sensor if coated or oxidized / Check flue piping for blockage, proper length, elbows, and termination / Verify proper induced draft blower performance |
| Furnace fails to operate | EE1 | Pressure switch circuit is closed at start of heating cycle / Pressure switch contacts sticking / Short in pressure switch circuit wiring | Replace low stage pressure switch Repair short in wiring |
| Induced draft blower runs continuously with no furnace operation | EE2 | Pressure switch circuit is not closed / Pressure switch hose blocked pinched, or connected improperly / Blocked flue and/or inlet air pipe, blocked drain system or weak induced draft blower / Incorrect pressure switch set point or malfunctioning switch contacts / Loose or improperly connected wiring | Inspect pressure switch hose, repair/replace if necessary / Inspect flue and/or inlet air piping for blockage, proper length, elbows, and termination / Check drain system, correct as necessary / Check induced draft blower performance, correct as necessary / Check pressure switch operation, replace as needed / Tighten or correct wiring connection |
| Circulator blower runs continuously No furnace operation | EE3 | Primary limit circuit is open / Insufficient conditioned air over the heat exchanger / Blocked filters, restrictive ductwork, improper circulator blower speed, or failed circulator blower motor / Loose or improperly connected wiring in high limit circuit | Check filters and ductwork for blockage Clean filters or remove obstruction / Check circulator blower speed and performance / Correct speed or replace blower motor if necessary / Tighten or correct wiring connection |
| Induced draft blower and circulator blower runs continuously No furnace operation | EE4 | Flame sensed with no call for heat / Short to ground in flame sense circuit / Lingering burner flame Slow closing gas valve | Correct short at flame sensor or in flame sensor wiring / Check for lingering or lazy flame Verify proper operation of gas valve |
| No furnace operation | EE5 | Open fuse / Short in low voltage wiring | Replace fuse / Locate and correct short in low voltage wiring |
| Normal furnace operation | EE6 | Flame sense micro amp signal is minimal / Flame sensor is coated/oxidized / Flame sensor incorrectly positioned in burner fame / Lazy burner flame due to improper gas pressure or combustion air | Clean flame sensor if coated or oxidized Inspect for proper flame sensor alignment / Check inlet air piping for blockage, proper length, elbows, and termination / Compare current gas pressure to rating plate and adjust as needed |
| Furnace fails to operate | EEL | Problem with igniter circuit / Improperly connected or shorted igniter / Poor unit ground / Igniter relay fault on integrated control module | Check and correct wiring from integrated control module to igniter / Diagnose and replace shorted igniter as needed Verify and correct unit ground wiring if needed / Check igniter output from control, replace if necessary |
| Furnace fails to operate | EEA | Polarity of 115 volt AC is reversed / Poor unit ground | Correct polarity, check and correct wiring if necessary / Verify proper ground, correct if necessary |
| Furnace fails to operate | EEb | Gas valve is not energized when it should be / External Gas Valve Error | Check wiring in gas valve circuit / Replace integrated control board |
| Furnace fails to operate | EEC | Gas valve is energized when it should not be / Internal gas valve error | Check wiring in gas valve circuit / Replace integrated control board |
| Furnace fails to operate. / Integrated control module LED display provides no signal | None | No 115 power to furnace or no 24 volt power to integrated control module. / Blown fuse or tripped circuit breaker / Integrated control module is non- functional | Restore high voltage power to furnace and integrated control module. / Correct condition which caused fuse to open, replace fuse / Replace non-functional integrated control module. |
| Furnace fails to operate | E10 | Grounding fault Poor neutral connection | Verify neutral wire connection to furnace & continuity to ground source |
| Furnace fails to operate | E11 | Open roll out switch | Check for correct gas pressure Check for correct burner alignment Check for and correct burner restriction |
| Furnace fails to operate | EEn | Ignitor Open | Check for Ignitor wiring. Replace Damaged Ignitor |
| Furnace fails to operate | EEJ | Inducer relay Error | Replace integrated control board |
| Twinning feature not working | EEH | TWIN Error | Check for wiring connections. Replace integrated control board |
| Furnace fails to operate | EEE | Internal Faults or IRQ Loss in Control Board | Replace integrated control board |
| Furnace fails to operate and goes to hard lockout | EbL | Main blower motor is consuming very little current after heat on delay, below an expected value | Check for loose motor wiring connections. Verify if the blower motor is burnt, replace blower motor if found burnt |
| Furnace fails to operate and goes to hard lockout | EbU | Main blower motor is consuming too much current during inducer pre-purge, above an expected value. | Verify wiring connections to and from motor are not loose. Verify that line voltage wires to the control and the main blower motor are not reversed at the control. |
| Furnace stops heating and only the fan is operating | EAF | Furnace has lost communication with the R- 32 sensor and the furnace is in mitigation mode. | Furnace may not be paired with an R-32 cooling unit. Refer to the R-32 Information Section Verify wire connection to R-32 sensor is not loose. Verify that the R-32 sensor wire is not damaged. Replace R-32 Sensor. |
| Furnace stops heating and only the fan is operating | EAL | R-32 sensor has detected a refrigerant leak and furnace is in mitigation mode. | Investigate the indoor coil for a refrigerant leak. Furnace will resume normal operation once a leak is not detected and the 5 minute delay period is over. |
| Furnace stops heating and only the fan is operating | EAS | R-32 sensor has detected a fault and the furnace is in mitigation mode. | Investigate the R-32 sensor. Replace the R-32 sensor. |
| Furnace stops heating and only the fan is operating | Ear | A2L relay in the furnace control board has detected a fault and the furnace is in mitigation mode. | Investigate A2L relay. Cycle power on the furnace. Replace integrated control board. |

To View & Clear Fault Codes (p.36)
Press either the Left or Right switch until L 6 F is displayed.
Press the center switch to view stored faults.
Press and hold the center switch for 5 to 30 seconds.
All stored faults will be erased, and the display will flash - - - three times and return to L 6 F.

1 Stage Status Codes — menu (p.34)

| Menu Description | LED Display — Main Menu | LED Display — Option Menu | Notes |
|---|---|---|---|
| Active Alarm menu | Err | Exx | ( xx: code numbers ) |
| Last 10 Faults | F10 | Exx | ( xx: code numbers ) |
| Code Release Number | Cr | CR Number |  |
| Reset to Factory Default | rFd | yes, no |  |
| Blower Speed for Continuous Fan Mode | FSd | Fxx | ( xx: Blower Speed Number F01, F02.. ) |
| Blower Speed for 1st Stage Compressor Mode | AC1 | Fxx | ( xx: Blower Speed Number F01, F02.. ) |
| Blower Speed for 2nd Stage Compressor Mode | AC2 | Fxx | ( xx: Blower Speed Number F01, F02.. ) |
| Cool On Delay | Cnd | Delay, Seconds | Default set at 7 Secs, Adjustments can be made in 7 Secs increments from 0 to 35 Secs |
| Cool Off Delay | Cf d | Delay, Seconds | Default set at 65 Secs, Adjustments can be made in 5 Secs increments from 0 to 120 Secs |
| Blower Speed for Gas Heat Mode | gAF | Fxx | ( xx: Blower Speed Number F01, F02.. ) |
| Gas Heat On Delay | gnd | Delay, Seconds | Default set at 30 Secs, Adjustments can be made in 5 Secs increments from 5 to 30 Secs |
| Gas heat Off Delay | gFd | Delay, Seconds | Default set at 90 Secs, Adjustments can be made in 30 Secs increments from 30 to 180 Secs |
| Automatic Heat Staging - For Two Stage Control | AHS | no, 10, 20, 30, 60, AUt | Refer to Section " CHANGING HEATING MODE SETTING" |
| A2L Function Verification | A2u | yes, no | Refer to the R-32 Information Section |
| A2L Function Enabled | A2E | yes, no | Refer to the R-32 Information Section |

## REVERSING VALVE — ELECTRICAL, PRESSURE & TEMPERATURE TESTS (Doc RSD6200301 p.30-31)

Source: Daikin RSD6200301 (service manual linked on the DC4SE, DC5SE, DH4SE and DH5SE product pages), p.30-31. Text as printed.

Reversing valve used in heat pumps could potentially leak internally. Discharge gases can leak into the suction inside the valve. Compound gages will give the same symptoms as bad compressor valves or broken scroll flanks. The temperature between true suction and the suction line after the valve should not be greater than 4 degrees. Note: The center tube is always the suction line and should be cold.

Troubleshooting the Reversing Valve for Electrical Failure

1. Place unit into the cooling mode. Test for 24 volts at the solenoid. If there is no voltage present at coil, check the control voltage.
2. If voltage is present, loosen the nut on the top of the coil. Remove the coil, there should be slight resistance.
3. If the slight resistance is felt, remove the coil. As you remove the coil listen carefully, an audible click should be detected. The clicking is due to the movement of the pilot valve plunger. The absence of a clicking sound indicates the plunger is stuck.

Troubleshooting Mechanical Failures on a Reversing Valve by Pressure

1. Troubleshooting the reversing valve can be done by pressure and touch.
2. Raise the head pressure. In the cooling mode block the fan exhaust. Once head pressure has been raised, cycle between cooling and heating and see if the piston can be freed.

Troubleshooting Mechanical Failures on a Reversing Valve by Temperature

1. When operating properly the valve contains refrigerant gases at certain temperatures.
2. The discharge line should be the same temperature after the valves discharge line.
3. The true suction should be the same as the suction line after the valve. If there is a 4-degree difference, valve is leaking

When stuck in the mid-position, part of the discharge gas from the compressor is directed back to the suction side, resulting in excessively high suction pressure. An increase in the suction line temperature through the reversing valve can also be measured. Check operation of the valve by starting the system and switching the operation from COOLING to HEATING cycle.

If the valve fails to change its position, test the voltage (24V) at the valve coil terminals, while the system is on the COOLING cycle.

All heat pumps and communicating heat pumps wired in legacy - If no voltage is registered at the coil terminals, check the operation of the thermostat and the continuity of the connecting wiring from the “O” terminal of the thermostat to the unit.

If voltage is registered at the coil, tap the valve body lightly while switching the system from HEATING to COOLING, etc. If this fails to cause the valve to switch positions, remove the coil connector cap and test the continuity of the reversing valve solenoid coil. If the coil does not test continuous - replace it.

If the coil test continuous and 24 volts is present at the coil terminals, the valve is inoperative - replace it.

## DEFROST CONTROL & DEFROST THERMOSTAT TEST (Doc RSD6200301 p.31)

Source: Daikin RSD6200301 (service manual linked on the DC4SE, DC5SE, DH4SE and DH5SE product pages), p.31. Text as printed.

Testing Defrost Control

To check the defrost control for proper sequencing, proceed as follows: With power ON; unit not running.

1. Jumper defrost thermostat by placing a jumper wire across the terminals “DFT” and “R”/”R-DFT” at defrost control board.
2. Remove jumper from timer pins and jump across test pins on defrost control board. NOTE: Do not use screwdriver or field supplied jumper to test the control.
3. Set thermostat to call for heating. System should go into defrost within 21 seconds
4. Immediately remove jumper from test pins.
5. Using VOM check for voltage across terminals “C & O”. Meter should read 24 volts.
6. Using VOM check for voltage across fan terminals DF1 and DF2 on the board. You should read line voltage (208-230 VAC) indicating the relay is open in the defrost mode.
7. Using VOM check for voltage across “W”/”W2” & “C” terminals on the board. You should read 24 volts.
8. If not as above, replace control board.
9. Set thermostat to off position and disconnect power. Remove jumper from defrost thermostat and replace timer jumper to the desired defrost time.

NOTE: Remove jumper across defrost thermostat before returning system to service.

Testing Defrost Thermostat

1. Install a thermocouple type temperature test lead on the tube adjacent to the defrost control. Insulate the lead point of contact.
2. Check the temperature at which the control closes its contacts by lowering the temperature of the control. Part # 0130M00009P which is used on 2 and 2.5 ton units should close at 34°F ± 5°F. Part # 0130M00001P or B1370803 which is used on 3 thru 5 ton units should close at 31°F ± 3°F.
3. Check the temperature at which the control closes its contacts by lowering the temperature of the control. Part # 0130M00085, which is used on units with 5 mm coils, should close at 30°F ± 5°F.

## TWO-STAGE COMPRESSOR UNLOADER TEST (Doc RSD6200301 p.29-30)

Source: Daikin RSD6200301 (service manual linked on the DC4SE, DC5SE, DH4SE and DH5SE product pages), p.29-30. Text as printed.

Unloader Test Procedure (2 Stage Compressors Only)

A nominal 24-volt direct current coil activates the compressor internal unloader solenoid. The input control circuit voltage must be 18 to 28 volt ac (remove). The coil power requirement is 5 VA. The external electrical connection is made with a molded plug assembly. This plug contains a full wave rectifier to supply direct current to the unloader coil. The measured DC voltage at the connectors in the plug should be 15 to 27 volt dc.

If it is suspected that the unloader is not working, the following methods may be used to verify operation.

1. Operate the system and measure compressor amperage. Cycle the unloader ON and OFF at 10 second intervals. The compressor amperage should increase when switching from part-load to full-load and decrease when switching from full-load to part-load. The percent change depends on the operating conditions and voltage, but should be at least 25 percent.
2. If step one does not give the expected results, shut unit off. Apply 18 to 28 volt ac to the unloader molded plug leads and listen for a click as the solenoid pulls in. Remove power and listen for another click as the unloader returns to its original position.
3. If clicks can’t be heard, shut off power to the unit and remove the control circuit molded plug from the compressor and measure the unloader coil resistance (connections on the compressor). The solenoid coil should have continuity and not be grounded or have infinite resistance. If the coil resistance is infinite, zero, or grounded, the compressor must be replaced.
4. Next check the molded plug.
   a. Voltage check: Apply control voltage to the plug wires (18 to 28 volt ac). The measured dc voltage at the female connectors in the plug should be around 15 to 27 vdc.
   b. Resistance check: Measure the resistance from the end of one molded plug lead to either of the two female connectors in the plug. One of the connectors should read close to zero ohms while the other should read infinity. Repeat with other wire. The same female connector as before should read zero while the other connector again reads infinity. Reverse polarity on the ohmmeter leads and repeat. The female connector that read infinity previously should now read close to zero ohms.

Replace plug if either of these test methods doesn’t show the desired results.

## COMPRESSOR GROUND TEST, OPERATION TEST, CRANKCASE HEATER & FAN RELAY (Doc RSD6200301 p.17, 29-30)

Source: Daikin RSD6200301 (service manual linked on the DC4SE, DC5SE, DH4SE and DH5SE product pages), p.17, 29-30. Text as printed.

Ground Test (p.29)

If fuse, circuit breaker, ground fault protective device, etc., has tripped, this is a strong indication that an electrical problem exists and must be found and corrected. The circuit protective device rating must be checked, and its maximum rating should coincide with that marked on the equipment nameplate.

With the terminal protective cover in place, it is acceptable to replace the fuse or reset the circuit breaker ONE TIME ONLY to see if it was just a nuisance opening. If it opens again, DO NOT continue to reset.

Disconnect all power to unit, making sure that all power legs are open.

1. DO NOT remove protective terminal cover. Disconnect the three leads going to the compressor terminals at the nearest point to the compressor.
2. Identify the leads and using an ohmmeter on the R x 10,000 scale or the highest resistance scale on your ohmmeter check the resistance between each of the three leads separately to ground (such as an unpainted tube on the compressor).
3. If a ground is indicated, then carefully remove the compressor terminal protective cover and inspect for loose leads or insulation breaks in the lead wires.
4. If no visual problems indicated, carefully remove the leads at the compressor terminals.
5. Carefully retest for ground, directly between compressor terminals and ground.
6. If ground is indicated, replace the compressor. The resistance reading should be infinity. If there is any reading on meter, there is some continuity to ground and compressor should be considered defective.

WARNING: Damage can occur to the glass embedded terminals if the leads are not properly removed. This can result in terminal and hot oil discharging.

Operation Test (p.30)

If the voltage, capacitor, overload and motor winding test fail to show the cause for failure:

1. Remove unit wiring from disconnect switch and wire a test cord to the disconnect switch. NOTE: The wire size of the test cord must equal the line wire size and the fuse must be of the proper size and type.
2. With the protective terminal cover in place, use the three leads to the compressor terminals that were disconnected at the nearest point to the compressor and connect the common, start and run clips to the respective leads.
3. Connect good capacitors of the right MFD and voltage rating into the circuit as shown.
4. With power ON, close the switch.
   • If the compressor starts and continues to run, the cause for failure is somewhere else in the system.
   • If the compressor fails to start - replace.

Testing Crankcase Heater (Optional Item) (p.30)

The crankcase heater must be energized a minimum of four (4) hours before the condensing unit is operated.

Crankcase heaters are used to prevent migration or accumulation of refrigerant in the compressor crankcase during the off cycles and prevents liquid slugging or oil pumping on start up.

A crankcase heater will not prevent compressor damage due to a floodback or over charge condition.

1. Disconnect the heater lead in wires.
2. Using an ohmmeter, check heater continuity - should test continuous. If not, replace.

NOTE: The positive temperature coefficient crankcase heater is a 40 watt 265 voltage heater. The cool resistance of the heater will be approximately 1800 ohms. The resistance will become greater as the temperature of the compressor shell increases.

Checking Fan Relay Contacts (p.17)

1. Disconnect wire leads from terminals 2 and 4 of Fan Relay Cooling and 2 and 4, 5 and 6 of Fan Relay Heating.
2. Using an ohmmeter, test between 2 and 4 - should read open. Test between 5 and 6 - should read continuous.
3. With power ON, energize the relays.
4. Using an ohmmeter, test between 2 and 4 - should read continuous. Test between 5 and 6 - should read open.
5. If not as above, replace the relay.
