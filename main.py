import pandas as pd 
import numpy as np
import pickle 
import streamlit as st 

pickle_in = open('Automating_Loan_Prediction_System.pkl', 'rb')
model = pickle.load(pickle_in)

def prediction(Education, ApplicantIncome, CoapplicantIncome,LoanAmount,  Credit_History):
    if Education == "Non Graduate":
        Education = 0
    else:
        Education = 1

    if Credit_History == "Bad":
        Credit_History = 0
    else:
        Credit_History = 1
    
    ApplicantIncome = ApplicantIncome
    CoapplicantIncome = CoapplicantIncome
    LoanAmount = LoanAmount
    

    prediction = model.predict([[Education, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History]])
    if prediction == 0:
        pred = 'Rejected'

    else:
        pred = "Accepted"

    return pred

def main():

    html_temp = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Magic - Your Loan Eligibility Wizard</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #2196F3;
            padding: 20px;
            text-align: center;
            color: white;
        }
        .title {
            font-size: 36px;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 24px;
            margin-top: 0;
        }
        .content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">Loan Magic</div>
        <div class="subtitle">Your Loan Eligibility Wizard</div>
    </div>

</body>
</html>

        """
    
    st.markdown(html_temp, unsafe_allow_html= True)

    Education = st.selectbox('Education', ('Graduated', 'Non Graduate'))
    ApplicantIncome = st.number_input("Applicant Monthly Income")
    CoapplicantIncome = st.number_input("Coapplicant Montly Income")
    
    LoanAmount = st.number_input("Loan Amount")
    Credit_History = st.selectbox('Credit_History', ('Good', 'Bad'))
    result = " "

    if st.button("Predict"):
        result = prediction(Education,ApplicantIncome,CoapplicantIncome,LoanAmount,Credit_History)
        st.success("Your Loan Application is {}".format(result))

if __name__ == '__main__':
    main()

