from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "4.2"')
obj_end = text.find('"id": "5.1"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 4.2 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 4.2 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Correct the private-cloud guarantees and Internet-outage claim.
en_old = (
    "Conversely, a private cloud offers dedicated infrastructure solely for one organization, ensuring enhanced control and security over data and applications.\\n\\n"
    "This isolation from others minimizes the risk of unauthorized access and data breaches. With complete control over data management, compliance with regulatory requirements and internal policies is ensured. "
    "Private clouds also guarantee reliability and availability, maintaining access even during local internet outages.\\n\\n"
    "The limited attack surface increases security, making private clouds ideal for storing sensitive information."
)
en_new = (
    "Conversely, a private cloud provides cloud infrastructure for the exclusive use of one organization, which can give the organization greater control over its environment and security configuration.\\n\\n"
    "Isolation from other organizations can reduce some exposure, but a private cloud does **not** automatically prevent unauthorized access or data breaches, and it does **not** by itself guarantee regulatory compliance. "
    "Compliance still depends on how the environment is designed, configured, secured, monitored, and operated.\\n\\n"
    "Technical correction — availability and Internet outages: A private cloud does **not** automatically guarantee uptime or continued access during a local Internet outage. "
    "Private-cloud infrastructure may exist **on-premises or off-premises**, so availability depends on the deployment architecture and the user's access path. "
    "An on-premises private cloud may remain reachable to local users during an Internet outage if the internal network and required services are still operating; an off-premises private cloud or remote user may depend on Internet/WAN/private-link connectivity and can lose access if that path fails. "
    "High availability comes from architecture such as redundancy and failover, not simply from the cloud being labeled private.\\n\\n"
    "Exam memory: **Private cloud = exclusive use by one organization; outage behavior = topology/access-path dependent.**"
)
english = replace_exact(english, en_old, en_new, "English private-cloud technical correction")

# Replace the Uyghur source-framing caution with a direct learner-facing correction.
ug_old = (
    "**Private cloud**\\n"
    "- بىر organization ئۈچۈن dedicated infrastructure\\n\\n"
    "Source-stated benefits:\\n"
    "- enhanced control\\n"
    "- enhanced security\\n"
    "- data/application isolation\\n"
    "- compliance support\\n"
    "- internal-policy control\\n"
    "- reliability/availability\\n"
    "- sensitive information ئۈچۈن ماس\\n\\n"
    "مەنبە private cloud نىڭ isolation سەۋەبىدىن:\\n"
    "- unauthorized access\\n"
    "- data breach\\n\\n"
    "خەۋپىنى ئازايتىشقا ياردەم بېرىدىغانلىقىنى چۈشەندۈرىدۇ.\\n\\n"
    "### Source-Framing Caution\\n\\n"
    "Transcript يەنە private cloud:\\n"
    "> **local Internet outage ۋاقىتتىمۇ access نى ساقلايدۇ**\\n\\n"
    "دەپ source claim بېرىدۇ.\\n\\n"
    "Reviewed Uyghur بۇنى:\\n"
    "- **مەنبەنىڭ ئۆز teaching claim ى**\\n\\n"
    "سۈپىتىدەلا ساقلايدۇ.\\n\\n"
    "بۇ claim نى ھەر private-cloud architecture ئۈچۈن universal rule دەپ كېڭەيتمەيدۇ، چۈنكى source topology detail بەرمەيدۇ.\\n\\n"
    "**Exam memory: Private cloud = One organization + Dedicated control/security**"
)
ug_new = (
    "**Private cloud**\\n"
    "- بىر organization نىڭ exclusive use ى ئۈچۈن cloud infrastructure\\n"
    "- organization غا environment/security configuration ئۈستىدە تېخىمۇ كۆپ control بېرەلەيدۇ\\n\\n"
    "Isolation باشقا organization لار بىلەن resource exposure نى ئازايتىشقا ياردەم بېرەلەيدۇ. لېكىن:\\n"
    "- unauthorized access نى ئاپتوماتىك يوقىتىۋەتمەيدۇ\\n"
    "- data breach نى ئاپتوماتىك توختاتمايدۇ\\n"
    "- regulatory compliance نى ئاپتوماتىك guarantee قىلمايدۇ\\n\\n"
    "Compliance environment نىڭ design، configuration، security control، monitoring ۋە operation ىغا باغلىق.\\n\\n"
    "### Technical Correction — Internet Outage / Availability\\n\\n"
    "Private cloud بولغانلىقىنىڭ ئۆزى:\\n"
    "- uptime نى guarantee قىلمايدۇ\\n"
    "- local Internet outage ۋاقىتتا access نى چوقۇم ساقلايدۇ دېگەنلىك ئەمەس\\n\\n"
    "Private cloud **on-premises ياكى off-premises** بولالايدۇ. شۇڭا outage ۋاقتىدىكى access:\\n"
    "- deployment architecture\\n"
    "- user نىڭ access path ى\\n"
    "- LAN/WAN/Internet/private-link connectivity\\n\\n"
    "غا باغلىق.\\n\\n"
    "Example:\\n"
    "- on-prem private cloud + local user → Internet ئۈزۈلسىمۇ internal LAN/service ئىشلىسە access داۋاملىشىشى مۇمكىن\\n"
    "- off-prem private cloud ياكى remote user → WAN/Internet/private-link path ئۈزۈلسە access يوقىلىشى مۇمكىن\\n\\n"
    "High availability بولسا redundancy/failover غا ئوخشاش architecture ئارقىلىق قۇرۇلىدۇ؛ پەقەت **private** دېگەن label بىلەن guarantee بولمايدۇ.\\n\\n"
    "**Exam memory: Private cloud = One organization / exclusive use; outage behavior = topology + access path dependent**"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur private-cloud technical correction")

# Update comparison table wording.
uyghur = replace_exact(
    uyghur,
    "| **Private** | One organization / dedicated control |",
    "| **Private** | One organization / exclusive use / greater control; availability depends on architecture |",
    "Uyghur private-cloud comparison row",
)

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 4.2 review documentation.
review = Path("OBJECTIVE_4_2_REVIEW.md")
r = review.read_text(encoding="utf-8")
old = (
    "Private-cloud caution:\n"
    "the transcript says private clouds maintain access during local Internet outages. The reviewed lesson labels this as source teaching rather than a universal topology guarantee."
)
new = (
    "Private-cloud technical correction:\n"
    "- the transcript says private clouds maintain access during local Internet outages and uses guarantee-style wording for reliability/compliance\n"
    "- learner-facing English and Uyghur no longer preserve those claims as study rules\n"
    "- **private cloud = exclusive use by one organization**; it may exist on-premises or off-premises\n"
    "- outage behavior depends on deployment topology and the user's access path\n"
    "- on-prem local access may survive an Internet outage if internal networking/services remain available; off-premises or remote access may depend on WAN/Internet/private-link connectivity\n"
    "- high availability depends on redundancy/failover architecture, not the private-cloud label alone\n"
    "- private cloud can support compliance/security goals but does not automatically guarantee compliance or prevent breaches"
)
r = replace_exact(r, old, new, "review private-cloud correction")
r = replace_exact(
    r,
    "- Preserve source categories, hierarchy and examples.\n- Keep source simplifications/source claims labeled when architecture-dependent.\n- Correct only clear grammatical/transcription artifacts.\n- Do not add cloud services or operational details absent from Objective 4.2.",
    "- Preserve source categories, hierarchy and examples.\n- Correct architecture-dependent source claims when preserving them would create a learner-facing technical error.\n- Keep the private-cloud correction concise: exclusive use, on/off premises, topology-dependent access, and architecture-dependent availability.\n- Correct clear grammatical/transcription artifacts.\n- Do not add unrelated cloud services or operational details absent from Objective 4.2.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 4.2 source-framing note: the private-cloud section states that private clouds maintain access even during local Internet outages. The reviewed Uyghur preserves this as the transcript's own claim and does not generalize it to every private-cloud topology."
new = (
    "- Objective 4.2 technical correction: the private-cloud section says private clouds maintain access during local Internet outages and uses guarantee-style wording for reliability/compliance. "
    "The original transcript remains unchanged; learner-facing English and Uyghur correct this. A private cloud is for **exclusive use by one organization** and may exist **on-premises or off-premises**; outage access therefore depends on topology and access path. "
    "High availability requires architecture such as redundancy/failover, and private-cloud deployment alone does not guarantee compliance, uptime, or freedom from unauthorized access/data breaches."
)
c = replace_exact(c, old, new, "transcript Objective 4.2 private-cloud correction")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "4.2"')
end = final.find('"id": "5.1"', start)
obj = final[start:end]
required = [
    "Technical correction — availability and Internet outages:",
    "Private-cloud infrastructure may exist **on-premises or off-premises**",
    "High availability comes from architecture such as redundancy and failover",
    "Exam memory: **Private cloud = exclusive use by one organization; outage behavior = topology/access-path dependent.**",
    "### Technical Correction — Internet Outage / Availability",
    "Private cloud **on-premises ياكى off-premises** بولالايدۇ.",
    "outage behavior = topology + access path dependent",
    "| **Private** | One organization / exclusive use / greater control; availability depends on architecture |",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 4.2 private-cloud corrections: {missing}")

stale = [
    "Private clouds also guarantee reliability and availability, maintaining access even during local internet outages.",
    "With complete control over data management, compliance with regulatory requirements and internal policies is ensured.",
    "> **local Internet outage ۋاقىتتىمۇ access نى ساقلايدۇ**",
]
stale_found = [x for x in stale if x in obj]
if stale_found:
    raise SystemExit(f"Stale Objective 4.2 private-cloud claims remain: {stale_found}")

print("Objective 4.2 private-cloud patch validation passed")
