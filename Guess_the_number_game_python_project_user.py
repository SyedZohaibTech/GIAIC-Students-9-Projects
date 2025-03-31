import streamlit as st

def start_game():
    st.title("Guess the Number - Computer Guesses")
    
    # Initialize game variables only once
    if 'lower_bound' not in st.session_state:
        st.session_state.lower_bound = 1
        st.session_state.upper_bound = 100
        st.session_state.computer_guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
        st.session_state.attempts = 1
    
    st.write(f"I guess your number is: {st.session_state.computer_guess}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Too Low"):
            if st.session_state.lower_bound <= st.session_state.computer_guess:
                st.session_state.lower_bound = st.session_state.computer_guess + 1
                st.session_state.computer_guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
                st.session_state.attempts += 1
                st.rerun()
    with col2:
        if st.button("Correct!"):
            st.success(f"Awesome! I guessed your number in {st.session_state.attempts} tries!")
            del st.session_state.lower_bound
            del st.session_state.upper_bound
            del st.session_state.computer_guess
            del st.session_state.attempts
            st.button("Play Again", on_click=start_game)
    with col3:
        if st.button("Too High"):
            if st.session_state.upper_bound >= st.session_state.computer_guess:
                st.session_state.upper_bound = st.session_state.computer_guess - 1
                st.session_state.computer_guess = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
                st.session_state.attempts += 1
                st.rerun()
    
if __name__ == "__main__":
    start_game()
