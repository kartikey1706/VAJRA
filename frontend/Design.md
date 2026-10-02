# VAJRA UI/UX Design System

## Design direction
VAJRA is a serious Meteorological Intelligence + AI Operations Platform: scientific, dense, calm, and operational. It should feel like a forecasting workstation rather than a generic SaaS dashboard. The map is the primary visual element; every color and number communicates a defined state.

## Theme and tokens
- Background: deep navy `#07111F`.
- Panels: blue-black `#0D1B2A`, elevated panel `#12263A`.
- Text: white `#F4F7FB`, secondary slate `#9FB1C5`, muted `#6F8298`.
- Analytical accent: cyan `#44D7E8` and blue `#4E8CFF`.
- Elevated risk: amber `#F4B740`; high risk: red `#F05D5E`.
- High confidence: green `#43C59E`.
Use tokens, not ad hoc colors. Risk colors must be paired with labels, not used alone. Borders are subtle and surfaces are separated through contrast more than shadows.

## Typography
Use one modern sans-serif family such as Geist or Inter, with a monospace face only for technical IDs, coordinates, timestamps, and model versions. Large numerals show probability/confidence; compact uppercase labels show metadata; body text remains readable at normal zoom.

## Layout
```text
┌──────────────────────────────────────────────┐
│ VAJRA | cycle | data status | last update     │
├───────────────┬──────────────────────────────┤
│ Controls      │         Weather map           │
│ Day 1–10      │  Bust probability + legend   │
│ Variable      │  clusters + selected region   │
│ Region        │                              │
├───────────────┴──────────────────────────────┤
│ Region details | Evidence | Historical cases  │
└──────────────────────────────────────────────┘
```

Desktop uses a compact control rail and large map. Tablet collapses controls into a top bar/drawer. Smaller screens stack controls, map, summary, and detail panels; map remains first and retains a usable minimum height. Avoid overcrowded cards and preserve a clear selected-region state.

## Core components
- **Header:** VAJRA wordmark, forecast cycle, data mode, freshness, readiness indicator.
- **Control rail:** lead-time segmented control, variable select limited to backend-supported values, cycle/region selectors.
- **Map:** established geospatial library, geographic context, probability surface/regions, cluster outlines, selected region, legend, accessible textual summary.
- **Risk summary:** counts/rankings for high risk, medium risk, low confidence, current lead time.
- **Region detail:** probability, confidence, definition, forecast/ensemble statistics, data quality.
- **Evidence panel:** ranked model-supported signals with value, direction, timestamp, and model version.
- **Analogue panel:** computed historical case, similarity, observed error, and provenance.
- **Status states:** loading, no data, stale data, limited quality, unavailable, and API failure.

## Interaction principles
Controls update the map and detail panels together and preserve the selected region when possible. Changing lead time makes the active state obvious. Tooltips provide precise values without hiding essential information. The user can navigate every control by keyboard; focus is visible. Map selections have a non-map list/table alternative for accessibility and small screens.

## Data language
Always show `Bust probability`, never “failure certainty.” Use labels such as `LOW`, `MODERATE`, and `HIGH` only with the configured mapping and a visible probability. Distinguish `RAW` from `CALIBRATED`; show `DEMO MODE` prominently when applicable. Use “model evidence” rather than causal language.

## Responsive behavior
- **Desktop:** two-column workspace, persistent controls, map 60–70% of primary area, details below.
- **Tablet:** map-first layout, controls in a collapsible sheet, details in tabs or stacked panels.
- **Small screens:** horizontal scroll or wrapped Day 1–10 control, full-width map, summary cards in a compact grid, details stacked, no essential information dependent on hover.

## Accessibility and trust
Maintain WCAG-conscious contrast, semantic headings, labeled controls, ARIA selected/expanded states, reduced-motion support, and text equivalents for map information. Include timestamps, cycle, variable, units, data quality, source, and model version in the UI. Never use decorative weather imagery to imply live conditions.

## Motion and density
Use restrained transitions for selection and loading only. Avoid animated weather effects that compete with analysis. Prefer compact spacing, aligned metadata, and clear dividers. Visual density should support comparison, not create noise.

## MVP visual scope
Implement one polished map workspace, not multiple speculative pages. Prioritize map readability, lead-time switching, region inspection, evidence, provenance, and robust unavailable/demo states over decorative charts.
