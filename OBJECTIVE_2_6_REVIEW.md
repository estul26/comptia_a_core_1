# Objective 2.6 — Deep Translation Review

## Source structure

The transcript contains four Objective 2.6 sections:

1. IP address
2. APIPA
3. Subnet mask
4. Default gateway

## IP address

Source-stated IPv4 details:
- Internet Protocol version 4
- 32 binary digits / bits
- four groups of 8 bits
- each group is an octet
- dot-decimal notation
- each octet 0–255
- over 4.2 billion numerical combinations

Source-stated IPv6 details:
- 128 binary digits / bits
- eight groups
- four hexadecimal digits per group
- groups separated by colons
- each group can be called a hextet

The source does not teach IPv6 abbreviation/compression rules here, so none were added.

## Static vs dynamic

**Static**
- manually assigned
- remains constant
- source examples: servers and printers

**Dynamic**
- automatically assigned through DHCP
- improves ease of connection and address use

## Private vs public IPv4

Source teaching:
- private IPv4 is for local-area-network/internal communication
- private addresses are not routable on the Internet
- public IPv4 is used for Internet-connected communication
- ISPs assign public IP addresses

Important source gap:
the transcript says the private ranges are shown visually “to the right,” but the ranges themselves are not present in transcript text. No RFC1918 ranges were added.

## APIPA

Source:
- Automatic Private IP Addressing
- fallback/self-configuration when DHCP cannot be reached
- source-stated range: 169.254.0.1–169.254.255.254
- possible causes include DHCP server offline, congestion, faulty cables, or incorrect network settings
- same-local-segment APIPA communication is possible
- external network / Internet communication is not

## Subnet mask

Source model:
- works with the IP address
- helps determine which addresses are on the same local network
- source analogy: neighborhood boundary
- local destination → direct local communication
- non-local destination → use default gateway

No subnetting math, prefix length or CIDR notation was added.

## Default gateway

Source model:
- router/network device connecting a local network to other networks
- exit point for traffic not destined to the LAN
- device uses subnet mask first to determine local vs non-local
- gateway handles non-local traffic
- commonly supplied by DHCP in SOHO networks
- may also be entered manually

The transcript includes a simplified description of return traffic through the gateway. The reviewed translation preserves that teaching model without adding NAT/state-table mechanics.

## Translation approach

- Preserve source numbers and comparisons exactly.
- Do not reconstruct visual-only information missing from the transcript.
- Keep IPv4, IPv6, DHCP, APIPA and SOHO visible for exam recognition.
- Use natural Uyghur for the explanatory structure.
- Avoid adding subnetting, NAT, routing or IPv6 details not present in this objective.
