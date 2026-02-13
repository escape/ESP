# ESP — Epistemic Sovereignty Protocol

## **The idea**

### **1. Purpose**

To safeguard the cognitive independence of citizens by guaranteeing transparency, traceability, and auditability of digital influence systems — political, commercial, or algorithmic — within the democratic sphere.

### **2. Core Principles**

*   **Transparency of Influence:** Every actor attempting to shape public opinion must leave a verifiable, publicly accessible trace of authorship, funding, and distribution mechanisms.

*   **Algorithmic Explainability:** All large-scale content-distribution systems must provide auditable logs of recommendation and moderation criteria.

*   **Data Minimization in Politics:** Personal data may not be used to micro-target political or civic persuasion beyond legally defined parameters.

*   **Reciprocity:** Citizens have the right to see the same data that machines use to categorize or target them.

*   **Accountability of Automation:** When automated systems make decisions that affect public visibility, a human entity remains legally responsible.

### **3. Institutional Framework**

*   **Epistemic Authority (EA):** An independent public agency with technical and judicial arms.

    *   **Technical arm:** Conducts continuous algorithmic audits and maintains open registries of political spending, ad targeting, and content amplification.

    *   **Judicial arm:** Can impose sanctions, revoke digital advertising licenses, and refer systemic manipulation to constitutional courts.

*   **Civic Observatories:** Federated citizen groups, journalists, and researchers with API access to inspect data flows and report irregularities.

### **4. Rights of Citizens**

1.  **Right to Transparency:** To know who paid for any persuasive content, how it was targeted, and why it appeared.

2.  **Right to Algorithmic Visibility:** To inspect their own data profile and the inference categories used for targeting.

3.  **Right to Audit Participation:** To request external audit of specific campaigns or datasets when credible manipulation is suspected.

4.  **Right to Democratic Silence:** To opt out of all personalized political content without penalty or reduced access.

### **5. Obligations of Platforms and Parties**

*   Maintain **Public Ledgers** of all paid political communications (spend, creative, target, date, medium).

*   Submit quarterly **Algorithmic Transparency Reports** audited by EA-certified experts.

*   Implement **Open Influence APIs** for approved civic observatories.

*   Disclose **All AI-Generated Media** that could be mistaken for human-authored content in civic contexts.

### **6. Enforcement & Sanctions**

*   Fines proportional to campaign or platform turnover (1–5%).

*   Temporary suspension of political advertising privileges.

*   Personal liability for executives who obstruct audits or falsify transparency data.

### **7. Civic Tools (Implementation Layer)**

*   **Public Dashboard:** Aggregates all political ad and funding data in real time.

*   **Citizen Plug-in:** Browser/mobile tool flagging paid political content and exposing its origin.

*   **Audit Ledger:** Cryptographically verifiable registry of algorithmic audit trails.

*   **Open ESP API:** Standardized schema for interoperability between watchdogs, journalists, and regulators.

### **8. Funding and Governance**

*   Funded by a levy on political digital advertising and large-scale recommender systems (>10M users).

*   Operates under multi-partisan parliamentary oversight.

*   Annual public report on algorithmic risks and epistemic health indicators (trust levels, misinformation prevalence, transparency scores).

### **9. International Coordination**

*   Mutual recognition with other democracies’ E.S.P. agencies to share data and harmonize audit standards.

*   Inclusion of transparency clauses in trade and data-transfer agreements.


## Draft Protocol

**Tagline:** Know who pays to change your mind.

ESP is a public-interest repo to **make digital political influence transparent, traceable, and auditable**.
It ships a minimal, pragmatic stack:
- **Open Influence Registry** (open data of paid political influence: ads, boosted posts, influencer content)
- **Audit Ledger** (verifiable logs of amplification + targeting decisions)
- **Observatory Dashboard** (public UI for citizens, journalists, researchers)
- **ESP API** (standard endpoints for registries, audits, and civic observatories)
- **Municipal Pilot Playbook** (win small, replicate fast)

> ESP is designed for average audiences and public servants. Keep language clear. No baroque idioms.

---

## Why ESP
Without transparency, democracy devolves into a managed attention market. ESP provides the **minimum viable infrastructure** for citizens to see **who paid**, **who was targeted**, **what was shown**, and **how it was amplified**.

---

## Core Principles
1. **Transparency of influence** (funding, creative, distribution)
2. **Algorithmic auditability** (amplification rationale + logs)
3. **Data minimization in politics** (no exploitative microtargeting)
4. **Reciprocity** (citizens can inspect profiles/inferences used to target them)
5. **Accountability of automation** (a human entity is responsible)

