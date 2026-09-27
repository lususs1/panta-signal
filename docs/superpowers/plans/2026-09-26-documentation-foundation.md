# Panta Signal Documentation Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete documentation and continuity foundation for Panta Signal so future development can proceed without relying on chat memory and hackathon requirements remain traceable.

**Architecture:** The repository will use a documentation-first operating model derived from `nano-json-lens-402`, extended with product, provenance, evaluation, and hackathon-specific artifacts. `docs/checkpoints/CHECKPOINT_CURRENT.md` becomes the primary resume entrypoint, while roadmap, decision log, execution ledger, and evidence-focused documents separate verified state from plans and AI interpretation.

**Tech Stack:** Markdown, Git/GitHub, environment-template files; no product runtime or application dependencies in this plan.

**Spec:** `docs/superpowers/specs/2026-09-26-panta-signal-foundation-design.md`

## Global Constraints

- Repository artifacts, source code, comments, API fields, public errors, issues, releases, and public-facing communication use English.
- Private working conversation with the operator may remain in Portuguese.
- No personal capital is required for the MVP.
- Trading, wallet execution, swaps, or autonomous fund movement are outside the initial MVP.
- Panta credentials or other secrets must never be committed.
- Every work block must end with an updated current checkpoint.
- Planned work must never be reported as completed work.
- The repository must remain understandable without relying on chat memory.
- Source data, deterministic derived data, and AI-generated interpretation must remain explicitly distinguishable.
- Product implementation, live Panta API integration, deployment, and real hackathon submission are outside this plan.

## Review Focus

1. **Secret leakage:** `.env.example` and all documentation must contain names/placeholders only, never usable credentials.
2. **Fact/plan confusion:** roadmap, README, ledger, and checkpoint must never claim API validation, deployment, signals, or submission work that has not happened.
3. **Provenance ambiguity:** documentation must clearly distinguish Panta source fields, deterministic derived fields, and AI-generated interpretation.
4. **Resume failure:** a new agent following `CHECKPOINT_CURRENT.md` and `ROADMAP.md` must be able to identify the exact next step without chat context.
5. **Hackathon overclaiming:** official criteria not yet revalidated during execution must be marked `UNVERIFIED` rather than copied as authoritative fact.

---

## File Map

### Root
- `README.md` — public project entrypoint, current status, principles, resume order.
- `.env.example` — safe placeholder-only configuration surface.
- `.gitignore` — local secret/generated-state exclusions.

### Core documentation
- `docs/WHITEPAPER.md` — problem, proposal, product thesis, scope, success criteria.
- `docs/ARCHITECTURE.md` — system boundaries and logical data flow.
- `docs/ROADMAP.md` — phased execution state using explicit completion markers.
- `docs/SECURITY.md` — credential, API, logging, abuse, dependency, and AI boundaries.
- `docs/CONTINUITY_RULES.md` — mandatory checkpoint and resume protocol.
- `docs/DECISIONS.md` — decision log with status and rationale.
- `docs/EXECUTION_LEDGER.md` — verified actions/evidence only.
- `docs/OPERATIONS.md` — current and future operational procedures without claiming deployment.

### Product / hackathon documentation
- `docs/HACKATHON_CRITERIA.md` — traceability matrix for externally verified criteria; unknown items remain `UNVERIFIED`.
- `docs/PRODUCT_SPEC.md` — MVP users, flows, requirements, acceptance criteria, non-goals.
- `docs/SIGNAL_ENGINE.md` — deterministic signal model requirements and design constraints; formulas may remain planned until validated.
- `docs/DATA_PROVENANCE.md` — source/derived/AI data classes and required metadata.
- `docs/EVALUATION.md` — quality and demo evaluation framework.
- `docs/SUBMISSION_CHECKLIST.md` — final deliverables and evidence gates.

### Continuity / future-work directories
- `docs/checkpoints/CHECKPOINT_CURRENT.md` — mutable current state.
- `docs/checkpoints/history/2026-09-26_001.md` — first immutable foundation snapshot.
- `docs/specs/README.md` — purpose and rules for technical specifications.
- `docs/research/README.md` — purpose and evidence rules for external research.
- `docs/superpowers/specs/2026-09-26-panta-signal-foundation-design.md` — existing approved design.
- `docs/superpowers/plans/2026-09-26-documentation-foundation.md` — this plan.

