from pathlib import Path

def replace_exact(text, old, new, label, expected=1):
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{label}: expected {expected} match(es), found {count}")
    return text.replace(old, new)

index = Path("index.html")
text = index.read_text(encoding="utf-8")

obj_start = text.find('"id": "4.1"')
obj_end = text.find('"id": "4.2"', obj_start)
if obj_start < 0 or obj_end < 0:
    raise SystemExit("Could not locate Objective 4.1 object boundaries")

en_marker = text.find('"english": "', obj_start, obj_end)
ug_marker = text.find('", "uyghur": "', en_marker, obj_end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Could not locate Objective 4.1 language boundaries")

en_start = en_marker + len('"english": "')
ug_start = ug_marker + len('", "uyghur": "')
english = text[en_start:ug_marker]
uyghur = text[ug_start:obj_end]

# Add the current Objective 4.1 named VM requirements after the existing resource-allocation teaching.
en_old = (
    "Each virtual machine will also be allocated a configurable portion of the host machine's physical resources with which to use.\\n\\n"
    "While you can configure the virtual machine with as little or as much resources as you would like, just make sure to save enough resources for the host OS. "
    "Moving on, client-side virtualization provides a versatile solution for various use cases."
)
en_new = (
    "Each virtual machine will also be allocated a configurable portion of the host machine's physical resources with which to use.\\n\\n"
    "While you can configure the virtual machine with as little or as much resources as you would like, just make sure to save enough resources for the host OS.\\n\\n"
    "Exam Note — VM requirements (current 220-1201): In addition to allocating host CPU and memory, explicitly consider **Security, Network, and Storage** requirements.\\n\\n"
    "- **Security:** control access to the virtualized environment, maintain isolation between the VM and host/other VMs, and protect the host/hypervisor and guest systems.\\n"
    "- **Network:** provide the VM with the appropriate virtual network/adapter and IP connectivity for the scenario; decide whether it needs network/Internet access or should remain isolated.\\n"
    "- **Storage:** allocate enough host storage for the VM's virtual disk, guest OS, applications, and data while leaving adequate storage for the host system.\\n\\n"
    "Memory rule: **Security = protect/isolate; Network = connect/isolate correctly; Storage = enough disk space.**\\n\\n"
    "Moving on, client-side virtualization provides a versatile solution for various use cases."
)
english = replace_exact(english, en_old, en_new, "English VM requirements Exam Note")

# Add matching Uyghur exam-support section after the resource-allocation note.
ug_old = (
    "**Source wording note:** transcript `as little or as much resources as you would like` دەپ ئاددىيلاشتۇرىدۇ؛ reviewed lesson بۇنى unlimited-resource rule دەپ كېڭەيتمەيدۇ.\\n\\n"
    "---\\n\\n"
    "## Client-Side Virtualization Use Cases"
)
ug_new = (
    "**Source wording note:** transcript `as little or as much resources as you would like` دەپ ئاددىيلاشتۇرىدۇ؛ reviewed lesson بۇنى unlimited-resource rule دەپ كېڭەيتمەيدۇ.\\n\\n"
    "## VM Requirements — Current 220-1201 Exam Note\\n\\n"
    "Current Objective 4.1 VM requirement نى ئۈچ category بويىچە ئېنىق تىلغا ئالىدۇ:\\n\\n"
    "### 1. Security\\n"
    "- virtualized environment غا access نى control قىلىش\\n"
    "- VM بىلەن host/other VM ئارىسىدىكى isolation نى ساقلاش\\n"
    "- host/hypervisor ۋە guest system نى قوغداش\\n\\n"
    "### 2. Network\\n"
    "- VM غا مۇۋاپىق virtual network/adapter تەڭشەش\\n"
    "- scenario غا ماس IP/connectivity تەمىنلەش\\n"
    "- network/Internet access لازىممۇ ياكى VM isolated بولۇشى كېرەكمۇ، شۇنى بەلگىلەش\\n\\n"
    "### 3. Storage\\n"
    "- VM virtual disk ئۈچۈن يېتەرلىك host storage\\n"
    "- guest OS، application ۋە data ئۈچۈن space\\n"
    "- host system ئۈچۈنمۇ يېتەرلىك storage قالدۇرۇش\\n\\n"
    "**Exam memory:**\\n"
    "> **Security = Protect / Isolate**\\n"
    "> **Network = Connect / Isolate correctly**\\n"
    "> **Storage = Enough disk space**\\n\\n"
    "---\\n\\n"
    "## Client-Side Virtualization Use Cases"
)
uyghur = replace_exact(uyghur, ug_old, ug_new, "Uyghur VM requirements Exam Note")

text = text[:en_start] + english + text[ug_marker:ug_start] + uyghur + text[obj_end:]
index.write_text(text, encoding="utf-8")

# Update Objective 4.1 review documentation.
review = Path("OBJECTIVE_4_1_REVIEW.md")
r = review.read_text(encoding="utf-8")
anchor = "## Hypervisors\n"
requirements = (
    "## Current-objective VM requirements\n"
    "Current 220-1201 Objective 4.1 explicitly names three requirement categories:\n"
    "- **Security**\n"
    "- **Network**\n"
    "- **Storage**\n\n"
    "The transcript already discusses host resource allocation, networking capability, and virtualization security, but it does not present **Security / Network / Storage** together as the objective's named requirements. Learner-facing English and Uyghur now add a clearly labeled **Exam Note**:\n"
    "- Security = access control/protection + VM isolation\n"
    "- Network = appropriate virtual networking/IP connectivity or deliberate isolation\n"
    "- Storage = enough host space for the VM virtual disk, guest OS/apps/data while preserving host capacity\n\n"
    "No vendor-specific virtual-network modes, storage platforms, or advanced virtualization features are added.\n\n"
    + anchor
)
r = replace_exact(r, anchor, requirements, "review VM requirements section")
r = replace_exact(
    r,
    "- Preserve source architecture and use cases.\n- Mark course simplifications as source models.\n- Correct only clear transcription artifacts.\n- Avoid external virtualization/vendor/platform material not taught in 4.1.",
    "- Preserve source architecture and use cases.\n- Mark course simplifications as source models.\n- Add missing current-objective requirements as clearly labeled learner-facing **Exam Notes** without changing the archival transcript.\n- Correct only clear transcription artifacts.\n- Avoid vendor-specific or advanced virtualization/platform material not needed for 4.1.",
    "review translation approach",
)
review.write_text(r, encoding="utf-8")

# Record the source gap in corrections documentation.
corrections = Path("TRANSCRIPT_CORRECTIONS.md")
c = corrections.read_text(encoding="utf-8")
anchor = "- Objective 4.1 source-scope note: Type 1 and Type 2 hypervisor differences are preserved at the source level; no vendor examples, nested virtualization, paravirtualization, snapshots, cloning, or migration features are added."
insert = (
    "- Objective 4.1 exam-coverage note: current 220-1201 explicitly lists VM **Requirements — Security, Network, Storage**. "
    "The transcript discusses these concepts separately but does not teach the three named requirement categories together. "
    "The original transcript remains unchanged; learner-facing English and Uyghur add a concise Exam Note covering security/isolation, appropriate VM networking/connectivity, and sufficient VM/host storage.\n"
    + anchor
)
c = replace_exact(c, anchor, insert, "transcript Objective 4.1 requirements note")
corrections.write_text(c, encoding="utf-8")

# Bounded validation.
final = index.read_text(encoding="utf-8")
start = final.find('"id": "4.1"')
end = final.find('"id": "4.2"', start)
obj = final[start:end]
required = [
    "Exam Note — VM requirements (current 220-1201):",
    "**Security, Network, and Storage** requirements",
    "**Security = protect/isolate; Network = connect/isolate correctly; Storage = enough disk space.**",
    "## VM Requirements — Current 220-1201 Exam Note",
    "### 1. Security",
    "### 2. Network",
    "### 3. Storage",
    "> **Security = Protect / Isolate**",
    "> **Network = Connect / Isolate correctly**",
    "> **Storage = Enough disk space**",
]
missing = [x for x in required if x not in obj]
if missing:
    raise SystemExit(f"Missing expected Objective 4.1 VM requirements content: {missing}")

print("Objective 4.1 VM requirements patch validation passed")
