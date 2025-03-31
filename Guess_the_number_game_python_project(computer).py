import streamlit as st
import random

st.title("Guess the Number Game")

# Generate a random number between 1 and 100
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0

st.write("I've picked a number between 1 and 100. Try to guess it!")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Check Guess"):
    st.session_state.tries += 1
    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"Congratulations! You guessed the number in {st.session_state.tries} tries.")
        st.session_state.number = random.randint(1, 100)  # Reset the number for a new game
        st.session_state.tries = 0