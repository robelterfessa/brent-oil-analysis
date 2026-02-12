# Interim Report – Task 1

## Change Point Analysis and Statistical Modeling of Brent Oil Prices

### 1. Project Overview

Brent oil prices react strongly to geopolitical events, OPEC decisions, sanctions, and global economic shocks. This project aims to detect structural breaks (change points) in Brent oil prices and relate them to major events, helping investors, policymakers, and energy companies understand and respond to price shifts more effectively. [file:1]

### 2. Data Sources

- **Brent price data**: Daily Brent oil prices from the file `brent_oil_prices_daily.csv`, provided by 10 Academy, covering approximately 20-May-1987 to 30-Sep-2022, with columns for Date and Price in USD per barrel. [file:1]
- **Event data**: Manually compiled `events_brent_oil.csv` containing 10–15 key geopolitical, OPEC, sanctions, and economic events with approximate start dates, event types, and brief descriptions, chosen for their likely impact on oil markets.

### 3. Planned Analysis Workflow

The analysis follows these main stages:

1. Data loading and cleaning (parse dates, sort by date, check for missing values).
2. Exploratory data analysis (EDA) of price levels and log returns, including visual inspection of trends and volatility.
3. Construction of a Bayesian change point model to detect structural breaks in the price or return series using PyMC.
4. Interpretation of posterior change point distributions and parameter shifts (before vs after).
5. Matching detected change points to the event dataset and forming hypotheses about which events contributed to the shifts.
6. Building a Flask + React dashboard to expose historical prices, change points, and events to stakeholders.
7. Reporting, including limitations and suggestions for future extensions. [file:1]

(Details are documented in `reports/analysis_plan.md`.)

### 4. Event Dataset Summary

The `events_brent_oil.csv` file includes events such as:

- OPEC production cuts (e.g., 2016 output cut).
- Major geopolitical events (e.g., Russia–Ukraine war outbreak, Saudi Aramco facility attack).
- Sanctions-related events (e.g., US withdrawal from the Iran nuclear deal, EU embargo on Iranian oil).
- Global economic and financial shocks (e.g., 2008 financial crisis, COVID-19 demand collapse). [web:25][web:26][web:27]

Each row has: `event_id`, `date`, `event_name`, `event_type`, and `description`, which will later be aligned with detected change points.

### 5. Initial EDA Findings

Based on the first notebook (`01_task1_eda.ipynb`):

- The raw Brent price series shows long-term trends with multiple sharp spikes and drops, indicating structural changes and crisis periods.
- The level series appears non-stationary, with changing mean and variance over time.
- Daily log returns fluctuate around zero and show volatility clustering, with calm periods and periods of large swings.
- Rolling statistics of log returns (rolling mean and standard deviation) confirm that volatility is time-varying, suggesting that modeling returns or changes is more appropriate than modeling raw prices directly.

### 6. Assumptions, Limitations, and Correlation vs Causation

Key assumptions include:

- The Brent price dataset is accurate and sufficiently complete.
- Brent is a good proxy for global oil market conditions.
- Event dates in `events_brent_oil.csv` are approximate but close enough for meaningful comparison.
- A simple change point structure (initially one main change) can capture the most important structural breaks.
- A Normal distribution is an acceptable approximation for daily prices or returns in the initial model. [web:36][web:39]

Key limitations:

- Temporal alignment between events and change points only shows correlation in time and does not prove causal impact; other confounding factors may be at play. [web:30][web:34]
- The model’s simplicity may miss multiple smaller breaks and heavy tails in returns.
- The event list is selective and may omit relevant events.
- Resource constraints limit the use of more complex multi-break or regime-switching models.

In the analysis, results will be described as associations (“consistent with” or “suggestive of” an impact) rather than strong causal claims.

### 7. Next Steps

- Fix PyMC installation in the Conda environment and implement the Bayesian change point model as described in the plan.
- Estimate the posterior distribution of the main change point and before/after parameters.
- Quantify the impact of key events in terms of changes in mean price or returns.
- Start preparing the Flask backend and React frontend structure for the dashboard as required for the final submission. [file:1]

### Preliminary Change Point Result (Draft)

The Bayesian change point model on daily log returns identifies a main structural break around **[CHANGE_DATE]** (median posterior estimate). Around this date, the average daily log return shifts from approximately **[BEFORE_PCT]%** per day to **[AFTER_PCT]%** per day.

This suggests that after the change point, Brent prices experienced a [stronger/weaker] average drift, together with time-varying volatility seen in the return plots. When this date is compared to the event dataset, it is close to **[EVENT_NAME]** (event type: [EVENT_TYPE]), which is economically plausible as a driver of a structural change in oil markets. However, this temporal alignment indicates association, not definitive causality, given the presence of other potential confounding macroeconomic factors. [web:25][web:26][web:27][web:34]
