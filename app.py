import streamlit as st
import pickle
import pandas as pandas
import numpy as np
Gender  = {
"Female" : 0,"Male" : 1,}
Married  = {
"No" : 0,"Yes" : 1,}

Dependents  = {
"0" : 0,"1" : 1,"2" : 2,"3+" : 3,}

Education  = {
"Graduate" : 0,"Not Graduate" : 1,}

Self_Employed  = {
"No" : 0,"Yes" : 1,}

Credit_History  = {
"0.0" : 0,"1.0" : 1,}

Property_Area  = {
"Rural" : 0,"Semiurban" : 1,"Urban" : 2,}

Loan_Status  = {
"N" : 0,"Y" : 1,}
model=pickle.load(open('lin_model.pkl','rb'))
if(__name__=="__main__"):
    st.header('Loan Status Prediction')
    col1,col2=st.columns([2,1])
    apin=int(col1.number_input(label='Enter applicant income'))
    gender=col1.selectbox('Select your gender',list(Gender.keys()))
    coin=int(col1.number_input(label='Enter Coapplicant income'))
    loan_amount=int(col1.number_input(label='Enter Loan Amount'))
    term = int(col1.number_input("Enter the Duration:"))
    credit_history=col1.selectbox('Select your credit history',list(Credit_History.keys()))
    prar=col1.selectbox('Select your propert area',list(Property_Area.keys()))
    mar=col1.selectbox('Select your maratial status',list(Married.keys()))
    dependents=col1.selectbox('Enter no of dependents',list(Dependents.keys()))
    education=col1.selectbox('Enter your education',list(Education.keys()))
    self_employed=col1.selectbox('Are you self employed',list(Self_Employed.keys()))
    submit_button=st.button(label="Submit")
    if submit_button:
        user_input = np.array([[apin,coin,loan_amount,term,Gender[gender],Married[mar],Dependents[dependents],Education[education],Self_Employed[self_employed],Credit_History[credit_history],Property_Area[prar]]])
        prediction = model.predict(user_input)[0]
        if prediction == 1:
            st.write("Loan will be Approved")
        else:
            st.write("Loan is Rejected")
    
    