import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = {
    "PIN CODE": [210507,160047,110059,120089,178900],
    "LATITUDE": [23,34,54,65,76],
    "LONGITUDE": [23,40,50,70,100],
    "LOCATION": [23,40,50,70,100],
    "NO OF CAR_CRASH":[100,400,600,800,900]
}
df = pd.DataFrame(data)
features = df[['PIN CODE','LATITUDE','LONGITUDE','LOCATION']]
target = df[ "NO OF CAR_CRASH"]

X_train,X_test,y_train,y_test = train_test_split(features,target,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

prediction = model.predict(X_test)
mse = mean_squared_error(y_test,prediction)

st.title("NO_OF_Car_crash_prediction")

zip_code =st.slider('PIN CODE',min_value=110001, max_value=191001,value=130001)
Lati = st.slider('LATITUDE',min_value=0, max_value =  90 , value=5)
Long = st.slider('LONGITUDE',min_value=0, max_value = 180 , value= 20 )
LOC = st.slider('LOCATION', min_value = 0 , max_value=100, value= 23)

if st.button("Prediction"):
    prediction_time = model.predict([[zip_code,Lati,Long,LOC]])[0]
    st.write(f"NO of_Car_Crash_prediction: {prediction_time}")