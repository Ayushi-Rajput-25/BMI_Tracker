import streamlit as st

st.title("⚖️BMI Calculator")

height = st.number_input("Enter your height in cm", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kg", min_value=0.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")
else:
    st.write("Please enter both height and weight.")

st.write("Thank you for using our BMI calculator!")
