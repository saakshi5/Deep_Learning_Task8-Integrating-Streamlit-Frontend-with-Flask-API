import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Sample student dataset
data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 4,
        5, 6, 7, 8, 3, 5, 7, 9, 2, 6
    ],

    "attendance": [
        55, 60, 65, 70, 75, 80, 85, 90, 95, 98,
        62, 68, 72, 78, 82, 88, 92, 96, 99, 74,
        79, 84, 89, 93, 67, 76, 86, 94, 58, 81
    ],

    "previous_score": [
        45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
        48, 53, 58, 63, 68, 73, 78, 83, 88, 61,
        66, 71, 76, 81, 56, 64, 74, 87, 47, 69
    ],

    "sleep_hours": [
        5, 5, 6, 6, 7, 7, 7, 8, 8, 8,
        5, 6, 6, 7, 7, 8, 8, 8, 9, 6,
        7, 7, 8, 8, 6, 7, 8, 9, 5, 7
    ],

    "assignments_completed": [
        3, 4, 5, 5, 6, 7, 7, 8, 9, 10,
        3, 5, 5, 6, 7, 8, 8, 9, 10, 6,
        7, 7, 8, 9, 5, 6, 8, 9, 4, 7
    ],

    "final_score": [
        42, 48, 53, 59, 65, 71, 76, 83, 89, 94,
        46, 52, 57, 64, 69, 75, 81, 86, 92, 61,
        67, 72, 79, 85, 55, 65, 77, 89, 44, 70
    ]
}

df = pd.DataFrame(data)

# Input features
X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "sleep_hours",
        "assignments_completed"
    ]
]

# Target
y = df["final_score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Completed")
print("-------------------------")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save model
joblib.dump(model, "model.pkl")

print("\nModel saved successfully as model.pkl")