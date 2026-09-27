# Panta Signal — Foundation Design

**Date:** 2026-09-26  
**Status:** Approved design; implementation pending  
**Repository:** `uknwplayer/panta-signal`

## 1. Purpose

Panta Signal is an intelligence layer for prediction-market data. Its initial goal is to turn Panta market activity into explainable, queryable signals for humans and AI agents without requiring the operator to place trades or commit personal capital.

The first development phase focuses on creating a durable repository foundation that can survive changes of chat, agent, session, or tool while remaining suitable for hackathon submission and public review.

## 2. Project Constraints

- Repository artifacts, source code, comments, API fields, public errors, issues, releases, and public-facing communication use English.
- Private working conversation with the operator may remain in Portuguese.
- No personal capital is required for the MVP.
- Trading, wallet execution, swaps, or autonomous fund movement are outside the initial MVP.
- Panta credentials or other secrets must never be committed.
- Every work block must end with an updated current checkpoint.
- Planned work must never be reported as completed work.
- The repository must remain understandable to a new agent or contributor without relying on chat memory.

## 3. Product Direction

The MVP is not merely a market dashboard. It combines three layers:

### 3.1 Market Intelligence
- active markets;
- probabilities and market state;
- categories and metadata;
- volume/trade activity where available;
- historical snapshots collected by the application;
- search, filtering, ranking, and watchlists.

### 3.2 Signal Engine
A deterministic analytical layer that derives explainable indicators from market changes, such as:
- probability movement;
- movement velocity;
- abnormal change detection;
- recency and persistence;
- related-market divergence;
- configurable signal scoring.

The exact scoring model must be specified and testable before production use. AI-generated prose must not be the source of truth for numerical signals.

### 3.3 AI Analyst
A natural-language layer that answers questions over structured market and signal data. Answers should identify the supporting markets, relevant numbers, time window, and provenance. The language model explains derived evidence; it does not invent unsupported market facts.

## 4. Logical Architecture

```text
Panta API
   |
   v
Server-side ingestion / protected API client
   |
   v
Normalized market data
   |
   +--> Snapshot store
   |
   v
Deterministic Signal Engine
   |
   +--> Signal records / rankings
   |
   +--> Internal API
            |
            +--> Web dashboard
            |
            +--> AI Analyst / agent interface
```

### Architectural principles

1. Panta credentials stay server-side.
2. Raw external data and locally derived data are distinguishable.
3. Derived signals are reproducible from stored inputs whenever feasible.
4. AI explanation is downstream of structured analysis.
5. The MVP avoids transactional trading paths unless explicitly added in a later approved design.
6. The first deployment should minimize cost and operational complexity.

## 5. Documentation Foundation

The repository will use the successful continuity pattern from `nano-json-lens-402`, adapted for a competitive product/hackathon context.

### Root

- `README.md` — project overview, status, resume instructions, public entrypoint.
- `.env.example` — configuration names only, with no real secrets.
- `.gitignore` — prevents secrets, generated files, and local state from entering version control.

### Core documentation

- `docs/WHITEPAPER.md` — problem, proposal, product thesis, value, initial scope, success criteria.
- `docs/ARCHITECTURE.md` — system boundaries, components, data flow, deployment assumptions.
- `docs/ROADMAP.md` — phased execution path from documentation through public submission.
- `docs/SECURITY.md` — credential handling, API boundary, abuse limits, logging, dependency and AI safety rules.
- `docs/CONTINUITY_RULES.md` — mandatory work-block closure and resume procedure.
- `docs/DECISIONS.md` — accepted, pending, superseded, and rejected technical/product decisions.
- `docs/EXECUTION_LEDGER.md` — verifiable record of meaningful tests, external validations, deployments, and submissions.
- `docs/OPERATIONS.md` — local execution, deployment, observability, incident and maintenance guidance.

### Panta/hackathon-specific documentation

- `docs/HACKATHON_CRITERIA.md` — official judging/submission criteria converted into traceable project requirements.
- `docs/PRODUCT_SPEC.md` — user flows, MVP scope, non-goals, functional requirements, acceptance criteria.
- `docs/SIGNAL_ENGINE.md` — signal definitions, formulas, windows, thresholds, scoring model, limitations, tests.
- `docs/DATA_PROVENANCE.md` — source fields, timestamps, normalization rules, derived fields, evidence boundaries.
- `docs/EVALUATION.md` — how usefulness, correctness, latency, explainability, and demo quality are evaluated.
- `docs/SUBMISSION_CHECKLIST.md` — public URL, repository, video, screenshots, required text, judging evidence, final checks.

