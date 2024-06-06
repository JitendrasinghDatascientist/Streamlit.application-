import streamlit as st
import pandas as pd

data = {
    'Column 1' : [1,2,3,4,5],
    'Column 2' : ['A','B','C','D','E']
}

df = pd.DataFrame(data)

st.write(df)