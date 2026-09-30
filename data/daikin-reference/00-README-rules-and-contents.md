# Daikin / Goodman / Amana / EWC — Complete Field Reference
Compiled 2026-09-30 for Casteel Heating and Air (James Ford). This is the FULL combined Daikin dataset: everything from the HVAC Pro Field Guide app (hvactoolkit.netlify.app) PLUS everything saved separately from manual extraction that hasn't been built into the app yet. Lennox content is intentionally excluded — Daikin/Goodman/Amana/EWC only.

## Rules for using this file
- Every fact here is either (a) sourced to a specific manufacturer document and page/section, or (b) explicitly marked as a field note / not yet verified. Do not state anything as fact that isn't sourced.
- Do not invent, average, interpolate, or "fill in" any spec, fault code, wiring color, or setting not explicitly present below or in a cited manufacturer document.
- If a question isn't answered by this file, say so — don't guess. Point back to the specific manual/doc number for anything that needs to be looked up.
- The unit's own nameplate and the wiring diagram physically on the unit always win over anything in this file — equipment changes revisions over time.
- R-410A and R-32 generations of Daikin equipment are different platforms with different control logic, DIP switch layouts, and fault codes. Always confirm which generation before applying anything below.
- EWC UT3000 zoning is a THIRD-PARTY product (EWC Controls Inc.), not a Daikin product, even though it's commonly paired with Daikin equipment and covered here. Daikin's own zoning system is the DOZP-6-A panel — they are different systems with different wiring, different termination rules, and different bypass-damper requirements. Don't conflate them.

## Contents
1. App content — Furnace & AC, Heat Pump & Air Handler, Zoning (DOZP-6-A + EWC UT3000), DIP Switches (all subtabs as currently live on hvactoolkit.netlify.app)
2. App content — Full fault code tables (all Daikin/Goodman/Amana code groups in the app)
3. App content — Daikin Unit Lookup dataset (specs, charging, codes, conflicts, gaps by model family)
4. Manual extraction — cased coils (CHPE/CAPEA), AMST air handler, gas furnace families, DMVE/DFVE/DMVT air handlers (fault codes, wiring, CFM/DIP tables)
5. Manual extraction — furnace thermostat wiring, gas piping/pressure specs, heater kit DIP tables
6. Manual extraction — CoreSense (3-wire & 2-wire) diagnostics, R-32 A2L PCB codes, ComfortNet DX/DZ 7TC-18TC air handler codes
7. Manual extraction — DX6VS/DZ6VS inverter EEV outdoor unit full E-code table, EEV indoor codes, emergency mode DIP switches
8. AHRI lookup workflow & distributor catalog notes

---

## How this folder is organized (repo note, added when saved)
This reference was pasted into the project chat as one long document on 2026-09-30 and saved here unchanged, split into files by section so each stays a workable size. No content was edited, reordered within a section, or corrected when saving.

| File | What's in it |
|---|---|
| `00-README-rules-and-contents.md` | This file: rules for using the data + contents |
| `01-app-dip-furnace-heatpump-zoning.md` | App content: DIP SWITCHES, FURNACE & AC, HEAT PUMP & AIR HANDLER, ZONING (Daikin DOZP-6-A + EWC UT3000) |
| `02-app-fault-codes.md` | App content: FAULT CODES (general/unitary, ClimateTalk, Fit outdoor, CoreSense, A2L board, ComfortNet, EEV indoor) |
| `03-app-unit-data.md` | App content: UNIT DATA — R-32 outdoor units, air handlers & furnaces |
| `04-app-model-specific-code-tables.md` | App content: MODEL-SPECIFIC CODE TABLES (as printed) |
| `05-app-conflicts-catalog-gaps-documents.md` | App content: where Daikin's documents disagree, catalog vs spec sheet differences, NOT COVERED / GAPS, OFFICIAL DOCUMENTS |
| `06-section4-cased-coils-amst-furnaces-air-handlers.md` | Section 4 manual extraction |
| `07-section5-furnace-wiring-gas-piping-heater-kits.md` | Section 5 manual extraction |
| `08-section6-coresense-a2l-comfortnet.md` | Section 6 manual extraction |
| `09-section7-dx6vs-dz6vs-eev-emergency-mode.md` | Section 7 manual extraction |
| `10-section8-ahri-lookup-workflow.md` | Section 8 AHRI lookup workflow & catalog notes |