### Continuity and planning directories

```text
docs/
  checkpoints/
    CHECKPOINT_CURRENT.md
    history/
  specs/
  research/
  superpowers/
    specs/
    plans/
```

`CHECKPOINT_CURRENT.md` is the primary resume entrypoint. Historical checkpoints capture material milestones and should not be silently rewritten.

## 6. Continuity Model

Every work block must close by updating `docs/checkpoints/CHECKPOINT_CURRENT.md`.

A work block includes any unit that:
- changes code or documentation;
- makes or revises a technical/product decision;
- performs a meaningful API validation or research step;
- completes or fails a test;
- changes configuration or deployment state;
- discovers a blocker or material risk;
- creates hackathon/submission evidence.

The checkpoint must distinguish:
- **COMPLETED** — verified work;
- **PLANNED** — intended work;
- **BLOCKED** — unresolved dependency;
- **UNVERIFIED** — claim or state without sufficient evidence.

Minimum checkpoint contents:
- date and block identifier;
- current overall state;
- completed work;
- evidence/tests;
- active decisions;
- files/commits relevant to the block;
- blockers and risks;
- pending work;
- exact next step;
- items requiring operator confirmation.

Resume order for any new agent:
1. read `docs/checkpoints/CHECKPOINT_CURRENT.md`;
2. read `docs/ROADMAP.md`;
3. inspect referenced files and evidence;
4. verify claimed repository state;
5. execute only the recorded next step or explicitly record a plan revision.

## 7. Data and Provenance Boundary

The system must distinguish at least three classes of information:

1. **Source data** — fields received from the Panta API or another explicitly documented external source.
2. **Derived deterministic data** — normalized fields, deltas, rates, rankings, scores, clustering results, or other reproducible calculations.
3. **AI-generated interpretation** — natural-language explanation, summaries, or suggested lines of inquiry.

The UI and internal contracts should avoid presenting AI interpretation as if it were original Panta data.

Every important signal should be traceable to:
- market identifier;
- source timestamps;
- input observations/snapshots;
- signal algorithm/version;
- calculation time.

## 8. Initial Security Boundary

The first version will:
- keep Panta credentials server-side;
- never commit live API keys;
- use `.env.example` with placeholders only;
- avoid arbitrary user-controlled URL fetching unless separately designed and approved;
- validate and bound user inputs;
- sanitize logs;
- avoid logging secrets or full credential-bearing headers;
- use least-privilege credentials where supported;
- pin important dependencies before release;
- treat external API responses as untrusted input;
- ensure AI prompts cannot override deterministic data or system-level constraints.

Trading execution, wallet custody, private keys, automated swaps, and autonomous capital movement remain outside this design.

## 9. Hackathon Optimization Layer

The documentation system improves on the Nano reference repository by making competition requirements first-class artifacts rather than leaving them scattered across notes.

### Required traceability

`HACKATHON_CRITERIA.md` should map each official criterion to:
- relevant product capability;
- repository evidence;
- demo evidence;
- current completion status;
- remaining gap.

### Demonstrability

`EVALUATION.md` and `SUBMISSION_CHECKLIST.md` should ensure that the product can demonstrate:
- useful market intelligence;
- clear differentiation from a generic dashboard;
- explainable signal generation;
- reliable use of Panta data;
- coherent AI integration;
- public working deployment;
- reproducible repository setup;
- concise final demo narrative.

## 10. Initial MVP Non-Goals

The initial MVP does not require:
- real-money trading;
- autonomous execution of trades;
- custody of user funds;
- social features;
- native mobile applications;
- complex multi-tenant accounts;
- paid infrastructure unless free options prove insufficient;
- a generalized prediction-market platform supporting every provider.

These can be reconsidered only after the core Panta Signal workflow works end to end.

## 11. Success Criteria for the Foundation Block

The documentation foundation is complete when:
- all approved foundation documents exist;
- README clearly points to current checkpoint and roadmap;
- project language and continuity rules are explicit;
- product direction and non-goals are clear;
- security and provenance boundaries are documented;
- hackathon criteria have a dedicated traceability document;
- roadmap separates planned work from verified work;
- a current checkpoint records the repository state and exact next step.

No product implementation should be claimed merely because documentation exists.

## 12. Next Stage After This Design

After operator review and approval of this written design:
1. create a detailed implementation plan for the documentation foundation;
2. execute the plan in controlled work blocks;
3. finish each block by updating `CHECKPOINT_CURRENT.md`;
4. only after the foundation is coherent, move to Panta API validation and the product's technical specification.
