# Objective 5.5 — Deep Translation Review

## Source boundaries
- Objective 5.5 starts at transcript line 9689.
- Objective 5.6 starts at transcript line 9826.
- Objective 5.5 spans lines 9689–9825.

## Topics
1. Limited connectivity / no Internet
2. Slow network speeds
3. Port flapping
4. Wired EMI
5. Wireless interference
6. Intermittent wireless connectivity
7. Latency
8. Jitter
9. Poor VoIP quality
10. Authentication failures
11. Intermittent Internet connectivity

## Source cautions
- APIPA numeric range is not stated here and is not imported.
- `Speed and latency are inverses` is kept as source-level troubleshooting wording, not a universal mathematical law.
- Signal filtering/adaptive channel selection remain possible mitigation examples, not guaranteed fixes.

## Key flows
- Limited connectivity → APIPA/DHCP/config → remote test → cables/connections.
- Slow network → scope → speed/duplex → cables → congestion → malware.
- Port flapping → cable/connector/NIC.
- Wired EMI → shielding/grounding/routing.
- Intermittent Wi-Fi → interference/obstacles/distance/hardware.
- Latency = delay; jitter = variation in delay.
- Poor VoIP → latency/jitter.
- Authentication failure → password/key + WPA2/WPA3 match.
- Internet drops while local network remains connected → ISP/congestion/router.

## Translation approach
Preserve source symptom/cause/action relationships while avoiding external commands, numeric ranges and vendor-specific network configuration.
