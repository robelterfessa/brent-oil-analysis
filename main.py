import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt
# Load your data
df = pd.read_csv('BrentOilPrices.csv') # Replace with your file name
df['Date'] = pd.to_datetime(df['Date']) # Tell Python 'Date' is a date
df.set_index('Date', inplace=True) # Use Date as the reference

# Draw a simple chart to see the prices
df['Price'].plot(figsize=(12, 6))
plt.title('Brent Oil Prices Over Time')
plt.show()

# --- STEP 5: CHANGE POINT DETECTION ---

# 1. We take the price column and turn it into a list of numbers for the math model
price_data = df['Price'].values 

# 2. We use the "Pelt" algorithm. Think of this as a detective 
# searching for spots where the "vibe" of the data changed.
model = "l2"  
algo = rpt.Pelt(model=model).fit(price_data)

# 3. Predict the change points. 
# 'penalty' is like sensitivity. Higher number = finds fewer, bigger changes.
result = algo.predict(pen=10) 

# 4. Show the result on a graph
rpt.display(price_data, result)
plt.title('Change Point Detection (Vertical lines are major shifts)')
plt.show()

# 5. Print the dates of these changes so you can see them
print("Change points detected at these positions:", result)