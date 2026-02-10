## Initial EDA Findings (Draft Notes)

- The Brent price series shows long periods of gradual trends with several sharp spikes and drops, consistent with major geopolitical and economic events over the sample period.
- The level series (prices) appears non-stationary, with changing mean and variance over time.
- Daily log returns fluctuate around zero and show clear volatility clustering: periods of relative calm followed by periods of large swings.
- Rolling statistics of log returns indicate that volatility is time-varying, which will motivate modeling returns (or changes) rather than raw prices for change point analysis.
