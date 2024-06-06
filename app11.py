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

# Streamlit app
def main():
    st.title("DhirajGPT")
    st.write("Type a message and the DhirajAI will respond!")

    # User input
    user_input = st.text_input("You:", "")

    # Chatbot response
    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.text("Dhiraj AI: " + response)

if __name__ == "__main__":
    main()
