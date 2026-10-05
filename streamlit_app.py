import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Prediction System")

st.write(
    "Enter student information below. "
    "The Streamlit frontend will communicate with the Flask API "
    "to generate a real-time prediction."
)

st.divider()

# API URL
API_URL = "http://127.0.0.1:5000/predict"

# Input section
st.subheader("📋 Student Information")

study_hours = st.number_input(
    "📚 Study Hours per Day",
    min_value=0.0,
    max_value=15.0,
    value=5.0,
    step=0.5
)

attendance = st.number_input(
    "📅 Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

previous_score = st.number_input(
    "📝 Previous Exam Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

sleep_hours = st.number_input(
    "😴 Sleep Hours per Day",
    min_value=0.0,
    max_value=15.0,
    value=7.0,
    step=0.5
)

assignments_completed = st.number_input(
    "📚 Assignments Completed",
    min_value=0,
    max_value=10,
    value=7,
    step=1
)

st.divider()

# Prediction button
if st.button(
    "🔮 Predict Student Performance",
    use_container_width=True
):

    # Prepare data
    input_data = {
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "sleep_hours": sleep_hours,
        "assignments_completed": assignments_completed
    }

    try:

        # Send request to Flask API
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=10
        )

        # Check response
        if response.status_code == 200:

            result = response.json()

            predicted_score = result["predicted_score"]
            performance = result["performance"]

            st.success("Prediction generated successfully!")

            st.subheader("📊 Prediction Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Predicted Score",
                    f"{predicted_score}%"
                )

            with col2:
                st.metric(
                    "Performance",
                    performance
                )

            # Progress bar
            st.write("### Performance Level")

            progress = predicted_score / 100

            st.progress(progress)

            if performance == "Excellent":
                st.success(
                    "🌟 Excellent performance! Keep up the great work."
                )

            elif performance == "Good":
                st.info(
                    "👍 Good performance. Continue working consistently."
                )

            elif performance == "Average":
                st.warning(
                    "📖 Average performance. More practice can help."
                )

            else:
                st.error(
                    "💪 More improvement is needed. "
                    "Focus on regular study and assignments."
                )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            try:
                error = response.json()
                st.write(error)

            except:
                st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to Flask API."
        )

        st.info(
            "Please make sure Flask is running at "
            "http://127.0.0.1:5000"
        )

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ The API request timed out."
        )

    except Exception as e:

        st.error(
            f"Unexpected error: {e}"
        )

st.divider()

st.caption(
    "Task 8 – Streamlit Frontend Integrated with Flask API"
)