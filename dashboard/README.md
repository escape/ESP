# ESP Observatory Dashboard (MVP)

Goals:
- Search and filter political ad entries (payer, publisher, time, spend, targeting).
- Visualize spend over time, top payers, top publishers, and cohort sizes.
- Export filtered views to CSV/JSONL.

MVP stack suggestion:
- Backend: FastAPI (Python) or Node (Express) wrapping the registry datasets.
- Frontend: SvelteKit or React.
- Auth: Public read access for most views, researcher token for advanced queries.

TODO:
- Wire to /api
- Add charts (no dark patterns)
- Accessibility first
