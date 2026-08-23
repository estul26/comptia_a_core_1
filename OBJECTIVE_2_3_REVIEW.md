# Objective 2.3 — Deep Translation Review

## Source structure

The transcript contains four Objective 2.3 sections:

1. Server roles
2. Internet appliances
3. Legacy and embedded systems
4. IoT devices

## Server roles covered by the source

- DNS server
- DHCP server
- File server
- Print server
- Mail server
- Syslog server
- Web server
- AAA server
- Database server
- NTP server

### AAA
The source explicitly teaches:
- Authentication — verify who the user is
- Authorization — determine allowed access
- Accounting — keep activity records

It names **RADIUS** and **TACACS+** as common AAA implementations. No protocol ports or vendor-specific behavior were added.

### NTP
The source emphasizes synchronized time for:
- logs
- security events
- authentication
- troubleshooting
- correlation of events

## Internet appliances

The course groups the following under `Internet appliances`:
- spam gateway
- UTM
- load balancer
- proxy server

The translation intentionally preserves this course framing.

### Spam gateway
Source techniques:
- blacklisting
- whitelisting
- content analysis
- regularly updated rules and keyword filters

### UTM
Source-listed functions include:
- firewall
- antivirus
- anti-spam
- intrusion detection
- intrusion prevention
- VPN
- content filtering

### Load balancer
Distributes network/application traffic across multiple servers to avoid overloading one server.

### Proxy server
Acts as a middleman:
- intercepts traffic
- permits approved traffic
- denies traffic violating rules
- supports a traffic exemption when something should not be blocked

## Legacy vs embedded

**Legacy system**
- old system/software/technology still in use
- replacement may be complex/risky/costly
- may lack support, updates, or compatibility

**Embedded system**
- specialized computing system
- performs dedicated functions
- optimized for specific requirements
- source examples: microwave, traffic lights, thermostat

## SCADA

The source describes SCADA as monitoring and controlling industrial environments and says it may rely on both:
- legacy systems for longevity/stability
- embedded systems for specific control tasks

Source examples:
- power plants
- water treatment
- pipeline pressure
- industrial temperature control

No SCADA protocol details were added beyond the transcript.

## IoT

The source defines IoT from the IT perspective as network-connected physical devices/objects/sensors capable of collecting, exchanging and transmitting data.

Typical source-described characteristics:
- sensors
- embedded operating system
- network connectivity
- cloud or centralized-controller communication
- automation
- remote monitoring/control

Examples preserved:
- smart appliances
- home automation
- doorbells
- thermostats
- security cameras
- streaming devices
- connected vehicles
- medical devices
- fitness equipment
- smartwatches / fitness trackers

The exam-focused idea is that IoT devices are **network-connected endpoints extending networking beyond traditional computers**.

## Translation approach

- Preserve all server roles and appliance categories exactly as taught.
- Keep AAA sub-functions distinct.
- Keep legacy and embedded systems distinct.
- Keep acronyms such as DNS, DHCP, AAA, RADIUS, TACACS+, NTP, UTM, SCADA and IoT visible.
- Use natural Uyghur around the canonical technical terms.
- Do not add missing ports, SCADA architectures, or IoT security details from outside knowledge.
