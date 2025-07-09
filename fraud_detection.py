import streamlit as st
import pandas as pd
import joblib 
model = joblib.load("onlinefrauddetection.pkl")
st.title("online fraud detection app")
st.markdown("please enter the transaction detailes and use the button")
st.driver()
transaction_type = st.selectbox("Transaction Type",["Payment","Transfer","Cash_Out","Deposite"])
amount = st.number_input("Amount", min_value = 0.0,value = 1000.0)
oldbalanceOrg = st.number_input("old Balance(Sender)",min_value = 0.0,value = 9000.0)
newbalanceOrig = st.number_input("New Balance (Sender)",min_value = 0.0, value = 9000.0)
oldbalancedest = st.number_input("old balance(Receiver)",min_value = 0.0, value =0.0)
newbalancedest = st.number_input("New Balance (Receiver)",min_value = 0.0,value=0.0)

if st.button("predict"):
    
  input_data = pd.DataFrame([{
      "type":transaction_type,
      "amount":amount,
      "oldbalanceOrg":oldbalanceOrg,
      "newbalanceOrig":newbalanceOrig,
      "oldbalanceDest":oldbalanceDest,
      "newbalanceDest":newbalanceDest
  }])

  prediction = model.predict(input_data)[0]
  st.subheader(f"prediction:'{int(prediction)}' ")
  
  if prediction == 1:
       st.error("This transaction is fraud")
  else:
       st.success("This transaction looks like is not a fraud")
       