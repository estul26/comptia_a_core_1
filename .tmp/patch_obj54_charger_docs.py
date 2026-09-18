from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")
start = text.find('"id": "5.4"')
end = text.find('"id": "5.5"', start)
if start < 0 or end < 0:
    raise SystemExit("Objective 5.4 bounds not found")
obj = text[start:end]

# The live learner content is already technically corrected. Assert it rather than rewriting it.
required_live = [
    "A charger that cannot provide enough supported power may charge the device slowly or fail to charge it.",
    "A compatible charger's higher maximum wattage does not, by itself, damage the battery.",
    "Compatibility depends on the supported charging protocol, voltage, and cable",
    "Compatible charger نىڭ maximum wattage ى يۇقىرى بولۇشى ئۆزىلا battery نى زىيانغا ئۇچراتمايدۇ",
    "Charging problem → Cable → Port/debris → Protocol/voltage/supported-power compatibility",
]
missing = [x for x in required_live if x not in obj]
if missing:
    raise SystemExit(f"Expected corrected learner content is missing: {missing}")

# Update stale Objective 5.4 review documentation to match the live lesson.
review = Path("OBJECTIVE_5_4_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "- Charger power-rating statements are preserved as source teaching; no USB-PD/charging-negotiation material is imported.",
    "- Charger power-rating wording is technically corrected in learner-facing content: **insufficient supported power can cause slow/no charging, while a compatible charger's higher maximum wattage does not by itself damage the battery**. Compatibility depends on the supported charging protocol, voltage, and cable. The archival transcript remains unchanged.",
    "review charger framing",
)
r = replace_exact(
    r,
    "- Charging issue → cable → port/debris → source-described power rating.",
    "- Charging issue → cable → port/debris → charging protocol / voltage / cable / supported-power compatibility.",
    "review charging flow",
)
r = replace_exact(
    r,
    "Preserve source symptom/cause/action relationships, source uncertainty, and safety wording without importing external mobile-repair procedures.",
    "Preserve source symptom/cause/action relationships, source uncertainty, and safety wording, but correct learner-facing charger-compatibility claims when the transcript's wattage shortcut would be technically misleading. Do not expand into device-specific repair procedures.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Update stale transcript-corrections note.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 5.4 source-framing note: the improper-charging section says insufficient charger power can cause slow/no charging and a charger with a higher-than-required power rating can potentially damage the battery over time. Reviewed Uyghur preserves this as the transcript's teaching claim and does not import modern USB-PD/charging-negotiation behavior."
new = (
    "- Objective 5.4 technical correction: the improper-charging transcript says insufficient charger power can cause slow/no charging and suggests a higher-than-required charger power rating can damage the battery over time. "
    "The original transcript remains unchanged; learner-facing English and Uyghur correct this shortcut. **Insufficient supported power may cause slow/no charging, but a compatible charger's higher maximum wattage does not by itself damage the battery.** "
    "Compatibility depends on the supported charging protocol, voltage, and cable, and a compatible device uses the power level it supports."
)
c = replace_exact(c, old, new, "transcript charger correction")
corrections.write_text(c, encoding="utf-8")

print("Objective 5.4 charger documentation alignment passed")
