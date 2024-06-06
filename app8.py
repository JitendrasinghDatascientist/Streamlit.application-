# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dummy election data with state name and party names
data = {
    'State': ['MP', 'Rajasthan', 'Karnataka', 'State B', 'State C', 'State C'],
    'Candidate': ['BJP', 'BJP', 'Congress', 'Candidate D', 'Candidate E', 'Candidate F'],
    'Party': ['Party 1', 'Party 2', 'Party 1', 'Party 2', 'Party 1', 'Party 2'],
    'Votes': [4500, 3200, 2800, 1800, 4000, 3000]
}

# Create a DataFrame from the dummy data
df = pd.DataFrame(data)

# Create the Streamlit web app
st.title('Indian State Election Results')

# Display the election results as a table
st.subheader('Election Results')
st.write(df)

# Create a bar chart to visualize the election results by state
st.subheader('Election Results Visualization by State')
plt.figure(figsize=(10, 6))
sns.barplot(x='Votes', y='State', hue='Candidate', data=df, palette='viridis')
plt.xlabel('Votes')
plt.ylabel('State')
plt.title('Election Results by State')
st.pyplot(plt)

# Display the winners by state
st.subheader('Winners by State')
winners = df.loc[df.groupby('State')['Votes'].idxmax()].reset_index(drop=True)
st.write(winners)

