from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "2.8"')
obj_end = text.find('"id": "3.1"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 2.8 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 2.8 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Replace the generic overclaim with a verification/qualification/certification distinction.
en_old = (
    "The cable tester is an analytical tool, essential for verifying the integrity of network cables. "
    "It checks for proper wire pinouts, essential for communication between devices, evaluates signal quality by measuring resistance, signal attenuation, noise, and interference, and can even estimate the length of a cable. "
    "This tool is crucial not just for troubleshooting, but also for certifying that a cable meets the required performance standards before it becomes part of a critical network infrastructure."
)
en_new = (
    "A cable tester is used to check network cabling, but the exact capabilities depend on the class of tester. "
    "A basic verification tester checks connectivity—especially continuity and wiremap/pinout—and can identify wiring faults such as opens, shorts, or miswires; some models also provide features such as cable length or toning.\\n\\n"
    "Exam Note — Verification vs qualification vs certification: A qualification tester goes beyond basic verification to determine whether an existing link can support a particular network technology or speed. "
    "A certification tester (cable certifier) performs the standards-based measurements required to determine whether installed cabling passes or fails a defined cabling standard/category. "
    "Do not assume a basic cable tester can certify cable performance.\\n\\n"
    "Source correction note: the transcript groups resistance, attenuation, noise/interference, cable-length estimation, and performance certification under one generic cable tester. "
    "Learner-facing study content separates these capability levels: advanced signal/performance measurements are model- and tester-class-dependent, and standards certification requires certification-grade test equipment.\\n\\n"
    "Memory rule: Verification = wired correctly? Qualification = can it support the application/speed? Certification = does it meet the cabling standard?"
)
english = replace_exact(english, en_old, en_new, "English cable tester capability correction")

# Replace the Uyghur generic tester overclaim section.
ug_old = (
    "**Cable tester** — network cable نىڭ توغرا ئىشلەۋاتقانلىقى ۋە integrity سىنى تەكشۈرۈشكە ئىشلىتىلىدىغان diagnostic / analytical tool.\\n\\n"
    "مەنبە cable tester نىڭ تۆۋەندىكى ئىشلارنى تەكشۈرەلەيدىغانلىقىنى بايان قىلىدۇ:\\n\\n"
    "- **wire pinout** نىڭ توغرىلىقى\\n"
    "- resistance\\n"
    "- signal attenuation\\n"
    "- noise\\n"
    "- interference\\n"
    "- cable length نى تەخمىنەن باھالاش\\n\\n"
    "### Pinout نى تەكشۈرۈش\\n\\n"
    "Cable ئىچىدىكى سىملار connector غا توغرا pin تەرتىپىدە ئۇلانمىسا، network communication توغرا ئىشلىمەسلىكى مۇمكىن.\\n\\n"
    "Cable tester:\\n"
    "- wire-to-pin connection نى تەكشۈرۈپ\\n"
    "- cable نىڭ توغرا سىملىنىشىغا ياردەم بېرىدۇ\\n\\n"
    "### Signal Quality\\n\\n"
    "مەنبە cable tester نىڭ:\\n"
    "- resistance\\n"
    "- attenuation\\n"
    "- noise\\n"
    "- interference\\n\\n"
    "قاتارلىق ئامىللارنى ئۆلچەش ئارقىلىق signal quality نى باھالىيالايدىغانلىقىنى چۈشەندۈرىدۇ.\\n\\n"
    "### Troubleshooting ۋە Certification\\n\\n"
    "Cable tester:\\n"
    "- مەسىلە بار cable نى تېپىشتا\\n"
    "- cable network infrastructure غا قوشۇلۇشتىن بۇرۇن performance standard غا ماس كېلىدىغانلىقىنى دەلىللەشتە\\n\\n"
    "مۇھىم.\\n\\n"
    "**ئەستە تۇتۇڭ:**\\n\\n"
    "> **Cable tester = pinout + cable integrity / signal quality تەكشۈرۈش**"
)
ug_new = (
    "**Cable tester** — network cable نى تەكشۈرۈشكە ئىشلىتىلىدىغان قورال، ئەمما capability سى tester نىڭ **class/model** ىغا باغلىق.\\n\\n"
    "### 1. Verification Tester — Basic Cable Tester\\n\\n"
    "ئاساسىي verification tester كۆپىنچە:\\n"
    "- **continuity**\\n"
    "- **wiremap / pinout**\\n"
    "- open / short / miswire غا ئوخشاش wiring fault\\n\\n"
    "لارنى تەكشۈرىدۇ. بەزى model لار cable length ياكى toning غا ئوخشاش قوشۇمچە feature نىمۇ تەمىنلىشى مۇمكىن.\\n\\n"
    "**Exam memory:** **Verification = Cable توغرا سىملىنامدۇ؟**\\n\\n"
    "### 2. Qualification Tester\\n\\n"
    "Qualification tester basic verification دىن ھالقىپ، بار بولغان cable/link نىڭ:\\n"
    "- مەلۇم network technology\\n"
    "- مەلۇم speed/application\\n\\n"
    "نى قوللىيالامدۇ-يوق، شۇنى باھالايدۇ.\\n\\n"
    "**Exam memory:** **Qualification = بۇ cable بۇ speed/application نى كۆتۈرەلەمدۇ؟**\\n\\n"
    "### 3. Certification Tester / Cable Certifier\\n\\n"
    "Certification tester — installed cabling نىڭ بەلگىلەنگەن cabling standard/category غا ماس كېلىدىغان-كەلمەيدىغانلىقىنى standards-based measurement ئارقىلىق **Pass/Fail** قىلىپ باھالايدىغان advanced tool.\\n\\n"
    "**Basic cable tester نى certification tester دەپ قارىماڭ.** Standards certification ئۈچۈن certification-grade test equipment كېرەك.\\n\\n"
    "### Source Correction Note\\n\\n"
    "Original transcript resistance، attenuation، noise/interference، cable-length estimation ۋە performance certification نى بىر generic **cable tester** ئاستىدا بىرلەشتۈرۈپ چۈشەندۈرىدۇ. Original transcript ئۆزگەرتىلمەيدۇ.\\n\\n"
    "Learner-facing study rule:\\n"
    "- advanced signal/performance measurement → model/tester-class غا باغلىق\\n"
    "- standards certification → certification-grade tester\\n\\n"
    "**ئەستە تۇتۇڭ:**\\n"
    "> **Verification = Wired correctly?**\\n"
    "> **Qualification = Supports speed/application?**\\n"
    "> **Certification = Meets cabling standard?**"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur cable tester capability correction")

# Update the quick comparison table entry.
uyghur = replace_exact(
    uyghur,
    "| **Cable tester** | Pinout، integrity، signal quality ۋە cable length نى تەكشۈرۈش/باھالاش |",
    "| **Cable tester** | Basic verification: continuity / wiremap / pinout; advanced qualification/certification depends on tester class |",
    "Uyghur cable tester comparison row",
)

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 2.8 review documentation.
review = Path("OBJECTIVE_2_8_REVIEW.md")
r = review.read_text(encoding="utf-8")
old_review = (
    "## Cable tester\\n\\n"
    "Source-stated checks:\\n"
    "- proper wire pinout\\n"
    "- resistance\\n"
    "- signal attenuation\\n"
    "- noise\\n"
    "- interference\\n"
    "- estimated cable length\\n"
    "- performance certification before critical deployment\\n\\n"
    "The translation preserves these as one source-described tester. It does not split them into different industry tester categories."
)
new_review = (
    "## Cable tester\\n\\n"
    "The transcript groups all of the following under one generic cable tester:\\n"
    "- proper wire pinout\\n"
    "- resistance\\n"
    "- signal attenuation\\n"
    "- noise/interference\\n"
    "- estimated cable length\\n"
    "- performance certification\\n\\n"
    "Learner-facing English and Uyghur now correct that overgeneralization by distinguishing tester levels:\\n"
    "- **verification/basic tester:** continuity + wiremap/pinout; wiring faults; optional features vary by model\\n"
    "- **qualification tester:** determines whether an existing link can support a specific network technology/speed/application\\n"
    "- **certification tester/cable certifier:** performs standards-based measurements and produces standards-compliance pass/fail results\\n\\n"
    "The original transcript remains unchanged. The key study correction is: **a basic cable tester is not automatically a cable certifier**."
)
r = replace_exact(r, old_review, new_review, "review cable tester section")
r = replace_exact(
    r,
    "- Preserve all source-stated connector/tool examples.\\n- Do not introduce extra tools such as TDR, OTDR, packet sniffer or spectrum analyzer.",
    "- Preserve all source-stated connector/tool examples, but correct capability overgeneralizations that could create a study mistake.\\n- Distinguish **verification, qualification, and certification** without expanding into unrelated troubleshooting tools.\\n- Do not introduce extra tools such as TDR, OTDR, packet sniffer or spectrum analyzer.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Update transcript corrections/source-framing record.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
old = "- Objective 2.8 source-scope note: the cable-tester segment says the tool can check pinouts, measure resistance/attenuation/noise/interference, estimate length, and certify performance. The reviewed Uyghur preserves that transcript-level description without splitting those capabilities across different tester classes from outside knowledge."
new = (
    "- Objective 2.8 technical correction: the cable-tester segment groups pinout, resistance/attenuation/noise/interference, length estimation, and standards certification under one generic tester. "
    "The original transcript remains unchanged; learner-facing English and Uyghur now distinguish **verification/basic testers** (continuity/wiremap), **qualification testers** (whether a link supports a target speed/application), and **certification testers/cable certifiers** (standards-based pass/fail). "
    "Advanced signal/performance measurements are treated as model/tester-class dependent rather than universal basic-tester capabilities."
)
c = replace_exact(c, old, new, "transcript Objective 2.8 tester correction")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "2.8"')
end = final.find('"id": "3.1"', start)
obj = final[start:end]
required = [
    "Exam Note — Verification vs qualification vs certification:",
    "Do not assume a basic cable tester can certify cable performance.",
    "Verification = wired correctly? Qualification = can it support the application/speed? Certification = does it meet the cabling standard?",
    "### 1. Verification Tester — Basic Cable Tester",
    "### 2. Qualification Tester",
    "### 3. Certification Tester / Cable Certifier",
    "**Basic cable tester نى certification tester دەپ قارىماڭ.**",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 2.8 cable tester correction: {missing}")

forbidden = [
    "This tool is crucial not just for troubleshooting, but also for certifying that a cable meets the required performance standards",
    "> **Cable tester = pinout + cable integrity / signal quality تەكشۈرۈش**",
]
stale = [x for x in forbidden if x in obj]
if stale:
    raise SystemExit(f"Stale generic cable tester overclaim remains: {stale}")

print("Objective 2.8 cable tester capability patch validation passed")
