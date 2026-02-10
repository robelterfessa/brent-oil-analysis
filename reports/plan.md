Title: Change Point Analysis and Statistical Modeling of Brent Oil Prices
Problem: Brent oil prices are strongly affected by geopolitical events, OPEC decisions, conflicts, and economic shocks. This makes it hard for investors, policymakers, and energy companies to make stable and informed decisions. I need to detect structural changes (change points) in Brent oil prices and relate them to major events to provide clear, data-driven insights.

## Overall Data Analysis Workflow (High Level)

1. Data understanding and planning
   - Read the challenge document and clarify objectives.
   - List all deliverables (code, reports, dashboard, GitHub link).

2. Data collection and organization
   - Obtain the Brent oil price dataset (daily prices).
   - Store raw data in a dedicated data folder.
   - Create a separate CSV for key geopolitical and economic events.

3. Exploratory data analysis (EDA)
   - Load the Brent data into a notebook.
   - Clean and format the Date and Price columns.
   - Plot the price series over time to see trends and shocks.
   - Compute and plot log returns to inspect volatility and stationarity.

4. Change point modeling (Bayesian with PyMC)
   - Choose an appropriate transformation (prices or log returns).
   - Define a Bayesian change point model with a discrete switch point.
   - Fit the model using MCMC sampling.
   - Diagnose convergence and inspect posterior distributions.

5. Event association and impact quantification
   - Compare detected change point dates with the event CSV.
   - Hypothesize which events are linked to each major change.
   - Quantify before/after changes in average prices or returns.

6. Dashboard and API development
   - Expose cleaned data and model outputs via a Flask backend.
   - Build a React frontend to visualize prices, change points, and events.
   - Add filters, date range selection, and event highlighting.

7. Reporting and communication
   - Write an interim report (Task 1).
   - Write the final report in blog style with figures and explanations.
   - Capture dashboard screenshots and prepare final submission via GitHub.

## Detailed Analysis Steps (From Data Loading to Insights)

Step 1: Data loading and initial checks

- Load the Brent prices CSV into a Jupyter notebook using pandas.
- Convert the Date column to datetime format.
- Sort the data by date and check for missing values or duplicated dates.
- Create simple summary statistics (min, max, mean, standard deviation of Price).

Step 2: Basic visualization

- Plot the full Price time series to visually inspect long-term trends and major spikes or drops.
- Mark a few obvious crisis periods (e.g., big spikes) for later comparison with events.
- If needed, resample to monthly averages to see smoother long-term behavior.

Step 3: Transformations and stationarity checks

- Compute daily log returns: log(price*t) – log(price*{t-1}).
- Plot the log returns series to observe volatility clustering and outliers.
- Use simple tests and plots (rolling mean, rolling variance, ACF) to discuss whether prices or returns look more stationary.
- Decide whether to model prices directly or model log returns based on these observations.

Step 4: Building the Bayesian change point model

- Choose the time index representation (integer day index).
- Define a prior for the change point (tau) as a discrete uniform over all days.
- Define separate parameters for “before” and “after” segments (e.g., different means and possibly different standard deviations).
- Use a switch function in PyMC to combine these into a single time series mean.
- Define the likelihood using a Normal distribution for prices or returns.
- Run MCMC sampling to obtain posterior distributions of tau and the other parameters.

Step 5: Model diagnostics and interpretation

- Check MCMC diagnostics (r_hat, effective sample size, trace plots) to ensure convergence.
- Plot the posterior distribution of tau (the change point position).
- Extract credible intervals for the “before” and “after” means.
- Interpret the magnitude and direction of the shift and describe the uncertainty.

Step 6: Linking change points to real-world events

- Compare the posterior change point dates and credible intervals with the event dataset.
- For each major change point, identify candidate events that occurred near that date.
- Formulate narrative explanations (hypotheses) connecting events to price shifts.
- Quantify the impact for each case (e.g., percentage change in average price).

Step 7: Dashboard preparation and deployment

- Prepare cleaned data and model outputs (e.g., CSV or JSON) for the dashboard.
- Design Flask API endpoints to serve price data, change point results, and event data.
- Build React components to display time series plots, change points, and event markers.
- Add interactive filters (date range, event type) and event highlight features.
- Test the dashboard with example workflows that a stakeholder would follow.

Step 8: Reporting and finalization

- Summarize the methodology and main findings in a final report.
- Include figures showing price trends, change points, and event annotations.
- Discuss limitations (data coverage, model assumptions, causality vs correlation).
- Suggest future extensions (additional variables, more complex models).
- Ensure code, documentation, and dashboard are pushed to GitHub for final submission.

## Event Dataset Plan

I will use a separate CSV file (events_brent_oil.csv) to store major geopolitical, OPEC, economic, and financial events that are likely to influence Brent oil prices. Each row contains an event_id, an approximate start date, a short event name, an event type, and a brief description.

The events include, for example, OPEC production cuts, sanctions on major oil producers, wars or conflicts affecting supply routes, and global economic or financial crises. Dates are approximate and chosen to match the period of the dataset (up to September 2022). This structure will make it easy to join or visually overlay events with the Brent price time series when interpreting detected change points later.

