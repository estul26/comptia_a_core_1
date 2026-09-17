from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

start = text.find('"id": "3.3"')
end = text.find('"id": "3.4"', start)
if start < 0 or end < 0:
    raise SystemExit("Objective 3.3 bounds not found")

en_marker = text.find('"english": "', start, end)
ug_marker = text.find('", "uyghur": "', en_marker, end)
if en_marker < 0 or ug_marker < 0:
    raise SystemExit("Objective 3.3 language bounds not found")

en_start = en_marker + len('"english": "')
english = text[en_start:ug_marker]

primary = "As for the 21,300, this indicates that the RAM can theoretically transfer up to 21,300 megabytes per second of theta."
if english.count(primary) != 1:
    raise SystemExit("Primary theta sentence was not found exactly once")

sentinel = "__PRIMARY_THETA_SENTINEL__"
work = english.replace(primary, sentinel, 1)

if work.count("theta") != 1:
    raise SystemExit(f"Expected exactly one additional theta artifact, found {work.count('theta')}")

work = work.replace("theta", "data", 1)
work = work.replace(sentinel, primary, 1)

text = text[:en_start] + work + text[ug_marker:]
path.write_text(text, encoding="utf-8")
print("Additional Objective 3.3 theta artifact corrected")
