# SECTION 8 — AHRI LOOKUP WORKFLOW & DISTRIBUTOR CATALOG NOTES

---
name: daikin-ahri-lookup
description: James's AHRI reference number lookups for Daikin/Goodman equipment combos from his Casteel R32 distributor catalog — workflow, data files, and known gaps.
sources: [chat]
aliases: [ahri lookup, ahri numbers, ahri reference]
---

**DAIKIN/GOODMAN REFERENCE SET — read together for any Daikin/Goodman task (troubleshooting, equipment lookup, AHRI matching for job write-ups):**
- [[daikin-ahri-lookup]] (this file) — AHRI number lookups, combo matching, distributor catalog data/gaps
- [[daikin-goodman-manuals-reference]] — fault codes + wiring diagrams + CFM/dip switch tables for cased coils (CHPE/CAPEA), AMST air handler, all 4 gas furnace families, DMVE/DFVE and DMVT air handlers
- [[daikin-goodman-manuals-reference-2]] — continuation: furnace thermostat wiring, gas piping/pressure specs, DFVE/DMVE heater kit DIP tables
- [[daikin-goodman-manuals-reference-3]] — Amana/Goodman condenser CoreSense diagnostics, R-32 A2L PCB codes, ComfortNet DX/DZ 7TC-18TC air handler diagnostic codes
- [[daikin-goodman-manuals-reference-4]] — DX6VS/DZ6VS inverter EEV outdoor unit full E-code table, EEV cased coil/air handler indoor error codes, emergency mode DIP switch setup
- [[hvac-pro-field-guide-app]] — the toolkit app this data feeds into (hvactoolkit.netlify.app), plus James's own curated Daikin research
For fastest field troubleshooting: check the manuals-reference files first for the exact fault code/wiring/CFM data on the model in hand. For quoting/selling a job: use this AHRI file's combo-matching workflow, cross-checked against the manuals-reference files' exact model specs/dimensions/electrical data to confirm the right SKU before searching ahridirectory.org.

- [stated] has a Casteel Heating and Air Daikin R32 distributor catalog PDF (84 pages, "Daikin R32 Catalog for Casteel Heating and Cooling - 183822", generated 10/03/2025, Daikin-Atlanta territory) covering condensers, heat pumps, furnaces, air handlers, evap coils, packaged units, heat kits, zoning gear, and Casteel's Georgia branch directory
- [stated] wants AHRI reference numbers for specific equipment combos (condenser + furnace/air-handler + coil) pulled reliably, not guessed
- [stated] confirmed working method: paste the exact AHRI Directory search result row (from ahridirectory.org) into chat when a combo isn't in the distributor catalog, and Claude reads/confirms it — this worked for DC6VSS4810A* + CA*EA4830*3A* coil = AHRI 215488579 (13.8 SEER2, 45,000 BTU, Southeast/North region)
- [stated] confirmed combo: DH6VSA2410A* condenser + DFVE24BP1300A* air handler + HKTSN05X1 heat kit = AHRI 215415503 (18.0 SEER2/10.2 EER2/8.5 HSPF2, 23,200 CCAP2, 25C tax credit eligible) — read directly off catalog page 26
- [stated] confirmed combo: DH6VSA3010A* condenser + DFVE36CP1300A* air handler + HKTSN08X1 heat kit = AHRI 216611547 (17.5 SEER2/10.0 EER2/8.5 HSPF2, 28,400 CCAP2, 25C tax credit eligible) — note: his stated model "DFVE30BP1300" does not exist in the catalog table; the actual matched air handler for a 2.5-ton DH6VSA3010 is DFVE36CP1300A* (36 = 3-ton frame, not tied to condenser tonnage digit)
- [stated] has a two-file dataset from this work, both delivered to him: daikin_r32_catalog.json (structured specs: MOCP/MCA/dimensions/line sizes/SEER2/EER2/HSPF2 for every family, real AHRI numbers ONLY on packaged units — DP5HH/DP5HM/DP3HH/DP3HM/DP5GM/DP3GM/GPHM/GPGM — plus heat kit kW tables, accessories, Georgia branch contacts) and the original PDF (Daikin_R32_Catalog_Casteel_10.3.25.pdf)
- [stated] IMPORTANT GAP: the JSON does NOT reliably contain AHRI numbers for split-system combos (condenser+furnace/air-handler+coil) — those numbers exist per EXACT combo row in the source PDF combo tables (pages 11-50), which were extracted condenser-by-condenser without capturing the AHRI column; only packaged units (single-SKU) have real AHRI numbers in the JSON
- [stated] working process going forward: for a split-system AHRI number, either (a) tell Claude the exact condenser + furnace/air-handler combo so it can open the specific catalog page and read the row directly, or (b) paste a raw AHRI Directory search result row and Claude reads/confirms it — do NOT trust the JSON file for split-system AHRI numbers
- [stated] DMVT-R32 air handler (9-tap ECM, e.g. DMVT48CP1300A* = 4-ton, 53-7/16"x21-1/8"x21", MOCP 15) blower tap CFM table was NOT in the distributor catalog — RESOLVED: full DMVT P1400 speed tap/CFM/heater kit tables now saved in [[daikin-goodman-manuals-reference]] (source: official IO-4040B manual, uploaded and extracted in full)
- [stated] wants a dedicated AHRI section/tab eventually in the HVAC Pro Field Guide toolkit app (see [[hvac-pro-field-guide-app]]) once the lookup data is solid
- [stated] the 11 official install/service manuals saved in [[daikin-goodman-manuals-reference]] and [[daikin-goodman-manuals-reference-2]] help with AHRI matching too — even without a printed AHRI number, those manuals nail down exact model spec/dimension/CFM/electrical data per unit (cased coils CHPE/CAPEA-CAPE, two-way coil, AMST air handler, 4 gas furnace families, DMVE/DFVE EEV air handler, DMVT P1400 air handler), which cross-checks or narrows down which exact SKU a combo needs before searching ahridirectory.org — e.g. confirmed CAPE = EEV cased coil vs. CAPT = TXV cased coil, a distinction that matters for matching the right coil to an EEV-equipped condenser/air handler combo
