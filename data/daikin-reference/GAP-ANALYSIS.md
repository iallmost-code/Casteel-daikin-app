# Gap analysis — saved reference data vs. the live guide (`index.html` on `main`)

Checked 2026-09-30 against `origin/main` commit `2189744`. Nothing in `index.html` was changed by this check.
Method: every table cell / bullet of 40+ characters in the saved files was searched for, word for word, in the guide's text.

## 1. What already matches (no action)
| Saved file | Result |
|---|---|
| `02-app-fault-codes.md` | **663 / 663** long cells found word for word in the guide |
| `03-app-unit-data.md` | **45 / 45** found |
| `04-app-model-specific-code-tables.md` | **807 / 807** found |
| `05-app-conflicts-catalog-gaps-documents.md` | 74 / 118 found. The 44 "not found" are the source-document **links** — the guide shows them as "source" link labels, so the URL text isn't in the page text. Not a content gap. |
| `01-app-dip-furnace-heatpump-zoning.md` | 97 / 142 found; see section 3 for the 45 that are not |
| AHRI confirmed combos | 215415503 and 216611547 match the guide's AHRI records exactly (outdoor, components, SEER2/EER2/HSPF2, capacity, 25C, catalog p.26). 215488579 came from the AHRI Directory, not the catalog, so it is correctly not in the guide's catalog data. |

The four items an earlier audit listed as missing (comm-bus bias procedure, pressure-switch tests, capacitor testing, terminal maps) **are now in the guide** (`2,652`, `610 PSIG`, `0.61 VDC`, `3–5 minutes` all present).

## 2. Missing from the guide entirely — new data in sections 4–8 (`06`–`10`)
Checked by key terms; "0/N" means none of the N distinctive terms appear in the guide.

**Section 4 (`06`)**
- CHPE / CAPEA-CAPE coil transformer bracket table (Bracket A/B/C by furnace type and width) — 0/5
- CAPE = EEV coil, CAPT = TXV coil; CHP = horizontal only, CAP-prefix = up/downflow only (matters for AHRI matchups) — 0/2
- AMST air handler data: speed-tap wiring (T1–T9), CFM-by-static table, heater minimum-CFM table, temperature-rise tables and formula, mitigation-mode room-area table, UV purifier kits — only 2/9 terms present
- Gas furnace pieces: manifold gas pressure (natural/propane, low/high stage) — 0/5; gas supply/piping capacity, filter sizing, call-for-heat sequence, blower-speed menu (gA1 / FSd), A2L enable/verify menu (A2E / A2u) — 1/11; thermostat wiring diagrams, twinning (in-phase L1 check), humidifier/EAC/ventilation/A2L alarm terminals — 1/5
- DMVT P1400 tables: tap DIP table S1–S6/S12/S13, cooling CFM by tap, electric-heat CFM by kW, minimum-CFM table, humidity/condensate kit numbers, CFM LED — 0/7
- DFVE/DMVE heater-kit mapping per model (First–Seventh valid kit vs kW) and maximum-CFM trim table — 1/6
- Furnace EE-code universal table, DMVE/DFVE code list — present

**Section 6 (`08`)**
- EEM blower replacement steps (AWST/AWSF), high-efficiency motor 230V/24V check, compressor overload reset time (3–4 hours) — mostly missing (1/5, 3/4)

**Section 7 (`09`)**
- Outdoor-unit diagnostic flowchart details: E13 trips above 605 PSIG, E15 below 17 PSIG, E22 above 120°C/248°F, E32 fin 95°C / plate 110°C, E41, E44 cooling/heating limits, E57, E58 — 0/9
- Ed2 system-mismatch airflow-trim limits (DX6VS/DZ6VS*361 with listed indoor units = 10% limit; *601 = 5% limit) — 0/4
- Fault recall and display navigation (how to view and erase the last 6 faults; "88" clears) — 0/4
- Testing capacitor DC voltage safety (10 min wait, 50V or less) — 0/4
- Emergency mode — present

**Section 8 (`10`)**
- AHRI workflow notes and the three confirmed combos — 0 (the AHRI page has the catalog records but none of the workflow notes)

