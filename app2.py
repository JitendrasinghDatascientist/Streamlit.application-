import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = {
    'Patient':[1,8,16,24,32,40],
    'Age':[38,40,50,60,70,80],
    'Gender':["Male","Female","Male","Female","Male","Female"],
    'Hemoglobin':[12,11,9,6,4,7]
}

res = pd.DataFrame(data)
Gender_mapping = {"Male":1,"Female":0}
res['Gender'] = res['Gender'].map(Gender_mapping)

X = res[['Patient','Gender','Hemoglobin']]
Y = res['Age']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

prediction = model.predict(X_test)
mse = mean_squared_error(Y_test,prediction)

st.title("Patient Age prediction")

Patient = st.slider('patient',min_value=0,max_value=100,value=40)
Hemoglobin = st.slider('Hemoglobin',min_value=0,max_value=15,value=5)
Gender = st.selectbox('Gender',options=['Male','Female'])

Gender_num = Gender_mapping[Gender]

if st.button("Predict"):
    prediction_age = model.predict([[Patient, Gender_num, Hemoglobin]])[0]
    st.write(f"The predicted age is: {prediction_age}")

