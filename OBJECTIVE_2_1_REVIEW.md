# Objective 2.1 — Deep Translation Review

## Source structure

The transcript contains three repeated Objective 2.1 segments:

1. Networking protocols — networking, protocol and port fundamentals
2. Ports and protocols — common application protocols and source-stated default ports
3. TCP versus UDP — transport behavior and trade-offs

## Source-stated ports

| Protocol | Port(s) stated in source |
|---|---:|
| FTP | 20, 21 |
| SSH | 22 |
| Telnet | 23 |
| SMTP | 25 |
| DNS | 53 |
| DHCP | 67, 68 |
| HTTP | 80 |
| POP3 | 110 |
| NetBIOS | 137, 139 |
| IMAP | Not stated |
| SNMP | 161, 162 |
| LDAP | 389 |
| HTTPS | 443 |
| SMB | 445 |
| RDP | 3389 |

## Important source-boundary decisions

### IMAP
The source explains server-based synchronization and multi-device behavior, but does not provide an IMAP default port. No outside port number was inserted.

### NetBIOS
The source says NetBIOS uses multiple ports, but only explicitly explains:
- 137 — name service
- 139 — session service

No additional NetBIOS port was inserted.

### POP3
The transcript presents POP3 as downloading messages and then deleting them from the server. The reviewed Uyghur attributes that behavior to the source rather than broadening or correcting it from external knowledge.

### SNMP
The transcript says SNMP is not directly tested in this objective, explains monitoring/management, and names ports 161/162. The reviewed translation stays within that description.

## TCP vs UDP

Source teaching model:

**TCP**
- connection-oriented
- three-way handshake
- verifies packets/order
- requests resend when data is missing
- prioritizes reliable delivery

**UDP**
- connectionless
- faster / lower-overhead teaching model
- no guaranteed delivery
- source examples: live streaming and online gaming

## Translation approach

- Protocol names and abbreviations remain unchanged for exam recognition.
- Explanations use natural Uyghur rather than English grammar with Uyghur suffixes.
- Source omissions are labeled instead of filled with outside knowledge.
- Source speech-to-text brand errors such as `Comp-TA plus` are documented, while the original English file remains unchanged.
