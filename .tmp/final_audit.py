from pathlib import Path
t=Path("index.html").read_text(encoding="utf-8").lower()
order="1.1 1.2 1.3 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 4.1 4.2 5.1 5.2 5.3 5.4 5.5 5.6".split()
spec={
"1.1":"battery;keyboard;ram;hdd&ssd;wireless card;biometric;nfc;antenna;camera;microphone",
"1.2":"usb-c&micro usb&mini usb;lightning;nfc;bluetooth;hotspot;stylus;headset;speaker;webcam;docking station;port replicator;trackpad&drawing pad&track point",
"1.3":"3g&4g&5g;hotspot;wi-fi;sim&esim;bluetooth&pairing&pin;gps;cellular location services;mdm;byod;policy enforcement;corporate application;data cap;calendar;contact;mail;cloud storage",
"2.1":"ftp&20&21;ssh&22;telnet&23;smtp&25;dns&53;dhcp&67&68;http&80;pop3&110;imap&143;netbios&137&138&139;ldap&389;https&443;smb&445;rdp&3389;tcp&udp",
"2.2":"2.4&5 ghz&6 ghz;regulation;channel selection;channel width;bluetooth;802.11;nfc;rfid",
"2.3":"dns;dhcp;file server;print server;mail server;syslog;web server;authentication&authorization&accounting;database;ntp;spam gateway;utm;load balancer;proxy;scada;iot",
"2.4":"a record;aaaa;cname;mx;txt;dkim;spf;dmarc;lease;reservation;scope;exclusion;vlan;vpn",
"2.5":"router;managed&unmanaged&switch;access point;patch panel;firewall;poe&injector;poe standard;cable modem;dsl;ont;nic&mac address",
"2.6":"ipv4&private&public;ipv6;apipa;static&dynamic;subnet mask;gateway",
"2.7":"satellite;fiber;cable;dsl;cellular;wisp;lan;wan;pan;man;san;wlan",
"2.8":"crimper;cable stripper;wi-fi analyzer;toner probe;punchdown;cable tester;loopback;network tap",
"3.1":"lcd;ips;twisted nematic;vertical alignment;oled;mini-led;digitizer;inverter;pixel density;refresh rate;resolution;color gamut",
"3.2":"t568a&t568b;coax;shielded twisted;direct-burial;unshielded twisted;plenum;single-mode;multimode;usb 2.0;usb 3.0;serial cable;thunderbolt;hdmi;displayport;dvi;vga;usb-c;sata;esata;adapter;rj11;rj45;f-type;straight tip;subscriber connector;lucent connector;punchdown block;micro-usb;mini-usb;molex;lightning;db9",
"3.3":"sodimm;dimm;ddr3&ddr4&ddr5;ecc&non-ecc;single channel&dual channel",
"3.4":"spindle&rpm;2.5&3.5;nvme;sata;pcie;sas;m.2;msata;raid 0&raid 1&raid 5&raid 6&raid 10;flash drive;memory card;optical drive",
"3.5":"atx&micro atx&itx;pci&pcie;power connector;sata&esata;header;m.2;amd&intel&socket;multi-socket;boot order;usb permission;tpm;fan;secure boot;boot password;bios password;temperature;virtualization;hsm;x86&x64;arm;core;sound card;video card;capture card;network interface card;heat sink;thermal paste;liquid",
"3.6":"110–120&220–240;3.3&5 v&12 v;20+4;redundant;modular;wattage;efficiency",
"3.7":"unbox&setup location;driver&operating system;pcl&postscript;firmware;usb&ethernet&wireless;printer share;print server;duplex;orientation;tray;quality;authentication;badging;audit log;secured print;email&smb&cloud;adf&flatbed",
"3.8":"toner&maintenance kit&calibrat&clean;ink cartridge&printhead&roller&feeder;thermal paper&heating element&debris;multipart&ribbon",
"4.1":"sandbox;test&development;application virtualization;legacy;cross-platform;security&network&storage;vdi;container;type 1&type 2",
"4.2":"private cloud;public cloud;hybrid cloud;community cloud;iaas;saas;paas;shared resource&dedicated resource;metered;ingress&egress;elasticity;availability;file synchronization;multi-tenancy",
"5.1":"post&beep;crash screen;blank screen;no power;sluggish;overheating;burning smell;random shutdown;application crash;unusual noise;capacitor;date&time",
"5.2":"led;grinding;clicking;bootable device;data loss&corruption;raid failure;smart;read/write;iops;missing drive;array missing;alarm",
"5.3":"incorrect input;cabling;bulb;fuzzy;burn-in;dead pixel;flashing;incorrect color;audio;dim;projector&shutdown;sizing;distorted",
"5.4":"battery health;swollen;broken screen;charging;connectivity;liquid;overheating;digitizer;damaged port;malware;cursor drift&calibration;install new application;stylus;degraded performance",
"5.5":"intermittent wireless;slow network;limited connectivity;jitter;voip;port flapping;latency;external interference;authentication failure;intermittent internet",
"5.6":"lines;garbled;paper jam;faded;not feeding;misfeed;pending&queue;speckling;double&echo;grinding;staple;hole punch;orientation;tray&recognized;connectivity;frozen&queue"
}
def block(oid):
 i=order.index(oid);s=t.find(f'"id": "{oid}"');e=t.find(f'"id": "{order[i+1]}"',s) if i+1<len(order) else len(t)
 if s<0 or e<0: raise SystemExit(f"missing bounds {oid}")
 return t[s:e]
total=0;miss=[]
for oid in order:
 b=block(oid);bad=[]
 for group in spec[oid].split(";"):
  req=group.split("&");total+=1
  absent=[x for x in req if x not in b]
  if absent: bad.append((group,absent))
 print(f"{oid}: {'PASS' if not bad else 'REVIEW '+str(len(bad))}")
 for x in bad: print("  ",x)
 miss.extend((oid,*x) for x in bad)
print("TOTAL",total,"GAPS",len(miss),"OBJECTIVES_WITH_GAPS",len(set(x[0] for x in miss)))
