# air_quality_prediction.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Step 1: Load Dataset
df = pd.read_csv("air_quality.csv")

# Step 2: Basic Preprocessing
df = df.dropna()

# Example columns (modify based on dataset)
# ['PM2.5', 'PM10', 'NO', 'NO2', 'SO2', 'CO', 'O3', 'AQI']

# Step 3: Feature Engineering
df['PM_ratio'] = df['PM2.5'] / (df['PM10'] + 1)

# Step 4: Define Features & Target
X = df.drop('AQI', axis=1)
y = df['AQI']

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Model Training
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Step 7: Evaluation
y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Step 8: Save Model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved as model.pkl")
