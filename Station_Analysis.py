import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_stations():
    # 1. Load the dataset
    try:
        df = pd.read_csv('stations.csv')
        print("Stations dataset loaded successfully!")
    except FileNotFoundError:
        print("Error: stations.csv not found.")
        return

    # 2. Data Cleaning & Preparation
    # Fill missing Status values as 'Inactive/Unknown'
    df['Status'] = df['Status'].fillna('Inactive/Unknown')

    # 3. Basic Insights
    total_stations = len(df)
    total_cities = df['City'].nunique()
    total_states = df['State'].nunique()

    print(f"\n--- Quick Stats ---")
    print(f"Total Monitoring Stations: {total_stations}")
    print(f"Total Cities Covered: {total_cities}")
    print(f"Total States Covered: {total_states}")

    # 4. Visualization 1: Top 10 States with most stations
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='State', order=df['State'].value_counts().index[:10], palette='viridis')
    plt.title('Top 10 States by Number of Monitoring Stations')
    plt.xlabel('Count of Stations')
    plt.tight_layout()
    plt.show()

    # 5. Visualization 2: Station Status Distribution
    plt.figure(figsize=(8, 8))
    df['Status'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff','#ff9999'], startangle=90)
    plt.title('Distribution of Station Status (Active vs. Others)')
    plt.ylabel('')
    plt.show()

    # 6. Grouping Data for GitHub display
    state_summary = df.groupby('State')['StationId'].count().sort_values(ascending=False)
    print("\n--- Stations per State (Top 5) ---")
    print(state_summary.head(5))

if __name__ == "__main__":
    analyze_stations()
