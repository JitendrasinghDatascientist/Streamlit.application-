import streamlit as st
import pandas as pd

df = pd.read_csv('datasets/used_phones_dataset.csv')

st.write(df)