# Objective 2.5 — Deep Translation Review

## Source structure

The transcript contains seven Objective 2.5 sections:

1. Common networking hardware
2. Patch panel
3. Power over Ethernet
4. Network firewall
5. Modern modems
6. NIC
7. MAC address

## Common networking hardware

Source teaching model:

### Hub
- connects multiple devices
- broadcasts received data to all connected devices
- less efficient / less secure than a switch
- described as mostly obsolete

### Switch
- connects devices within a LAN
- forwards toward intended recipient
- source uses Ethernet-frame/destination-address explanation

### Unmanaged switch
- plug-and-play
- little/no configuration
- source examples: 4 or 8 ports
- small/SOHO networks

### Managed switch
- configurable
- source examples include security, traffic control and traffic segregation
- source examples: 24, 48 or more ports
- larger/corporate networks

### Access point
- provides wireless local-network connectivity
- source analogy: wireless version of a switch
- bridges wireless devices to the network

### Router
- forwards between networks
- source contrasts router with switch: switch handles LAN-local traffic, router handles traffic entering/leaving a LAN
- source describes router as a gateway at the network edge

### SOHO router
The source combines:
- router
- built-in switch
- built-in wireless AP

Transcript correction: `RG45` is reviewed as **RJ45**.

## Patch panel

Source role:
- central cable-organization point
- cables converge there
- connects onward to switches/routers
- makes moves/reconfiguration easier
- improves troubleshooting and reduces wear on permanent cabling

Important distinction:
**Patch panel organizes cable connections; it does not perform switch-style data forwarding.**

## PoE

Source examples:
- AP
- IP camera
- VoIP phone

Source delivery mechanisms:
- PoE switch
- PoE injector

Source-stated standards/power:
- 802.3af / PoE — 15.4 W
- 802.3at / PoE+ — 30 W
- 802.3bt Type 3 / PoE++ — 60 W
- 802.3bt Type 4 / PoE++ — 90 W

## Network firewall

Source model:
- monitors incoming/outgoing traffic
- inspects packet source, destination and content
- compares against predefined rules/policies
- ACL provides allow/deny criteria
- allow match → permit/forward
- no allow match → deny, according to the transcript's example

No extra firewall features were imported.

## Modern modems

Source distinctions:
- cable modem → coaxial cable
- DSL modem → telephone line
- ONT → fiber-optic connection

The source defines modem as converting between signaling formats for local-network ↔ ISP communication.

## NIC

Source distinctions:
- wired vs wireless
- integrated/onboard vs add-on/expansion
- wired source benefits: speed, lower latency, reliability
- wireless source benefits: flexibility/mobility, with interference/signal/environment trade-offs

The phrase `gaming sabs` is unintelligible in the transcript. No specific replacement noun was invented.

## MAC address

Source-stated details:
- Media Access Control
- hardware identifier associated with a network interface
- hexadecimal
- 12 hexadecimal characters
- 48 bits
- first half: OUI
- second half: manufacturer-assigned interface portion
- source/destination MAC addresses in an Ethernet frame
- switch uses destination MAC information to direct local delivery

The reviewed translation preserves the course's global-uniqueness/manufacturing teaching model and does not add outside material about randomized or locally administered MAC addresses.

## Translation approach

- Preserve source structure and comparisons.
- Keep exam acronyms and hardware names visible.
- Use natural Uyghur around canonical terms.
- Correct only documented speech-to-text artifacts in the reviewed Uyghur.
- Do not add unstated network-layer, routing, switching, firewall, PoE, modem, NIC or MAC details.
