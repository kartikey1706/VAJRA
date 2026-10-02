# VAJRA Technical Architecture

## System architecture
```text
NWP / Ensembles / Observations / Archive
                 ↓
        Source adapters + ingestion
                 ↓
     Validation, alignment, unit normalization
                 ↓
      Verification + bust-label generation
                 ↓
      Feature engineering + regime detection
                 ↓
       Baseline ML + analogue retrieval
                 ↓
      Calibration (only when validated)
                 ↓
          Evidence-based explanations
                 ↓
              FastAPI v1
                 ↓
       Next.js operational dashboard
```

## Component architecture
- **Data adapters:** typed interfaces for NWP, ensemble, observation, and reference providers; demo adapter is isolated.
- **Data quality/alignment:** canonical schemas, coordinate/grid alignment, lead-time normalization, unit conversion, missingness and freshness checks.
- **Verification:** joins forecasts to eligible references, computes metrics, creates configurable labels.
- **Feature services:** ensemble statistics, gradients, temporal change, historical performance, regime features.
- **ML service:** training/evaluation artifacts, inference, probability output, model/version metadata.
- **Analogue service:** feature-vector similarity over eligible historical cases.
- **Explanation service:** model-native feature contributions and evidence records.
- **API:** FastAPI routers, Pydantic contracts, structured errors, health and metadata.
- **Frontend:** Next.js App Router, TypeScript, Tailwind/shadcn primitives, map visualization via an established geospatial library.

## Data flow
Raw scientific files are ingested into immutable/versioned object storage. Validation emits quality reports and canonical partitions. Verified forecast/reference pairs produce error records and labels. Feature tables feed chronological training and inference. Results are stored as queryable slices keyed by cycle, variable, lead time, and spatial unit. API responses include provenance and quality metadata.

## ML pipeline
1. Define information cutoff for each forecast cycle.
2. Split chronologically into train/validation/test.
3. Fit preprocessing only on training data.
4. Train interpretable logistic regression or gradient boosting baseline.
5. Evaluate discrimination, Brier score, reliability, and error by lead time/region.
6. Calibrate only if validation supports it; persist calibration artifact.
7. Generate probabilities, confidence mapping, risk clusters, and model-native explanations.
8. Register model, feature schema, dataset versions, and configuration.

## Backend architecture
Python 3.x, FastAPI, Pydantic, NumPy, Pandas, Xarray, scikit-learn, and scientific file tooling as justified. Separate pure domain services from I/O. Use dependency injection for repositories/providers. Keep long-running ingestion/training outside request handlers; MVP may use scripts/jobs and precomputed result slices.

## Frontend architecture
Next.js App Router with server-rendered metadata and a client dashboard shell for controls/map interactions. Components: shell/header, status strip, control rail, probability map, legend, risk summary, region detail, explanation list, analogue list, and data-quality states. Fetch API data through a typed client and SWR where client-side revalidation is needed. Keep domain types separate from presentation components.

## API architecture
Version routes under `/api/v1` internally while preserving concise preview aliases if needed. Use query validation for cycle, variable, lead time, region, and pagination. Return envelopes containing `data`, `metadata`, `provenance`, and `quality`. Health checks separate liveness from data/model readiness. No endpoint may promise data that the pipeline cannot produce.

## Storage architecture
- **Object storage:** raw and processed NetCDF/GRIB/Zarr and model artifacts.
- **PostgreSQL/PostGIS:** metadata, runs, quality reports, verification summaries, risk regions, and indexed result slices when spatial queries are needed.
- **Cache:** optional bounded cache for read-heavy API slices; not the system of record.
- **Local development:** filesystem samples and a local database-compatible repository interface.

The initial dashboard can run against a demo repository, but the repository contract must match production records and visibly identify demo mode.

## Model storage
Store serialized model, preprocessing, calibration, feature schema, training window, dataset identifiers, metrics, and code/configuration version together. Never load an unverified artifact silently. A model registry can be introduced after the baseline workflow stabilizes.

## Configuration management
Use environment variables for credentials and deployment settings. Use versioned typed configuration for supported variables, thresholds, grids, confidence bands, source endpoints, and freshness policies. Configuration is data, reviewed and recorded with each run.

## Logging and monitoring
Structured logs include run ID, source, cycle, lead time, variable, model version, and outcome without secrets. Monitor ingestion freshness, validation failures, missingness, inference latency, API errors, model drift, calibration, and data/model readiness. Emit metrics at pipeline boundaries.

## Error handling
Invalid source records are quarantined with reasons. Service errors map to stable API error codes. Stale or insufficient inputs produce explicit quality states. Retries are limited and idempotent. Unexpected exceptions are logged with correlation IDs and returned without internal details.

## Deployment architecture
Frontend deploys as a Next.js application. FastAPI and worker services deploy as containers, with object storage and PostgreSQL/PostGIS as managed dependencies. CI runs lint, type checks, tests, schema checks, and a reproducible sample pipeline. Docker Compose can provide local API, worker, database, and object-store-compatible development services.

## Development environment
Repository structure follows `backend/`, `frontend/` or the existing Next.js app, `data/`, `models/`, `scripts/`, `tests/`, and root documentation. Phase 0 establishes `.env.example`, logging, configuration, and contracts before real ingestion. Python and TypeScript dependencies are pinned or lockfile-managed.

## Key architectural decisions
- Prefer precomputed inference slices for large maps and predictable UX.
- Preserve scientific formats rather than flattening all grid data into SQL.
- Use established map tooling, never hand-authored geographic paths.
- Treat probability calibration as an evidence-based capability, not a label.
- Keep demo providers replaceable and impossible to confuse with production sources.
