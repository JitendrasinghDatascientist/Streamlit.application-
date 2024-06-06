import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Creating an extended dataset
data = pd.DataFrame({
    'Experience': [1, 3, 5, 7, 10, 12],
    'EducationLevel': ['Bachelor', 'Bachelor', 'Master', 'Master', 'PhD', 'PhD'],
    'Industry': ['Tech', 'Finance', 'Healthcare', 'Tech', 'Tech', 'Finance'],
    'Location': ['Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Urban'],
    'SkillLevel': ['Junior', 'Junior', 'Mid', 'Mid', 'Senior', 'Senior'],
    'CompanySize': ['Small', 'Medium', 'Large', 'Small', 'Large', 'Medium'],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000]
})

# Convert non-numeric values to numeric
education_mapping = {'Bachelor': 1, 'Master': 2, 'PhD': 3}
industry_mapping = {'Tech': 1, 'Finance': 2, 'Healthcare': 3}
location_mapping = {'Urban': 1, 'Rural': 2}
skill_level_mapping = {'Junior': 1, 'Mid': 2, 'Senior': 3}
company_size_mapping = {'Small': 1, 'Medium': 2, 'Large': 3}

data['EducationLevel'] = data['EducationLevel'].map(education_mapping)
data['Industry'] = data['Industry'].map(industry_mapping)
data['Location'] = data['Location'].map(location_mapping)
data['SkillLevel'] = data['SkillLevel'].map(skill_level_mapping)
data['CompanySize'] = data['CompanySize'].map(company_size_mapping)

# Splitting the data
X = data[['Experience', 'EducationLevel', 'Industry', 'Location', 'SkillLevel', 'CompanySize']]
y = data['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title('Salary Prediction')

# User input
experience = st.slider('Experience (Years)', min_value=0, max_value=20, value=5)
education_level = st.selectbox('Education Level', ['Bachelor', 'Master', 'PhD'])
industry = st.selectbox('Industry', ['Tech', 'Finance', 'Healthcare'])
location = st.selectbox('Location', ['Urban', 'Rural'])
skill_level = st.selectbox('Skill Level', ['Junior', 'Mid', 'Senior'])
company_size = st.selectbox('Company Size', ['Small', 'Medium', 'Large'])

education_num = education_mapping[education_level]
industry_num = industry_mapping[industry]
location_num = location_mapping[location]
skill_level_num = skill_level_mapping[skill_level]
company_size_num = company_size_mapping[company_size]

# Prediction
if st.button('Predict'):
    predicted_salary = model.predict([[experience, education_num, industry_num, location_num, skill_level_num, company_size_num]])[0]
    st.write(f"The predicted salary is Rs.{predicted_salary:.2f}")



