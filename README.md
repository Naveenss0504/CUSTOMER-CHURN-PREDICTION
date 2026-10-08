# Telecom Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn based on their demographic details, services, contract information, and billing details.

## Project Overview

Customer churn is an important problem for telecom companies. Predicting customers who are likely to leave can help companies take preventive actions and improve customer retention.

This project uses Machine Learning classification algorithms to predict customer churn using the IBM Telco Customer Churn dataset.

## Dataset

The project uses the **IBM Telco Customer Churn Dataset**, containing information about approximately 7,000 telecom customers.

### Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

### Target

- `0` → Customer will likely stay
- `1` → Customer will likely churn

## Machine Learning Models

The following classification algorithms were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

The best-performing model was saved as `churn_model.pkl`.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## Project Structure

```text
telecom-customer-churn/
│
├── app.py
├── churn_model.pkl
├── telecom_customer_churn_ml.ipynb
└── README.md
