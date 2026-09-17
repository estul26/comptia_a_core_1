from pathlib import Path


def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)


def replace_present(text, old, new, label):
    if old not in text:
        raise SystemExit(f"{label}: expected at least one match")
    return text.replace(old, new)


index = Path("index.html")
text = index.read_text(encoding="utf-8")
obj_start = text.find('"id": "3.2"')
obj_end = text.find('"id": "3.3"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 3.2 object boundaries")
en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 3.2 language boundaries")
en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# English learner-facing corrections.
english = replace_present(english, "The 80 stands for augmented.", "The 'a' in CAT6a stands for augmented.", "CAT6a augmented wording")
english = replace_present(english, "For the 80 plus core one exam", "For the A+ Core 1 exam", "A+ Core 1 wording")
english = replace_present(english, "T5-68A", "T568A", "T568A spelling")
english = replace_present(english, "T5-68B", "T568B", "T568B spelling")
english = replace_present(english, "pinup standards", "pinout standards", "pinout spelling")
english = replace_present(english, "DVI-T is the digital variant", "DVI-D is the digital variant", "DVI-D variant")
english = replace_present(english, "where the RG stands for registered jack", "where RJ stands for registered jack", "RJ expansion")
english = replace_present(english, "100BaseTx standard", "100BASE-TX standard", "100BASE-TX")
english = replace_present(english, "1000BaseTx standard", "1000BASE-T standard", "1000BASE-T")
english = replace_present(english, "10GBaseTx standard", "10GBASE-T standard", "10GBASE-T")

direct_old = "These STP cables are commonly used in environments where there are high levels of electromagnetic interference, such as industrial settings or areas with heavy machinery. Another construction consideration is a plenum rating."
direct_new = "These STP cables are commonly used in environments where there are high levels of electromagnetic interference, such as industrial settings or areas with heavy machinery.\\n\\nExam Note — Direct-burial cable: Direct-burial cable is designed for outdoor or underground runs and uses a durable, moisture-resistant outer construction. It is not the same as plenum-rated cable: direct-burial focuses on environmental and moisture protection, while plenum-rated cable focuses on fire and smoke requirements in air-handling spaces.\\n\\nAnother construction consideration is a plenum rating."
english = replace_exact(english, direct_old, direct_new, "English direct-burial Exam Note")

blue_old = "USB 3.0 cables, easily distinguishable by their blue connectors, revolutionized data transfer with substantially increased speeds compared to their predecessors."
blue_new = "USB 3.x ports and connectors have often used blue as a visual convention, but the color is not universal and should not be the only way you identify a USB version. USB 3.0 substantially increased data-transfer speeds compared with earlier USB generations."
english = replace_exact(english, blue_old, blue_new, "English USB color guidance")

rj11 = english.find("RJ11")
heading = max(english.rfind("Exam objective 3.2", 0, rj11), english.rfind("Exam Objective 3.2", 0, rj11))
if rj11 < 0 or heading < 0:
    raise SystemExit("Could not locate final connector-types segment")
adapter_en = "Exam Note — Adapters. Adapters connect devices or cables that use different connector or interface types. Common examples include USB-C-to-HDMI or DisplayPort adapters and USB-to-Ethernet adapters. An adapter can bridge compatible interfaces, but changing the physical connector does not automatically add a capability that the source or destination hardware does not support.\\n\\n"
if "Exam Note — Adapters." in english:
    raise SystemExit("Adapter Exam Note already exists unexpectedly")
english = english[:heading] + adapter_en + english[heading:]

# Matching Uyghur updates.
uyghur = replace_exact(uyghur, "- blue connector بىلەن ئاسان پەرقلەندۈرگىلى بولىدۇ", "- blue color كۆپ ئىشلىتىلىدىغان convention، ئەمما universal rule ئەمەس؛ USB version نى پەقەت رەڭ بىلەنلا بەلگىلىمەڭ", "Uyghur USB color guidance")
uyghur = replace_exact(uyghur, "- مەنبە بۇنى `100BaseTx` دەپ ئاتايدۇ", "- **Canonical standard: 100BASE-TX** (source transcript `100BaseTx` دەپ بېرىدۇ)", "Uyghur 100BASE-TX")
uyghur = replace_exact(uyghur, "- مەنبە بۇنى `1000BaseTx` دەپ ئاتايدۇ", "- **Canonical standard: 1000BASE-T** (source transcript `1000BaseTx` دەپ بېرىدۇ)", "Uyghur 1000BASE-T")
uyghur = replace_exact(uyghur, "**Source wording note:** transcript Ethernet standard names نى `100BaseTx`, `1000BaseTx`, `10GBaseTx` شەكلىدە بېرىدۇ. Reviewed Uyghur speed/distance نى source بويىچە ساقلايدۇ، بۇ standard ناملىرىنى سىرتقى مەنبە بىلەن silently ئالماشتۇرمايدۇ.", "**Source wording note:** transcript Ethernet standard names نى `100BaseTx`, `1000BaseTx`, `10GBaseTx` شەكلىدە بېرىدۇ. Learner-facing study content canonical نام ئىشلىتىدۇ: **100BASE-TX, 1000BASE-T, 10GBASE-T**؛ original transcript بولسا ئۆزگەرتىلمەيدۇ.", "Uyghur Ethernet naming note")

direct_anchor = "**ئەستە تۇتۇڭ:**\\n- **UTP = Twisting only**\\n- **STP = Twisting + Extra shielding**\\n\\n---\\n\\n## Plenum-Rated Cable"
direct_ug = "**ئەستە تۇتۇڭ:**\\n- **UTP = Twisting only**\\n- **STP = Twisting + Extra shielding**\\n\\n---\\n\\n## Direct-Burial Cable — Exam Note\\n\\n**Direct-burial cable** سىرتقى مۇھىت ياكى يەر ئاستىدىكى cable run ئۈچۈن لايىھەلەنگەن.\\n\\nئاساسىي نۇقتىلار:\\n- durable outer construction\\n- moisture/environment protection\\n- outdoor ياكى underground installation\\n\\n**Direct-burial** بىلەن **plenum-rated** نى ئارىلاشتۇرماڭ: direct-burial سىرتقى مۇھىت ۋە نەملىككە قارشى قوغداشقا، plenum-rated بولسا air-handling space دىكى fire/smoke requirement قا مەركەزلەشكەن.\\n\\n---\\n\\n## Plenum-Rated Cable"
uyghur = replace_exact(uyghur, direct_anchor, direct_ug, "Uyghur direct-burial Exam Note")

adapter_ug = "## Adapters — Exam Note\\n\\n**Adapter** connector/interface تۈرى پەرقلىق بولغان device ياكى cable لارنى ئۆزئارا ئۇلاشقا ئىشلىتىلىدۇ.\\n\\nمىسال:\\n- USB-C → HDMI ياكى DisplayPort\\n- USB → Ethernet\\n\\nAdapter compatible interface لارنى bridge قىلالايدۇ، ئەمما پەقەت connector شەكلىنى ئۆزگەرتىش source ياكى destination hardware قوللىمايدىغان capability نى يېڭىدىن پەيدا قىلمايدۇ.\\n\\n**Exam memory: Adapter = Different connector/interface types ئارىسىدا bridge**\\n\\n---\\n\\n## Connector Types"
uyghur = replace_exact(uyghur, "## Connector Types", adapter_ug, "Uyghur Adapter Exam Note")
uyghur = replace_exact(uyghur, "- **STP** → Extra EMI shield\\n- **Plenum** → HVAC air space / fire-safety material", "- **STP** → Extra EMI shield\\n- **Direct-burial** → Outdoor/underground / moisture-resistant construction\\n- **Plenum** → HVAC air space / fire-safety material", "memory-map direct burial")
uyghur = replace_exact(uyghur, "### Storage\\n- **SATA** → Internal drive\\n- **eSATA** → External drive\\n\\n### Connectors", "### Storage\\n- **SATA** → Internal drive\\n- **eSATA** → External drive\\n\\n### Adapters\\n- **Adapter** → Bridge compatible connector/interface types; does not create unsupported capabilities\\n\\n### Connectors", "memory-map adapters")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Review docs.
review = Path("OBJECTIVE_3_2_REVIEW.md")
r = review.read_text(encoding="utf-8")
r = replace_exact(r, "- plenum-rated cable\n- T568A / T568B", "- direct-burial cable — **Exam Note; absent from transcript but required by current 220-1201**\n- plenum-rated cable\n- T568A / T568B", "review direct burial")
r = replace_exact(r, "The transcript's Ethernet-standard labels are not externally normalized.", "The original transcript's Ethernet-standard labels remain unchanged in `source/`. Learner-facing study content uses the canonical names **100BASE-TX, 1000BASE-T, and 10GBASE-T**.", "review Ethernet naming")
r = replace_exact(r, "The serial-vs-USB wording is preserved as source framing, not externally corrected.", "The original transcript incorrectly contrasts legacy serial transmission with `parallel transmission used in interfaces like USB`. Learner-facing English and Uyghur explicitly correct this: **USB is also a serial interface (Universal Serial Bus)**. The source transcript remains unchanged.", "review serial/USB")
r = replace_exact(r, "## Connector types\n", "## Adapters\n\nThe current 220-1201 objective includes **adapters**, but the transcript has no dedicated adapter section. Learner-facing English and Uyghur therefore add a clearly labeled **Exam Note** explaining that adapters bridge compatible connector/interface types and do not automatically create unsupported capabilities.\n\n## Connector types\n", "review adapters")
r = replace_exact(r, "- Keep source-era claims source-attributed.\n- Do not import newer cable/interface specifications.", "- Keep source-era claims source-attributed.\n- Correct materially false learner-facing claims while preserving the original transcript.\n- Add current 220-1201-required facts missing from the transcript as clearly labeled **Exam Notes**.\n- Do not import unrelated newer cable/interface specifications.", "review policy")
review.write_text(r, encoding="utf-8")

corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
c = replace_exact(c, "- Objective 3.2: `T5-68A`, `T5-68B`, and `pinup standards` are treated as speech-to-text errors for **T568A**, **T568B**, and **pinout standards**.", "- Objective 3.2: `T5-68A`, `T5-68B`, and `pinup standards` are treated as speech-to-text errors for **T568A**, **T568B**, and **pinout standards** in learner-facing study content; the original transcript remains unchanged.", "corrections pinout")
c = replace_exact(c, "- Objective 3.2: the DVI narration says `DVI-T is the digital variant`, but the same source section later summarizes `DVI-D transmits digital signals`; reviewed Uyghur uses canonical **DVI-D**.", "- Objective 3.2: the DVI narration says `DVI-T is the digital variant`, but the same source section later summarizes `DVI-D transmits digital signals`; learner-facing study content uses canonical **DVI-D**.", "corrections DVI")
c = replace_exact(c, "- Objective 3.2: `RJ11, where the RG stands for registered jack` is treated as a speech-to-text error; reviewed Uyghur uses **RJ = Registered Jack**.", "- Objective 3.2: `RJ11, where the RG stands for registered jack` is treated as a speech-to-text error; learner-facing study content uses **RJ = Registered Jack**.", "corrections RJ")
c = replace_exact(c, "- Objective 3.2 source-scope note: the transcript labels Ethernet standards as `100BaseTx`, `1000BaseTx`, and `10GBaseTx`. The reviewed Uyghur preserves the source-stated speed/distance teaching and does not silently substitute externally verified standard names.", "- Objective 3.2 source-scope note: the transcript labels Ethernet standards as `100BaseTx`, `1000BaseTx`, and `10GBaseTx`. The original transcript remains unchanged; learner-facing content normalizes these to **100BASE-TX, 1000BASE-T, and 10GBASE-T**.", "corrections Ethernet")
c = replace_exact(c, "- Objective 3.2 source-framing note: the serial-cable segment contrasts serial transmission with `parallel transmission used in interfaces like USB`. Reviewed Uyghur preserves the source lesson without silently replacing that claim from outside knowledge.", "- Objective 3.2 technical correction: the serial-cable segment incorrectly contrasts serial transmission with `parallel transmission used in interfaces like USB`. The original transcript remains unchanged; learner-facing English and Uyghur explicitly state that **USB is a serial interface**.", "corrections serial/USB")
lightning = "- Objective 3.2 source-time note: Lightning connector/device wording is retained as transcript-era course content and is not updated from current Apple product information."
extra = "- Objective 3.2 source-gap note: the transcript does not provide dedicated **direct-burial cable** or **adapter** teaching required by the current 220-1201 objective. Learner-facing English and Uyghur add both as clearly labeled **Exam Notes**.\n- Objective 3.2 identification note: the transcript presents blue connectors as an easy USB 3.0 identifier. Learner-facing content clarifies that blue is a common convention, not a universal rule.\n" + lightning
c = replace_exact(c, lightning, extra, "corrections added notes")
corrections.write_text(c, encoding="utf-8")

# Scoped verification: only Objective 3.2 English learner pane for stale source artifacts.
updated = index.read_text(encoding="utf-8")
start = updated.find('"id": "3.2"')
end = updated.find('"id": "3.3"', start)
en_m = updated.find('"english": "', start, end)
ug_m = updated.find('", "uyghur": "', en_m, end)
english_final = updated[en_m:ug_m]
required = ["Exam Note — Direct-burial cable:", "Exam Note — Adapters.", "100BASE-TX standard", "1000BASE-T standard", "10GBASE-T standard", "USB is also a serial interface", "The 'a' in CAT6a stands for augmented", "DVI-D is the digital variant", "where RJ stands for registered jack"]
missing = [x for x in required if x not in english_final]
if missing:
    raise SystemExit(f"Missing expected Objective 3.2 English content: {missing}")
forbidden = ["The 80 stands for augmented.", "For the 80 plus core one exam", "pinup standards", "DVI-T is the digital variant", "where the RG stands for registered jack", "easily distinguishable by their blue connectors"]
stale = [x for x in forbidden if x in english_final]
if stale:
    raise SystemExit(f"Stale Objective 3.2 English wording remains: {stale}")
if "## Direct-Burial Cable — Exam Note" not in updated or "## Adapters — Exam Note" not in updated or "USB version نى پەقەت رەڭ بىلەنلا بەلگىلىمەڭ" not in updated:
    raise SystemExit("Missing expected Uyghur Objective 3.2 additions")
print("Objective 3.2 rebased patch verification passed")
