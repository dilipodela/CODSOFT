import streamlit as st
import pickle 
import numpy as np
   
data=pickle.load(open("C:/Users/Delip/customer_chun/Diabetes.sav", "rb"))
# def load_model():
#     with open("C:/Users/Delip/2111CS010124/Diabetes.pkl", "rb") as file:
#         data = pickle.load(file)
#     return data

# data=load_model()

st.title(""" CUSTOMER CHURN PREDICTION""")
st.header("Age")
a=st.number_input("Enter the Age",20,100)
st.header("Active Member")
b=st.number_input("ENTER 1 if you are active member",0,1)
st.header("Balance")
c=st.number_input("ENTER THE Balance", value=0.0, format="%.2f")
st.header("Number of Products")
d=st.number_input("ENTER THE Number of Products",0,3)
st.header("Credit Score")
e=st.number_input("Enter your credit score ",0,1000)
st.header("Tenure")
f=st.number_input("Enter your Tenure score ",0,10)

s=st.button("PREDICT RATING")
if(s):
    Age=a
    IsActiveMember=b
    Balance=c
    NumOfProducts=d
    CreditScore=e
    Tenure=f
    y_p=data.predict([[Age,IsActiveMember,Balance,NumOfProducts,CreditScore,Tenure]])
    print(f"chances of getting the customer will exit the company:", y_p)
    

    




