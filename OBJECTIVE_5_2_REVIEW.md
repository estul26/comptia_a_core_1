# Objective 5.2 — Deep Translation Review

## Source boundaries
Objective 5.2 spans transcript lines 8935–9201; Objective 5.3 begins at 9202.

## Topics
LED status indicators; audible alarms; HDD grinding/clicking; data loss/corruption; RAID failure/degraded state; SMART; slow read/write and fragmentation; IOPS; missing drives; bootable device not found; missing/offline/degraded RAID.

## Clear STT correction
- `rate array` → **RAID array**
- `rate controller` → **RAID controller**

## Important source-model cautions
- LED colors are typical examples, not universal vendor meanings.
- IOPS = transfer rate ÷ average operation size is the transcript's simplified teaching formula.
- `Drive initialization` is used broadly by the source for partition-table creation plus formatting.
- Defragmentation remains in the HDD context; no SSD guidance is imported.

## Key source actions
- Grinding/clicking HDD → backup critical data, prepare replacement.
- SMART failure warning → immediate backup, replace drive.
- Degraded RAID → replace failed member, rebuild.
- Missing boot device → connection, drive failure, BIOS boot order.
- Missing RAID → check member-drive connection/power and RAID-controller status.
