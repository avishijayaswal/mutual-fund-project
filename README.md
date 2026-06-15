

```markdown
#  Bluestock Mutual Fund Analytics Capstone Project

##  Project Overview

The Bluestock Mutual Fund Analytics Project is an end-to-end data analytics system built to analyze mutual fund performance, investor behavior, and market trends in the Indian mutual fund ecosystem.

The project combines **data engineering, financial analytics, and business intelligence** to transform raw datasets into actionable insights. It covers the full lifecycle of data: ingestion, cleaning, transformation, analysis, and visualization.

The main goals of this project are:
- Build an automated ETL pipeline for mutual fund data
- Analyze NAV trends and fund performance
- Evaluate risk-adjusted returns using financial metrics
- Study investor behavior and SIP trends
- Build a mutual fund recommendation system
- Visualize insights using Power BI dashboards

---

##  Project Workflow

The system follows a structured data pipeline:

```

Data Sources → ETL Pipeline → Data Cleaning → Analytics → Recommendation System → Dashboard

```

---

##  Folder Structure

```

Mutual Fund Project/
│
├── scripts/
│   ├── data_ingestion.py     # Fetches live NAV data from API
│   ├── recommender.py        # Mutual fund recommendation engine
│   ├── profiling.py          # Dataset profiling and validation
│
├── data/
│   ├── raw/                  # Raw API and CSV data
│   ├── processed/            # Cleaned datasets
│
├── run_pipeline.py           # Master pipeline script
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bluestock-mf-analytics.git
cd bluestock-mf-analytics
````

---

### 2. Create virtual environment (optional)

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Required libraries:

* pandas
* numpy
* requests
* matplotlib
* seaborn
* plotly

---

##  How to Run the Project

### Run the full pipeline

```bash
python run_pipeline.py
```

This will:

* Fetch live NAV data from API
* Save raw datasets into `/data/raw`
* Run dataset profiling
* Generate mutual fund recommendations

---

##  ETL Pipeline (Data Ingestion)

The ETL pipeline fetches live mutual fund NAV data using the MFAPI service:

```
https://api.mfapi.in/mf/<scheme_code>
```

### Features:

* Automated API data extraction
* Multiple scheme support
* CSV file storage in raw data folder
* Error-handling for API requests

---

## 📊 Dataset Description

### 1. NAV Data

Daily Net Asset Value (NAV) of mutual funds used for:

* Return calculation
* Volatility analysis
* Trend analysis

---

### 2. Scheme Performance Data

Includes:

* Sharpe Ratio
* Beta
* Alpha
* Expense Ratio
* Risk Grade

Used for:

* Performance ranking
* Risk-adjusted analysis

---

### 3. Investor Transaction Data

Contains:

* SIP investments
* Lump sum investments
* Redemption data

Used for:

* Investor behavior analysis
* Cohort segmentation
* SIP continuity tracking

---

### 4. Portfolio Holdings Data

Contains sector-wise allocation of funds used for:

* Sector concentration analysis
* Diversification study

---

## 📈 Key Features

* Automated ETL pipeline
* Live NAV data ingestion
* Mutual fund recommendation system
* Financial metrics (Sharpe, Sortino, Alpha, Beta)
* Investor behavior analysis
* SIP trend analysis
* Power BI dashboard integration

---

##  Recommendation System

Funds are recommended based on investor risk profile:

*  Low Risk → Debt / large-cap stable funds
*  Moderate Risk → Balanced hybrid funds
*  High Risk → Equity / small-cap funds

Ranking is based on:

* Sharpe Ratio
* Risk Grade
* Historical performance

---

##  Power BI Dashboard

The dashboard includes 4 pages:

1. Industry Overview
2. Fund Performance Analysis
3. Investor Analytics
4. SIP & Market Trends

### Features:

* KPI cards (AUM, SIP inflow, folios)
* Interactive filters
* Drill-through analysis
* Trend visualizations

---

##  Limitations

* Uses historical data only
* No real-time market prediction
* External macroeconomic factors not included
* Behavioral assumptions based only on transactions

---

##  Author

Bluestock Mutual Fund Analytics Capstone Project
Developed as part of Data Analytics Project Submission

---

##  Conclusion

This project demonstrates a complete end-to-end data analytics pipeline combining data engineering, financial modeling, and business intelligence.

It provides insights into mutual fund performance, investor behavior, and market trends, enabling data-driven investment decisions.

```


