# Objective 3.5 — Deep Translation Review

## Source structure
The transcript contains eight Objective 3.5 sections:

1. Motherboard connector types
2. Motherboard form factors
3. Motherboard compatibility
4. CPU architecture
5. Expansion cards
6. Cooling
7. Encryption / TPM / HSM
8. BIOS and UEFI

## Clear transcript corrections
- PCIe `by one/by four/by eight/by 16` → x1/x4/x8/x16
- `Advanced Risk Machine` → **Advanced RISC Machine**
- `graphical processing unit` → **Graphics Processing Unit**
- TPM `passwords and pens` → passwords and **PINs**
- `iOS password` → **BIOS password**

Original English transcript remains unchanged.

## Motherboard connectors
Source covers:
- PCI
- PCIe x1/x4/x8/x16
- 20-pin / 24-pin / 20+4-pin power
- SATA
- eSATA
- M.2
- USB headers
- audio headers
- front-panel headers
- fan headers

## Form factors
Source covers:
- ATX
- Micro ATX
- ITX

Source-stated typical examples:
- ATX: multiple PCIe, 4+ DIMM
- Micro ATX: fewer PCIe, often 2–4 DIMM
- ITX: often 1 PCIe and 2 DIMM

## Compatibility
Source covers:
- Intel/AMD socket incompatibility teaching
- LGA
- PGA
- multi-socket server boards
- ARM-based mobile processors

Intel=LGA / AMD=PGA is kept as source-time framing, not universal current guidance.

## CPU architecture
Source covers:
- instruction sets
- x86 / 32-bit exam shorthand
- x64 / 64-bit
- source 4 GB 32-bit RAM limit
- OS/application compatibility model
- ARM / RISC efficiency
- CPU cores
- single vs multi-core
- Intel VT / AMD-V

The source's x86 history paragraph contains a questionable historical characterization. The reviewed lesson keeps the exam takeaway but does not promote that paragraph as externally verified history.

## Expansion cards
- sound card
- graphics card
- GPU distinction
- VRAM
- capture card
- NIC

## Cooling
- heat sink
- fans
- liquid cooling
- thermal paste
- thermal throttling
- shutdown/damage risk

Cooling hierarchy and thermal-paste maintenance remain explicitly source-framed.

## Encryption / TPM / HSM
- plaintext
- ciphertext
- encryption key/algorithm
- TPM hardware security
- drive-encryption key storage
- motherboard/TPM relationship
- HSM as enterprise centralized cryptographic hardware

BitLocker/FileVault are source examples, not externally researched product claims.

## BIOS / UEFI
- firmware
- BIOS
- POST
- bootable-device search / boot order
- UEFI
- GPT
- GUI/mouse
- Secure Boot
- setup keys
- USB boot scenario
- TPM-enable scenario
- virtualization-enable scenario
- USB permissions
- BIOS password vs boot password
- temperature monitoring
- fan profiles / fan curves

## Translation approach
- Preserve every source section and source-stated scenario.
- Correct only clear transcription artifacts.
- Mark time-sensitive, overgeneralized, or questionable source wording as source framing rather than silently rewriting it from outside knowledge.
- Avoid adding motherboard/CPU/security specifications absent from the transcript.
