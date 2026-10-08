import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("churn_model.pkl")


st.set_page_config(
    page_title="Telecom Customer Churn",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telecom Customer Churn Prediction")
st.write("Predict whether a telecom customer is likely to churn.")

st.divider()


# Sample customers
samples = {
    "Sample 1": {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 2,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 90.0,
        "TotalCharges": 180.0
    },

    "Sample 2": {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 24,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "One year",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Mailed check",
        "MonthlyCharges": 75.0,
        "TotalCharges": 1800.0
    },

    "Sample 3": {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 60,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Two year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Bank transfer (automatic)",
        "MonthlyCharges": 55.0,
        "TotalCharges": 3300.0
    }
}


st.subheader("Choose Prediction Mode")

mode = st.radio(
    "Select an option",
    ["Sample Customer", "Manual Entry"],
    horizontal=True
)


# Sample customer
if mode == "Sample Customer":

    selected_sample = st.selectbox(
        "Select a sample",
        list(samples.keys())
    )

    customer = samples[selected_sample]

    st.divider()
    st.subheader("Customer Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Personal Information**")
        st.write(f"Gender: {customer['gender']}")
        st.write(f"Senior Citizen: {customer['SeniorCitizen']}")
        st.write(f"Partner: {customer['Partner']}")
        st.write(f"Dependents: {customer['Dependents']}")
        st.write(f"Tenure: {customer['tenure']} months")

    with col2:
        st.write("**Services**")
        st.write(f"Phone Service: {customer['PhoneService']}")
        st.write(f"Multiple Lines: {customer['MultipleLines']}")
        st.write(f"Internet Service: {customer['InternetService']}")
        st.write(f"Online Security: {customer['OnlineSecurity']}")
        st.write(f"Online Backup: {customer['OnlineBackup']}")
        st.write(f"Device Protection: {customer['DeviceProtection']}")
        st.write(f"Tech Support: {customer['TechSupport']}")

    with col3:
        st.write("**Billing Information**")
        st.write(f"Contract: {customer['Contract']}")
        st.write(f"Paperless Billing: {customer['PaperlessBilling']}")
        st.write(f"Payment Method: {customer['PaymentMethod']}")
        st.write(f"Monthly Charges: ${customer['MonthlyCharges']}")
        st.write(f"Total Charges: ${customer['TotalCharges']}")


# Manual entry
else:

    st.subheader("Enter Customer Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=12
        )

    with col2:

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        online_security = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"]
        )

    with col3:

        tech_support = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"]
        )

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.subheader("Billing Information")

    col4, col5 = st.columns(2)

    with col4:
        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0
        )

    with col5:
        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=840.0
        )

    customer = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }


# Prediction
st.divider()

if st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True
):

    customer_df = pd.DataFrame([customer])

    # Get prediction and probability
    prediction = model.predict(customer_df)[0]
    probability = model.predict_proba(customer_df)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error("Prediction: Likely to Churn")
        else:
            st.success("Prediction: Likely to Stay")

    with col2:

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    st.progress(float(probability))