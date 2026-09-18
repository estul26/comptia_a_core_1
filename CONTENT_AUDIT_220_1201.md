# CompTIA A+ Core 1 (220-1201) Content Audit

Original audit baseline: `main` at `4ab72092ded84d68c00f345a8c77c9b664077113`.

Recheck baseline: `main` at `535be58ad1714264972cdc696e1e39dc7243f1a5` (2026-09-17).

Reference baseline: **CompTIA A+ Core 1 (220-1201) V15 — Exam Objectives Document Version 4.0**.


## Recheck summary — 2026-09-17

The original TODO list was re-run against the current learner-facing `index.html` after PRs #3–#17.

- **All Critical, High and Medium technical/coverage findings are resolved.**
- Known stale bad claims were searched again; the learner-facing content no longer contains the audited Wi-Fi expansion, USB-parallel, private-cloud outage guarantee, higher-wattage charger damage, Intel/AMD socket shortcut, or oversized-PSU inefficiency claims.
- Objective 3.2 was manually rechecked after exact-marker false negatives: USB is correctly described as **serial**, and blue USB 3.x coloring is correctly described as a **non-universal visual convention**.
- Three **Low / scope-labeling** cleanups remain:
  1. label SNMP 161/162 explicitly **Supplemental** in Objective 2.1 (the lesson already says it is not directly tested in this objective);
  2. label USB 1.0/1.x **Supplemental/Legacy** in Objective 3.2;
  3. label MiniSD/xD and similar uncommon removable formats **Legacy/Supplemental** in Objective 3.4.

## Audit goal

The original English transcript under `source/` should remain an immutable source artifact. The learner-facing English/Uyghur study content should instead prioritize:

1. current 220-1201 objective coverage;
2. technical correctness;
3. clear beginner-friendly explanations;
4. English/Uyghur semantic alignment;
5. explicit `Exam Note` / `Supplemental` labels when information is added beyond the transcript or retained beyond the current objective list.

## Severity definitions

- **Critical** — can directly teach a wrong answer or omit a memorization fact explicitly required by the current objective.
- **High** — clear current-objective coverage gap or materially misleading technical statement.
- **Medium** — useful exam-completeness/precision improvement; learner could otherwise form an incomplete mental model.
- **Low** — wording, scope labeling, or optional supplemental cleanup.

## 27-objective coverage matrix