---

### Task 1: Establish Safe Root Entry Point

**Files:**
- Create: `README.md`
- Create: `.env.example`
- Create: `.gitignore`

**Interfaces:**
- Consumes: approved foundation design.
- Produces: public project entrypoint and safe configuration boundary used by every later task.

- [ ] **Step 1: Create `.gitignore` with secret/local-state exclusions**

Include at minimum `.env`, `.env.*` except `.env.example`, `node_modules/`, build artifacts, logs, editor/OS noise, and local database/state files likely to contain runtime data.

- [ ] **Step 2: Create `.env.example` with placeholders only**

Document configuration names for a future server-side Panta API base URL/key and optional application/database/AI provider settings, but do not insert a live key, wallet, token, or authenticated endpoint secret.

- [ ] **Step 3: Create `README.md`**

The README must state:
- Panta Signal product thesis;
- English project-language rule;
- current phase as documentation foundation only;
- no trading/capital requirement for the initial MVP;
- the three product layers: Market Intelligence, Signal Engine, AI Analyst;
- current non-goals;
- links to current checkpoint, roadmap, architecture, product spec, security, provenance, evaluation, and submission checklist;
- resume order beginning with `CHECKPOINT_CURRENT.md`;
- explicit warning that documentation does not mean implementation exists.

- [ ] **Step 4: Verify root safety and truthfulness**

Check that `.env.example` contains no usable credential and that README does not claim live API access, deployment, signal generation, or hackathon submission.

- [ ] **Step 5: Commit Task 1**

Commit message: `docs: establish panta signal repository entrypoint`

---

### Task 2: Create the Core Project Source of Truth

**Files:**
- Create: `docs/WHITEPAPER.md`
- Create: `docs/ARCHITECTURE.md`
- Create: `docs/ROADMAP.md`
- Create: `docs/CONTINUITY_RULES.md`
- Create: `docs/DECISIONS.md`

**Interfaces:**
- Consumes: approved design and root README terminology.
- Produces: authoritative project thesis, system shape, phase model, continuity protocol, and decision vocabulary used by later documents.

- [ ] **Step 1: Create `WHITEPAPER.md`**

Cover problem, proposal, prediction-market-as-information-sensor thesis, three-layer product model, desired properties, initial scope/non-goals, zero-capital constraint, and measurable success criteria. Do not claim signal effectiveness before evaluation exists.

- [ ] **Step 2: Create `ARCHITECTURE.md`**

Document the logical flow:

`Panta API -> server-side ingestion -> normalized market data -> snapshots -> deterministic Signal Engine -> signal records/internal API -> dashboard + AI Analyst`

Define security boundaries, data-class boundaries, planned persistence, server-side credential handling, and the rule that AI explanation is downstream of deterministic analysis.

- [ ] **Step 3: Create `ROADMAP.md`**

Use phases with checkboxes and explicit state:
- Phase 0 documentation foundation;
- Phase 1 external criteria/API validation;
- Phase 2 technical specification/data contracts;
- Phase 3 ingestion and normalization;
- Phase 4 snapshots and Signal Engine;
- Phase 5 dashboard/internal API;
- Phase 6 AI Analyst;
- Phase 7 public deployment/evaluation;
- Phase 8 hackathon evidence/submission.

Only already verified repository work may be checked complete.

- [ ] **Step 4: Create `CONTINUITY_RULES.md`**

Port the strongest Nano rules and adapt them to Panta Signal. Define work block, resume order, minimum checkpoint content, historical snapshot policy, `COMPLETED / PLANNED / BLOCKED / UNVERIFIED`, evidence handling, project language, secret handling, and prohibition on converting intent into fact.

- [ ] **Step 5: Create `DECISIONS.md`**

