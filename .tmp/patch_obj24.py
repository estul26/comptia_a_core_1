from pathlib import Path


def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)


index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "2.4"')
obj_end = text.find('"id": "2.5"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 2.4 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('\", \"uyghur\": \"', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 2.4 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('\", \"uyghur\": \"')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

if "CNAME" in english or "CNAME" in uyghur:
    raise SystemExit("Objective 2.4 already contains CNAME unexpectedly")

# Add current 220-1201-required CNAME material as a clearly labeled Exam Note.
en_old = (
    "Quad A records ensure that domains can be resolved and connected over the IPv6 infrastructure, "
    "future-proofing the internet's expansion. Moving on, we have the MX record or mail exchange record."
)
en_new = (
    "Quad A records ensure that domains can be resolved and connected over the IPv6 infrastructure, "
    "future-proofing the internet's expansion.\\n\\n"
    "Exam Note — CNAME (Canonical Name) record: A CNAME record maps an alias hostname to another hostname, "
    "called its canonical name. It does not map the alias directly to an IP address; DNS then resolves the "
    "target hostname using its own records. For example, www.example.com could be an alias for example.com. "
    "For the exam, remember: CNAME = alias hostname → canonical hostname.\\n\\n"
    "Moving on, we have the MX record or mail exchange record."
)
english = replace_exact(english, en_old, en_new, "English CNAME Exam Note")

ug_old = "**ئەستە تۇتۇڭ:**\\n- **AAAA = IPv6**\\n\\n### MX Record — Mail Exchange Record"
ug_new = (
    "**ئەستە تۇتۇڭ:**\\n- **AAAA = IPv6**\\n\\n"
    "### CNAME Record — Canonical Name — Exam Note\\n\\n"
    "**CNAME record** بىر **alias hostname / FQDN** نى باشقا بىر hostname غا، يەنى ئۇنىڭ **canonical name** ىغا باغلايدۇ.\\n\\n"
    "ئۇ alias نامنى IP address قا بىۋاسىتە باغلىمايدۇ؛ DNS ئالدى بىلەن target hostname نى تېپىپ، ئاندىن شۇ hostname نىڭ ئۆزىدىكى record لار ئارقىلىق IP address نى resolve قىلىدۇ.\\n\\n"
    "مىسال:\\n- `www.example.com` → `example.com`\\n\\n"
    "**Exam memory:**\\n- **CNAME = Alias hostname → Canonical hostname**\\n\\n"
    "### MX Record — Mail Exchange Record"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur CNAME Exam Note")

summary_old = "| **AAAA** | FQDN → IPv6 |\\n| **MX** | Email → mail server |"
summary_new = "| **AAAA** | FQDN → IPv6 |\\n| **CNAME** | Alias hostname → canonical hostname (**Exam Note**) |\\n| **MX** | Email → mail server |"
uyghur = replace_exact(uyghur, summary_old, summary_new, "Uyghur CNAME summary row")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 2.4 review documentation.
review = Path("OBJECTIVE_2_4_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "- DMARC\n\nNo other record types were added.",
    "- DMARC\n\nCurrent 220-1201-required addition:\n- **CNAME — Canonical Name** → alias hostname to canonical hostname — **Exam Note; absent from transcript**\n\nThe original transcript remains unchanged. Learner-facing English and Uyghur add CNAME only as a clearly labeled Exam Note.",
    "review CNAME coverage",
)
r = replace_exact(
    r,
    "- Do not import facts from earlier objectives unless explicitly marked as cross-reference.\n- Document transcript artifacts instead of modifying the original English source.",
    "- Do not import facts from earlier objectives unless explicitly marked as cross-reference.\n- Add facts required by the current 220-1201 objectives but missing from the transcript only as clearly labeled **Exam Notes**.\n- Document transcript artifacts instead of modifying the original English source.",
    "review policy",
)
review.write_text(r, encoding="utf-8")

# Record the source gap and learner-facing correction policy.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
anchor = (
    "- Objective 2.4: the DNS example says `www.certificationsenergy.com`; this appears to be a speech-to-text/name transcription inconsistency relative to the course name. "
    "The reviewed Uyghur avoids relying on that malformed example and uses the source's later `www.example.com` walkthrough; the original English source remains unchanged."
)
addition = anchor + (
    "\n- Objective 2.4 source-gap note: the transcript covers **A, AAAA, MX, TXT, DKIM, SPF, and DMARC** but omits **CNAME (Canonical Name)**, which is required by the current 220-1201 objective. "
    "The original transcript remains unchanged; learner-facing English and Uyghur add CNAME as a clearly labeled **Exam Note** explaining **alias hostname → canonical hostname**."
)
c = replace_exact(c, anchor, addition, "transcript corrections CNAME note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "2.4"')
end = final.find('"id": "2.5"', start)
obj = final[start:end]
required = [
    "Exam Note — CNAME (Canonical Name) record:",
    "CNAME = alias hostname → canonical hostname",
    "### CNAME Record — Canonical Name — Exam Note",
    "**CNAME** | Alias hostname → canonical hostname (**Exam Note**)",
]
missing = [item for item in required if item not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 2.4 CNAME content: {missing}")

# Ensure the change did not spill into neighboring lessons.
if final[:start].count("Exam Note — CNAME") or final[end:].count("Exam Note — CNAME"):
    raise SystemExit("CNAME Exam Note found outside Objective 2.4")

print("Objective 2.4 CNAME patch validation passed")
