import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    'Experience': [1, 3, 5, 7, 10, 12],
    'EducationLevel': ['Bachelor', 'Bachelor', 'Master', 'Master', 'PhD', 'PhD'],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000]
}
res = pd.DataFrame(data)
Education_mapping = {'Bachelor': 1, 'Master': 2, 'PhD': 3}
res['EducationLevel'] = res['EducationLevel'].map(Education_mapping)
X = res[['EducationLevel', 'Experience']]
Y = res['Salary']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, Y_train)
prediction = model.predict(X_test)
mse = mean_squared_error(Y_test, prediction)

st.title("Salary Prediction app by Jitendra")

Experience = st.slider('Experience', min_value=0, max_value=20, value=5)
Education_level = st.selectbox('Education Level', options=['Bachelor', 'Master', 'PhD'])
Education_num = Education_mapping[Education_level]

if st.button("Predict"):
    prediction_salary = model.predict([[Education_num, Experience]])[0]
    st.write(f"The predicted salary is: RS{prediction_salary:.2f}")

