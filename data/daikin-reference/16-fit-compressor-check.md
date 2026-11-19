# FIT OUTDOOR — IS THE COMPRESSOR BAD? STEP-BY-STEP CHECK (DX6VS/DZ6VS, SiUS612209EB)
Compiled 2026-11-19 for Casteel Heating and Air. Source: Daikin service manual SiUS612209EB (sha256 f4a4eebe6161d7c4d33fad3d40fe757bc92f101bd14f61a8d40a03c6789cb8ea, downloaded from https://www.daikinac.com/docs/default-source/dfve/sm-sius612209eb.pdf). Every page number below was read directly off that PDF; the code tables, analysis charts, flowcharts and wiring pages were read from the page images.
Rules: do NOT guess or fill gaps. If a value is not in this file, say so. The unit nameplate and the wiring diagram on the unit always win.
App location: Diagnostics → Faults → "Tests & safety" group, card id `fit-compressor-check`.

---
**Source:** Daikin service manual SiUS612209EB, DX6VS\*\*\*1\*A\* / DZ6VS\*\*\*1\*A\* inverter outdoor units, R-410A (2023). Page numbers are the manual's printed pages. This manual does **not** cover the R-32 Fit units (DC6VS, DH6VS, DC9VS, DH7VS, DH9VS).

#### Read this first

- The Fit compressor has three terminals: **U, V and W**. The outdoor control board drives it, and the inverter on the board takes its position signal from the UVW line (p.20).
- The single-phase C-R / C-S / S-R winding test in the "Compressor overload and winding test" card is **not** for the Fit. It has U/V/W terminals, not C/S/R.
- SiUS612209EB publishes **no** winding resistance (ohms) for U-V / V-W / W-U, **no** resistance value for the OL sensor, and **no** inverter output voltage check. Don't condemn a Fit compressor using a number from another unit's manual.
- E34, E36 and E38 all list "the compressor wire is lost phase" and "faulty control board" as causes (p.46). Check the U/V/W wiring before ordering a compressor.

#### Step 1 — Make it safe (pp.5–6, 20)

1.  Shut down the power and leave the control box for 10 minutes.
2.  Touch the Earth ground terminal to release static from your body. This prevents control board failure.
3.  With a VOM on DC volts, measure the residual voltage between **C+ and C−** at the points shown in the manual: p.5 for the 1.5–3.0 ton board, p.6 for the 3.5–5.0 ton board. Don't touch the charged area until it reads **50 V or less**.
4.  Right after measuring, unplug the outdoor fan motor connector. If wind spins the fan blade, it recharges the capacitor and you can get shocked.

**Terminal venting warning (p.20):** if the insulation that supports a hermetic terminal breaks down from physical abuse or a short between the terminal and the housing, the terminal can be expelled and vent oil and refrigerant. If the terminal cover and gasket aren't in place and secured, that discharge can ignite and spout flames several feet. Turn off all open flame, electrical power and other heat sources before servicing.

#### Step 2 — Pull the code and the fault history at the outdoor board (pp.36–42)

- The outdoor board has a 3-digit display and three buttons: **LEARN, RECALL, TEST**.
- **Screen 0** (default) shows the present fault.
- **Screen 1** (last 6 faults): from Screen 0, hold RECALL for 5 sec. Each press of RECALL steps from the latest to the 6th most recent.
- **Screen 2** (monitoring): from Screen 1, hold RECALL for 5 sec. Press RECALL to change the item number, then TEST to confirm and see the value.
- Press LEARN to go back to Screen 0.
- Code 57 may not show on the thermostat. Check the outdoor unit's error code history (p.47 note).


| Screen 2 item | What it shows (p.42)                                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| 1             | Compressor operation time — unit: hr (multiply by 200)                                                                        |
| 2             | Operation code — 0 Stop, 1 Cooling start-up, 2 Heating start-up (HP), 3 Oil return, 4 Heating (HP), 5 Defrost (HP), 6 Cooling |
| 3             | Compressor Reduction Mode — 0 OFF, 1 ON                                                                                       |
| 4 / 5         | % Demand / Act % demand (unit: %)                                                                                             |
| 9             | Ta outdoor air temp (°F)                                                                                                      |
| 10            | Td outdoor discharge temp (°F)                                                                                                |
| 11            | Tm outdoor coil temp (°F)                                                                                                     |
| 13            | Tl outdoor liquid temp (°F)                                                                                                   |
| 14            | Pressure sensor (PSIG)                                                                                                        |
| 15            | Ts outdoor suction temp (°F)                                                                                                  |


The inverter can stop the compressor or outdoor fan to protect the unit, and it can run the compressor faster than the thermostat calls for to recover oil (p.7). On its own, that isn't a fault.

#### Step 3 — Codes that point at the compressor (pp.45–48)


| T-stat / Board | Meaning                                                                                  | Every cause the manual lists                                                                                                                                                                                                                  | Manual's corrective actions                                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 17 / E17       | Frequent compressor faults                                                               | Stop valve not completely open; faulty outdoor solenoid valve coil; faulty outdoor solenoid valve; compressor wire lost phase; compressor motor failure                                                                                       | Check stop valve is fully open; check solenoid valve coil and valve; check the wire between control board and compressor; inspect compressor motor, replace if necessary          |
| 52 / —         | Same as E17, but the control decided continued operation is acceptable                   | Stop valve not completely open; compressor wire lost phase; compressor motor failure                                                                                                                                                          | Check stop valve; check the wire between control board and compressor; inspect compressor motor, replace if necessary                                                             |
| 22 / E22       | Frequent high discharge temperature faults; discharge thermistor not in correct position | Faulty outdoor solenoid valve coil or valve; discharge thermistor inoperable or improperly connected; discharge thermistor in incorrect position or off; compressor enclosure temperature too high; low charge; overcharge; faulty compressor | Check solenoid valve coil and valve; check discharge thermistor resistance, connections and position; check charge; check the compressor, repair/replace if needed                |
| 55 / —         | Same as E22, continued operation acceptable                                              | Discharge thermistor inoperable/improperly connected or in incorrect position/off; low charge; overcharge; faulty compressor                                                                                                                  | Check discharge thermistor resistance, connections and position; check charge; check the compressor                                                                               |
| 34 / E34       | High current — potential short circuit                                                   | Current spike in supply; stop valve not completely open; compressor wire lost phase; faulty control board; faulty compressor                                                                                                                  | Check supply for in-rush current during start-up or steady state; check stop valve; check the wire between board and compressor; replace board if necessary; check the compressor |
| 35 / E35       | High current                                                                             | Short circuit condition; stop valve not completely open; overcharge; faulty control board; faulty compressor                                                                                                                                  | Check installation clearances; check stop valve; check charge; replace board if necessary; check the compressor                                                                   |
| 36 / E36       | Abnormal condition during start-up                                                       | Faulty outdoor solenoid valve coil or valve; blocked/restricted outdoor coil and/or lines; compressor wire lost phase; inconsistent compressor load; faulty control board                                                                     | Check solenoid valve coil and valve; check and clean outdoor coil/lines; check the wire between board and compressor; replace board if necessary                                  |
| 38 / E38       | Voltage-related issue with the compressor                                                | High or low supply voltage; compressor wire lost phase; faulty control board                                                                                                                                                                  | Correct line voltage (contact the utility if needed); check the wire between board and compressor; replace board if necessary                                                     |
| 40 / E40       | Compressor requirement doesn't match compressor capability                               | Memory card not correct; control board mismatch                                                                                                                                                                                               | Check memory card data against the outdoor model; verify control board size against the outdoor model                                                                             |
| 58 / E58       | Compressor overload protection (OL) sensor opened                                        | OL sensor inoperable; OL sensor (X33A) in incorrect position or off                                                                                                                                                                           | Check OL sensor resistance (no value published); check OL position on the compressor body; check the X33A connection                                                              |


#### Step 4 — Rule out the cheap stuff first

- **Stop valves:** both fully open. This is listed under E17, 52, E34 and E35 (pp.45–47).
- **Outdoor solenoid valve coil (p.21):** unplug its cable from the control board and read across the connector pins. The spec is **1,480–1,820 Ω**. This is listed under E17, E22 and E36.
- **EEV coils (p.21):** unplug the EEV cable from the board. Each pin to COM should read **40–50 Ω**. On the 1.5–3.0 ton outdoor unit, read pins 1-5, 2-5, 3-5 and 4-5 (COM \[+\] gray = pin 5). On the 3.5–5.0 ton outdoor unit and the indoor unit, read 1-6, 2-6, 3-6 and 4-6 (COM \[+\] gray = pin 6). The coil must be clicked onto the valve body, with the protrusion on the coil seated in the dimple on the EEV body (p.52).
- **Line voltage:** E38 / E42 / E43 / E50 are voltage codes (pp.46–47). The D-Checker addendum gives a supply range of **187–253 VAC** (p.134). Go by the rating plate.
- **Discharge thermistor (Td)** for E22/55: unplug it from the board and ohm it against the chart (p.21). Replace it if it's open, shorted or out of range. Selected Td values from the full table on p.72:


| Temp          | Td resistance (kΩ) | Volts DC |
|---------------|--------------------|----------|
| 32°F (0°C)    | 806.47             | 4.77     |
| 68°F (20°C)   | 292.86             | 4.41     |
| 77°F (25°C)   | 231.44             | 4.28     |
| 104°F (40°C)  | 118.68             | 3.76     |
| 140°F (60°C)  | 52.76              | 2.87     |
| 176°F (80°C)  | 25.38              | 1.97     |
| 212°F (100°C) | 13.06              | 1.25     |
| 248°F (120°C) | 7.13               | 0.77     |


#### Step 5 — U/V/W wiring check (pp.20, 55, 84, 89, 91, 98, 102, 119, 122)

- Lead colors at the compressor: **U = Red, V = Yellow, W = Blue**. Each terminal is labeled on top of the compressor (p.20).
- **3.5/4.0 ton and 5.0 ton are wired differently** at the compressor terminals. When reconnecting, match the picture for that tonnage on p.119 (HP) or p.122 (AC).
- On 1.5–3.0 ton units, remove 3 clamps to disconnect the compressor lead wire at the compressor connector (U, V, W) (p.89 HP, p.91 AC).
- On 1.5/2.0 ton units, clamp the compressor lead wires about 20–50 mm (13/16–2 in) from the end of the fan motor lead's protective tube. Make sure the compressor leads aren't under tension (p.84).
- The E41 heating flowchart has a separate check: if the compressor wiring has an open circuit or is on the wrong terminal, fix the wiring (p.55).

#### Step 6 — Insulation / ground test (S-17A p.20, S-17B p.21)

This is the manual's main electrical test for a bad Fit compressor.

1.  If a fuse blew or the breaker tripped, there's an electrical problem to find. The protective device rating must match the nameplate. With the terminal cover in place, you may reset or replace it **ONE TIME ONLY** to see if it was a nuisance trip. If it opens again, **do not keep resetting it**.
2.  Disconnect all power and make sure every power leg is open.
3.  **Leave the terminal cover on.** Disconnect the three leads going to the compressor terminals at the point nearest the compressor.
4.  Set the ohmmeter to R × 10,000, or its highest scale. Check each of the three leads separately to ground, such as an unpainted tube on the compressor.
5.  If a ground shows, carefully remove the terminal cover and look for loose leads or insulation breaks in the lead wires.
6.  If nothing is visible, carefully remove the leads at the compressor terminals. Retest directly from each terminal to ground or unpainted refrigerant piping, and check the U/V/W connections while you're there.
7.  The reading must be **infinity**. If it reads anything other than infinity, there's continuity to ground: the compressor is defective, so replace it.

**Warning (p.21):** pulling the leads off wrong can damage the glass-embedded terminals and cause a terminal and hot-oil discharge.

#### Step 7 — OL (overload) sensor: E58 (pp.48, 58, 98, 102, 117, 120, 123)

- The board detects E58 when the OL switch has no continuity at the start of compressor operation.
- The OL plugs into **X33A** on the outdoor main control board.
- The E58 flowchart, as printed: is the OL connected to the PCB properly? If NO, connect it properly. Is the OL switch opened? If NO, replace the PCB. If YES, replace the OL switch.
- Check the OL's position on the compressor body. The E22 flowchart also lists "OL sensor in incorrect position or off" as a cause (p.52).
- To refit the OL, insert the retainer's lower hooks into the fixture's square holes, then push the upper hooks until they catch.
- No OL resistance value is published.

#### Step 8 — Running test: compressor efficiency (S-104, p.22)

Put gauges on the high and low sides, start the system and run **CHARGE MODE**. If the charge is correct and you see all four of these, the compressor is faulty and gets replaced:

- below-normal high-side pressure
- above-normal low-side pressure
- low temperature difference across the coil
- low compressor amp draw

Analysis charts (pp.12–13): "Compressor failure → Replace compressor" is marked under these symptoms.

- **Cooling** (valid at 67–115°F outdoor / 65–85°F indoor): comp discharge temp \> 200°F; comp discharge temp \< 105°F; comp discharge SH \> 70°F; high pressure \< 255 PSIG; low pressure \> 185 PSIG; repeated stop/start; weak cooling; noise; stop operation.
- **Heating** (valid at 17–62°F outdoor / 65–85°F indoor): comp discharge temp \> 200°F; comp discharge temp \< 105°F; comp discharge SH \> 80°F; comp discharge SH \< 20°F; high pressure SSV \< 270 PSIG; high pressure LSV \< 270 PSIG; repeated stop/start; weak heating; noise; incomplete defrost; stop operation.
- The same symptoms also show up for other causes on the charts (leak, undercharge, ID failure and others). Use them to confirm, not on their own.

#### Step 9 — E22 high discharge temp flowchart (p.52)

- E22 trips when discharge temp is above 120°C (248°F). The first branch asks whether discharge temp is actually higher than that criterion. If YES: **check for a refrigerant leak and check for a compressor fault**.
- If NO, work down this order: discharge thermistor connected to the PCB → thermistor attached to the discharge pipe properly → thermistor characteristic normal → indoor/outdoor EEV coils connected to the PCB → EEV coils attached to the EEV body → EEV coil resistance normal → replace PCB.

#### Step 10 — D-Checker (pp.128–134)

- The cable plugs into **X41A** on the outdoor PCB.
- Check that target discharge temp matches actual. The software can take about 20 minutes to calculate the target. Target higher than actual may mean an overcharge; actual higher than target may mean an undercharge.
- A protection value of 255 means inactive. An active protection doesn't automatically mean a problem.
- Supply should be 187–253 VAC.
- Daikin notes the addendum's values are for instruction only. Use the IO manual for the unit's operating ranges.

#### Step 11 — Confirming a burnout and replacing (S-115 p.23, S-100 p.22, p.4)

- A burnout creates acids and sludge. Recover the refrigerant properly, remove the compressor, and take an oil sample from the gas stub for an **oil acid test**.
- If the oil isn't acidic, either there was no burnout or it's so mild a full cleanup isn't needed.
- If the acid level is unacceptable, clean the system with the **clean-up drier method**. The R-11 flushing method is no longer approved. Don't let sludge or oil touch your skin; it can cause severe burns.
- There is **no pump-down function**. Recover through the service ports on both stop valves (2 locations), or you may not get all the refrigerant out.
- Never open a system that's under vacuum.
- Sweep with dry nitrogen while brazing, and protect the stop valves, EEV and filters with a heat trap or wet rags.
- Finish by replacing the liquid line drier, then evacuate and charge.
- Copper-to-copper joints: Sil-Fos with no flux, about 1400°F. Copper-to-steel joints: silver solder with no flux, about 1200°F.
- The PVE oil in these R-410A compressors absorbs moisture very easily, and that moisture can cause compressor failure. Don't leave the system open to the air any longer than necessary.

#### Not in this manual (don't guess)

- Compressor winding resistance (U-V / V-W / W-U ohms)
- OL sensor resistance
- An inverter output / power module voltage test

Get any of these from Daikin tech support before relying on them.
