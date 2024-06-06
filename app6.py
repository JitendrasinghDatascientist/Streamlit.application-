# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create a hardcoded dataset (you can replace this with your own data)
data = {
    'Car Model': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan'],
    'Year': [2019, 2018, 2020, 2017, 2019],
    'Mileage (in miles)': [30000, 25000, 35000, 40000, 28000],
    'Price (in dollars)': [20000, 22000, 18000, 15000, 23000]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Create the Streamlit web app
st.title('Car Price Prediction App')

# Display the dataset
st.subheader('Dataset')
st.write(df)

# Create input fields for user to input car details
st.sidebar.header('Enter Car Details')

car_model = st.sidebar.selectbox('Select Car Model', df['Car Model'])
year = st.sidebar.number_input('Enter Year', min_value=1980, max_value=2025)
mileage = st.sidebar.number_input('Enter Mileage (in miles)', min_value=0)
prediction_button = st.sidebar.button('Predict Price')

# Split the dataset into features (X) and target (y)
X = df[['Year', 'Mileage (in miles)']]
y = df['Price (in dollars)']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Function to predict car price
def predict_price(year, mileage):
    return model.predict([[year, mileage]])[0]

# Make a prediction if the prediction button is clicked
if prediction_button:
    prediction = predict_price(year, mileage)
    st.sidebar.text(f'Predicted Price: ${prediction:.2f}')
