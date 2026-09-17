from pathlib import Path


def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)


index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "3.5"')
obj_end = text.find('"id": "3.6"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.5 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('\", \"uyghur\": \"', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.5 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('\", \"uyghur\": \"')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Learner-facing English: keep LGA/PGA mechanics, remove vendor-as-socket shortcut.
en_old = (
    "Therefore, an Intel CPU cannot be installed in a motherboard intended for an AMD CPU and vice versa. "
    "This is primarily due to the different CPU socket types they use. Intel processors typically use an LGA type socket, which is short for land grid array."
)
en_new = (
    "Therefore, an Intel CPU cannot be installed in a motherboard intended for an AMD CPU and vice versa. "
    "CPU compatibility depends on the exact processor platform, socket, chipset support, and motherboard firmware—not on the vendor name alone. "
    "One common socket design is LGA, which stands for land grid array. The transcript uses Intel processors as its LGA example."
)
english = replace_exact(english, en_old, en_new, "English LGA vendor wording")

en_old2 = (
    "This design facilitates easy installation and removal of the CPU, reducing the risk of damage during handling. "
    "Conversely, AMD processors commonly utilize PGA or pin grid array sockets. In this configuration, the CPU itself contains a grid of pins that align with corresponding holes on the motherboard socket, creating a grid-like pattern for connection."
)
en_new2 = (
    "This design facilitates easy installation and removal of the CPU, reducing the risk of damage during handling. "
    "Another socket design is PGA, or pin grid array. The transcript uses earlier AMD desktop processors as its PGA example. "
    "In this configuration, the CPU itself contains a grid of pins that align with corresponding holes on the motherboard socket, creating a grid-like pattern for connection.\\n\\n"
    "Exam Note — CPU socket compatibility: Do not memorize Intel = LGA and AMD = PGA as a universal rule. "
    "Socket design changes by platform and generation. For example, AMD Socket AM5 uses a 1718-pin LGA design. "
    "For installation questions, identify the exact CPU platform/socket and verify motherboard support. "
    "Memory rule: vendor ≠ socket type; platform/generation determines compatibility."
)
english = replace_exact(english, en_old2, en_new2, "English PGA vendor wording and AM5 Exam Note")

# Uyghur: replace source-time caution with explicit current study guidance while preserving source attribution.
ug_old = (
    "### Source-time caution\\n\\n"
    "بۇ Intel=LGA / AMD=PGA سېلىشتۇرمىسى **transcript نىڭ ئۆز teaching model ى**. Reviewed Uyghur بۇنى current CPU socket market نىڭ ھەممە ئەھۋالىغا ماس كېلىدىغان مەڭگۈلۈك rule دەپ كېڭەيتمەيدۇ.\\n\\n"
    "**Exam memory:**\\n"
    "- **LGA** = CPU contact pads / socket contacts\\n"
    "- **PGA** = CPU pins / socket holes"
)
ug_new = (
    "### Current Socket Guidance — Exam Note\\n\\n"
    "**Source note:** transcript Intel نى LGA بىلەن، AMD نى PGA بىلەن باغلاپ چۈشەندۈرىدۇ. Original transcript ئۆزگەرتىلمەيدۇ.\\n\\n"
    "ئەمما بۇنى current market ئۈچۈن universal rule دەپ ئەستە ساقلىماڭ. **Socket type platform/generation غا باغلىق.**\\n\\n"
    "مۇھىم current example:\\n"
    "- **AMD Socket AM5 = 1718-pin LGA**\\n\\n"
    "شۇڭا CPU ئورنىتىش/ماسلاشتۇرۇش سوئالىدا vendor نامىغا قاراپلا LGA ياكى PGA دەپ پەرەز قىلماڭ. Exact CPU platform/socket نى motherboard support بىلەن ماسلاشتۇرۇڭ.\\n\\n"
    "**Exam memory:**\\n"
    "- **LGA** = CPU contact pads / socket contacts\\n"
    "- **PGA** = CPU pins / socket holes\\n"
    "- **Vendor ≠ socket type**\\n"
    "- **Platform / generation → compatibility**\\n"
    "- **AM5 → LGA**"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur current socket guidance")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 3.5 review documentation.
review = Path("OBJECTIVE_3_5_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "Intel=LGA / AMD=PGA is kept as source-time framing, not universal current guidance.",
    "The original transcript uses Intel=LGA / AMD=PGA as its teaching model. Learner-facing English and Uyghur no longer present that as a universal current rule. They explicitly teach that socket type depends on the processor platform/generation and add **AMD Socket AM5 = 1718-pin LGA** as a current example. The original transcript remains unchanged.",
    "review socket guidance",
)
r = replace_exact(
    r,
    "- Mark time-sensitive, overgeneralized, or questionable source wording as source framing rather than silently rewriting it from outside knowledge.\n- Avoid adding motherboard/CPU/security specifications absent from the transcript.",
    "- Preserve the original transcript, but correct materially outdated or overgeneralized learner-facing guidance when it could create an exam or real-world compatibility mistake.\n- Add narrowly scoped current examples only when they clarify required compatibility concepts; here, **AM5 uses LGA** demonstrates why vendor name alone does not determine socket type.\n- Avoid unrelated motherboard/CPU/security specifications absent from the objective.",
    "review translation policy",
)
review.write_text(r, encoding="utf-8")

# Update transcript correction/source-gap record.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 3.5 source-time note: the Intel=LGA / AMD=PGA comparison is presented as the transcript's teaching model and is not generalized into a current universal socket rule."
new = (
    "- Objective 3.5 source-time correction: the transcript teaches Intel=LGA / AMD=PGA as a broad comparison. "
    "The original transcript remains unchanged, but learner-facing English and Uyghur explicitly state that **socket type depends on platform/generation rather than vendor name alone** and add the current example **AMD Socket AM5 = 1718-pin LGA**."
)
c = replace_exact(c, old, new, "transcript corrections socket note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "3.5"')
end = final.find('"id": "3.6"', start)
obj = final[start:end]
required = [
    "Exam Note — CPU socket compatibility:",
    "AMD Socket AM5 uses a 1718-pin LGA design",
    "vendor ≠ socket type; platform/generation determines compatibility",
    "### Current Socket Guidance — Exam Note",
    "**AM5 → LGA**",
]
missing = [item for item in required if item not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 3.5 socket content: {missing}")

forbidden = [
    "Intel processors typically use an LGA type socket",
    "Conversely, AMD processors commonly utilize PGA",
    "current CPU socket market نىڭ ھەممە ئەھۋالىغا ماس كېلىدىغان مەڭگۈلۈك rule",
]
stale = [item for item in forbidden if item in obj]
if stale:
    raise SystemExit(f"Stale Objective 3.5 socket wording remains: {stale}")

print("Objective 3.5 socket modernization validation passed")
