import streamlit as st

# Website title
st.title("Welcome to Our Personal Space")

# Short introduction
st.markdown("""
Hello there! We're so glad you're here. 

This is a simple website created using Python and Streamlit. It's designed to give you a quick, interactive experience where you can explore what we have to offer and get in touch with us. 
""")

# User-friendly input for name
st.markdown("**What should we call you?**")
user_name = st.text_input("Your Name")

if user_name:
    st.write(f"Hey {user_name}, it's great to meet you! 😊")

# Some interactive features
st.markdown("**What would you like to do next?**")
if st.button("Learn more about us"):
    st.write("""
    We're passionate about building creative and functional web apps using Python. 
    Our goal is to make technology accessible and fun for everyone, and we're always open to new ideas and collaborations.
    """)

# Display an image
st.image("https://via.placeholder.com/800x400", caption="Our Journey Together")

# Footer with a personal touch
st.markdown("""
---
Made with ❤️ by a passionate team.
If you have any questions, feel free to [reach out to us](mailto:contact@ourwebsite.com).
""")

