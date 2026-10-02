'use client'

import useSWR from 'swr'
import { useMemo, useState } from 'react'
import { Activity, ChevronDown, CircleHelp, Clock3, Crosshair, Layers3, MapPin, Radio, ShieldCheck, SlidersHorizontal, Wind } from 'lucide-react'

type Region = { name: string; latitude: number; longitude: number; value: number; tone: string; detail: string; temperature?: number; wind?: number }

const leadTimes = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10']
const regions: Region[] = [
  { name: 'Delhi NCR', latitude: 28.6139, longitude: 77.209, value: 0, tone: 'low', detail: 'Waiting for the live Open-Meteo forecast' },
  { name: 'Mumbai Coast', latitude: 19.076, longitude: 72.8777, value: 0, tone: 'low', detail: 'Waiting for the live Open-Meteo forecast' },
  { name: 'Bengaluru', latitude: 12.9716, longitude: 77.5946, value: 0, tone: 'low', detail: 'Waiting for the live Open-Meteo forecast' },
  { name: 'Kolkata Delta', latitude: 22.5726, longitude: 88.3639, value: 0, tone: 'low', detail: 'Waiting for the live Open-Meteo forecast' },
]

const fetcher = (url: string) => fetch(url).then((response) => {
  if (!response.ok) throw new Error('API error');
  return response.json();
})

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://127.0.0.1:8001';

function forecastUrl(regionName: string, day: string) {
  const dayNum = day.replace('D', '');
  return `${API_BASE_URL}/api/v1/weather/forecast/${encodeURIComponent(regionName)}?day=${dayNum}`;
}

function RiskBadge({ tone, children }: { tone: string; children: React.ReactNode }) {
  return <span className={`risk-badge risk-${tone}`}>{children}</span>
}

