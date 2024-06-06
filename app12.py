import streamlit as st

# Define a function to handle user input and provide responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    elif "price of redmi phone" in user_input:
        return "The price of the Redmi phone is Rs.9999."
    else:
        return "I'm sorry, I don't have information on that topic."

# Streamlit app
def main():
    st.title("Simple Chatbot")
    st.write("Type a message, and the chatbot will respond!")

    # User input
    user_input = st.text_input("You:", "")

    # Chatbot response
    if st.button("Send"):
        if user_input:
            response = chatbot_response(user_input)
            st.text("Chatbot: " + response)

if __name__ == "__main__":
    main()
