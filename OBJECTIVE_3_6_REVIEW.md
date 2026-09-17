# Objective 3.6 — Deep Translation Review

## Source structure
Objective 3.6 is one continuous transcript segment, organized as:
1. PSU and AC→DC conversion
2. Voltage and motherboard power connectors
3. Wattage / PSU sizing
4. Energy efficiency / 80 Plus
5. Modular power supplies
6. Redundant power supplies
7. UPS

## Input voltage
Transcript nominal values:
- 120 VAC
- 240 VAC

Current 220-1201 learner-facing Exam Note:
- **110–120 VAC**
- **220–240 VAC**

Common outputs:
- 3.3 V DC
- 5 V DC
- 12 V DC

Motherboard power:
- 20-pin
- 24-pin
- 20+4-pin

## Wattage
- Watt = unit of electrical power.
- PSU wattage = maximum output capacity.
- Add component requirements, load, and future expansion.
- Too little wattage can cause instability/shutdown/damage.
- Transcript says excessive wattage may create unnecessary expense/inefficiency. Learner-facing content corrects the blanket efficiency implication: higher wattage alone does not inherently make a PSU inefficient; efficiency varies with PSU design and operating load, while right-sizing should still include reasonable headroom.

The source asks whether a fictional 500 W PSU is sufficient, but the transcript omits the component wattage values needed to answer it. No answer is invented.

## Efficiency / 80 Plus
- efficiency = AC→DC conversion effectiveness
- lost energy becomes heat
- 80 Plus = at least 80% efficiency at certain load levels
- Bronze / Silver / Gold / Platinum / Titanium
- efficiency does not increase PSU wattage capacity

No external certification matrix is added.

## Modular PSU
- detachable cables
- only needed cables connected
- less clutter
- cleaner layout
- improved airflow/cooling

## Redundant PSU
- backup PSU
- primary failure can fail over to backup
- continuity / reduced downtime

## UPS — Supplemental for Objective 3.6
Current 220-1201 Objective 3.6 does not list UPS as a named bullet. The transcript's UPS material is retained as supporting knowledge.

Source covers:
- immediate short-term emergency power
- save/shutdown or move to longer-term power
- battery-backup + surge-protection outlets vs surge-only
- critical device examples: computer/server, monitor, router, cable modem, critical switch/storage
- avoid printers/scanners/large speakers on battery-backed outlets
- laser printers highlighted as high draw
- not intended to run the whole office for hours

Transcript correction:
- `UPDES` → **UPS**

## Translation approach
- Preserve the original transcript and its device examples.
- Correct learner-facing input voltage to the current objective ranges **110–120 VAC vs. 220–240 VAC** while noting the transcript's nominal 120/240 values.
- Correct the blanket oversized-PSU inefficiency implication without adding a detailed efficiency-curve matrix.
- Do not answer missing-data wattage questions.
- Label UPS as **Supplemental for Objective 3.6** rather than removing the source material.
- Do not import unrelated modern PSU/UPS specifications.
