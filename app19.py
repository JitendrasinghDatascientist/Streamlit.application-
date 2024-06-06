import streamlit as st

# Define a function to simulate responses from the chatbot
def chatbot_response(input_text):
    input_text = input_text.lower()
    if "hello" in input_text:
        return "Hello! How can I help you today?"
    elif "how are you" in input_text:
        return "I'm just a chatbot, but thanks for asking!"
    elif "what is python" in input_text:
        return "Python is a computer language that's easy to learn, and it lets you tell the computer what to do by writing instructions in a way that's a bit like talking to it in a secret code."
    elif "bye" in input_text:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand that question."

# Define a function to process uploaded files (dummy function)
def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_type = uploaded_file.type.split('/')[1]
        if file_type == 'pdf':
            st.write("You uploaded a PDF file.")
        elif file_type in ('jpeg', 'jpg', 'png'):
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        else:
            st.warning("Unsupported file format. Please upload an image (jpeg, jpg, png) or a PDF.")

# Set colorful theme
st.set_page_config(
    page_title="DhirajGPT App",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS styles for colorful UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f7f7f7;
    }
    .st-eb {
        background-color: #e6f7ff;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        box-shadow: 2px 2px 5px #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1 style='text-align: center; color: #009688;'>DhirajGPT App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #333;'>Chat with DhirajAI and Upload Files</h3>", unsafe_allow_html=True)

# User input for chat
user_input = st.text_input("You (Chat):", "")

# Send button for chat
if st.button("Send (Chat)", key='send_button', help="Click to send your chat message"):
    if user_input:
        response = chatbot_response(user_input)
        st.text("Dhiraj AI: " + response)

# Upload file section
st.write("Upload an image (jpeg, jpg, png) or a PDF file:")
uploaded_file = st.file_uploader("Choose a file...", type=["jpg", "jpeg", "png", "pdf"])

# Process uploaded file
if uploaded_file is not None:
    process_uploaded_file(uploaded_file)