| Objective | Status | Review result |
|---|---|---|
| 1.1 Mobile device hardware | PASS | Current audit covers all v4.0 bullets, including battery, keyboard, RAM, storage, wireless cards, privacy/security, antenna placement, camera and microphone. |
| 1.2 Mobile accessories/connectivity | PASS | Add **track point / pointing stick** coverage. Current review covers trackpad/drawing pad but does not document the official `track points` bullet. |
| 1.3 Mobile connectivity/support | PASS | Current audit covers cellular/Wi-Fi/hotspot/SIM/eSIM, Bluetooth workflow, location, MDM and synchronization. |
| 2.1 TCP/UDP ports/protocols | PASS* | Add **IMAP 143** and complete **NetBIOS/NetBT 137–139** (including 138). Current learner content intentionally follows transcript omissions. Mark SNMP 161/162 supplemental because it is not in the v4.0 2.1 port list. |
| 2.2 Wireless technologies | PASS | Coverage is strong, but remove/correct the transcript claim that Wi-Fi is short for `wireless fidelity`; keep IEEE 802.11 terminology. |
| 2.3 Networked-host services | PASS | DNS, DHCP, file/print/mail/syslog/web, AAA, DB, NTP, appliances, SCADA and IoT are covered. |
| 2.4 Network configuration concepts | PASS | Add the missing **CNAME (Canonical Name)** DNS record. Current review explicitly lists A/AAAA/MX/TXT/DKIM/SPF/DMARC but not CNAME. |
| 2.5 Networking hardware | PASS | Current audit covers routers, switches, APs, patch panel, firewall, PoE, cable/DSL/ONT and NIC/MAC. |
| 2.6 SOHO wired/wireless configuration | PASS | Add the three private IPv4 ranges as a concise exam note: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. The transcript references a visual list but the text omits it. |
| 2.7 Internet/network types | PASS | Current audit maps to satellite/fiber/cable/DSL/cellular/WISP and LAN/WAN/PAN/MAN/SAN/WLAN. |
| 2.8 Networking tools | PASS | Tool list is complete. Tighten the cable-tester wording so basic testers are not presented as universally providing certification-grade attenuation/noise/performance measurements. |
| 3.1 Displays | PASS | LCD/IPS/TN/VA/OLED/Mini-LED, digitizer/inverter and all four display attributes are covered. |
| 3.2 Cables/connectors | PASS* | Add **direct-burial cable** and **adapters**. Correct USB-vs-parallel wording. Normalize Ethernet names (`100BASE-TX`, `1000BASE-T`, `10GBASE-T`). |
| 3.3 RAM | PASS | Make **ECC vs non-ECC** an explicit comparison. Use **MT/s** for DDR effective data rate (with a short note that MHz is commonly but imprecisely used in marketing/conversation). |
| 3.4 Storage | PASS* | Objective coverage is complete. Add minimum-drive memory notes for RAID 6 (4) and RAID 10 (4); label as exam-support detail rather than pretending it came from the transcript. |
| 3.5 Motherboards/CPUs/add-on cards | PASS | Remove the broad `Intel=LGA / AMD=PGA` teaching rule. Teach that socket type depends on platform/generation; modern AMD AM5 is LGA. |
| 3.6 Power supplies | PASS | Align input wording to current objective ranges: **110–120 VAC vs 220–240 VAC**. Keep UPS content only if clearly labeled supplemental because UPS is not listed under v4.0 Objective 3.6. Reword the claim that an oversized PSU is inherently inefficient. |
| 3.7 MFDs/printers/settings | PASS | Add **proper unboxing and setup-location considerations**, an explicit v4.0 bullet missing from the documented source structure. Other driver/connectivity/settings/security bullets are well covered. |
| 3.8 Printer maintenance | PASS | Laser, inkjet, thermal and impact maintenance map well to v4.0. |
| 4.1 Virtualization | PASS | Explicitly frame **security, network and storage** as VM requirements, not only as configuration/resource topics. Other VM/VDI/container/hypervisor content is strong. |
| 4.2 Cloud | PASS | Keep the cloud-model/service coverage, but correct the implication that a private cloud generally stays accessible during a local Internet outage; availability depends on where it is hosted and the network path. |
| 5.1 Motherboard/RAM/CPU/power troubleshooting | PASS | Current symptom set maps to v4.0. |
| 5.2 Drive/RAID troubleshooting | PASS | Current symptom set maps to v4.0. Keep IOPS calculations supplemental; the objective tests low-IOPS symptoms, not a calculation formula. |
| 5.3 Video/projector/display troubleshooting | PASS | Current symptom set maps to v4.0. |
| 5.4 Mobile-device troubleshooting | PASS | Reword the claim that using a higher-power charger inherently damages the battery. Modern charging commonly negotiates supported voltage/current; focus on incompatible/damaged/noncompliant chargers and manufacturer guidance. |
| 5.5 Network troubleshooting | PASS | Current symptom set maps to v4.0. |
| 5.6 Printer troubleshooting | PASS | Current symptom set maps to v4.0. Toner-not-fusing can remain explicitly supplemental. |

`PASS*` = technical/exam issue resolved; only low-priority scope labeling remains.

## Priority TODO

### Critical

- [x] **2.1 — Add IMAP port 143.**
- [x] **2.1 — Add NetBIOS/NetBT UDP 138 so the study set covers 137–139.**
- [x] **3.2 — Correct the statement that USB uses parallel transmission.** Learner-facing content now explicitly says USB is serial and is not an example of parallel transmission.

### High

