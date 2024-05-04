import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load data
data = {
    "Car_Name": ["Mahindra", "Tata", "Hundai", "Toyota", "MarutiSuzuki"],
    "Car_Speed": [70, 100, 150, 200, 250],
    "Car_Engine_horse": [2000, 3000, 4000, 5000, 6000],
    "Car_air_bag": [4, 5, 6, 7, 8],
    "Color": ["Red", "Orange", "White", "Black", "Blue"]
}
df = pd.DataFrame(data)

# Map colors to numerical values
ColorM = {"Red": 1, "Black": 2, "White": 3, "Blue": 4, "Orange": 5}
df["Color_Num"] = df["Color"].map(ColorM)

# Encode the target variable
label_encoder = LabelEncoder()
df['Car_Label'] = label_encoder.fit_transform(df['Car_Name'])

# Prepare features and target
X = df[["Car_Speed", "Car_Engine_horse", "Car_air_bag", "Color_Num"]]
y = df["Car_Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Model evaluation
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

st.title("Car Company Prediction")

Car_speed = st.number_input("Car_Speed", min_value=50, max_value=300, value=50)
Car_Engine_horse = st.number_input("Car_Engine_horse", min_value=1000, max_value=7000, value=1500)
Car_air_bag = st.number_input("Car_air_bag", min_value=0, max_value=15, value=0)
Color = st.selectbox("Color", options=["Red", "Black", "White", "Blue", "Orange"])
Color_Num = ColorM[Color]

if st.button("Predict Car Company"):
    # Make prediction
    input_features = [[Car_speed, Car_Engine_horse, Car_air_bag, Color_Num]]
    prediction = label_encoder.inverse_transform(model.predict(input_features))
    st.write("Predicted Car Company:", prediction[0])







