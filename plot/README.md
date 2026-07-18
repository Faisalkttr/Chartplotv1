# Relative Strength Breakout & Base Reference Charting Engine

A modular, production-ready Streamlit dashboard designed to track structural asset outperformance. By utilizing normalized indexing (Base-100 normalization) alongside active mathematical ratio analytics, this application allows engineers and market analysts to accurately uncover structural pivots, asset accumulations, and momentum shifts against an established base asset or market benchmark.

## ⚙️ Structural Architecture

```text
├── engines/
│   ├── data_engine.py      # Data fetching layer utilizing yfinance with asset caching
│   └── chart_engine.py     # High-fidelity Plotly multi-panel chart rendering configuration
├── app.py                  # Streamlit execution core and UI window matrix
├── requirements.txt        # Production dependencies declaration
└── README.md               # Operations manual documentation
```

## 🚀 Step-by-Step Deployment Instructions

### 1. Local Configuration Setup
Clone your workspace and configure your local environment runtime:
```bash
# Clone or create your project directory
mkdir relative-strength-engine && cd relative-strength-engine

# Initialize a clean python virtual environment environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install exact production dependencies
pip install -r requirements.txt
```

### 2. Execution Protocol
Launch the analytic processing frame engine locally:
```bash
streamlit run app.py
```

### 3. Deploying Production App to GitHub
Commit your dynamic analytics architecture changes directly upstream to GitHub:
```bash
git init
git add .
git commit -m "feat: implement high-fidelity modular relative strength analytics charting engine"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 4. Continuous Streamlit Cloud Deployment
1. Navigate directly onto the web panel dashboard at [Streamlit Community Cloud](https://share.streamlit.io/).
2. Select the **New App** workflow path option.
3. Link your respective target GitHub repository tracking address (`YOUR_REPO_NAME`).
4. Designate the runtime target production main execution node path file as `app.py`.
5. Trigger **Deploy**; your enterprise application layer goes live on the public cloud instantly.

## 📊 Analytics Interpretation Guide

* **Normalized Indexing (Top Chart):** Adjusts all stock tracking coordinates back to a static base value of `100` on day one of your selected tracking frame window. This removes nominal currency differences, matching absolute return velocity cleanly.
* **Price Ratio Modeling (Bottom Chart):** Computes `Target Stock Price / Reference Base Price`. 
    * A **declining line** implies the target asset is losing ground to the base reference asset.
    * A **horizontal base consolidation** denotes equal performance stability (accumulation matrix).
    * A **clean upward structural break** signals the precise date alpha generation has started.
