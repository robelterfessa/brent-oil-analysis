import pymc as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az

# 1. Prepare small sample (PyMC is slow on huge data)
df = pd.read_csv('your_data.csv')
data_values = df['Price'].values[:500] # Let's test first 500 days
n_count = len(data_values)

# 2. The Bayesian Model
with pm.Model() as model:
    # Prior for the switch point (it could happen anywhere in the timeline)
    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count - 1)

    # Priors for the average price before and after the change
    mu_1 = pm.Exponential("mu_1", 1.0/data_values.mean())
    mu_2 = pm.Exponential("mu_2", 1.0/data_values.mean())

    # Define which 'mu' to use based on 'tau'
    idx = np.arange(n_count)
    mu_ = pm.math.switch(tau > idx, mu_1, mu_2)

    # Link the model to the actual data
    observation = pm.Poisson("obs", mu_, observed=data_values)

    # 3. RUN THE SIMULATION (MCMC)
    trace = pm.sample(1000, return_inferencedata=True)

# 4. Visualize the Result
az.plot_trace(trace, var_names=["tau"])
plt.show()

# Find the most likely date of change
predicted_tau = int(trace.posterior["tau"].mean())
print(f"The model found a change point at day: {predicted_tau}")