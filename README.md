# ESP — Epistemic Sovereignty Protocol

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

# start minimal local stack (registry API + observatory dashboard)
docker compose -f infra/docker/compose.yml up --build

# Services will be available at:
# - Registry API:   http://localhost:8000
# - Observatory:    http://localhost:5173

# ingest sample data
python ingestion/pipelines/load_samples.py data/samples/example_ads.jsonl

# run CLI
python cli/espctl.py --help
```

> **Note:** This skeleton contains mock services and sample data. Swap in real connectors as they become available.

### Docker Services

- **Registry** (Python Flask): Machine-readable political influence data service with health checks
- **Observatory** (Node.js): Dashboard + API interface for search and analysis

Both services are networked and will restart automatically on failure. Check logs with `docker compose logs <service-name>`.

---

## Repository Layout

```
esp/
├─ .github/
│  └─ ISSUE_TEMPLATE/ (bug_report.md, feature_request.md)
├─ api/
│  ├─ open-influence-api.md          # ESP API surface
│  └─ examples/                      # curl/httpie samples
├─ audit-ledger/
│  └─ README.md                      # Append-only, signed logs of amplification
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
│  ├─ docker/
│  │  ├─ compose.yml                 # dev compose (registry + observatory)
│  │  ├─ registry/                   # Registry service Docker setup
│  │  └─ observatory/                # Observatory service Docker setup
│  └─ terraform/                     # IaC stubs
├─ ingestion/
│  ├─ scrapers/                      # platform/library scrapers (stubs)
│  └─ pipelines/                     # ETL + validation
├─ legal/
│  └─ policy/esp-policy.md           # policy baseline
├─ registries/
│  └─ README.md                      # Open, machine-readable political influence data
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

(...)
