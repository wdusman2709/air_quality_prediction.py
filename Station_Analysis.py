import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: Load the data ---
# This will print an error if the file isn't found
try:
    df = pd.read_csv('stations.csv')
    print("✅ Success: stations.csv loaded!")
except Exception as e:
    print(f"❌ Error: Could not find the file. {e}")

# --- STEP 2: Quick Data Check ---
# This ensures there is data to process
print(f"Total Stations found: {len(df)}")
print(f"Total States covered: {df['State'].nunique()}")

# --- STEP 3: Data Cleaning ---
# If Status is empty, we mark it as 'Unknown'
df['Status'] = df['Status'].fillna('Unknown')

# --- STEP 4: Visualization 1 (State Distribution) ---
plt.figure(figsize=(10, 6))
state_counts = df['State'].value_counts().head(10)
state_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 States with Most Monitoring Stations')
plt.xlabel('State')
plt.ylabel('Number of Stations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() # This command forces the window/output to pop up

# --- STEP 5: Visualization 2 (Status Distribution) ---
plt.figure(figsize=(7, 7))
df['Status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Station Operational Status')
plt.ylabel('') # Hides the vertical label for a cleaner look
plt.show()

print("--- Analysis Complete ---")
