from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "1.2"')
obj_end = text.find('"id": "1.3"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 1.2 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 1.2 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Add current-exam Track Point / Pointing Stick coverage after the existing trackpad/drawing-pad section.
en_old = (
    "Regular calibration helps ensure the device accurately reflects finger or stylus movements. "
    "Additionally, connecting external peripherals or changing system settings can sometimes disable a track pad automatically. "
    "If cursor input suddenly stops working, checking the device settings to confirm the track pad is enabled is a critical troubleshooting step.\\n\\n"
    "Exam objective 1.2, compare and contrast accessories and connectivity options for mobile devices. Mobile device connections."
)
en_new = (
    "Regular calibration helps ensure the device accurately reflects finger or stylus movements. "
    "Additionally, connecting external peripherals or changing system settings can sometimes disable a track pad automatically. "
    "If cursor input suddenly stops working, checking the device settings to confirm the track pad is enabled is a critical troubleshooting step.\\n\\n"
    "Exam Note — Track Point / Pointing Stick: A track point is a small pressure-sensitive pointing control, usually located between keyboard keys on some laptops. "
    "The user applies pressure to move the on-screen pointer without moving a hand to the trackpad or an external mouse. "
    "It is an alternative pointing device, not the same thing as a trackpad/drawing pad. "
    "For the exam, recognize the names **track point** and **pointing stick** and identify it as a keyboard-integrated pointer-control device.\\n\\n"
    "Memory rule: Trackpad = touch surface; Track point = small keyboard pointing nub.\\n\\n"
    "Exam objective 1.2, compare and contrast accessories and connectivity options for mobile devices. Mobile device connections."
)
english = replace_exact(english, en_old, en_new, "English track point Exam Note")

ug_old = (
    "قەرەللىك calibration ئۈسكۈنىنىڭ بارماق ياكى stylus ھەرىكىتىنى تېخىمۇ توغرا ئەكس ئەتتۈرۈشىگە ياردەم بېرىدۇ.\\n\\n"
    "سىرتقى قوشۇمچە ئۈسكۈنە ئۇلاش ياكى سىستېما تەڭشەكلىرىنى ئۆزگەرتىش بەزىدە trackpad نى ئاپتوماتىك توختىتىپ قويۇشى مۇمكىن. ئەگەر cursor كىرگۈزۈشى تۇيۇقسىز توختاپ قالسا، ئۈسكۈنە تەڭشەكلىرىدىن trackpad نىڭ قوزغىتىلغانلىقىنى تەكشۈرۈش مۇھىم troubleshooting قەدىمىدۇر.\\n\\n"
    "Exam Objective 1.2"
)
ug_new = (
    "قەرەللىك calibration ئۈسكۈنىنىڭ بارماق ياكى stylus ھەرىكىتىنى تېخىمۇ توغرا ئەكس ئەتتۈرۈشىگە ياردەم بېرىدۇ.\\n\\n"
    "سىرتقى قوشۇمچە ئۈسكۈنە ئۇلاش ياكى سىستېما تەڭشەكلىرىنى ئۆزگەرتىش بەزىدە trackpad نى ئاپتوماتىك توختىتىپ قويۇشى مۇمكىن. ئەگەر cursor كىرگۈزۈشى تۇيۇقسىز توختاپ قالسا، ئۈسكۈنە تەڭشەكلىرىدىن trackpad نىڭ قوزغىتىلغانلىقىنى تەكشۈرۈش مۇھىم troubleshooting قەدىمىدۇر.\\n\\n"
    "### Track Point / Pointing Stick — Exam Note\\n\\n"
    "**Track point / pointing stick** — بەزى laptop keyboard لاردا key لارنىڭ ئارىسىغا جايلاشتۇرۇلغان كىچىك pressure-sensitive pointing control.\\n\\n"
    "ئىشلەتكۈچى ئۇنىڭغا بېسىم ئىشلىتىپ:\\n"
    "- cursor/pointer نى يۆتكەيدۇ\\n"
    "- قولىنى trackpad ياكى external mouse قا يۆتكىمەي pointer نى كونترول قىلالايدۇ\\n\\n"
    "ئۇ **trackpad/drawing pad بىلەن بىر نەرسە ئەمەس**؛ ئۇ keyboard ئىچىگە بىرلەشتۈرۈلگەن ئايرىم pointing device.\\n\\n"
    "**Exam memory:**\\n"
    "- **Trackpad = touch surface**\\n"
    "- **Track point / pointing stick = small keyboard pointing nub**\\n\\n"
    "---\\n\\n"
    "Exam Objective 1.2"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur track point Exam Note")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 1.2 review documentation.
review = Path("OBJECTIVE_1_2_REVIEW.md")
r = review.read_text(encoding="utf-8")
anchor = "## Key source-derived comparisons\n"
insert = (
    "## Current-objective source gap — Track Point / Pointing Stick\n\n"
    "The transcript covers **drawing pads** and **trackpads/touchpads** but does not teach **track points / pointing sticks**, which are part of current Objective 1.2 input/accessory coverage. The original transcript remains unchanged. Learner-facing English and Uyghur add a clearly labeled **Exam Note** that distinguishes:\n"
    "- **trackpad** = touch-sensitive surface\n"
    "- **track point / pointing stick** = small pressure-sensitive keyboard-integrated pointer control\n\n"
    + anchor
)
r = replace_exact(r, anchor, insert, "review track point gap")
r = replace_exact(
    r,
    "- preserves the source's organization and level of detail.",
    "- preserves the source's organization and level of detail;\n- adds missing current-objective facts as clearly labeled **Exam Notes** without changing the archival transcript.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections/source-gap record.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 1.2: `NSC` → `NFC` in the Near-Field Communication segment (speech-to-text error in the original transcript)."
new = (
    old + "\n"
    "- Objective 1.2 source-gap note: the transcript teaches **drawing pads** and **trackpads/touchpads** but omits **track points / pointing sticks** from the current objective coverage. The original transcript remains unchanged; learner-facing English and Uyghur add a clearly labeled **Exam Note** explaining **track point / pointing stick = small pressure-sensitive keyboard-integrated pointer control**."
)
c = replace_exact(c, old, new, "transcript Objective 1.2 track point note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "1.2"')
end = final.find('"id": "1.3"', start)
obj = final[start:end]
required = [
    "Exam Note — Track Point / Pointing Stick:",
    "small pressure-sensitive pointing control",
    "Trackpad = touch surface; Track point = small keyboard pointing nub.",
    "### Track Point / Pointing Stick — Exam Note",
    "**Trackpad = touch surface**",
    "**Track point / pointing stick = small keyboard pointing nub**",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 1.2 track point content: {missing}")

print("Objective 1.2 track point patch validation passed")
