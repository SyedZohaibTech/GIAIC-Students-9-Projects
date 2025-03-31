import streamlit as st
import random

# Function to randomly select a word from the word list
def choose_random_word():
    word_list = ["python", "streamlit", "developer", "machine", "algorithm"]
    return random.choice(word_list)

# Function to display the current state of the word
# For unguessed letters, we'll show underscores
def display_word_progress(word, guessed_letters):
    word_progress = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(word_progress)

# Main game function
def hangman_game():
    st.title("Welcome to Hangman Game!")

    # Initialize game session state if not already initialized
    if 'secret_word' not in st.session_state:
        st.session_state.secret_word = choose_random_word()
        st.session_state.guessed_letters = set()
        st.session_state.incorrect_guesses = 0
        st.session_state.max_incorrect = 6

    # Show the current progress of the word
    current_progress = display_word_progress(st.session_state.secret_word, st.session_state.guessed_letters)
    st.write(f"Current word: {current_progress}")

    # User input for a guessed letter
    user_guess = st.text_input("Guess a letter (one at a time):", max_chars=1).lower()

    if st.button("Submit Guess") and user_guess:
        # Check if the guessed letter is in the word
        if user_guess in st.session_state.secret_word:
            st.session_state.guessed_letters.add(user_guess)
        else:
            st.session_state.incorrect_guesses += 1

        # Check for win or loss conditions
        if set(st.session_state.secret_word).issubset(st.session_state.guessed_letters):
            st.success(f"Congratulations! You guessed the word: {st.session_state.secret_word}")
            st.session_state.secret_word = choose_random_word()  # New word for next round
            st.session_state.guessed_letters = set()
            st.session_state.incorrect_guesses = 0
        elif st.session_state.incorrect_guesses >= st.session_state.max_incorrect:
            st.error(f"Game Over! The correct word was: {st.session_state.secret_word}")
            st.session_state.secret_word = choose_random_word()  # New word for next round
            st.session_state.guessed_letters = set()
            st.session_state.incorrect_guesses = 0

    # Display the number of incorrect guesses remaining
    remaining_incorrect_guesses = st.session_state.max_incorrect - st.session_state.incorrect_guesses
    st.write(f"Incorrect guesses remaining: {remaining_incorrect_guesses}")

if __name__ == "__main__":
    hangman_game()
