import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_chars = lower + upper + digits + special
    if not all_chars:
        return "Please select at least one character set!"
    
    password = ''.join(random.sample(all_chars, length))
    return password

st.title("🔑 Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=24, value=12)
digits = st.checkbox("Include Numbers (0-9)")
special_chars = st.checkbox("Include Special Characters (!@#$%^&*)")

if st.button("Generate Password"):
    password = generate_password(length, digits, special_chars)
    st.text_area("Your Generated Password:", password, height=70)

