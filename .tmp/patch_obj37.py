from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "3.7"')
obj_end = text.find('"id": "3.8"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.7 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.7 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Add the required unboxing/setup-location coverage before the transcript moves into printer/scanner definitions.
en_old = (
    "Exam objective 3.7. Given a scenario, deploy and configure multifunction devices, printers, and settings. Printer and scanner.\\n\\n"
    "In this video segment, we will cover printers and scanners together, as they are fairly similar."
)
en_new = (
    "Exam objective 3.7. Given a scenario, deploy and configure multifunction devices, printers, and settings. Printer and scanner.\\n\\n"
    "Exam Note — Proper unboxing and setup location: Before connecting or configuring a new printer/MFD, follow the manufacturer’s setup instructions, inspect the device and packaging for damage, verify included parts/accessories, and remove shipping tape, locks, spacers, protective material, and cartridge/toner transport seals as applicable. "
    "Place the device on a stable, level surface with enough ventilation and clearance for trays, doors, covers, paper paths, and maintenance access. Keep it away from excessive heat, moisture, and dust, use an appropriate accessible power source, and make sure the chosen location supports the required USB, Ethernet, or reliable Wi-Fi connection. "
    "For large or heavy devices, use safe lifting/moving practices and the manufacturer’s guidance.\\n\\n"
    "Quick setup order: unbox safely → remove shipping restraints → choose a stable/ventilated location → connect power/network → install the correct driver/firmware → configure/test.\\n\\n"
    "In this video segment, we will cover printers and scanners together, as they are fairly similar."
)
english = replace_exact(english, en_old, en_new, "English unboxing/setup-location section")

# Mark 3D printing as supplemental rather than core 3.7 coverage.
en_old_3d = (
    "Some of the most common printer types are laser printers, inkjet printers, thermal printers, impact printers, and 3D printers. "
    "While a printer outputs digital data, a scanner does the exact opposite."
)
en_new_3d = (
    "Some of the most common printer types are laser printers, inkjet printers, thermal printers, impact printers, and 3D printers. "
    "Supplemental source note: the transcript mentions 3D printers, but current 220-1201 Objective 3.7 does not list 3D printing as a required subtopic. "
    "While a printer outputs digital data, a scanner does the exact opposite."
)
english = replace_exact(english, en_old_3d, en_new_3d, "English 3D supplemental label")

# Uyghur: add a matching exam-focused setup checklist near the start.
ug_old = (
    "Exam Objective 3.7\\nبىر ئەھۋال بېرىلگەندە، كۆپ ئىقتىدارلىق ئۈسكۈنىلەر (MFD)، پرىنتېرلار ۋە ئۇلارنىڭ تەڭشەكلىرىنى ئورۇنلاشتۇرۇڭ ۋە تەڭشەڭ.\\n\\n"
    "## پرىنتېر ۋە سكاننېر (Printer and Scanner)"
)
ug_new = (
    "Exam Objective 3.7\\nبىر ئەھۋال بېرىلگەندە، كۆپ ئىقتىدارلىق ئۈسكۈنىلەر (MFD)، پرىنتېرلار ۋە ئۇلارنىڭ تەڭشەكلىرىنى ئورۇنلاشتۇرۇڭ ۋە تەڭشەڭ.\\n\\n"
    "## Proper Unboxing & Setup Location — Exam Note\\n\\n"
    "Printer/MFD نى ئۇلاشتىن بۇرۇن تۆۋەندىكى setup نۇقتىلىرىنى تەكشۈرۈڭ:\\n"
    "- manufacturer setup instruction غا ئەگىشىڭ\\n"
    "- box/device دا damage بار-يوقلۇقىنى تەكشۈرۈڭ\\n"
    "- included part/accessory لارنى verify قىلىڭ\\n"
    "- shipping tape، lock، spacer، protective material ۋە cartridge/toner transport seal لارنى ئېلىۋېتىڭ\\n"
    "- stable، level surface تاللاڭ\\n"
    "- vent، tray، door، cover ۋە paper path ئۈچۈن يېتەرلىك clearance قالدۇرۇڭ\\n"
    "- heat، moisture ۋە dust كۆپ جايدىن ساقلىنىڭ\\n"
    "- power source ئاسان ۋە بىخەتەر زىيارەت قىلىنىدىغان بولسۇن\\n"
    "- USB/Ethernet ياكى reliable Wi-Fi connection نى location بويىچە ئالدىن ئويلاڭ\\n"
    "- heavy device بولسا manufacturer guidance ۋە safe lifting/moving practice ئىشلىتىڭ\\n\\n"
    "**Exam setup order:**\\n"
    "> **Unbox → Remove shipping restraints → Choose stable/ventilated location → Power/network → Driver/firmware → Configure/Test**\\n\\n"
    "---\\n\\n"
    "## پرىنتېر ۋە سكاننېر (Printer and Scanner)"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur unboxing/setup-location section")

ug_old_3d = (
    "مەنبە تىلغا ئالغان common printer types:\\n"
    "- laser printer\\n"
    "- inkjet printer\\n"
    "- thermal printer\\n"
    "- impact printer\\n"
    "- 3D printer"
)
ug_new_3d = (
    "مەنبە تىلغا ئالغان common printer types:\\n"
    "- laser printer\\n"
    "- inkjet printer\\n"
    "- thermal printer\\n"
    "- impact printer\\n"
    "- 3D printer\\n\\n"
    "**Supplemental source note:** transcript 3D printer نى تىلغا ئالىدۇ، ئەمما current 220-1201 Objective 3.7 نىڭ required bullet لىرى ئىچىدە 3D printing ئايرىم subtopic سۈپىتىدە كۆرسىتىلمەيدۇ."
)
uyghur = replace_exact(uyghur, ug_old_3d, ug_new_3d, "Uyghur 3D supplemental label")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 3.7 review documentation.
review = Path("OBJECTIVE_3_7_REVIEW.md")
r = review.read_text(encoding="utf-8")
anchor = "## Printer / scanner\n"
insert = (
    "## Unboxing / setup location\n\n"
    "Current 220-1201 Objective 3.7 explicitly requires candidates to **properly unbox the device and consider set-up location**. The transcript does not teach this step before moving into connectivity. Learner-facing English and Uyghur now add a clearly labeled **Exam Note** covering:\n"
    "- manufacturer setup instructions\n"
    "- inspection for shipping damage and verification of included parts/accessories\n"
    "- removal of shipping tape/locks/spacers/protective material and cartridge/toner transport seals as applicable\n"
    "- stable, level placement with ventilation and service/tray clearance\n"
    "- avoiding excessive heat, moisture, and dust\n"
    "- appropriate accessible power and required USB/Ethernet/Wi-Fi connectivity\n"
    "- safe lifting/moving practices for large or heavy devices\n\n"
    + anchor
)
r = replace_exact(r, anchor, insert, "review unboxing section")
r = replace_exact(
    r,
    "- 3D printer creates a physical object from a 3D model",
    "- 3D printer creates a physical object from a 3D model (**supplemental/source example; not listed as a required Objective 3.7 subtopic in the current 220-1201 objectives**)",
    "review 3D supplemental label",
)
r = replace_exact(
    r,
    "- Preserve all source workflows and examples.\n- Correct only strongly supported transcription artifacts.",
    "- Preserve all source workflows and examples, while clearly labeling source-only material that is outside the current objective bullets.\n- Add missing current-objective requirements as clearly labeled learner-facing **Exam Notes** without changing the archival transcript.\n- Correct only strongly supported transcription artifacts.",
    "review translation policy",
)
review.write_text(r, encoding="utf-8")

# Record the source gap and supplemental label.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
marker = "- Objective 3.7"
pos = c.find(marker)
if pos < 0:
    raise SystemExit("Could not locate Objective 3.7 section/note in TRANSCRIPT_CORRECTIONS.md")

# Insert before the first Objective 3.7 correction note to keep related notes together.
note = (
    "- Objective 3.7 exam-coverage note: current 220-1201 explicitly requires **properly unbox device and consider set-up location**, but the transcript moves directly into printer/scanner definitions and connectivity. The original transcript remains unchanged; learner-facing English and Uyghur add a clearly labeled setup-location **Exam Note**.\n"
    "- Objective 3.7 scope note: the transcript mentions **3D printers**. Learner-facing content keeps that source example but labels it **Supplemental**, because current Objective 3.7 does not list 3D printing as a required subtopic.\n"
)
c = c[:pos] + note + c[pos:]
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "3.7"')
end = final.find('"id": "3.8"', start)
obj = final[start:end]
required = [
    "Exam Note — Proper unboxing and setup location:",
    "remove shipping tape, locks, spacers, protective material",
    "stable, level surface",
    "Quick setup order: unbox safely",
    "Supplemental source note: the transcript mentions 3D printers",
    "## Proper Unboxing & Setup Location — Exam Note",
    "**Exam setup order:**",
    "**Supplemental source note:** transcript 3D printer",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 3.7 content: {missing}")

print("Objective 3.7 printer setup patch validation passed")
