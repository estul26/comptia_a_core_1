# V6.9 Learner-Quality Audit

V6.9 is a learner-language quality release for the Uyghur CompTIA A+ Core 1 reader.

## Scope

The audit reviewed all 27 objectives in the live `LESSONS` data used by `index.html`, with extra line-by-line attention to objectives that contained the most mixed English/Uyghur learner prose.

Priority passes included:

- 3.2, 3.3, and 3.5
- Domains 1 and 2 learner-facing scaffolding
- 3.4 storage and RAID
- 4.1 virtualization
- 4.2 cloud computing
- 3.7 and 3.8 printers
- 5.1 through 5.6 troubleshooting
- residual learner-facing text in 3.1 and 3.6

## Quality rules

The release aims to:

- explain ordinary concepts in natural Uyghur;
- preserve canonical A+ identifiers and abbreviations when students need the English exam term;
- keep official terms such as PCIe, DIMM, DDR, RAID, NVMe, BIOS/UEFI, TPM, IaaS/PaaS/SaaS, DHCP, DNS, Wi-Fi, SMART, and similar identifiers recognizable;
- remove accidental English teaching scaffolding that does not help the learner;
- remove malformed mixed-language grammar and duplicated verb constructions;
- keep technical facts and troubleshooting order unchanged unless a prior wording defect required correction.

## Regression guard

`tests/mobile.spec.cjs` now includes a learner-quality regression guard that:

- parses the live `LESSONS` payload;
- confirms all 27 objectives are present;
- confirms every lesson still contains Uyghur text;
- rejects known editorial leftovers;
- rejects placeholder leakage;
- rejects recurring malformed Uyghur spacing and duplicated-verb patterns.

## Release metadata

- Package version: `6.9.0`
- Service-worker cache: V6.9 learner-quality cache
- Content target: live `index.html` lesson data

## Release criterion

V6.9 is ready for merge only after repository checks and the mobile Playwright suite pass on the branch.
