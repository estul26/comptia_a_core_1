# Objective 2.4 — Deep Translation Review

## Source structure

The transcript contains five Objective 2.4 sections:

1. DNS
2. DNS records
3. DHCP
4. VLAN
5. VPN

## DNS

The source teaches:
- DNS translates domain names/FQDNs into IP addresses.
- An FQDN can contain subdomain(s), domain name and TLD.
- The example `www.example.com` is split into `www` (subdomain), `example` (domain), `.com` (TLD).
- Lookup path: DNS recursive server/resolver → root name server → TLD server → domain name server → IP returned to resolver/browser.

The earlier `www.certificationsenergy.com` example appears inconsistent with the course naming and is not used as a canonical example in the reviewed Uyghur.

## DNS records

Source-covered records/mechanisms:
- A → IPv4
- AAAA → IPv6
- MX → mail server FQDN + priority
- TXT → text-based application values / domain ownership
- DKIM
- SPF
- DMARC

No other record types were added.

## DHCP

The source covers automatic IP/network configuration, DORA, subnet mask, default gateway, DNS server information, lease, scope, reservation and exclusion.

Objective 2.4 itself does not state DHCP ports, so ports 67/68 from Objective 2.1 were deliberately not inserted.

## VLAN

Source model:
- one physical network
- multiple separate logical networks
- same-VLAN devices communicate as if on a dedicated network
- different VLANs remain separated unless communication is intentionally allowed
- benefits: security, reduced unnecessary traffic, easier management, performance

No VLAN tagging protocol or VLAN-ID range was added because this segment does not provide those details.

## VPN

Source model:
- secure encrypted connection between a device and remote network
- protected tunnel over the Internet
- data encrypted before leaving the system
- remote access to internal resources
- access protected by credentials/authentication
- useful for remote work and public Wi-Fi
- VPN does not replace the Internet; it secures communication over public infrastructure

No VPN protocol, cipher, tunnel mode or port was added.

## Translation approach

- Preserve source structure and examples.
- Keep exam acronyms and record names visible.
- Translate surrounding explanations into natural Uyghur.
- Do not import facts from earlier objectives unless explicitly marked as cross-reference.
- Document transcript artifacts instead of modifying the original English source.