- [x] **2.4 — Add CNAME / Canonical Name DNS record.**
- [x] **3.2 — Add direct-burial cable.**
- [x] **3.2 — Add adapters as an explicit cable/connectivity concept.**
- [x] **3.7 — Add unboxing and setup-location considerations.**
- [x] **3.5 — Replace Intel=LGA / AMD=PGA as a general rule.** Teach socket compatibility by platform/generation.
- [x] **2.2 — Correct `Wi-Fi = wireless fidelity`.** Do not teach this as the expansion of Wi-Fi.

### Medium

- [x] **1.2 — Add track point / pointing-stick input device.**
- [x] **2.6 — Add RFC1918 private IPv4 ranges as an Exam Note.**
- [x] **2.8 — Narrow cable-tester capability claims.** Distinguish a basic continuity/wiremap tester from higher-end qualification/certification instruments.
- [x] **3.2 — Normalize Ethernet standard names:** `100BASE-TX`, `1000BASE-T`, `10GBASE-T`.
- [x] **3.2 — Avoid saying USB 3.x connectors are always blue.** Color is a common convention, not a reliable universal identifier.
- [x] **3.3 — Add explicit ECC vs non-ECC comparison.**
- [x] **3.3 — Correct DDR rate terminology to MT/s where discussing effective transfer rate.**
- [x] **3.4 — Add RAID 6 and RAID 10 minimum-drive memory notes.**
- [x] **3.6 — Use `110–120 VAC` and `220–240 VAC` to mirror the current objective.**
- [x] **3.6 — Reword oversized-PSU efficiency guidance.** Capacity alone does not determine efficiency.
- [x] **4.1 — Add explicit VM requirements summary: security, network, storage.**
- [x] **4.2 — Qualify private-cloud outage behavior as architecture-dependent.**
- [x] **5.4 — Correct higher-power-charger wording; focus on compatibility/negotiation and manufacturer specifications.**

### Low / scope labeling

- [ ] **2.1 — Mark SNMP 161/162 supplemental** rather than part of the current v4.0 2.1 memorization list.
- [ ] **3.2 — Mark USB 1.x material supplemental** because the current objective explicitly calls out USB 2.0 and USB 3.0.
- [x] **3.6 — Mark UPS material supplemental** under the current v4.0 Objective 3.6.
- [x] **3.7 — Mark 3D-printer discussion supplemental** if retained in this objective.
- [ ] **3.4 — Consider labeling uncommon legacy removable formats (for example xD/MiniSD) as supplemental/legacy** so they do not receive the same study emphasis as current objective bullets.

## Content policy for fixes

For every fix:

- Preserve `source/comptia_a_core_1_English.txt` unchanged.
- Correct the learner-facing English study text.
- Apply the same corrected meaning to the learner-facing Uyghur text.
- If the fact is required by 220-1201 but absent from the transcript, add it as an **Exam Note** rather than pretending it was in the source.
- If useful material is outside the current v4.0 objective, retain it only when helpful and label it **Supplemental** / **Legacy**.
- Update the corresponding `OBJECTIVE_*_REVIEW.md`, `TRANSCRIPT_CORRECTIONS.md` or audit documentation where appropriate.
- Do not rewrite unrelated prose while fixing one checklist item.

## Recommended implementation order

1. Objective **2.1** — ports/protocols.
2. Objective **3.2** — cables/connectors and USB/Ethernet corrections.
3. Objective **2.4** — CNAME.
4. Objective **3.5** — CPU socket generalization.
5. Objective **3.7** — printer setup location.
6. Objective **2.2** — Wi-Fi terminology.
7. Objective **3.3** — ECC/non-ECC and MT/s.
8. Objective **2.6** — private IPv4 ranges.
9. Objective **5.4** — charger wording.
10. Remaining medium/low scope and precision items.

## Definition of done

The content audit is complete when:

- all 27 v4.0 objectives are represented in the learner-facing material;
- no known source/transcription statement remains learner-facing when it is materially false or misleading;
- additions not present in the transcript are clearly identified as Exam Notes;
- supplemental/legacy content is clearly distinguished from current objective requirements;
- English and Uyghur versions communicate the same corrected technical meaning;
- a final keyword/objective audit finds no remaining explicit v4.0 bullet omissions.
