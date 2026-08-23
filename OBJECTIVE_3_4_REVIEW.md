# Objective 3.4 — Deep Translation Review

## Source structure
Objective 3.4 contains four source sections:

1. Hard disk drives
2. Solid state drives
3. RAID
4. Removable storage

## Transcript corrections
- `SADOC` → **SATA** in the SAS comparison.
- repeated `many SD cards` → **MiniSD**, based on the source's own description of the smaller SD variant later replaced by microSD.

Original English transcript remains unchanged.

## HDD
Source covers:
- magnetic storage on spinning platters
- spindle / read-write head
- mechanical wear
- RPM and source examples 5,400 / 7,200 / 10,000 / 15,000
- 3.5-inch desktop/server
- 2.5-inch laptop/portable

## SSD
Source covers:
- NAND flash
- no moving parts
- controller
- cache
- SATA data + separate SATA power
- SATA 3 theoretical 6 Gbps
- PCIe lanes
- NVMe protocol over PCIe
- SAS enterprise/redundancy
- M.2
- mSATA

No outside generation/version matrices were added.

## RAID

**RAID 0**
- striping
- speed / maximum usable capacity
- no redundancy

**RAID 1**
- mirroring
- two disks in source
- strong redundancy
- half usable capacity

**RAID 5**
- striping + distributed parity
- minimum 3 drives
- withstand one-drive failure

**RAID 6**
- striping + two parity sets
- withstand two-drive failures
- source does not state minimum drive count

**RAID 10**
- RAID 1+0
- striping + mirroring
- high performance / redundancy
- faster rebuild than parity-based source comparison
- half usable capacity
- source does not state minimum drive count

## Removable storage

Source covers:
- flash/thumb/USB flash drive
- SD
- smaller SD variant interpreted as MiniSD from context
- microSD
- CF
- xD
- CD / DVD / Blu-ray

Source-stated optical maximums:
- CD: 700 MB
- DVD: approximately 17 GB
- Blu-ray: 128 GB

## Translation approach
- Preserve source structure and numerical values.
- Correct only clear transcript errors or internally resolvable labels.
- Explicitly note source gaps.
- Avoid importing newer storage standards/specifications.
