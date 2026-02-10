import pandas as pd
from statsmodels.tsa.stattools import adfuller

def load_and_clean(filepath):
    # Load data
    df = pd.read_csv(filepath)
    # 1. Convert Date
    df['Date'] = pd.to_datetime(df['Date'])
    # 2. Sort by date (important for time series!)
    df = df.sort_values('Date')
    # 3. Handle missing values (if any)
    df = df.fillna(method='fill') 
    return df

def check_stationarity(series):
    # The PDF mentions statistical modeling. 
    # The Augmented Dickey-Fuller test checks if the data is stable.
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    if result[1] <= 0.05:
        print("Data is stationary (Good for modeling)")
    else:
        print("Data is non-stationary (Needs transformation)")

# Execution
if __name__ == "__main__":
    data = load_and_clean('BrentOilPrices.csv') # PUT YOUR FILENAME HERE
    check_stationarity(data['Price'])