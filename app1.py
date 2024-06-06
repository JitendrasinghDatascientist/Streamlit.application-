## Salary Prediction App

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Creating a hardcoded dataset
data = pd.DataFrame({
    'Experience': [1, 3, 5, 7, 10, 12],
    'EducationLevel': ['Bachelor', 'Bachelor', 'Master', 'Master', 'PhD', 'PhD'],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000]
})

# Convert 'EducationLevel' to numeric values
education_mapping = {'Bachelor': 1, 'Master': 2, 'PhD': 3}
data['EducationLevel'] = data['EducationLevel'].map(education_mapping)

# Splitting the data
X = data[['Experience', 'EducationLevel']]
y = data['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title('Salary Prediction By Gargi')

# User input
experience = st.slider('Experience (Years)', min_value=0, max_value=30, value=5)
education_levels = ['Bachelor', 'Master', 'PhD']
education_level = st.selectbox('Education Level', education_levels)
education_num = education_mapping[education_level]

# Prediction
if st.button('Predict'):
    predicted_salary = model.predict([[experience, education_num]])[0]
    st.write(f"The predicted salary is ${predicted_salary:.2f}")



