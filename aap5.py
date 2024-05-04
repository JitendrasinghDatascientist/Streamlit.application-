import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load data
try:
    df = pd.read_csv(r"C:\Users\jiten\Downloads\Customer_new_data.csv")
except FileNotFoundError:
    st.error("File not found. Please check the file path.")
    st.stop()

# Check for missing values
missing_values = df.isnull().sum()
if missing_values.any():
    st.warning("The dataset contains missing values. Columns with missing values:")
    st.write(missing_values[missing_values > 0])
    st.stop()

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df.drop('CUSTID', axis=1)), columns=df.columns[1:])

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_imputed)  # Standardize features

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Initialize KMeans object
kmeans.fit(X_scaled)  # Fit the model

# Display results
st.title("Customer Segmentation Model")
st.write("Number of clusters:", kmeans.n_clusters)
st.write("Cluster centers:")
st.write(kmeans.cluster_centers_)
st.write("Cluster labels:")
st.write(kmeans.labels_)

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=kmeans.labels_, ax=ax)
ax.set_xlabel("BALANCE")
ax.set_ylabel("PURCHASES")
ax.set_title("Customer Segmentation")
st.pyplot(fig)

# Download results
if st.button("Download results"):
    csv = pd.DataFrame({'CUSTID': df['CUSTID'], 'cluster': kmeans.labels_})
    st.download_button("Download CSV", csv.to_csv(index=False), "customer_segments.csv")




