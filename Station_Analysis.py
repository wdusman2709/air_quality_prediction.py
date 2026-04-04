import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    df = pd.read_csv('stations.csv')
    print("✅ Success: stations.csv loaded!")
except Exception as e:
    print(f"❌ Error: Could not find the file. {e}")
print(f"Total Stations found: {len(df)}")
print(f"Total States covered: {df['State'].nunique()}")

df['Status'] = df['Status'].fillna('Unknown')
plt.figure(figsize=(10, 6))
state_counts = df['State'].value_counts().head(10)
state_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 States with Most Monitoring Stations')
plt.xlabel('State')
plt.ylabel('Number of Stations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(7, 7))
df['Status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Station Operational Status')
plt.ylabel('') # Hides the vertical label for a cleaner look
plt.show()

print("--- Analysis Complete ---")
