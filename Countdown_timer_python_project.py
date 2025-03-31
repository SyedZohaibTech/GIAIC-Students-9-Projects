import streamlit as st
import time

# Function to update the time left in the countdown
# Takes the total time and updates every second

def countdown(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        time_left = f"{hours:02}:{minutes:02}:{seconds:02}"
        st.session_state.time_remaining = time_left
        total_seconds -= 1
        time.sleep(1)
        if st.session_state.stop_timer:
            break

# Function to start the countdown
def start_timer(seconds):
    st.session_state.stop_timer = False
    countdown(seconds)

# Main function to handle the UI and user input
def countdown_timer():
    st.title("Countdown Timer")

    # Timer setup
    if 'stop_timer' not in st.session_state:
        st.session_state.stop_timer = False
    if 'time_remaining' not in st.session_state:
        st.session_state.time_remaining = "00:00:00"

    st.write(f"**Time remaining:** {st.session_state.time_remaining}")

    # User input for the countdown time
    hours = st.number_input("Hours", min_value=0, max_value=23, value=0)
    minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)

    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Button to start the countdown
    if st.button("Start Countdown"):
        if total_seconds > 0:
            start_timer(total_seconds)
        else:
            st.warning("Please set a valid countdown time.")

    # Button to stop/pause the countdown
    if st.button("Stop Timer"):
        st.session_state.stop_timer = True

    # Button to reset the countdown
    if st.button("Reset Timer"):
        st.session_state.time_remaining = "00:00:00"
        st.session_state.stop_timer = True

if __name__ == "__main__":
    countdown_timer()