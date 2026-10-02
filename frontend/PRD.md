# VAJRA Product Requirements Document

## 1. Product overview
VAJRA (AI-Based Forecast Bust Detection) estimates where and when medium-range NWP forecasts are likely to experience unusually large error. It complements the forecast with calibrated reliability information, risk regions, evidence-backed explanations, and historical analogues. It must distinguish real observations from estimates and clearly identify demo mode when production data is unavailable.

## 2. Problem statement
Forecast reliability declines during rapidly evolving, convective, high-spread, and regime-transition situations. Meteorologists and operational teams need to know which forecast elements and lead times deserve reduced confidence, not only what the model predicts.

## 3. Goals
- Produce grid/region-level bust probabilities for Days 1–10.
- Identify high-risk clusters and lead-time deterioration.
- Explain results using measured model features and outputs.
- Compare current cases with historical forecast situations.
- Provide a versioned API and operational dashboard.
- Establish a scientifically defensible, leakage-safe MVP pipeline.

## 4. Non-goals
- Replacing official forecasts or issuing warnings.
- Claiming deterministic forecast failure or physical causality from feature importance.
- Supporting every model, variable, region, and observation source in the MVP.
- Introducing deep learning before a validated baseline justifies it.

## 5. Target users and personas
- **Meteorologist:** needs spatial, variable-specific reliability evidence.
- **Weather analyst:** needs regional risk ranking and lead-time comparison.
- **Operations decision maker:** needs fast, clear low-confidence signals.
- **Energy/weather operator:** needs uncertainty context for weather-dependent actions.
- **Researcher:** needs reproducible datasets, analogues, features, and explanations.

## 6. User stories
- As a meteorologist, I can select a cycle, variable, and lead time and inspect bust risk on a map.
- As an analyst, I can select a risk region and see probability, confidence, data quality, and supporting signals.
- As an operator, I can quickly identify the highest-risk regions and lowest-confidence lead times.
- As a researcher, I can retrieve analogue cases and distinguish raw from calibrated probability.
- As an engineer, I can query versioned results and metadata through documented endpoints.

## 7. Functional requirements
1. Ingest forecast, ensemble, reference/observation, and archive data through replaceable adapters.
2. Validate timestamps, cycles, valid times, coordinates, units, missingness, and lead times.
3. Calculate forecast error metrics and configurable bust labels.
4. Build ensemble, temporal, spatial, atmospheric, regime, and historical features when supported.
5. Train and evaluate a baseline model using chronological splits.
6. Return raw probability, calibrated probability only when validated, and confidence label.
7. Detect high-risk grid cells and neighboring clusters.
8. Retrieve computed historical analogues with similarity and observed error evidence.
9. Provide evidence-backed local explanations and data-quality status.
10. Display map, Days 1–10 selector, supported variables, region details, risk summary, and metadata.

## 8. Non-functional requirements
- Modular, typed, reproducible, testable, observable, and extensible.
- No fabricated production values; explicit demo/mock labeling.
- Secure configuration via environment variables and least-privilege deployment.
- Accessible responsive UI with semantic HTML and keyboard support.
- Deterministic pipelines through versioned configuration and datasets.

## 9. Data requirements
Canonical records must preserve source, dataset version, forecast cycle, initialization time, valid time, lead time, variable, units, spatial coordinates, member, value, quality flags, and ingestion timestamp. Large gridded data belongs in object storage or scientific formats such as NetCDF/Zarr; relational metadata and result indexes belong in PostgreSQL/PostGIS when spatial querying is needed.

## 10. ML requirements
The first model is an interpretable logistic regression or gradient-boosting baseline. Features and target definitions must be documented with information-availability times. Training, validation, and testing are chronological. Metrics include discrimination, Brier score, calibration error, reliability curves, and region/lead-time breakdowns where sample size supports them. Model and dataset versions are recorded.

## 11. Forecast bust definition
A bust is a configurable, variable-specific event where forecast error against an approved reference exceeds a documented threshold for a defined spatial/temporal aggregation. Thresholds are configuration, not arbitrary UI constants, and must include metric, units, aggregation, minimum data quality, and provenance. The MVP may begin with one supported variable and threshold while exposing the definition in metadata.