Record at minimum:
- dedicated Panta Signal repository;
- English official repository language;
- mandatory checkpoint every work block;
- Panta Signal as an intelligence layer rather than a generic dashboard;
- deterministic signals before AI explanation;
- no trading/capital movement in initial MVP;
- explicit provenance classes;
- documentation pattern inherited and improved from Nano.

Open decisions must remain visibly open, including runtime/provider, storage, exact Panta API contracts, AI provider, signal formulas, and license.

- [ ] **Step 6: Verify cross-document terminology**

Ensure product-layer names, non-goals, status vocabulary, and architecture flow are consistent across all five files.

- [ ] **Step 7: Commit Task 2**

Commit message: `docs: add core panta signal project foundation`

---

### Task 3: Establish Security, Provenance, Operations, and Evidence Rules

**Files:**
- Create: `docs/SECURITY.md`
- Create: `docs/DATA_PROVENANCE.md`
- Create: `docs/OPERATIONS.md`
- Create: `docs/EXECUTION_LEDGER.md`

**Interfaces:**
- Consumes: architecture, decisions, continuity rules.
- Produces: safety/evidence boundaries required before live API work or implementation.

- [ ] **Step 1: Create `SECURITY.md`**

Define:
- server-side-only API credentials;
- no credentials in repo/client/logs;
- external API responses treated as untrusted;
- bounded inputs and rate/abuse controls as production requirements;
- sanitized logs;
- dependency pin/review before release;
- no arbitrary fetch by user-provided URL unless separately designed;
- prompt-injection/data-poisoning boundary: AI cannot override deterministic records or provenance;
- no trading/private-key/wallet-custody paths in MVP.

- [ ] **Step 2: Create `DATA_PROVENANCE.md`**

Define the three mandatory classes:
1. Panta/external source data;
2. deterministic derived data;
3. AI-generated interpretation.

Require traceability for material signals to market identifier, source timestamp, observation/snapshot, algorithm version, and calculation time. Mark exact Panta field mappings as `UNVERIFIED` until live/API-documentation validation.

- [ ] **Step 3: Create `OPERATIONS.md`**

Describe current state as not deployed. Define future operational requirements for local execution, configuration, health/reachability, observability, incident recording, API outage behavior, snapshot gaps, credential rotation, and demo readiness without inventing commands that do not yet exist.

- [ ] **Step 4: Create `EXECUTION_LEDGER.md`**

Create a structured append-only format for date/block/action/evidence/result/status. Seed it only with actions actually verified so far: repository creation by operator, reference-repository review, approved foundation design, and creation of the implementation plan. Do not claim API calls or deployment.

- [ ] **Step 5: Verify Review Focus security/provenance cases**

Check explicitly that no file contains a real secret, provenance classes are defined consistently, and operational text says planned rather than deployed where appropriate.

- [ ] **Step 6: Commit Task 3**

Commit message: `docs: define security provenance and evidence boundaries`

---

### Task 4: Define Product, Signal, Evaluation, and Competition Traceability

**Files:**
- Create: `docs/PRODUCT_SPEC.md`
- Create: `docs/SIGNAL_ENGINE.md`
- Create: `docs/EVALUATION.md`
- Create: `docs/HACKATHON_CRITERIA.md`
- Create: `docs/SUBMISSION_CHECKLIST.md`
- Create: `docs/research/README.md`
- Create: `docs/specs/README.md`

**Interfaces:**
- Consumes: whitepaper, architecture, provenance and security rules.
- Produces: bounded MVP definition and the evidence framework needed to design/implement the application later.

- [ ] **Step 1: Create `PRODUCT_SPEC.md`**

Define target user, primary user stories, MVP flows, functional requirements, non-functional requirements, acceptance criteria, and non-goals for Market Intelligence, Signal Engine, and AI Analyst. Keep live trading out of scope.

- [ ] **Step 2: Create `SIGNAL_ENGINE.md`**

Define planned signal families and constraints: probability movement, movement velocity, abnormal change, recency/persistence, related-market divergence, and composite signal score. Require deterministic/reproducible formulas, versioned algorithms, minimum input windows, missing-data behavior, and tests before a formula can be considered implemented. Exact formulas/thresholds remain `PLANNED` until validated.

