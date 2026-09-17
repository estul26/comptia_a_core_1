from pathlib import Path


def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)


index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "2.2"')
obj_end = text.find('"id": "2.3"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 2.2 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('\", \"uyghur\": \"', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 2.2 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('\", \"uyghur\": \"')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Correct learner-facing English terminology without changing the source transcript.
en_old = (
    "Wi-Fi, short for wireless fidelity, is a technology that allows computing devices to connect to and communicate with other computing devices wirelessly. "
    "It enables the transmission of data over short distances using radio waves and is most commonly used in homes, small offices, and public spaces like cafes, airports, and campuses."
)
en_new = (
    "Wi-Fi is a technology that allows computing devices to connect to and communicate with other computing devices wirelessly. "
    "It enables the transmission of data over short distances using radio waves and is most commonly used in homes, small offices, and public spaces like cafes, airports, and campuses.\\n\\n"
    "Terminology Note — Wi-Fi is a brand name, not an acronym for ‘wireless fidelity.’ The source transcript uses the phrase ‘wireless fidelity,’ but learner-facing study content should not teach that as Wi-Fi’s official expansion."
)
english = replace_exact(english, en_old, en_new, "English Wi-Fi terminology")

# Correct the Uyghur learner-facing explanation while preserving explicit source attribution.
ug_old = (
    "مەنبە Wi‑Fi نى **“wireless fidelity”** نىڭ قىسقارتىلمىسى دەپ چۈشەندۈرىدۇ. "
    "بۇ deep-review تەرجىمىسى مەنبەنىڭ شۇ ئىپادىسىنى ئۆزگەرتмәй، مەنبەگە تەۋە دەپ ئېنىق كۆرسىتىدۇ."
)
ug_new = (
    "**Terminology Note:** مەنبە transcript Wi‑Fi نى **“wireless fidelity”** نىڭ قىسقارتىلمىسى دەپ چۈشەندۈرىدۇ. Original transcript ئۆزگەرتىلمەيدۇ.\\n\\n"
    "ئەمما learner-facing study content تا بۇنى توغرا expansion دەپ ئۆگەنمەڭ: **Wi‑Fi بىر brand name، acronym ئەمەس؛ ئۇ “Wireless Fidelity” نىڭ official قىسقارتىلمىسى ئەمەس.**\\n\\n"
    "**Exam memory:** **Wi‑Fi = brand name; not “Wireless Fidelity.”**"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur Wi-Fi terminology")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 2.2 review documentation.
review = Path("OBJECTIVE_2_2_REVIEW.md")
r = review.read_text(encoding="utf-8")
anchor = "## Source-stated 802.11 progression\n"
insert = (
    "## Wi-Fi terminology correction\n\n"
    "The transcript says **Wi-Fi is short for `wireless fidelity`**. That phrase is preserved only in the original transcript under `source/`. Learner-facing English and Uyghur now explicitly teach that **Wi-Fi is a brand name, not an acronym, and `Wireless Fidelity` is not its official expansion**.\n\n"
    "This correction is intentionally narrow: it does not alter the objective's 802.11, frequency-band, channel, or performance teaching.\n\n"
    + anchor
)
r = replace_exact(r, anchor, insert, "review Wi-Fi terminology section")
r = replace_exact(
    r,
    "- Explicit source attribution for claims not independently researched.\n- No silent insertion of missing 802.11 values.\n- Documented speech-to-text corrections only.",
    "- Preserve the original transcript, but correct materially misleading learner-facing terminology when it could become a study mistake.\n- Explicit source attribution for claims not independently researched.\n- No silent insertion of missing 802.11 values.\n- Keep terminology corrections narrowly scoped to the objective.",
    "review translation policy",
)
review.write_text(r, encoding="utf-8")

# Update transcript correction record.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = (
    "- Objective 2.2 source-attribution note: the transcript describes Wi-Fi as short for `wireless fidelity`. "
    "The reviewed Uyghur attributes that wording to the source rather than independently asserting or replacing it."
)
new = (
    "- Objective 2.2 terminology correction: the transcript describes Wi-Fi as short for `wireless fidelity`. "
    "The original transcript remains unchanged, but learner-facing English and Uyghur explicitly correct this: **Wi-Fi is a brand name, not an acronym, and `Wireless Fidelity` is not its official expansion**."
)
c = replace_exact(c, old, new, "transcript corrections Wi-Fi note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "2.2"')
end = final.find('"id": "2.3"', start)
obj = final[start:end]
required = [
    "Terminology Note — Wi-Fi is a brand name, not an acronym",
    "should not teach that as Wi-Fi’s official expansion",
    "**Wi‑Fi بىر brand name، acronym ئەمەس",
    "**Wi‑Fi = brand name; not “Wireless Fidelity.”**",
]
missing = [item for item in required if item not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 2.2 Wi-Fi terminology content: {missing}")

forbidden = [
    "Wi-Fi, short for wireless fidelity, is a technology",
    "بۇ deep-review تەرجىمىسى مەنبەنىڭ شۇ ئىپادىسىنى ئۆزگەرتмәй، مەنبەگە تەۋە دەپ ئېنىق كۆرسىتىدۇ.",
]
stale = [item for item in forbidden if item in obj]
if stale:
    raise SystemExit(f"Stale Objective 2.2 Wi-Fi terminology remains: {stale}")

print("Objective 2.2 Wi-Fi terminology validation passed")
