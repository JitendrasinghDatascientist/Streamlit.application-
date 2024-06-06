import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Streamlit Components")

# Text
st.header("Text and Input Components")

# Text input
user_input = st.text_input("Enter something:", "Type here...")
st.write(f"You entered: {user_input}")

# Date input
selected_date = st.date_input("Select a date:")
st.write(f"Selected date: {selected_date}")

# File upload
st.header("File Upload")
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.write(df)

# Button
if st.button("Click me"):
    st.write("You clicked the button!")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.text("This is a sidebar.")

# Plotting
st.header("Plotting")
st.write("Let's create a simple plot.")

# Generate some data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sine Wave")
st.pyplot(fig)

# Display HTML
st.header("Display HTML")
st.markdown("You can also display HTML in Streamlit:")
st.markdown("<b>This is bold HTML text.</b>", unsafe_allow_html=True)

# Columns
st.header("Columns Layout")
col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

# Expander
st.header("Expander")
with st.expander("Click to expand"):
    st.write("This content is hidden by default and can be expanded.")

# Code
st.header("Code Block")
st.code("""
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
""", language="python")

# Progress Bar
st.header("Progress Bar")
import time
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.02)  # Simulate some work being done
    progress_bar.progress(i)

# Display audio
# st.header("Audio")
# audio_file = open("sample_audio.mp3", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

# Display video
# st.header("Video")
# video_file = open("sample_video.mp4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes, format="video/mp4")

# Download link
st.header("Download Link")
download_link = st.button("Download Data")
if download_link:
    st.markdown("[Download Data](https://example.com/data.csv)")

# Display a map
# st.header("Map")
# st.map([{"location": (37.7749, -122.4194), "tooltip": "San Francisco"}])

# Placeholder
st.header("Placeholder")
st.empty()

# End of the app
st.header("That's it!")
st.write("You've reached the end of the Streamlit app!")

