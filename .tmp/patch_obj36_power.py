from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "3.6"')
obj_end = text.find('"id": "3.7"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.6 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.6 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Current exam uses voltage ranges, while transcript gives nominal 120/240 values.
en_old_voltage = (
    "When you plug your desktop PC into a wall outlet, it receives electrical power in the form of alternating current. "
    "This alternating current typically comes in two primary voltage standards, 120 volt alternating current, or VAC, and 240 volt alternating current. "
    "These voltage standards dictate the level of electrical pressure that flows through the wires and into your computer's PSU."
)
en_new_voltage = (
    "When you plug your desktop PC into a wall outlet, it receives electrical power in the form of alternating current. "
    "The transcript describes the common nominal values as 120 VAC and 240 VAC. "
    "Exam Note — Input voltage: for the current 220-1201 objective, learn the input ranges as **110–120 VAC vs. 220–240 VAC**. "
    "These input-voltage ranges describe the AC power supplied to the PSU."
)
english = replace_exact(english, en_old_voltage, en_new_voltage, "English input-voltage ranges")

# Correct the blanket oversized-PSU inefficiency claim.
en_old_wattage = (
    "Conversely, choosing a PSU with excessive wattage may lead to unnecessary expenses and inefficiencies, as the system will only draw the power it requires. "
    "Therefore, understanding wattage and accurately determining the power requirements of a computer build are essential steps in ensuring a stable and efficient system. "
    "This knowledge enables users to select an appropriate PSU that can adequately power their components while also accommodating any future upgrades or expansions."
)
en_new_wattage = (
    "Conversely, choosing much more wattage than the system needs may add unnecessary cost, but a higher wattage rating does **not** by itself make a PSU inefficient. "
    "The computer draws only the power it requires, and PSU conversion efficiency varies with the unit's design and operating load. "
    "Choose a PSU with enough capacity for the system's peak demand plus reasonable headroom for future upgrades rather than assuming either the smallest or the largest wattage is automatically best. "
    "Therefore, understanding wattage and accurately determining the power requirements of a computer build are essential steps in ensuring a stable and efficient system."
)
english = replace_exact(english, en_old_wattage, en_new_wattage, "English PSU sizing/efficiency correction")

# Label UPS as supplemental for Objective 3.6.
en_old_ups = (
    "Lastly, in situations where there are sudden and unexpected power interruptions, an uninterruptible power supply, or UPS, becomes an invaluable asset to ensure maximum uptime."
)
en_new_ups = (
    "Supplemental source note — UPS: The transcript includes UPS guidance, but UPS is not listed as a bullet under the current 220-1201 Objective 3.6 power-supply requirements. "
    "Keep this section as useful supporting knowledge rather than a named Objective 3.6 requirement.\\n\\n"
    "Lastly, in situations where there are sudden and unexpected power interruptions, an uninterruptible power supply, or UPS, becomes an invaluable asset to ensure maximum uptime."
)
english = replace_exact(english, en_old_ups, en_new_ups, "English UPS supplemental label")

# Uyghur input ranges.
ug_old_voltage = (
    "### Input Voltage\\n\\n"
    "مەنبە تامدىن كېلىدىغان AC توكنىڭ ئىككى common standard ىنى قاپلايدۇ:\\n\\n"
    "- **120 VAC**\\n"
    "- **240 VAC**\\n\\n"
    "بۇ يەردىكى **VAC**:\\n"
    "- Volts AC\\n\\n"
    "مەنىسىدە ئىشلىتىلگەن."
)
ug_new_voltage = (
    "### Input Voltage\\n\\n"
    "Original transcript nominal value سۈپىتىدە **120 VAC** ۋە **240 VAC** نى تىلغا ئالىدۇ.\\n\\n"
    "**Exam Note — current 220-1201:**\\n"
    "- **110–120 VAC**\\n"
    "- **220–240 VAC**\\n\\n"
    "دەپ range شەكلىدە ئەستە تۇتۇڭ.\\n\\n"
    "بۇ يەردىكى **VAC = Volts AC**."
)
uyghur = replace_exact(uyghur, ug_old_voltage, ug_new_voltage, "Uyghur input-voltage ranges")
uyghur = replace_exact(
    uyghur,
    "> **Input: 120/240 VAC**",
    "> **Input: 110–120 VAC / 220–240 VAC**",
    "Uyghur input memory",
)

# Uyghur right-sizing/efficiency correction.
ug_old_wattage = (
    "### Wattage بەك يۇقىرى بولسا\\n\\n"
    "مەنبە بويىچە excessively high wattage PSU:\\n"
    "- unnecessary cost\\n"
    "- inefficiency\\n\\n"
    "پەيدا قىلىشى مۇمكىن، چۈنكى system پەقەت ئۆزىگە لازىم بولغان power نىلا draw قىلىدۇ.\\n\\n"
    "**Source-framing note:** reviewed lesson بۇنى transcript نىڭ ئۆز wording ى سۈپىتىدە ساقلايدۇ؛ PSU efficiency curve ياكى modern PSU sizing rule لارنى سىرتتىن قوشمايدۇ."
)
ug_new_wattage = (
    "### Wattage بەك يۇقىرى بولسا\\n\\n"
    "PSU wattage system requirement دىن ناھايىتى يۇقىرى بولسا unnecessary cost پەيدا بولۇشى مۇمكىن. "
    "لېكىن **wattage rating يۇقىرى بولغانلىقىنىڭ ئۆزى PSU نى inefficiency قىلىۋەتمەيدۇ**.\\n\\n"
    "System پەقەت ئۆزىگە لازىم بولغان power نى draw قىلىدۇ؛ PSU efficiency بولسا:\\n"
    "- PSU design/quality\\n"
    "- operating load\\n\\n"
    "غا باغلىق ئۆزگىرىدۇ.\\n\\n"
    "**Study rule:** system نىڭ peak demand ىغا يېتەرلىك capacity + future upgrade ئۈچۈن reasonable headroom تاللاڭ؛ «ئەڭ كىچىك» ياكى «ئەڭ چوڭ» PSU نى ئاپتوماتىك ئەڭ efficient دەپ قارىماڭ."
)
uyghur = replace_exact(uyghur, ug_old_wattage, ug_new_wattage, "Uyghur PSU sizing/efficiency correction")

# Uyghur UPS supplemental label.
ug_old_ups = "## UPS — Uninterruptible Power Supply\\n\\n**UPS (Uninterruptible Power Supply)**"
ug_new_ups = (
    "## UPS — Uninterruptible Power Supply — Supplemental\\n\\n"
    "**Scope note:** transcript UPS نى بۇ Objective 3.6 lesson ئىچىدە قاپلايدۇ، ئەمما current 220-1201 Objective 3.6 bullet list دا UPS ئايرىم requirement سۈپىتىدە كۆرسىتىلمەيدۇ. "
    "شۇڭا بۇ بۆلەكنى useful supporting knowledge دەپ ئوقۇڭ.\\n\\n"
    "**UPS (Uninterruptible Power Supply)**"
)
uyghur = replace_exact(uyghur, ug_old_ups, ug_new_ups, "Uyghur UPS supplemental label")
uyghur = replace_exact(
    uyghur,
    "- **Input** = 120 / 240 VAC",
    "- **Input** = 110–120 VAC / 220–240 VAC",
    "Uyghur memory-map input ranges",
)
uyghur = replace_exact(
    uyghur,
    "- **UPS** = Short-term emergency power",
    "- **UPS** = Short-term emergency power (**Supplemental for Objective 3.6**)",
    "Uyghur memory-map UPS label",
)

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 3.6 review documentation.
review = Path("OBJECTIVE_3_6_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "## Source-stated values\nInput:\n- 120 VAC\n- 240 VAC",
    "## Input voltage\nTranscript nominal values:\n- 120 VAC\n- 240 VAC\n\nCurrent 220-1201 learner-facing Exam Note:\n- **110–120 VAC**\n- **220–240 VAC**",
    "review input ranges",
)
r = replace_exact(
    r,
    "- Excessive wattage may create unnecessary expense/inefficiency according to source wording.",
    "- Transcript says excessive wattage may create unnecessary expense/inefficiency. Learner-facing content corrects the blanket efficiency implication: higher wattage alone does not inherently make a PSU inefficient; efficiency varies with PSU design and operating load, while right-sizing should still include reasonable headroom.",
    "review oversized PSU wording",
)
r = replace_exact(
    r,
    "## UPS\n- immediate short-term emergency power",
    "## UPS — Supplemental for Objective 3.6\nCurrent 220-1201 Objective 3.6 does not list UPS as a named bullet. The transcript's UPS material is retained as supporting knowledge.\n\nSource covers:\n- immediate short-term emergency power",
    "review UPS scope",
)
r = replace_exact(
    r,
    "- Preserve every source-stated number and device example.\n- Do not answer missing-data wattage questions.\n- Correct only clear transcription errors.\n- Do not import modern PSU/UPS specifications absent from Objective 3.6.",
    "- Preserve the original transcript and its device examples.\n- Correct learner-facing input voltage to the current objective ranges **110–120 VAC vs. 220–240 VAC** while noting the transcript's nominal 120/240 values.\n- Correct the blanket oversized-PSU inefficiency implication without adding a detailed efficiency-curve matrix.\n- Do not answer missing-data wattage questions.\n- Label UPS as **Supplemental for Objective 3.6** rather than removing the source material.\n- Do not import unrelated modern PSU/UPS specifications.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
c = replace_exact(
    c,
    "- Objective 3.6 source-scope note: the transcript states common wall input standards of **120 VAC and 240 VAC** and PSU outputs of **3.3 V, 5 V, and 12 V DC**; these are preserved exactly without adding rail/current specifications.",
    "- Objective 3.6 exam-alignment note: the transcript states nominal wall-input values of **120 VAC and 240 VAC**. The original transcript remains unchanged; learner-facing English and Uyghur align the current 220-1201 wording to **110–120 VAC vs. 220–240 VAC**. PSU outputs of **3.3 V, 5 V, and 12 V DC** remain unchanged.",
    "transcript voltage note",
)
anchor = "- Objective 3.6 source-scope note: the transcript states that an 80 Plus-rated PSU guarantees at least 80% efficiency at certain load levels and lists Bronze, Silver, Gold, Platinum, and Titanium; no external load-percentage table or certification threshold matrix is added."
insert = (
    "- Objective 3.6 technical correction: the transcript broadly suggests an excessively high-wattage PSU causes inefficiency. "
    "Learner-facing English and Uyghur clarify that **higher wattage alone does not inherently make a PSU inefficient**; the system draws the power it requires, while conversion efficiency varies with PSU design and operating load. Right-sizing still considers peak demand and reasonable upgrade headroom.\n"
    + anchor
)
c = replace_exact(c, anchor, insert, "transcript PSU efficiency note")
c = replace_exact(
    c,
    "- Objective 3.6 source-scope note: UPS guidance is preserved as short-term emergency power for critical systems, with battery-backup vs surge-only outlets and source examples of devices to include/avoid; no runtime calculations, VA ratings, topology types, or battery chemistry details are added.",
    "- Objective 3.6 scope note: the transcript includes UPS guidance, but current 220-1201 Objective 3.6 does not list UPS as a named bullet. Learner-facing English and Uyghur retain the section but label it **Supplemental for Objective 3.6**; no runtime calculations, VA ratings, topology types, or battery chemistry details are added.",
    "transcript UPS scope note",
)
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "3.6"')
end = final.find('"id": "3.7"', start)
obj = final[start:end]
required = [
    "Exam Note — Input voltage: for the current 220-1201 objective, learn the input ranges as **110–120 VAC vs. 220–240 VAC**.",
    "a higher wattage rating does **not** by itself make a PSU inefficient",
    "Supplemental source note — UPS:",
    "> **Input: 110–120 VAC / 220–240 VAC**",
    "wattage rating يۇقىرى بولغانلىقىنىڭ ئۆزى PSU نى inefficiency قىلىۋەتمەيدۇ",
    "## UPS — Uninterruptible Power Supply — Supplemental",
    "- **Input** = 110–120 VAC / 220–240 VAC",
    "- **UPS** = Short-term emergency power (**Supplemental for Objective 3.6**)",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 3.6 corrections: {missing}")

stale = [
    "Conversely, choosing a PSU with excessive wattage may lead to unnecessary expenses and inefficiencies",
    "**Source-framing note:** reviewed lesson بۇنى transcript نىڭ ئۆز wording ى سۈپىتىدە ساقلايدۇ",
    "- **Input** = 120 / 240 VAC",
]
stale_found = [x for x in stale if x in obj]
if stale_found:
    raise SystemExit(f"Stale Objective 3.6 learner wording remains: {stale_found}")

print("Objective 3.6 power-supply patch validation passed")
