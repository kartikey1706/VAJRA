VAJRA ⚡

AI-Based Forecast Bust Detection for Medium-Range Weather Forecasts

Medium-range Numerical Weather Prediction (NWP) forecasts can develop large errors during rapidly evolving situations such as:

• Monsoon depressions
• Heavy rainfall events
• Cyclones
• Western disturbances
• Heat waves
• Active / break monsoon phases
• Other rapidly changing atmospheric conditions

Operational users therefore need an additional system that can:

• Identify potentially error-prone regions
• Estimate forecast-bust risk across Day 1–Day 10
• Compare the current atmospheric situation with historical forecast behaviour
• Explain factors associated with lower forecast confidence
• Provide an operational dashboard and API


SOLUTION

VAJRA works as a forecast reliability layer on top of meteorological forecast data.

Core Workflow

Real Meteorological Data
        ↓
Data Ingestion & Quality Control
        ↓
Forecast Verification
        ↓
Forecast Error → Bust / No-Bust
        ↓
Feature Engineering
        ↓
VAJRA AI/ML Risk Model
        ↓
Bust Risk → Calibration → Confidence
        ↓
Historical Analogue + Weather Regime
+ Forecast Evolution + Explainability
        ↓
Regional Risk & Decision Support


CORE PRINCIPLE

VAJRA does not replace the weather forecast — it quantifies WHERE, WHEN and WHY the forecast may be unreliable.


SYSTEM ARCHITECTURE

METEOROLOGICAL DATA
NWP | Ensemble | Observations | Atmospheric | Historical
        ↓
DATA INGESTION & QUALITY ENGINE
Clean → Validate → Align → Quality Check
        ↓
FORECAST VERIFICATION
Forecast vs Observation → Error → Bust / No-Bust
        ↓
VAJRA AI/ML ENGINE
NWP + Ensemble + Atmospheric + Historical + Regime
        ↓
Bust Risk → Calibration → Confidence
        ↓
LIVE INFERENCE + INTELLIGENCE ENGINE
Current Forecast
Historical Analogues
Weather Regime
Forecast Evolution
Explainability
        ↓
DECISION SUPPORT
D1–D10 Confidence
Risk Regions
Explanations
        ↓
VAJRA DASHBOARD / API


CORE COMPONENTS

1. Meteorological Data

VAJRA is designed around multiple meteorological information sources:

• NWP forecast data
• Ensemble forecast information
• Weather observations
• Atmospheric / reanalysis information
• Historical forecasts
• Historical observations and forecast errors

The system keeps forecast cycle, valid time, lead time, variable and spatial information associated with the data wherever available.


2. Data Ingestion & Quality Control

Before analysis, meteorological data passes through validation and alignment steps.

Key checks include:

• Missing data
• Timestamp consistency
• Unit consistency
• Coordinate / grid consistency
• Forecast–observation temporal alignment
• Spatial alignment
• Data availability and completeness

This helps prevent poor-quality or misaligned inputs from being silently treated as reliable evidence.


3. Forecast Verification

Forecast bust detection must be based on measurable forecast error.

Forecast
   ↓
Observation / Reference
   ↓
Forecast Error
   ↓
Bust / No-Bust

Depending on the variable and evaluation design, verification can use appropriate error metrics such as:

• MAE
• RMSE
• Bias
• Event-based error measures

Bust thresholds should be defined and validated for the relevant variable and lead time rather than using one universal threshold for every forecast.


4. VAJRA AI/ML Risk Model

The model can combine several categories of information:

NWP Features
Forecast values, lead time and spatial patterns

Ensemble Features
Spread, member disagreement and uncertainty

Atmospheric Features
Temperature, pressure, wind and moisture

Historical Error Features
Previous forecast behaviour

Weather Regime Features
Monsoon, cyclone/depression, western disturbance, heat wave and heavy rainfall

Data Quality Features
Availability and completeness

The model estimates forecast-bust risk, which can then be calibrated before being presented as a probability.

Ensemble disagreement is treated as an uncertainty signal, not as direct proof that a forecast will fail.


INTELLIGENCE LAYER

Historical Analogue Engine

Current Atmospheric State
        ↓
Similarity Search
        ↓
Historical Cases
        ↓
Verified Forecast Errors
        ↓
Analogue Evidence

This provides additional context for the current risk estimate.


Weather Regime Engine

VAJRA can account for India-relevant weather regimes such as:

• Active / break monsoon
• Cyclone / depression
• Western disturbance
• Heat wave
• Heavy rainfall


Forecast Evolution Engine

Previous Forecast Cycle
        ↓
Current Forecast Cycle
        ↓
Risk Increase / Decrease
        ↓
Why did the risk change?

This helps users understand whether forecast reliability is improving or deteriorating between forecast cycles.


EXPLAINABILITY

VAJRA is designed to make risk understandable rather than presenting only a number.

Potential explanation signals include:

• Ensemble uncertainty
• Historical forecast-error behaviour
• Weather regime
• Forecast lead time
• Atmospheric variability
• Data quality
• Model feature importance / SHAP where applicable

Example:

WHY IS CONFIDENCE LOW?

• Higher ensemble disagreement
• Similar historical situations had larger errors
• Rapid atmospheric evolution
• Longer forecast lead time
• Current regime has historically higher error

