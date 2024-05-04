import streamlit as st
import random

secret_number = random.randint(1, 100)

st.title("Guessing Game")


guess = st.text_input("Enter your guess:", value="")


if st.button("Submit"):
   
    user_guess = int(guess)
    
    
    if user_guess == secret_number:
        st.write(" Congratulations! You guessed the correct number!")
    elif user_guess < secret_number:
        st.write("Too low! Try again.")
    else:
        st.write("Too high! Try again.")