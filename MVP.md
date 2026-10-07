# Read-only catalog MVP — 2026-10-07

## Run
Python 3.11 or newer; no external dependencies or paid services.
Set `PANTA_API_BASE_URL` to the official HTTPS API base supplied by Panta, and `PANTA_API_KEY` in the server environment. Do not paste secrets in browser fields or commit them.
Run `python panta_signal.py`; open http://127.0.0.1:8080.
Run checks with `python -m unittest test_panta_signal.py`.

## Implemented
Catalog listing, cursor pagination, category/phase filtering, search over loaded markets, detail inspection, source provenance, retrieval timestamps, explicit errors and configuration state. Powered by Panta attribution appears in the interface.
The server permits only GET /markets/ and GET /markets/{id}/ upstream. Redirects are blocked to avoid forwarding the API key to another host. Responses are size-bounded and validated. Source text is rendered with textContent, not HTML.

## Not verified or shipped
No live key or production API base was available. End-to-end Panta integration, public deployment, rate-limit policy, registration and submission remain unverified. No fixture is substituted for live data. Retrieval time is not market-update time. No probability, price-movement or prediction-accuracy claim is made.

## Scope revision
Continue the existing Panta Signal foundation with a catalog-first MVP. Defer snapshots, signal ranking and AI until catalog authentication and data semantics are verified. No wallet, transaction, signing, buy, create, claim or capital movement is implemented.

## Official evidence checked 2026-10-07
- https://superteam.fun/earn/listing/panta-api-side-track — 27 submissions observed; 5,000 USDG total, 2,000/1,000/1,000/1,000. Market discovery and analytics are listed use cases. Meaningful API use, working demo, English submission, official Colosseum registration and submission to both platforms are required.
- https://colosseum.com/legal/Crypto%20World%27s%20Fair%20Hackathon%20Rules.pdf — registration/submission ends October 12, 2026 23:59 PT (October 13, 15:59 Asia/Seoul). One team per entrant and one project per team. All content in English. Eligibility and rules acceptance must be checked by each participant.
- https://github.com/Kaito-HQ/panta-api-playground/blob/main/src/components/MarketsPanel.tsx — X-Api-Key catalog requests, category/status/limit/cursor, list/detail routes.
- https://github.com/Kaito-HQ/panta-api-playground/blob/main/src/lib/types.ts — items, nextCursor, marketId, title, category, phase, volumeUsdc.

## Human steps
Register each participant and accept official rules personally; verify eligibility and any existing team registration. Provide the official Panta API base and test key through server configuration. Before final submission, verify a live public demo and the submission form's exact asset requirements. Submit the same project to Colosseum and Superteam, then retain confirmation. No registration or submission is claimed here.