## 12. Confidence requirements
Bust probability is an estimate, not certainty. Confidence labels are a configurable interpretation of validated probability bands and must show whether the value is raw or calibrated. Missing, stale, or insufficiently validated inputs must produce an unavailable/limited status rather than false precision.

## 13. Explainability requirements
Only expose feature contributions or importance generated from the active model and input record. Label associations as model evidence, not physical causation. Each explanation includes feature name, observed value, direction/contribution where supported, model version, and data timestamp.

## 14. Historical analogue requirements
Analogue search must use computed feature vectors, a documented distance/similarity method, temporal eligibility rules, and verified historical outcomes. Each result includes case identifier, similarity, forecast context, observed error classification, and dataset version. No synthetic cases are presented as history.

## 15. Dashboard requirements
Header: VAJRA identity, cycle, update time, data status, demo/production state. Main view: primary probability/confidence map, legend, clusters, and selectable regions. Controls: Day 1–10, supported variable, cycle, and region. Detail view: probability, confidence, error definition, contributing evidence, analogue cases, ensemble statistics, and quality flags. Include loading, empty, stale, unavailable, and API-error states.

## 16. API requirements
Versioned REST endpoints: `/api/health`, `/api/metadata`, `/api/forecast`, `/api/bust-probability`, `/api/confidence`, `/api/risk-regions`, `/api/explanations`, and `/api/analogues`. Requests validate cycle, lead time, variable, region, and pagination. Responses include provenance, timestamps, versions, units, quality, and uncertainty. Errors use structured JSON and appropriate HTTP status codes.

## 17. Error handling and data quality
Reject malformed or ambiguous data; quarantine invalid records; surface quality flags and freshness. Never silently substitute values. The API returns actionable error codes. The UI distinguishes unavailable data from low confidence. Retries are bounded and observable.

## 18. Security considerations
No secrets in source or responses. Validate and bound all inputs, parameterize queries, protect administrative/model operations, restrict CORS, use HTTPS in deployment, and apply baseline security headers. Do not expose raw sensitive infrastructure metadata.

## 19. Performance requirements
MVP map responses should target sub-second reads for cached result slices and predictable degradation for uncached computation. Inference should be asynchronous or precomputed for large grids. Frontend should avoid rendering unnecessary grid detail and should remain usable on tablet and smaller screens.

## 20. Scope
### Prototype
A clearly labeled demo provider and representative schema can validate the dashboard contract without implying real weather.
### MVP
One region, one or a small documented set of variables, representative forecast/reference data, verification and labels, baseline model, Days 1–10 slices, risk clusters, evidence-backed explanations, analogue retrieval, API, and dashboard.
### Future enhancements
More models and regions, richer observations, PostGIS analytics, calibrated multi-model ensembles, drift monitoring, SHAP at scale, alerting, user roles, and production ingestion orchestration.

## 21. Acceptance criteria
- End-to-end run loads versioned data, validates it, computes errors/labels/features, trains chronologically, and serves results.
- Every displayed result has cycle, lead time, variable, timestamp, provenance, and quality state.
- No unsupported variable or unavailable result is displayed as real data.
- Map supports Days 1–10 and region selection.
- Risk clusters and explanations match backend results.
- Analogue cases are computed from historical records.
- API validation and structured errors are tested.
- Tests cover data validation, labels, leakage-sensitive splits, inference, API contracts, and key UI states.

## 22. Success metrics
Pipeline reproducibility; validation pass rate; API error rate and latency; data freshness; model Brier score/calibration error against baseline; analogue retrieval validity; explanation coverage; and user task success for finding high-risk regions. Metrics are reported with dataset/version and sample size.

## 23. Assumptions requiring confirmation
The initial geography, first supported variable, authoritative reference dataset, forecast source, bust metric/threshold, update cadence, deployment target, and whether the first release is demo-only or connected to real data must be confirmed before Phase 1 data work. Until then, the architecture uses provider interfaces and labels demo data explicitly.

## MVP vs prototype vs future
The prototype validates contracts and UX with an explicit demo provider. The MVP validates a real, leakage-safe forecast-reliability pipeline for a constrained domain. Future work expands scientific coverage and operational automation only after validation evidence supports it.
