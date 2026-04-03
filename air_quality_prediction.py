import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load dataset
df = pd.read_csv("air_quality_data.csv")

# Handle missing values (requirement: preprocessing)
df = df.fillna(method='ffill')

# Feature Engineering (requirement)
df['pollution_index'] = (df['pm2_5'] + df['pm10'] + df['no2']) / 3

# Define features & target
X = df[['pm2_5','pm10','no','no2','so2','co','o3','pollution_index']]
y = df['aqi']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully")
