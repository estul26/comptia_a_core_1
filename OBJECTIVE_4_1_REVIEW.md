# Objective 4.1 — Deep Translation Review

## Source boundaries
- Objective 4.1 starts at transcript line 8000.
- Objective 4.2 starts at transcript line 8365.
- Objective 4.1 therefore spans source lines 8000–8364.

## Source structure
Four sections:
1. Desktop virtualization / VDI
2. Client-side virtualization
3. Hypervisors + virtualization security
4. Containers

## Transcript correction
- `enterprise environments and beta centers` → **enterprise environments and data centers** in the Type 1 hypervisor/server-virtualization context.

Original English transcript remains unchanged.

## Desktop virtualization / VDI
Source model:
- desktop content separated from physical processing/storage hardware
- OS/apps/files hosted remotely
- accessed over network
- VDI simplified into client + server + VMs
- client may be called thin client in source context
- server may be on-premises or cloud
- VMs live on server and are controlled by Type 1 hypervisor
- source says each user has their own VM
- user authenticates; server locates VM; GUI appears on client; source says processing/storage occur server-side

Benefits:
- agility
- centralized management
- security/access control
- reduced operational/manual-configuration burden

No pooled/session/shared-desktop architecture is added.

## Client-side virtualization
Source:
- VMs run directly on end-user host
- Type 2 hypervisor installed on host OS
- each VM has isolated OS/apps/data
- allocate host CPU/memory/storage/network resources
- leave enough resources for host OS

Use cases:
- sandbox
- software development/testing
- legacy apps/OS
- cross-platform development/testing

## Hypervisors
Definition:
- software layer enabling multiple OS/VMs on one physical hardware platform
- divides/manages processing, memory and storage resources

Type 1:
- bare-metal
- directly on hardware
- no underlying OS
- source: high performance/efficiency/scalability
- enterprise/data-center server virtualization

Type 2:
- hosted
- application on Windows/macOS/Linux host OS
- source: client-side/smaller/individual use

Management:
- create/start/shutdown/terminate VM
- allocate RAM
- allocate CPU cores
- configure networking

Security:
- disable virtualization in BIOS/UEFI (source security measure)
- vTPM
- VM escape

## Containers
Source:
- lightweight packaging of app + libraries + config + required components
- consistent behavior across supported environments
- VMs contain a full OS per instance
- containers share host OS kernel
- containers are logically isolated
- source example: Linux-targeted containers run on Linux hosts
- smaller and faster-starting than VMs, per source
- useful in development/cloud
- VMs and containers can be combined

No cross-platform runtime/hidden-VM implementation details are imported.

## Translation approach
- Preserve source architecture and use cases.
- Mark course simplifications as source models.
- Correct only clear transcription artifacts.
- Avoid external virtualization/vendor/platform material not taught in 4.1.
