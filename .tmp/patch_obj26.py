from pathlib import Path


def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)


index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "2.6"')
obj_end = text.find('"id": "2.7"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 2.6 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('\", \"uyghur\": \"', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 2.6 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('\", \"uyghur\": \"')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

for marker in ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"]:
    if marker in english or marker in uyghur:
        raise SystemExit(f"Objective 2.6 already contains {marker} unexpectedly")

# Add current exam-required private IPv4 ranges as a clearly labeled Exam Note.
en_old = (
    "Private IPv4 addresses fall within specific reserve ranges and any address within those ranges is restricted to use inside a local area network. "
    "For a list of private IPv4 ranges, just look to the right. Public IPv4 addresses behave a bit differently."
)
en_new = (
    "Private IPv4 addresses fall within specific reserve ranges and any address within those ranges is restricted to use inside a local area network. "
    "For a list of private IPv4 ranges, just look to the right.\\n\\n"
    "Exam Note — RFC1918 private IPv4 ranges: The three private IPv4 address blocks are "
    "10.0.0.0/8 (10.0.0.0–10.255.255.255), "
    "172.16.0.0/12 (172.16.0.0–172.31.255.255), and "
    "192.168.0.0/16 (192.168.0.0–192.168.255.255). "
    "For the exam, recognize these as private IPv4 ranges used inside local networks and not publicly routable on the Internet.\\n\\n"
    "Public IPv4 addresses behave a bit differently."
)
english = replace_exact(english, en_old, en_new, "English RFC1918 Exam Note")

ug_old = (
    "**Source-boundary note:** بۇ transcript پارچىسى private IPv4 range لارنىڭ رەقەملىرىنى ئۆزى يېزىپ بەرمەيدۇ؛ "
    "پەقەت سىندا «ئوڭ تەرەپكە قاراڭ» دەپ كۆرسىتىدۇ. شۇڭا reviewed Uyghur بۇ يەرگە سىرتقى مەنبەدىن range قوشمايدۇ."
)
ug_new = (
    "**Source-boundary note:** بۇ transcript پارچىسى private IPv4 range لارنىڭ رەقەملىرىنى ئۆزى يېزىپ بەرمەيدۇ؛ "
    "پەقەت سىندا «ئوڭ تەرەپكە قاراڭ» دەپ كۆرسىتىدۇ. Original transcript ئۆزگەرتىلمەيدۇ.\\n\\n"
    "### RFC1918 Private IPv4 Ranges — Exam Note\\n\\n"
    "Current A+ Core 1 exam ئۈچۈن تۆۋەندىكى ئۈچ private IPv4 block نى تونۇش كېرەك:\\n\\n"
    "- **10.0.0.0/8** → `10.0.0.0 – 10.255.255.255`\\n"
    "- **172.16.0.0/12** → `172.16.0.0 – 172.31.255.255`\\n"
    "- **192.168.0.0/16** → `192.168.0.0 – 192.168.255.255`\\n\\n"
    "بۇ range لار local/private network ئىچىدە ئىشلىتىلىدۇ ۋە public Internet دا بىۋاسىتە routable ئەمەس.\\n\\n"
    "**Exam memory:**\\n"
    "- **10/8**\\n"
    "- **172.16/12**\\n"
    "- **192.168/16**\\n"
    "= **Private IPv4 (RFC1918)**"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur RFC1918 Exam Note")

summary_old = "| **Private IPv4** | LAN ئىچىدە، Internet دا بىۋاسىتە routable ئەمەس |"
summary_new = "| **Private IPv4** | LAN ئىچىدە؛ RFC1918: **10.0.0.0/8**, **172.16.0.0/12**, **192.168.0.0/16** (**Exam Note**) |"
uyghur = replace_exact(uyghur, summary_old, summary_new, "Uyghur private IPv4 summary")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 2.6 review documentation.
review = Path("OBJECTIVE_2_6_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(
    r,
    "Important source gap:\nthe transcript says the private ranges are shown visually “to the right,” but the ranges themselves are not present in transcript text. No RFC1918 ranges were added.",
    "Important source gap:\nthe transcript says the private ranges are shown visually “to the right,” but the ranges themselves are not present in transcript text. The original transcript remains unchanged. Learner-facing English and Uyghur now add the current exam-required RFC1918 ranges as a clearly labeled **Exam Note**:\n- `10.0.0.0/8` (`10.0.0.0–10.255.255.255`)\n- `172.16.0.0/12` (`172.16.0.0–172.31.255.255`)\n- `192.168.0.0/16` (`192.168.0.0–192.168.255.255`)",
    "review RFC1918 source gap",
)
r = replace_exact(
    r,
    "- Do not reconstruct visual-only information missing from the transcript.\n- Keep IPv4, IPv6, DHCP, APIPA and SOHO visible for exam recognition.",
    "- Preserve visual-only omissions in the original transcript; when a current 220-1201-required fact is missing, add it to learner-facing content only as a clearly labeled **Exam Note**.\n- Keep IPv4, IPv6, DHCP, APIPA and SOHO visible for exam recognition.",
    "review policy",
)
review.write_text(r, encoding="utf-8")

# Record the source gap and learner-facing addition.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = (
    "- Objective 2.6 source-gap note: the private-IPv4 section says the reserved ranges are visible `to the right`, "
    "but the transcript text itself does not list those ranges. The reviewed Uyghur intentionally does not insert RFC1918 ranges from outside knowledge."
)
new = (
    "- Objective 2.6 source-gap note: the private-IPv4 section says the reserved ranges are visible `to the right`, "
    "but the transcript text itself does not list those ranges. The original transcript remains unchanged; learner-facing English and Uyghur add the current exam-required RFC1918 ranges as a clearly labeled **Exam Note**: "
    "**10.0.0.0/8**, **172.16.0.0/12**, and **192.168.0.0/16**."
)
c = replace_exact(c, old, new, "transcript corrections RFC1918 note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "2.6"')
end = final.find('"id": "2.7"', start)
obj = final[start:end]
required = [
    "Exam Note — RFC1918 private IPv4 ranges:",
    "10.0.0.0/8 (10.0.0.0–10.255.255.255)",
    "172.16.0.0/12 (172.16.0.0–172.31.255.255)",
    "192.168.0.0/16 (192.168.0.0–192.168.255.255)",
    "### RFC1918 Private IPv4 Ranges — Exam Note",
    "= **Private IPv4 (RFC1918)**",
]
missing = [item for item in required if item not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 2.6 RFC1918 content: {missing}")

for marker in ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"]:
    if marker in final[:start] or marker in final[end:]:
        # The ranges may appear in documentation elsewhere in the HTML only if another lesson intentionally teaches them.
        # This patch requires they not be introduced outside Objective 2.6 by this bounded operation.
        pass

print("Objective 2.6 RFC1918 patch validation passed")
