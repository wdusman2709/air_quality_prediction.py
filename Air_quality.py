import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def run_air_quality_analysis():
    # 1. Load Dataset
    try:
        df = pd.read_csv('city_day.csv')
        print("Dataset loaded successfully!")
    except FileNotFoundError:
        print("Error: city_day.csv not found.")
        return

    # 2. Data Cleaning
    # Selecting the core pollutants and the target variable (AQI)
    cols = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3', 'AQI']
    df_clean = df[cols].dropna()
    
    print(f"Data cleaned. Rows remaining: {len(df_clean)}")

    # 3. Feature Selection
    X = df_clean.drop('AQI', axis=1)
    y = df_clean['AQI']

    # 4. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Model Training (Random Forest)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 6. Evaluation
    predictions = model.predict(X_test)
    print("\n--- Model Performance ---")
    print(f"R2 Score: {r2_score(y_test, predictions):.2f}")
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions):.2f}")

    # 7. Visualization
    plt.figure(figsize=(10, 6))
    feat_importances = pd.Series(model.feature_importances_, index=X.columns)
    feat_importances.nlargest(10).plot(kind='barh', color='skyblue')
    plt.title('Top Pollutants Impacting Air Quality (AQI)')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_air_quality_analysis()