## Assumptions

1. Data quality and completeness
   - I assume the Brent oil price dataset is correctly recorded, with accurate daily prices and minimal measurement errors.
   - I assume there are no large gaps in the data, or that any small gaps can be handled with simple methods (e.g., ignoring a few missing days).

2. Single main market benchmark
   - I assume Brent is a suitable benchmark for global oil prices and reflects the key market reactions to geopolitical and economic events.

3. Approximate event timing
   - I assume the approximate event dates in the event CSV are good enough to detect meaningful associations with price changes, even if they are not exact to the day.

4. Simple change point structure
   - I assume that a model with a small number of change points (starting with one main change point) can capture the most important structural breaks in the price or return series.

5. Distributional assumptions
   - I assume that daily prices or log returns can be reasonably approximated by a Normal distribution for the purpose of the initial Bayesian change point model, even though real financial returns may be heavy-tailed.

## Limitations

1. Correlation in time does not prove causation
   - Even if a detected change point in the price series occurs close in time to a geopolitical event or policy decision, this does not prove that the event caused the price change.
   - Other confounding factors (e.g., global demand shifts, monetary policy, unrelated supply disruptions) may influence prices at the same time, so we can only talk about associations, not guaranteed causal effects. [web:34]

2. Model simplifications
   - The initial model focuses on a single change point with simple before/after parameters, which may miss multiple smaller structural breaks or more complex dynamics. [web:39]
   - Assuming a Normal distribution for returns or prices can underestimate extreme movements and tail risk, which are common in oil markets. [web:36]

3. Limited explanatory variables
   - The core analysis uses only price data (and possibly log returns) plus qualitative event information. It does not explicitly model macroeconomic variables, exchange rates, or inventories that also affect oil prices. [web:23]

4. Data period and event selection
   - The event list is selective and may omit relevant events, especially smaller policy changes or regional conflicts that still influence prices. [web:27]
   - Approximate event dates and subjective choices of which events to include can bias the interpretation of which events “match” the detected change points.

5. Computational and practical constraints
   - For time reasons, the analysis may rely on relatively simple models and a limited number of MCMC samples, which may affect the precision of posterior estimates.
   - More advanced models (e.g., multiple change points, regime-switching volatility models) are possible but may not be fully implemented in this project.

## Correlation in Time vs Causal Impact

In this project, change points and events are compared mainly based on time alignment: I look for dates where the statistical properties of prices or returns change and see whether important events occur near those dates. This reveals temporal correlations, meaning that price behavior and events move together in time.

However, correlation in time alone is not enough to prove causality. To claim a causal impact, one would need stronger evidence, such as ruling out other confounding factors, using more detailed structural or econometric models, or designing quasi-experiments. In this project, I will therefore describe results as “consistent with” or “suggestive of” an impact from certain events, rather than making strong causal claims.

## Communication Channels and Output Formats

To communicate results to different stakeholders, I plan to use several channels:

1. Written reports
   - Interim report (1–2 pages) summarizing the planned workflow, event dataset, and initial EDA.
   - Final report in blog-post style (Markdown or PDF) with visuals, aimed at educated but non-technical readers (e.g., policymakers and business analysts).

2. Interactive dashboard
   - A web-based dashboard built with a Flask backend and React frontend.
   - Stakeholders can explore historical Brent prices, detect change points, and view highlighted events through interactive plots.

3. Presentations and slides (if required)
   - Short slide deck summarizing key findings, key change points, and their possible drivers.

4. Repository and technical documentation
   - GitHub repository containing code, notebooks, and README instructions so technical team members can reproduce and extend the analysis.

## Brent Price Data Source

I will use the BrentOilPrices.csv file provided by 10 Academy as the main dataset, stored in the data folder (renamed locally to brent_oil_prices_daily.csv if needed). The file contains daily Brent oil prices with at least:

- Date: the calendar date of each observation.
- Price: the Brent oil price in USD per barrel.

According to the challenge description, the dataset covers daily prices from 20-May-1987 to 30-Sep-2022, which provides a long historical window to detect structural breaks and relate them to major geopolitical and economic events.

## Initial EDA Findings (Draft Notes)

- The Brent price series shows long periods of gradual trends with several sharp spikes and drops, consistent with major geopolitical and economic events over the sample period.
- The level series (prices) appears non-stationary, with changing mean and variance over time.
- Daily log returns fluctuate around zero and show clear volatility clustering: periods of relative calm followed by periods of large swings.
- Rolling statistics of log returns indicate that volatility is time-varying, which will motivate modeling returns (or changes) rather than raw prices for change point analysis.

## Initial EDA Findings (Draft Notes)

- The Brent price series shows long periods of gradual trends with several sharp spikes and drops, consistent with major geopolitical and economic events over the sample period.
- The level series (prices) appears non-stationary, with changing mean and variance over time.
- Daily log returns fluctuate around zero and show clear volatility clustering: periods of relative calm followed by periods of large swings.
- Rolling statistics of log returns indicate that volatility is time-varying, which will motivate modeling returns (or changes) rather than raw prices for change point analysis.
