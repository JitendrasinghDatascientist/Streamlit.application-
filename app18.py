import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


upload_file = st.file_uploader("Choose CSV file",type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    salary_data =df.groupby('Name')['Salary'].sum()
    fig,ax=plt.subplots()
    ax.pie(salary_data,labels=salary_data.index,autopct='%1.1f%%')
    st.pyplot(fig)