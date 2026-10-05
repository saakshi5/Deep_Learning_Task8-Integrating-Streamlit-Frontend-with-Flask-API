from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student Performance Prediction API is running",
        "status": "success"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON data
        data = request.get_json()

        # Check whether data is provided
        if not data:
            return jsonify({
                "status": "error",
                "message": "No input data provided"
            }), 400

        # Extract values
        study_hours = float(data["study_hours"])
        attendance = float(data["attendance"])
        previous_score = float(data["previous_score"])
        sleep_hours = float(data["sleep_hours"])
        assignments_completed = float(data["assignments_completed"])

        # Create input array
        input_data = np.array([[
            study_hours,
            attendance,
            previous_score,
            sleep_hours,
            assignments_completed
        ]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Keep score between 0 and 100
        prediction = max(0, min(100, prediction))

        # Determine performance category
        if prediction >= 85:
            category = "Excellent"
        elif prediction >= 70:
            category = "Good"
        elif prediction >= 50:
            category = "Average"
        else:
            category = "Needs Improvement"

        # Return response
        return jsonify({
            "status": "success",
            "predicted_score": round(float(prediction), 2),
            "performance": category
        })

    except KeyError as e:

        return jsonify({
            "status": "error",
            "message": f"Missing field: {str(e)}"
        }), 400

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )