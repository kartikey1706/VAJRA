# VAJRA Implementation Phases

Every phase has an objective, inputs, outputs, acceptance criteria, and dependencies. Do not advance until the current phase is reasonably complete.

## Phase 0 — Project Foundation
**Objective:** establish reproducible structure and conventions.
**Tasks:** repository setup, environment configuration, docs, folder structure, logging, typed configuration, contracts.
**Inputs:** approved PRD, architecture, rules, design.
**Outputs:** runnable skeleton, `.env.example`, logging/configuration, no `Memory.md` until coding starts.
**Acceptance:** local checks run; configuration has safe validation; demo/production boundary is explicit.
**Dependencies:** none.

## Phase 1 — Data Ingestion
**Objective:** load representative forecast/reference data through replaceable adapters.
**Tasks:** schemas, provider interfaces, sample NWP/ensemble/observation loading, provenance, validation reports.
**Inputs:** confirmed source, geography, variables, formats.
**Outputs:** canonical records and quality report.
**Acceptance:** valid and invalid fixtures are distinguished and versioned.
**Dependencies:** Phase 0.

## Phase 2 — Data Alignment
**Objective:** make forecast and reference records comparable.
**Tasks:** timestamp/cycle/valid-time matching, spatial-grid alignment, lead-time alignment, units, missing data.
**Inputs:** canonical records.
**Outputs:** aligned verification dataset.
**Acceptance:** alignment decisions and rejected records are auditable.
**Dependencies:** Phase 1.

## Phase 3 — Forecast Verification
**Objective:** calculate errors and defensible bust labels.
**Tasks:** forecast/reference matching, MAE/RMSE/bias as appropriate, configurable metric and threshold, label generation.
**Inputs:** aligned data and approved bust definition.
**Outputs:** verification metrics and labels.
**Acceptance:** labels reproduce from a clean run and never use future information.
**Dependencies:** Phase 2.

## Phase 4 — Feature Engineering
**Objective:** produce documented predictive features.
**Tasks:** ensemble statistics, spatial/temporal forecast features, atmospheric diagnostics, historical error, regime features.
**Inputs:** aligned data, labels, supported diagnostics.
**Outputs:** feature matrix and schema.
**Acceptance:** every feature has provenance, units, availability time, missingness behavior, and tests.
**Dependencies:** Phase 3.

## Phase 5 — Baseline ML Model
**Objective:** establish an interpretable predictive baseline.
**Tasks:** chronological train/validation/test, logistic regression or gradient boosting, metrics, artifact persistence.
**Inputs:** feature matrix and labels.
**Outputs:** model, probabilities, evaluation report.
**Acceptance:** baseline beats or meaningfully informs naive baselines without leakage.
**Dependencies:** Phase 4.

## Phase 6 — Regime-Aware Prediction
**Objective:** add supported regime information.
**Tasks:** choose classification/clustering/rule-assisted method, validate regime features, compare against baseline.
**Inputs:** atmospheric features and baseline.
**Outputs:** regime-aware model/evaluation.
**Acceptance:** regime claims are supported by data and improve or clarify results.
**Dependencies:** Phase 5.

## Phase 7 — Historical Analogue Engine
**Objective:** retrieve similar historical forecast situations.
**Tasks:** vector encoding, eligible-record filtering, similarity method, outcome summaries, API contract.
**Inputs:** versioned historical feature records.
**Outputs:** computed analogues and evidence.
**Acceptance:** results are reproducible, historical, and linked to observed error outcomes.
**Dependencies:** Phase 4.

## Phase 8 — Probability Calibration
**Objective:** assess and calibrate probabilities only when justified.
**Tasks:** reliability diagrams, Brier score, ECE, Platt/isotonic comparison, artifact registration.
**Inputs:** held-out validation predictions.
**Outputs:** raw/calibrated comparison and optional calibrator.
**Acceptance:** UI/API clearly identifies calibration status and evaluation sample.
**Dependencies:** Phase 5.

## Phase 9 — Explainability
**Objective:** provide evidence-backed explanations.
**Tasks:** feature importance, local contributions, analogue evidence, explanation schema and guardrails.
**Inputs:** active model and inference record.
**Outputs:** ranked explanations with values and provenance.
**Acceptance:** every explanation can be traced to an input/model output and avoids causal overclaiming.
**Dependencies:** Phase 5; Phase 7 for analogue evidence.

## Phase 10 — Backend API
**Objective:** expose supported results safely.
**Tasks:** FastAPI endpoints, validation, structured errors, readiness/metadata, pagination, tests.
**Inputs:** result repositories and service contracts.
**Outputs:** documented versioned API.
**Acceptance:** endpoint responses and errors pass contract tests; unavailable data is explicit.
**Dependencies:** Phases 5, 7, 9.

## Phase 11 — Dashboard
**Objective:** deliver the operational VAJRA interface.
**Tasks:** map, Day 1–10 selector, supported variable selector, risk summary, region panel, explanations, analogues, status states.
**Inputs:** API contracts and Design.md.
**Outputs:** responsive accessible dashboard.
**Acceptance:** users can identify risk, inspect a region, and understand provenance without fake values.
**Dependencies:** Phase 10.

## Phase 12 — Integration
**Objective:** connect ingestion, inference, API, and UI.
**Tasks:** environment wiring, caching/precomputed slices, end-to-end flows, demo/production switches.
**Inputs:** completed services and UI.
**Outputs:** end-to-end MVP run.
**Acceptance:** a clean run produces matching backend/frontend results and visible metadata.
**Dependencies:** Phases 10–11.

## Phase 13 — Testing
**Objective:** validate scientific and product behavior.
**Tasks:** unit, integration, data validation, API, ML leakage, frontend, accessibility, failure-state tests.
**Inputs:** integrated MVP.
**Outputs:** test report and issue register.
**Acceptance:** required checks pass or known issues are explicitly recorded.
**Dependencies:** Phase 12.

## Phase 14 — Deployment
**Objective:** prepare a reproducible production-oriented deployment.
**Tasks:** Docker, environment configuration, production build, monitoring, operational documentation.
**Inputs:** tested MVP.
**Outputs:** deployable services and runbook.
**Acceptance:** deployment health/readiness, security headers, logs, and rollback/configuration behavior are verified.
**Dependencies:** Phase 13.
