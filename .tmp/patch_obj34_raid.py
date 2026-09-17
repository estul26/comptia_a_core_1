from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "3.4"')
obj_end = text.find('"id": "3.5"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.4 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.4 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Add RAID 6 minimum-drive Exam Note.
en_old_6 = (
    "Like RAID 5, it uses striping and distributed parity. However, RAID 6 stores two sets of parity information instead of one. "
    "This means it can sustain the failure of two drives simultaneously without losing data.\\n\\n"
    "That additional layer of protection makes RAID 6 more resilient than RAID 5, particularly in large arrays where the probability of multiple drive failures increases."
)
en_new_6 = (
    "Like RAID 5, it uses striping and distributed parity. However, RAID 6 stores two sets of parity information instead of one. "
    "This means it can sustain the failure of two drives simultaneously without losing data.\\n\\n"
    "Exam Note — Minimum drives: RAID 6 requires a minimum of **four drives**.\\n\\n"
    "That additional layer of protection makes RAID 6 more resilient than RAID 5, particularly in large arrays where the probability of multiple drive failures increases."
)
english = replace_exact(english, en_old_6, en_new_6, "English RAID 6 minimum")

# Add RAID 10 minimum-drive Exam Note.
en_old_10 = (
    "This design delivers both strong redundancy and high performance, though it can be costly. "
    "RAID 10 offers faster rebuild times and strong fault tolerance because data is mirrored rather than reconstructed from parity. "
    "However, like RAID 1, usable capacity is reduced since half of the total storage is dedicated to mirroring.\\n\\n"
    "Exam objective 3.4, compare and contrast storage devices."
)
en_new_10 = (
    "This design delivers both strong redundancy and high performance, though it can be costly. "
    "RAID 10 offers faster rebuild times and strong fault tolerance because data is mirrored rather than reconstructed from parity. "
    "However, like RAID 1, usable capacity is reduced since half of the total storage is dedicated to mirroring.\\n\\n"
    "Exam Note — Minimum drives: RAID 10 (RAID 1+0) requires a minimum of **four drives**.\\n\\n"
    "Exam objective 3.4, compare and contrast storage devices."
)
english = replace_exact(english, en_old_10, en_new_10, "English RAID 10 minimum")

# Replace Uyghur source-boundary notes with transparent Exam Notes.
ug_old_6 = "**Source-boundary note:** transcript RAID 6 نىڭ minimum drive count نى بۇ segment دا بەرمەيدۇ؛ reviewed Uyghur سىرتقى سان قوشمايدۇ."
ug_new_6 = (
    "**Exam Note — Minimum drives:** transcript بۇ segment دا RAID 6 نىڭ minimum drive count نى بەرمەيدۇ. "
    "Original transcript ئۆزگەرتىلمەيدۇ؛ learner-facing study content exam-support fact سۈپىتىدە **RAID 6 = minimum 4 drives** نى قوشىدۇ."
)
uyghur = replace_exact(uyghur, ug_old_6, ug_new_6, "Uyghur RAID 6 minimum")

ug_old_10 = "**Source-boundary note:** transcript RAID 10 نىڭ minimum drive count نى بۇ segment دا بەرمەيدۇ؛ reviewed Uyghur سىرتقى سان قوشمايدۇ."
ug_new_10 = (
    "**Exam Note — Minimum drives:** transcript بۇ segment دا RAID 10 نىڭ minimum drive count نى بەرمەيدۇ. "
    "Original transcript ئۆزگەرتىلمەيدۇ؛ learner-facing study content exam-support fact سۈپىتىدە **RAID 10 = minimum 4 drives** نى قوشىدۇ."
)
uyghur = replace_exact(uyghur, ug_old_10, ug_new_10, "Uyghur RAID 10 minimum")

# Update the compact Uyghur memory map.
uyghur = replace_exact(
    uyghur,
    "- **6** = Double parity / survive 2 drive failures\\n- **10** = Striping + mirroring",
    "- **6** = Double parity / min 4 / survive 2 drive failures\\n- **10** = Striping + mirroring / min 4",
    "Uyghur RAID memory map minimums",
)

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 3.4 review.
review = Path("OBJECTIVE_3_4_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "**RAID 6**\n- striping + two parity sets\n- withstand two-drive failures\n- source does not state minimum drive count",
    "**RAID 6**\n- striping + two parity sets\n- withstand two-drive failures\n- transcript does not state minimum drive count\n- learner-facing **Exam Note: minimum 4 drives**",
    "review RAID 6 minimum",
)
r = replace_exact(
    r,
    "**RAID 10**\n- RAID 1+0\n- striping + mirroring\n- high performance / redundancy\n- faster rebuild than parity-based source comparison\n- half usable capacity\n- source does not state minimum drive count",
    "**RAID 10**\n- RAID 1+0\n- striping + mirroring\n- high performance / redundancy\n- faster rebuild than parity-based source comparison\n- half usable capacity\n- transcript does not state minimum drive count\n- learner-facing **Exam Note: minimum 4 drives**",
    "review RAID 10 minimum",
)
r = replace_exact(
    r,
    "- Explicitly note source gaps.\n- Avoid importing newer storage standards/specifications.",
    "- Explicitly note source gaps.\n- Add missing exam-support facts as clearly labeled **Exam Notes** while preserving the original transcript.\n- Avoid importing newer storage standards/specifications.",
    "review translation policy",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 3.4 source-scope note: RAID 6 and RAID 10 minimum-drive counts are not stated in this transcript segment, so no outside values were inserted."
new = (
    "- Objective 3.4 source-gap note: RAID 6 and RAID 10 minimum-drive counts are not stated in this transcript segment. "
    "The original transcript remains unchanged; learner-facing English and Uyghur add clearly labeled exam-support notes: **RAID 6 = minimum 4 drives** and **RAID 10 = minimum 4 drives**."
)
c = replace_exact(c, old, new, "transcript RAID minimum note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "3.4"')
end = final.find('"id": "3.5"', start)
obj = final[start:end]
required = [
    "Exam Note — Minimum drives: RAID 6 requires a minimum of **four drives**.",
    "Exam Note — Minimum drives: RAID 10 (RAID 1+0) requires a minimum of **four drives**.",
    "**RAID 6 = minimum 4 drives**",
    "**RAID 10 = minimum 4 drives**",
    "- **6** = Double parity / min 4 / survive 2 drive failures",
    "- **10** = Striping + mirroring / min 4",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 3.4 RAID minimum content: {missing}")

stale = [
    "reviewed Uyghur سىرتقى سان قوشمايدۇ",
]
if any(x in obj for x in stale):
    raise SystemExit("Stale RAID minimum source-boundary wording remains")

print("Objective 3.4 RAID minimum-drive patch validation passed")
