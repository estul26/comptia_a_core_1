from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "3.3"')
obj_end = text.find('"id": "3.4"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.3 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.3 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Ensure the existing correct DDR data-rate explanation is present.
required_existing = [
    "approximately 2666 MT/s, or 2666 million transfers per second",
    "approximately 1333 MHz",
    "MT/s measures transfers per second, while MHz measures clock cycles per second",
]
missing_existing = [x for x in required_existing if x not in english]
if missing_existing:
    raise SystemExit(f"Existing MT/s correction missing unexpectedly: {missing_existing}")

# Add an explicit ECC vs non-ECC comparison.
en_old = (
    "Therefore, ECC RAM emerges as the preferred choice for servers where reliability and data integrity are non-negotiable priorities. "
    "Lastly, what good is it to go out and purchase some RAM if you can't decipher its specifications? Luckily, I got you covered."
)
en_new = (
    "Therefore, ECC RAM emerges as the preferred choice for servers where reliability and data integrity are non-negotiable priorities.\\n\\n"
    "Exam Note — ECC vs non-ECC RAM: ECC memory supports system-level error detection and correction when used on a compatible platform. "
    "Non-ECC memory does not provide this system-level ECC function and is common in general-purpose client systems. "
    "ECC operation depends on platform support from the processor/memory controller and motherboard. "
    "For the exam, remember: ECC = error detection/correction; non-ECC = no system-level ECC.\\n\\n"
    "Lastly, what good is it to go out and purchase some RAM if you can't decipher its specifications? Luckily, I got you covered."
)
english = replace_exact(english, en_old, en_new, "English ECC vs non-ECC note")

# Correct the remaining obvious learner-facing transcript artifact.
english = replace_exact(
    english,
    "As for the 21,300, this indicates that the RAM can theoretically transfer up to 21,300 megabytes per second of theta.",
    "As for the 21,300, this indicates that the RAM can theoretically transfer up to 21,300 megabytes per second of data.",
    "English theta-to-data correction",
)

ug_old = "**ئەستە تۇتۇڭ: ECC = Error detection/correction + Server/Data integrity**\\n\\n---"
ug_new = (
    "**ئەستە تۇتۇڭ: ECC = Error detection/correction + Server/Data integrity**\\n\\n"
    "### ECC vs Non-ECC — Exam Note\\n\\n"
    "- **ECC RAM** = system-level error detection/correction نى قوللايدۇ؛ platform مۇ ECC نى قوللىشى كېرەك.\\n"
    "- **Non-ECC RAM** = system-level ECC function يوق؛ ئادەتتىكى desktop/laptop client system لاردا كۆپ ئۇچرايدۇ.\\n"
    "- ECC نىڭ ئىشلەش-ئىشلىمەسلىكى RAM module دىن باشقا **CPU / memory controller + motherboard support** قا باغلىق.\\n\\n"
    "**Exam memory:**\\n"
    "- **ECC = Error detection/correction**\\n"
    "- **Non-ECC = No system-level ECC**\\n\\n"
    "---"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur ECC vs non-ECC note")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 3.3 review documentation.
review = Path("OBJECTIVE_3_3_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "### ECC\nSource:\n- additional circuitry for error detection/correction\n- server/critical-system focus\n- financial transactions and medical records examples\n- higher cost trade-off",
    "### ECC / non-ECC\nSource ECC coverage:\n- additional circuitry for error detection/correction\n- server/critical-system focus\n- financial transactions and medical records examples\n- higher cost trade-off\n\nLearner-facing exam clarification:\n- **ECC** supports system-level error detection/correction on a compatible platform\n- **non-ECC** does not provide the system-level ECC function\n- CPU/memory-controller and motherboard support are required for ECC operation",
    "review ECC section",
)
r = replace_exact(
    r,
    "The transcript describes 2666 as MHz / cycles per second. This is preserved as source teaching and not externally reconciled.",
    "The original transcript describes 2666 as MHz / cycles per second and remains unchanged. Learner-facing English and Uyghur correctly distinguish **DDR4-2666 ≈ 2666 MT/s effective transfer rate** from an **≈1333 MHz I/O clock**.",
    "review MT/s correction",
)
r = replace_exact(
    r,
    "- Preserve source-stated speed/bandwidth terminology without importing outside corrections.",
    "- Preserve the original source, but correct learner-facing DDR transfer-rate terminology to **MT/s** where the transcript confuses transfer rate with MHz.",
    "review translation policy",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old_speed = "- Objective 3.3 source-scope note: the RAM-speed example describes DDR4-2666 using MHz and `2666 million cycles per second`. Reviewed Uyghur preserves this as the transcript's teaching model and does not import the external MT/s-vs-MHz distinction."
new_speed = "- Objective 3.3 technical correction: the RAM-speed example describes DDR4-2666 using MHz and `2666 million cycles per second`. The original transcript remains unchanged; learner-facing English and Uyghur correctly use **≈2666 MT/s** for the effective transfer rate and distinguish it from the **≈1333 MHz** I/O clock."
c = replace_exact(c, old_speed, new_speed, "transcript MT/s note")

old_ecc = "- Objective 3.3 source-scope note: ECC is rendered from the transcript's `error correction code` wording; no extra ECC bit-error taxonomy, registered/buffered memory, XMP/EXPO, CAS latency, voltage, rank, or timing details are added."
new_ecc = "- Objective 3.3 exam clarification: the transcript explains ECC RAM but does not explicitly contrast **ECC vs non-ECC**. Learner-facing English and Uyghur now make that distinction explicit and note that ECC operation requires compatible processor/memory-controller and motherboard support; unrelated RAM timing/overclocking details are not added."
c = replace_exact(c, old_ecc, new_ecc, "transcript ECC note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "3.3"')
end = final.find('"id": "3.4"', start)
obj = final[start:end]
required = [
    "Exam Note — ECC vs non-ECC RAM:",
    "non-ECC = no system-level ECC",
    "### ECC vs Non-ECC — Exam Note",
    "**Non-ECC = No system-level ECC**",
    "approximately 2666 MT/s",
    "approximately 1333 MHz",
    "21,300 megabytes per second of data",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 3.3 content: {missing}")

if "21,300 megabytes per second of theta" in english:
    raise SystemExit("Stale theta transcript artifact remains in learner-facing Objective 3.3 English")

print("Objective 3.3 RAM terminology patch validation passed")