Model explanations describe model associations, not guaranteed physical causation.


SPATIAL RISK DETECTION

Grid-Level Bust Risk
        ↓
Spatial Aggregation
        ↓
Risk Clustering
        ↓
Error-Prone Regions

This supports region-wise forecast-confidence maps and identification of areas that deserve additional forecast scrutiny.


HISTORICAL BUST REPLAY

One of VAJRA's key validation and demonstration concepts is Historical Bust Replay.

Historical Event
        ↓
What the forecast predicted
        ↓
What actually happened
        ↓
Forecast Error
        ↓
Historical Analogue Evidence
        ↓
VAJRA Risk / Confidence

This allows the system to be evaluated against real historical cases instead of relying only on a static dashboard demonstration.


EXPECTED OUTPUTS

• Day 1–Day 10 forecast confidence
• Forecast-bust risk
• Error-prone region detection
• Historical analogue evidence
• Forecast evolution
• Explainable risk factors
• Data quality information
• Forecast verification metrics
• Operational API / dashboard outputs


TECHNOLOGY STACK

Backend

• Python
• FastAPI
• Pydantic
• Pydantic Settings
• NumPy
• scikit-learn
• HTTPX

AI / ML

• Python ML ecosystem
• Feature engineering
• Forecast verification
• Classification / risk modelling
• Probability calibration
• Explainability

Frontend / Visualization

The VAJRA project can expose model outputs through a web-based dashboard for:

• Forecast confidence
• Regional risk
• Day 1–Day 10 analysis
• Explanations
• Historical evidence

Deployment

• Local development
• Docker-based deployment
• Cloud deployment
• Future Cloud / HPC scaling


PROJECT STRUCTURE

VAJRA/
├── app/
│   ├── api/
│   ├── core/
│   ├── data/
│   ├── ml/
│   ├── models/
│   └── services/
├── requirements.txt
├── .gitignore
└── README.md


LOCAL SETUP

1. Clone the repository

git clone https://github.com/kartikey1706/VAJRA.git

cd VAJRA


2. Create a virtual environment

Windows:

python -m venv .venv

.venv\Scripts\activate

Linux / macOS:

python3 -m venv .venv

source .venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Start the FastAPI server

uvicorn app.main:app --reload

The API will be available at:

http://localhost:8000

Interactive API documentation:

http://localhost:8000/docs

Check the automatically generated Swagger documentation for the exact endpoints available in the current build.


API

The FastAPI backend provides the foundation for exposing forecast, risk, confidence and intelligence outputs to the dashboard.

Typical API areas include:

/api/v1/forecast
/api/v1/...

Check the automatically generated Swagger documentation at:

http://localhost:8000/docs

for the exact endpoints available in the current build.


VALIDATION AND MODEL EVALUATION

A production-grade VAJRA implementation should evaluate the model using chronological validation.

Past Data
   ↓
Training
   ↓
Later Historical Data
   ↓
Validation
   ↓
Future Hold-out Period
   ↓
Final Test

This helps prevent temporal data leakage.

Useful evaluation measures include:

• Precision
• Recall
• F1-score
• ROC-AUC
• PR-AUC
• Brier Score
• Reliability / calibration analysis
• MAE
• RMSE
• Bias

Model performance should be evaluated by variable, region and forecast lead time wherever sufficient data is available.


DRIFT-AWARE MODEL UPDATING

VAJRA is intended to support a controlled model-update loop.

New Forecast + Observations
          ↓
Verification
          ↓
Performance Monitoring
          ↓
Drift Detection
          ↓
Recalibration
          ↓
Retraining — if required

This is preferable to blindly retraining the model after every new forecast.


LIMITATIONS

VAJRA is a decision-support system, not a replacement for operational meteorologists or official weather warnings.

Important limitations include:

• Forecast busts are relatively rare events
• Historical behaviour may not fully represent future extreme events
• Observation quality directly affects forecast verification
• Atmospheric regimes are non-stationary
• Ensemble spread indicates uncertainty but does not guarantee forecast failure
• Explainability methods such as feature importance or SHAP describe model association, not causality
• Any probability shown to users should be properly calibrated and validated before being treated as a probabilistic forecast claim


FUTURE SCOPE

Possible future extensions include:

• Verified IMD / NCMRWF data integrations
• Larger historical NWP archives
• Multi-model forecast comparison
• More detailed spatial risk clustering
• Automated drift monitoring
• Advanced probabilistic calibration
• More India-specific weather regime detection
• Historical bust replay library
• Forecaster feedback / human-in-the-loop workflows
• Cloud / HPC scaling for larger spatial-temporal datasets


IMPACT

VAJRA aims to improve forecast reliability awareness, not simply forecast accuracy.

Instead of asking only:

“What will the weather be?”

VAJRA adds:

“How much confidence should we place in this forecast, where is the risk of a large error higher, and what evidence supports that assessment?”

This can help forecasters and operational users prioritize regions and lead times that deserve additional scrutiny.


LICENSE

This project is developed as a Smart India Hackathon prototype.

Add the project's final license when the team decides the appropriate open-source or institutional licensing model.


VAJRA

Real Data → Verification → Bust Label → ML Risk → Calibration → Explanation → Decision Support
