import streamlit as st
import random

def generate_story(noun, verb, adjective, place):
    templates = [
        f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was a sight to behold!",
        f"At the {place}, a {adjective} {noun} was trying to {verb}. Everyone was amazed!",
        f"Have you ever seen a {adjective} {noun} {verb} at the {place}? It's truly a rare event!"
    ]
    return random.choice(templates)

# Streamlit UI
st.title("Mad Libs Game")

st.write("Fill in the blanks below and create your own fun story!")

noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")

if st.button("Generate Story"):
    if noun and verb and adjective and place:
        story = generate_story(noun, verb, adjective, place)
        st.success(story)
    else:
        st.warning("Please fill all the fields before generating the story.")
