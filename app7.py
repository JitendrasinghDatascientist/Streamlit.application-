## Election Prediction App

# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dummy election data
data = {
    'Candidate': ['BJP', 'Congress', 'TMC', 'Candidate D'],
    'Votes': [4500, 3200, 2000, 1800]
}

# Create a DataFrame from the dummy data
df = pd.DataFrame(data)

# Create the Streamlit web app
st.title('Indian State Election Results')

# Display the election results as a table
st.subheader('Election Results')
st.write(df)

# Create a bar chart to visualize the election results
st.subheader('Election Results Visualization')
plt.figure(figsize=(8, 6))
sns.barplot(x='Votes', y='Candidate', data=df, palette='viridis')
plt.xlabel('Votes')
plt.ylabel('Candidate')
plt.title('Election Results')
st.pyplot(plt)

# Display the winner
winner = df.loc[df['Votes'].idxmax(), 'Candidate']
st.subheader('Winner')
st.write(f'The winner of the election is {winner}.')


