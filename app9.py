import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create a simple dataset with days, COVID-19 cases, and population (dummy data)
data = {
    'Country': ['Country A'] * 20,
    'Days': list(range(1, 21)),
    'Cases': [100, 150, 300, 500, 800, 1300, 2100, 3400, 5500, 8900, 14400, 23300, 37700, 61000, 98700, 159700, 258400, 418100, 676500, 1095200],
    'Population': [1000000] * 20  # Population for Country A (dummy data)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the Streamlit web app
st.title('COVID-19 Prediction App')

# Display the dataset
st.subheader('COVID-19 Dataset (Dummy Data)')
st.write(df)

# Create input fields for user to input country and days
st.sidebar.header('Predict COVID-19 Cases')

country = st.sidebar.text_input('Enter Country Name:', 'Country A')
days = st.sidebar.number_input('Enter Days Since First Case:', min_value=1)

# Filter data based on the selected country
filtered_df = df[df['Country'] == country]

# Train a simple linear regression model
X = filtered_df['Days'].values.reshape(-1, 1)
y = filtered_df['Cases']
model = LinearRegression()
model.fit(X, y)

# Make a prediction
predicted_cases = model.predict(np.array([[days]]))[0]

# Calculate cases per 100,000 population
population = filtered_df['Population'].values[0]
cases_per_100k = (predicted_cases / population) * 100000

# Display the prediction
st.sidebar.text(f'Predicted COVID-19 Cases: {int(predicted_cases):,}')
st.sidebar.text(f'Cases per 100,000 Population: {cases_per_100k:.2f}')

# Plot the data and regression line
plt.figure(figsize=(8, 6))
plt.scatter(X, y, label='Actual Cases', color='blue')
plt.plot(X, model.predict(X), label='Regression Line', color='red')
plt.xlabel('Days Since First Case')
plt.ylabel('COVID-19 Cases')
plt.title(f'COVID-19 Cases Prediction for {country}')
plt.legend()
st.pyplot(plt)
