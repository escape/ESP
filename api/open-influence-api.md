# ESP Open Influence API (draft)

Base URL: `/api/v1`

## Endpoints

### Registry
- `POST /registry/ads` — create a political ad record (validated against `political_ad.schema.json`)
- `GET  /registry/ads/{id}` — fetch by id
- `GET  /registry/ads` — list/filter (query by payer, publisher, date range, tags, jurisdiction)
- `PUT  /registry/ads/{id}` — update (with audit trail)
- `GET  /registry/export` — bulk export (JSONL/CSV)

### Audit Ledger
- `POST /ledger/append` — append signed audit event (body validated against `audit_ledger.schema.json`)
- `GET  /ledger/verify/{id}` — verify hash chain + signature
- `GET  /ledger/stream` — tail events (SSE/WebSocket)

### Researcher Access
- `POST /auth/researcher-token` — request scoped token (organization, use-case)
- `GET  /me/quotas` — see rate limits

## Status Codes
- 200 OK, 201 Created, 400 ValidationError, 401/403 Unauthorized, 409 Conflict, 422 SignatureInvalid

## Notes
- Personally identifiable data is *not* stored in the registry. Targeting is represented as **declared parameters** and **cohort sizes** only.
- All write operations emit an audit trail event.