## 3. Saved data that is NOT in the guide from the app-content file (`01`)
- DIP "READ THIS FIRST": photograph/record as-found positions before changing any switch; where setup lives on the 7-segment menu
- **EEV COIL BASICS** (what an EEV is, why Fit uses it, superheat control, no field procedure)
- "AC-only outdoor units": which models share which install manual
- CoreSense hardware context: 2-wire "Comfort Alert" wiring, reading the flash pattern
- Furnace & AC pointer bullets (dual-fuel balance point, legacy-AC wiring)
- **Old UT3000 facts** dropped when GPT replaced them with TB-280 Rev. H (see section 4): IAQ relay, built-in dual fuel, dampers open at idle, 500 mA damper breaker, Molex connector corrosion field note, match-damper-actuators field note, 1–2 min vs 2–4 min recognition time

## 4. Decisions needed before anything is added (conflicts between sources)
1. **UT3000 — old data vs. newer bulletin.** Saved data (TB-241 / Goodman TRC-2): spring-type dampers supported, 400 mA; damper breaker 500 mA; 2–3 zones. Guide (TB-280 Rev. H, 04/09/2026): spring-type dampers NOT compatible; 3 dampers/zone at 26 mA; 100 mA damper breaker; discovery 10–15 min. The guide follows the newer bulletin. Need the actual TB-280 Rev. H and TB-241 to confirm which governs, and whether the two field notes should be kept.
2. **DS-6 heating-emergency High/Low is stated two ways inside the saved data.** Section 7 text (`09`): "S-21 OFF + S-22 ON = Low Heat Level; S-21 ON + S-22 ON = High Heat Level". Section 7 switch-bank table (`09`) and app content (`01`): "OFF/ON = High (8 min on / 8 off), ON/ON = Low (7 min on / 15 off)". These are opposite. Affects heater strips; **check SiUS612209EB pp.32–34 before using either.**
3. **DMVE/DFVE fault code label.** `06` fault table lists `E_b3` as "Low indoor airflow (without electric heat mode)", but its own quick table says `b3` = blower motor power/temp/speed limit and `b9` = low indoor airflow (minor). Likely `E_b9` was mislabeled `E_b3`. Check IO-4039A.
4. **AMST30BU1300 airflow row.** `06` shows identical numbers for T5 and T9 (1185/1165/1125/1115/1070/1060/1015/1010/960). Likely a transcription error in one of them. Check IO-4011B p.13.
5. **Manual revision names differ.** `06` cites IO-2037A for DR92SN/DR96SN/DD96SN; the guide and app content cite IOD-2037B (12/2024). `06` says "11 manuals" but lists 10.
6. **Already documented conflicts** (not new): factory charge 1–2 oz spec sheet vs installation manual, DH7VS 9±1 vs 8±1°F, DH5SE 8 vs 5°F heating superheat, DH4SE 15 vs 16°F, DC5SE tonnage range, DR80TC `E100` vs `E10`, DFVE "(ON DISPLAY)".

## 5. Not checkable here
The manufacturer PDFs themselves are not in the repo, so every value above was checked against the saved data only, not against the original pages. Items 2–4 in section 4 need the PDFs.

## 6. Status — added to `index.html` on the work branch
Added (all generated directly from the saved files, not retyped): 15 Equipment Info cards (cased-coil identification rules, CHPE/CAPEA bracket and wiring, AMST wiring/taps/temperature rise/airflow/room-size, gas-furnace manifold pressure, piping, sequence, blower menu, filters, wiring/twinning, A2L enable/verify, DMVT tables and kits, DFVE/DMVE heater kits and max CFM, EEV basics and model families, blower motor and compressor checks), 4 Diagnostics cards (capacitor DC-voltage safety, big-code trip points and check order, Ed2 trim limits, view/clear last 6 faults), 1 DIP card ("Before you touch any switch").
Deliberately left out pending the PDFs (section 4 above): DS-6 High/Low emergency wording, the DMVE `E_b3` label, the AMST30BU1300 T9 row (shown as "not shown — check p.13"), the old UT3000 facts, and the IO-2037A/B naming.
Upgrades built with it: Start Here page (whole-guide lookup, problem buttons, safety box, glossary), jump-to-card lists, merged duplicate cards, source-line tags removed, plain-language Known Gaps and charge/catalog tables, readable bold text, phone-friendly small tables, AHRI table pre-filled so it shows without JavaScript.