---

## High-Level Architecture
```
registries/          -> Open, machine-readable political influence data
audit-ledger/        -> Append-only, signed logs of amplification + targeting
observatory/         -> Dashboard + API for search/analysis/download
ingestion/           -> Scrapers + pipelines (platform ad libraries, disclosures, FOIAs)
governance/          -> Policy, procedures, sanctions, oversight
```

### Components
- **Open Influence Registry**: JSON/CSV datasets of political spend and targeting (schema in `/schemas/political_ad.schema.json`).
- **Audit Ledger**: hash-chained log format (`/schemas/audit_ledger.schema.json`), with signing + proofs.
- **ESP API**: REST surface for read/write to registry + ledger (`/api/open-influence-api.md`).
- **Observatory Dashboard**: minimal web app to search, filter, and export (`/dashboard`).

---

## Quick Start (dev)
```bash
# clone + run
git clone <your-repo-url> esp
cd esp

# start minimal local stack (registry API + dashboard mock)
docker compose -f infra/docker/compose.yml up --build

# ingest sample data
python ingestion/pipelines/load_samples.py data/samples/example_ads.jsonl

# run CLI
python cli/espctl.py --help
```

> **Note:** This skeleton contains mock services and sample data. Swap in real connectors as they become available.

---

## Repository Layout
```
esp/
├─ .github/
│  └─ ISSUE_TEMPLATE/ (bug_report.md, feature_request.md)
├─ api/
│  ├─ open-influence-api.md          # ESP API surface
│  └─ examples/                      # curl/httpie samples
├─ cli/
│  └─ espctl.py                      # utility CLI
├─ dashboard/
│  └─ README.md                      # UI notes + TODOs
├─ data/
│  └─ samples/                       # small example datasets
├─ docs/
│  ├─ manifesto.md                   # 1‑pager civic explainer
│  ├─ governance.md                  # roles, processes
│  ├─ roadmap.md                     # 6–12 month plan
│  └─ pilots/municipal/              # municipal pilot pack
├─ governance/
│  ├─ CODE_OF_CONDUCT.md
│  ├─ CONTRIBUTING.md
│  ├─ SECURITY.md
│  └─ MAINTAINERS.md
├─ infra/
│  ├─ docker/compose.yml             # dev compose
│  └─ terraform/                     # IaC stubs
├─ ingestion/
│  ├─ scrapers/                      # platform/library scrapers (stubs)
│  └─ pipelines/                     # ETL + validation
├─ legal/
│  └─ policy/esp-policy.md           # policy baseline
├─ schemas/
│  ├─ political_ad.schema.json
│  └─ audit_ledger.schema.json
├─ scripts/                          # util scripts (hash, sign, validate)
├─ specs/
│  └─ esp-spec.md                    # ESP Protocol spec (living doc)
└─ threat-model/
   └─ threat-model.md                # misuse + mitigations
```

---

## Minimal Specs (fast read)
- **Political Ad Record**: who paid, who published, what creative, when/where, targeting, spend, provenance hashes. See `/schemas/political_ad.schema.json`.
- **Audit Entry**: which system amplified what content for which cohort, with what rule and score, at what time. See `/schemas/audit_ledger.schema.json`.
- **Open Influence API**: CRUD for registry items, signed append for ledger, researcher tokens, bulk export. See `/api/open-influence-api.md`.

---

## Pilot: Municipal Playbook (TL;DR)
1. Pass a city ordinance requiring any paid political content **shown to city residents** to be logged in an **ESP-compliant registry**.
2. Tie city communications procurement to ESP compliance.
3. Launch an **observatory microsite** showing money flows and targeting patterns.
4. Publish quarterly **transparency reports** + referrals to national authorities.

Deliverables in `/docs/pilots/municipal/`.

---

## Roadmap (first year)
- Q1: schema v1, sample ingestors, dashboard MVP, municipal pilot
- Q2: audit ledger v1, signing + proofs, first public report
- Q3: researcher API gates, red-team drills, two more pilots
- Q4: standards alignment w/ NGOs + regulators, v1.0 release

---

## Governance & License
- **License (code):** AGPL‑3.0 (keeps transparency tools open)
- **Docs / datasets:** CC BY 4.0
- See `/governance/*` for maintainers, contributing, security, and CoC.

---

## Credits
Initiated by civic collaborators. Contributions welcome from journalists, devs, lawyers, designers, and public servants.

> “If you can’t see who paid to change your mind, you’re not free.”
