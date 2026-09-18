from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    n=text.count(old)
    if n!=expected: raise SystemExit(f"{label}: expected {expected}, found {n}")
    return text.replace(old,new)

p=Path("index.html")
t=p.read_text(encoding="utf-8")

# Objective 2.1 — explicit Supplemental label for SNMP.
s=t.find('"id": "2.1"'); e=t.find('"id": "2.2"',s); o=t[s:e]
o=replace_exact(
    o,
    "Next, we have SNMP, or Simple Network Management Protocol. While SNMP is not directly tested within this exam objective it is an important protocol to become familiar with as you continue advancing in networking.",
    "Supplemental — SNMP (Simple Network Management Protocol): SNMP is not directly tested within this exam objective, but it is useful supporting networking knowledge. SNMP uses ports 161 and 162.",
    "English SNMP supplemental label"
)
# Uyghur has its own SNMP explanation; add an explicit scope label at its first SNMP heading/intro.
if "SNMP" not in o: raise SystemExit("SNMP unexpectedly absent")
# Insert once in Uyghur side before its first SNMP occurrence after language split.
ug=o.find('", "uyghur": "')
q=o.find("SNMP",ug)
if q<0: raise SystemExit("Uyghur SNMP not found")
o=o[:q]+"Supplemental — "+o[q:]
t=t[:s]+o+t[e:]

# Objective 3.2 — USB 1.x historical material is Legacy/Supplemental.
s=t.find('"id": "3.2"'); e=t.find('"id": "3.3"',s); o=t[s:e]
o=replace_exact(
    o,
    "USB cables have undergone significant evolution since their introduction with USB version 1.0. Initially, USB 1.0 provided modest data transfer speeds reaching up to 12 megabits per second, suitable for basic peripherals.",
    "Supplemental / Legacy — USB 1.x: USB cables have undergone significant evolution since their introduction with USB version 1.0. USB 1.x is retained here as historical context; current Objective 3.2 study emphasis is on USB 2.0 and USB 3.x. Initially, USB 1.0 provided modest data transfer speeds reaching up to 12 megabits per second, suitable for basic peripherals.",
    "English USB 1.x scope label"
)
# Add a concise Uyghur scope note immediately before the first Uyghur USB 1.x occurrence.
ug=o.find('", "uyghur": "')
for needle in ["USB 1.0","USB version 1.0","USB 1.x"]:
    q=o.find(needle,ug)
    if q>=0: break
if q<0: raise SystemExit("Uyghur USB 1.x occurrence not found")
o=o[:q]+"**Supplemental / Legacy:** current Objective 3.2 study emphasis = USB 2.0 + USB 3.x. Historical context: "+o[q:]
t=t[:s]+o+t[e:]

# Objective 3.4 — identify MiniSD correctly and label MiniSD/xD legacy/supplemental.
s=t.find('"id": "3.4"'); e=t.find('"id": "3.5"',s); o=t[s:e]
o=replace_exact(
    o,
    "Many SD cards are a smaller variant of the SD card format designed for use in compact electronic devices where space is limited.",
    "MiniSD is a smaller legacy variant of the SD card format designed for use in compact electronic devices where space is limited.",
    "English MiniSD transcript correction"
)
o=replace_exact(
    o,
    "However, many SD cards are less common nowadays as they have largely been supplanted by the even smaller micro SD format.",
    "MiniSD cards are now legacy/less common and have largely been supplanted by the smaller microSD format.",
    "English MiniSD legacy label"
)
o=replace_exact(
    o,
    "And then there are XD cards, short for extreme digital. These memory cards were developed by Olympus and Fujifilm as a proprietary memory card format for digital cameras.",
    "Supplemental / Legacy — xD card: The transcript calls these XD cards, short for extreme digital. These memory cards were developed by Olympus and Fujifilm as a proprietary memory card format for digital cameras.",
    "English xD legacy label"
)
o=replace_exact(o,"### MiniSD\\n\\n","### MiniSD — Legacy / Supplemental\\n\\n","Uyghur MiniSD label")
o=replace_exact(o,"### xD Card\\n\\n","### xD Card — Legacy / Supplemental\\n\\n","Uyghur xD label")
t=t[:s]+o+t[e:]
p.write_text(t,encoding="utf-8")

# Update audit checklist: all remaining low items complete.
audit=Path("CONTENT_AUDIT_220_1201.md")
a=audit.read_text(encoding="utf-8")
for item in [
"**2.1 — Mark SNMP 161/162 supplemental**",
"**3.2 — Mark USB 1.x material supplemental**",
"**3.4 — Consider labeling uncommon legacy removable formats"
]:
    lines=a.splitlines()
    found=False
    for i,line in enumerate(lines):
        if item in line:
            lines[i]=line.replace("- [ ] ","- [x] ")
            found=True
    if not found: raise SystemExit(f"Audit item not found: {item}")
    a="\n".join(lines)+"\n"
a=a.replace(
"Only three low/scope items remain:\n1. Objective 2.1 — explicitly label SNMP 161/162 **Supplemental** (the lesson already says it is not directly tested in 2.1).\n2. Objective 3.2 — label USB 1.x **Supplemental/Legacy**.\n3. Objective 3.4 — label MiniSD/xD and similar uncommon removable formats **Legacy/Supplemental**.",
"All three final low/scope-labeling items are now resolved: SNMP 161/162 is explicitly Supplemental in 2.1; USB 1.x is Legacy/Supplemental in 3.2; and MiniSD/xD are Legacy/Supplemental in 3.4."
)
audit.write_text(a,encoding="utf-8")

# Record scope-label changes.
corr=Path("TRANSCRIPT_CORRECTIONS.md")
c=corr.read_text(encoding="utf-8")
anchor="- Objective 2.1"
pos=c.find(anchor)
if pos<0: raise SystemExit("Objective 2.1 correction anchor missing")
note=(
"- Objective 2.1 scope-label note: SNMP 161/162 is retained as useful networking knowledge but explicitly labeled **Supplemental** because it is not directly tested in the current Objective 2.1 port list.\n"
"- Objective 3.2 scope-label note: USB 1.x history is retained but explicitly labeled **Legacy / Supplemental**; current Objective 3.2 emphasis remains USB 2.0 and USB 3.x.\n"
"- Objective 3.4 scope-label note: MiniSD and xD removable-media material is retained but explicitly labeled **Legacy / Supplemental** so it does not receive the same study emphasis as current storage topics. Learner-facing English also corrects the transcript's `many SD cards` wording to **MiniSD**.\n"
)
c=c[:pos]+note+c[pos:]
corr.write_text(c,encoding="utf-8")

# Validation
t=p.read_text(encoding="utf-8")
checks=[
"Supplemental — SNMP (Simple Network Management Protocol)",
"Supplemental / Legacy — USB 1.x",
"current Objective 3.2 study emphasis is on USB 2.0 and USB 3.x",
"MiniSD is a smaller legacy variant",
"MiniSD cards are now legacy/less common",
"Supplemental / Legacy — xD card",
"### MiniSD — Legacy / Supplemental",
"### xD Card — Legacy / Supplemental",
]
missing=[x for x in checks if x not in t]
if missing: raise SystemExit(f"Missing final labels: {missing}")
print("Final scope-label patch validation passed")