- [ ] **Step 3: Create `EVALUATION.md`**

Define evaluation dimensions: correctness, reproducibility, latency, explainability, provenance coverage, resilience to missing data, usefulness/ranking quality, and demo clarity. Separate objective mechanical checks from subjective demo/user-value evaluation.

- [ ] **Step 4: Create `HACKATHON_CRITERIA.md`**

Build a traceability table with columns for criterion/source verification status/product capability/repository evidence/demo evidence/gap. Any criterion not freshly verified against an authoritative external source during execution must be `UNVERIFIED`; do not turn prior chat summaries into official facts.

- [ ] **Step 5: Create `SUBMISSION_CHECKLIST.md`**

Include gates for repository cleanliness, README, public deployment, working demo path, required video/screenshot assets, architecture/product explanation, Panta integration evidence, judging-criteria mapping, secret scan, reproducibility check, final URL verification, and submission confirmation. Items stay unchecked until actually satisfied.

- [ ] **Step 6: Create research/spec directory guidance**

`docs/research/README.md` must require source/date/access details and distinguish primary evidence from interpretation. `docs/specs/README.md` must require technical specs to identify interfaces, contracts, acceptance tests, open decisions, and upstream design/decision references.

- [ ] **Step 7: Verify hackathon overclaiming and signal truthfulness**

Confirm no unverified prize, deadline, submission count, API capability, formula performance, or deployed feature is presented as completed/authoritative.

- [ ] **Step 8: Commit Task 4**

Commit message: `docs: add product signal and hackathon traceability framework`

---

### Task 5: Close the Foundation Block with Checkpoint and Historical Snapshot

**Files:**
- Create: `docs/checkpoints/CHECKPOINT_CURRENT.md`
- Create: `docs/checkpoints/history/2026-09-26_001.md`
- Modify: `docs/ROADMAP.md`
- Modify: `docs/EXECUTION_LEDGER.md`
- Modify: `README.md` if final links/status need correction.

**Interfaces:**
- Consumes: every artifact created by Tasks 1–4.
- Produces: a verified, resumable repository state and exact handoff to the next architectural stage.

- [ ] **Step 1: Create `CHECKPOINT_CURRENT.md`**

Record:
- date and block ID;
- overall state: documentation foundation complete / product implementation not started;
- completed files;
- evidence/verification performed;
- accepted decisions;
- open/unverified decisions;
- blockers/risks;
- exact next step: validate authoritative Panta hackathon/API sources and freeze the first technical/API contract;
- operator-confirmation requirements, if any.

- [ ] **Step 2: Create first historical checkpoint**

Copy the verified milestone state into `docs/checkpoints/history/2026-09-26_001.md` and mark it as an immutable historical snapshot except for explicitly documented corrections.

- [ ] **Step 3: Update roadmap state**

Mark only completed foundation items complete. Leave API validation, implementation, deployment, evaluation, and submission unchecked.

- [ ] **Step 4: Append execution evidence**

Add the completed documentation block and verification results to `EXECUTION_LEDGER.md` with repository paths and commit references available at execution time.

- [ ] **Step 5: Perform whole-foundation verification**

Verify all expected files exist and all README links resolve. Search repository text for likely secret patterns/placeholders accidentally replaced with live values. Check for contradictory state claims such as `deployed`, `live`, `implemented`, or `validated` where the evidence does not support them. Check that every hackathon-specific factual claim has either evidence or an `UNVERIFIED` label.

- [ ] **Step 6: Commit Task 5**

Commit message: `docs: complete panta signal documentation foundation`

- [ ] **Step 7: Final review**

Read `CHECKPOINT_CURRENT.md` as if no chat history exists. The next action must be unambiguous and must not depend on hidden conversation context.

---

## Completion Definition

This plan is complete when the repository contains the full approved documentation foundation, the current checkpoint accurately describes verified state, the historical snapshot exists, all cross-links and status claims have been checked, and no product implementation/API validation/deployment is falsely represented as complete.

The next plan must begin from authoritative external validation of Panta API/hackathon requirements and then define the first technical data contracts before application code is written.
