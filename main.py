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

    html_temp =  """ 
        <div style ="background-color:green;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Automatic Loan Eligibility Prediction System</h1> 
        </div> 
        
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

