import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Explanation message
st.markdown("""
Welcome to the BMI Calculator! 
To calculate your Body Mass Index (BMI), simply enter your weight and height below.
Your BMI will help you understand if your weight is in a healthy range.
""")

# Input fields for weight and height
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.1, step=0.01)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Show result if valid input is provided
if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # BMI categories and interpretation
    if bmi < 18.5:
        st.write("Your BMI indicates: **Underweight**. It's a good idea to consult a healthcare provider.")
    elif 18.5 <= bmi < 24.9:
        st.write("Your BMI indicates: **Normal weight**. Keep maintaining a balanced lifestyle!")
    elif 25 <= bmi < 29.9:
        st.write("Your BMI indicates: **Overweight**. Consider a healthy diet and regular exercise.")
    else:
        st.write("Your BMI indicates: **Obesity**. It's important to talk to a healthcare professional.")
