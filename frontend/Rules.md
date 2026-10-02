# VAJRA Development Rules

## General coding rules
- Write small, modular, readable modules with type hints.
- Keep configuration, domain logic, I/O, and presentation separate.
- Validate all external inputs and handle errors explicitly.
- Never silently swallow errors or invent fallback values.
- Never hard-code secrets; use environment variables and safe defaults.
- Prefer simple, testable abstractions over speculative frameworks.
- Record versions for code, configuration, datasets, and models.

## AI/ML rules
- Never fabricate weather data, observations, probabilities, or historical analogues.
- Clearly label demo/mock mode and never present it as a real forecast.
- Never claim calibration without validation evidence.
- Never claim a forecast is definitely wrong; output risk and uncertainty.
- Define every target and feature, including information-availability time.
- Preserve temporal ordering and prevent future information leakage.
- Do not random-split time-series verification when it leaks information.
- Evaluate against simple baselines and report sample sizes.
- Distinguish raw, calibrated, observed, and inferred values.
- Track model and dataset versions in every result.

## Meteorological rules
- Preserve forecast cycle, initialization time, valid time, and lead time.
- Preserve coordinates, grid definition, units, and transformations.
- Handle missing, stale, duplicate, and conflicting data explicitly.
- Use a documented, configurable bust metric and threshold.
- Do not infer physical causality from feature importance alone.
- Explain outputs with evidence from actual inputs and model outputs.

## Frontend rules
- Never display placeholder data as real data.
- Display demo/production state, data timestamp, cycle, lead time, variable, and quality.
- Use semantic HTML, keyboard-accessible controls, readable contrast, and useful alt text.
- Use color semantically and pair it with text/icons/patterns where needed.
- Provide loading, empty, stale, unavailable, and error states.
- Use established geospatial libraries for maps.
- Keep components focused; do not put the entire dashboard in one page component.

## API rules
- Validate and bound query parameters.
- Use structured error responses and appropriate status codes.
- Version contracts when breaking changes occur.
- Include provenance, units, timestamps, quality, and versions.
- Never expose secrets, stack traces, or internal credentials.
- Use parameterized queries and authorization boundaries for protected operations.

## Testing and delivery rules
- Test pure calculations, schemas, temporal splits, labels, inference, API contracts, and key UI states.
- Run the narrowest relevant check after each change, then broader checks when justified.
- Do not begin the next phase until acceptance criteria for the current phase are met.
- Update `Memory.md` only after implementation begins and after meaningful milestones.
- Prefer correctness, reproducibility, and transparent uncertainty over visual completeness.