export default function Page() {
  const [activeDay, setActiveDay] = useState('D3')
  const [selectedName, setSelectedName] = useState(regions[0].name)

  const { data, error, isLoading } = useSWR(
    forecastUrl(selectedName, activeDay),
    fetcher,
    { refreshInterval: 900000 }
  )

  const activeRegion = useMemo(() => {
    const base = regions.find((region) => region.name === selectedName) ?? regions[0]
    if (!data) return base

    return {
      ...base,
      value: Math.round(data.bust_probability),
      tone: data.confidence === 'HIGH' ? 'high' : data.confidence === 'MODERATE' ? 'moderate' : 'low',
      detail: data.detail,
      temperature: data.temperature,
      wind: data.wind_speed
    }
  }, [selectedName, activeDay, data])

  const updated = data?.timestamp ? new Date(data.timestamp).toISOString().replace('T', ' · ').slice(0, 16) : 'Connecting to VAJRA Backend'
  const sourceLabel = error ? 'Backend unavailable' : isLoading ? 'Backend connecting' : 'VAJRA Backend live'

  return (
    <main className="vajra-app">
      <header className="topbar">
        <div className="brand-lockup"><div className="brand-mark" aria-hidden="true"><Wind size={18} /></div><div><p className="eyebrow">Meteorological intelligence</p><h1>VAJRA</h1></div></div>
        <div className="topbar-meta"><div><span className="eyebrow">Forecast cycle</span><strong className="mono">{updated}</strong></div><div className="live-status"><span className="status-dot" /> LIVE</div><div className="update-meta"><Clock3 size={14} /><span>15 min refresh</span></div></div>
      </header>

      <section className="status-strip" aria-label="Data status">
        <div className="status-item"><ShieldCheck size={15} /><span>Pipeline readiness</span><strong className={error ? 'risk-text-high' : 'good'}>{error ? 'DEGRADED' : isLoading ? 'CONNECTING' : 'READY'}</strong></div>
        <div className="status-item"><Radio size={15} /><span>Source</span><strong>{sourceLabel}</strong></div><div className="status-item"><Activity size={15} /><span>Metric</span><strong className="mono">LIVE FORECAST PROXY</strong></div>
        <p className="status-note">Operational proxy derived from backend service; not a calibrated probability.</p>
      </section>

      <div className="workspace">
        <aside className="control-rail" aria-label="Forecast controls"><div className="panel-heading"><div><p className="eyebrow">Workspace</p><h2>Forecast view</h2></div><SlidersHorizontal size={17} /></div><label className="field-label" htmlFor="variable">Variable</label><div className="select-wrap"><select id="variable" defaultValue="temperature"><option value="temperature">2m temperature error proxy</option><option disabled>Precipitation (not supported)</option></select><ChevronDown size={15} /></div><fieldset className="day-fieldset"><legend className="field-label">Lead time</legend><div className="day-grid">{leadTimes.map((day) => <button key={day} className={`day-button ${activeDay === day ? 'selected' : ''}`} aria-pressed={activeDay === day} onClick={() => setActiveDay(day)}>{day}</button>)}</div></fieldset><label className="field-label" htmlFor="region">India region</label><div className="select-wrap"><select id="region" value={selectedName} onChange={(event) => setSelectedName(event.target.value)}>{regions.map((region) => <option key={region.name}>{region.name}</option>)}</select><ChevronDown size={15} /></div><div className="rail-divider" /><div className="definition-block"><p className="eyebrow">Proxy definition</p><p>Higher values indicate larger intraday temperature spread in the live forecast.</p><span className="mono">TEMP · SPREAD · 12H</span></div><button className="help-button"><CircleHelp size={15} /> Methodology & provenance</button></aside>

        <section className="main-column"><div className="map-panel panel"><div className="map-header"><div><p className="eyebrow">Forecast proxy · {activeDay}</p><h2>Indian domain</h2></div><div className="map-actions"><button aria-label="Center map"><Crosshair size={16} /></button><button aria-label="Map layers"><Layers3 size={16} /></button></div></div><div className="map-canvas" role="img" aria-label={`Live forecast proxy map for ${activeDay}. Selected region ${activeRegion.name} has ${activeRegion.value}% proxy score.`}><div className="map-grid" aria-hidden="true" /><div className="map-contours contour-one" aria-hidden="true" /><div className="map-contours contour-two" aria-hidden="true" /><div className="map-label label-north">DELHI NCR</div><div className="map-label label-lakes">KOLKATA DELTA</div><div className="map-label label-rockies">MUMBAI COAST</div><div className="map-label label-south">BENGALURU</div><button className="map-region region-north" onClick={() => setSelectedName(regions[0].name)} aria-label={`Delhi NCR, ${activeRegion.value} percent proxy score`}><span>{selectedName === regions[0].name ? activeRegion.value : '—'}</span></button><button className="map-region region-lakes" onClick={() => setSelectedName(regions[3].name)} aria-label="Kolkata Delta live forecast"><span>{selectedName === regions[3].name ? activeRegion.value : '—'}</span></button><button className="map-region region-rockies" onClick={() => setSelectedName(regions[1].name)} aria-label="Mumbai Coast live forecast"><span>{selectedName === regions[1].name ? activeRegion.value : '—'}</span></button><button className="map-region region-south" onClick={() => setSelectedName(regions[2].name)} aria-label="Bengaluru live forecast"><span>{selectedName === regions[2].name ? activeRegion.value : '—'}</span></button><div className="map-scale"><span>LOW</span><i /><span>MODERATE</span><i /><span>HIGH</span></div></div><div className="map-footer"><span><MapPin size={13} /> Click a region to inspect</span><span className="mono">SOURCE: VAJRA BACKEND · 10-DAY</span></div></div>

          <div className="summary-grid"><div className="stat-card"><span className="eyebrow">Current proxy</span><strong className="stat-value">{isLoading ? '—' : `${activeRegion.value}%`}</strong><span className="stat-caption">live {activeRegion.name} signal</span></div><div className="stat-card"><span className="eyebrow">Temperature</span><strong className="stat-value">{activeRegion.temperature == null ? '—' : `${activeRegion.temperature.toFixed(1)}°`}</strong><span className="stat-caption">forecast at selected lead time</span></div><div className="stat-card"><span className="eyebrow">Data quality</span><strong className={`stat-value ${error ? 'risk-text-high' : 'good'}`}>{error ? 'CHECK' : isLoading ? 'SYNC' : 'LIVE'}</strong><span className="stat-caption">direct API response</span></div></div>

          <div className="details-grid"><section className="panel detail-panel"><div className="panel-heading"><div><p className="eyebrow">Selected region</p><h2>{activeRegion.name}</h2></div><RiskBadge tone={activeRegion.tone}>{activeRegion.tone.toUpperCase()}</RiskBadge></div><div className="probability-row"><strong>{isLoading ? '—' : activeRegion.value}<span>{isLoading ? '' : '%'}</span></strong><div><p>Live forecast proxy</p><span className="raw-tag">NOT CALIBRATED</span></div></div><p className="detail-copy">{activeRegion.detail}. This is an operational weather signal, not a verified historical error probability.</p><div className="detail-meta"><span>Quality <b>{error ? 'CHECK' : 'GOOD'}</b></span><span>Valid through <b>+10D</b></span><span className="mono">{activeRegion.wind == null ? '—' : `WIND ${activeRegion.wind.toFixed(0)} KM/H`}</span></div></section><section className="panel evidence-panel"><div className="panel-heading"><div><p className="eyebrow">Live evidence</p><h2>Forecast signals</h2></div><span className="mono version">VAJRA-V1</span></div><ul className="signal-list"><li><span className="signal-bar cyan" /><div><strong>Temperature spread</strong><span>12-hour intraday range</span></div><b>{activeRegion.value}%</b></li><li><span className="signal-bar amber" /><div><strong>Wind speed</strong><span>Current forecast at selected lead</span></div><b>{activeRegion.wind == null ? '—' : `${activeRegion.wind.toFixed(0)}`}</b></li><li><span className="signal-bar blue" /><div><strong>Provider status</strong><span>FastAPI backend</span></div><b>{error ? 'ERR' : 'OK'}</b></li></ul></section></div>
        </section>
      </div>
    </main>
  )
}
