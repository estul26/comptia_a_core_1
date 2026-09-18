# Objective 4.2 — Deep Translation Review

## Source boundaries
- Objective 4.2 starts at transcript line 8365.
- Objective 5.1 starts at transcript line 8704.
- Objective 4.2 therefore spans source lines 8365–8703.

## Source structure
1. Cloud models
2. Cloud characteristics
3. Cloud service types + shared responsibility

## Cloud models
Source definition:
- on-demand network access
- shared pool of configurable resources
- networks, servers, storage, applications and services
- rapid provisioning/release
- remote servers instead of relying only on local server/PC

Source examples:
- AWS
- Microsoft Azure
- Google Cloud Platform

Models:
- Public
- Private
- Hybrid
- Community

Private-cloud technical correction:
- the transcript says private clouds maintain access during local Internet outages and uses guarantee-style wording for reliability/compliance
- learner-facing English and Uyghur no longer preserve those claims as study rules
- **private cloud = exclusive use by one organization**; it may exist on-premises or off-premises
- outage behavior depends on deployment topology and the user's access path
- on-prem local access may survive an Internet outage if internal networking/services remain available; off-premises or remote access may depend on WAN/Internet/private-link connectivity
- high availability depends on redundancy/failover architecture, not the private-cloud label alone
- private cloud can support compliance/security goals but does not automatically guarantee compliance or prevent breaches

## Cloud characteristics
Source characteristics:
- shared resources / resource pooling
- dedicated resources
- metered utilization
- rapid elasticity
- high availability
- file synchronization
- multi-tenancy

Metered usage examples:
- CPU utilization
- storage usage
- network ingress
- network egress

High availability:
- redundancy
- fault tolerance
- avoiding single points of failure
- failover to server/data center/region

Multi-tenancy:
- multiple tenants
- logical isolation
- shared physical platform
- source says dedicated-resource options can also exist within a multi-tenant platform

## Service types

### IaaS
- servers/storage/networking
- users manage VMs/networks
- flexible infrastructure
- less physical-hardware investment/maintenance burden

### PaaS
- development/deployment platform
- provider abstracts servers/networking
- developers focus on coding
- faster development/collaboration

### SaaS
- ready-made applications over Internet
- browser or dedicated client
- productivity/CRM examples
- source says installation/maintenance/update burden is removed from user side

Minor wording correction:
- a small grammatical transcript artifact is rendered naturally without changing the intended SaaS meaning.

## Shared responsibility
Source layer list:
- data center
- networking
- storage
- servers
- virtualization
- operating system
- data
- applications

IaaS:
- provider: data center/networking/storage/servers/virtualization
- user: OS/apps/data

PaaS:
- provider adds OS
- user: apps/data

SaaS:
- provider manages most/entire stack according to source
- user: application settings and user access

No vendor-specific responsibility model is imported.

## Translation approach
- Preserve source categories, hierarchy and examples.
- Correct architecture-dependent source claims when preserving them would create a learner-facing technical error.
- Keep the private-cloud correction concise: exclusive use, on/off premises, topology-dependent access, and architecture-dependent availability.
- Correct clear grammatical/transcription artifacts.
- Do not add unrelated cloud services or operational details absent from Objective 4.2.
