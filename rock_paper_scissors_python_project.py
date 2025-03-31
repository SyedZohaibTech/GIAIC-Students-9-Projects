import streamlit as st
import random

def get_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"

def main():
    st.title("Rock, Paper, Scissors Game")
    st.write("Choose your move below:")
    
    # Choices available
    choices = ["Rock", "Paper", "Scissors"]
    
    # User selection
    user_choice = st.radio("Your choice:", choices)
    
    if st.button("Play"):  # Only process when button is clicked
        computer_choice = random.choice(choices)
        st.write(f"Computer chose: **{computer_choice}**")
        
        result = get_winner(user_choice, computer_choice)
        st.success(result)
        
        # Extra message for fun
        if result == "You win! 🎉":
            st.balloons()
    
if __name__ == "__main__":
    main()