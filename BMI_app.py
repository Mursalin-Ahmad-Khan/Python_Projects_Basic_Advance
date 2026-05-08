# BMI Calculator Web App.

import streamlit as st

# App Title
st.set_page_config(page_title="BMI" , page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator ")
st.write("Calculate your Body Mass Index (BMI) using height in feet/inches and weight in kilograms.")

# User Inputs 
name = st.text_input("👤 Enter your name:")
age = st.number_input("🎂 Enter your age:", min_value=1, max_value=120, value=25)
gender = st.radio("🧬 Select your gender:", ("Male", "Female"))

col1, col2, col3 = st.columns(3)

with col1:
    feet = st.number_input(
        "Height (feet):",
        min_value=1,
        max_value=8,
        value=5,
        step=1
    )

with col2:
    inches = st.number_input(
        "Height (inches):",
        min_value=0,
        max_value=11,
        value=7,
        step=1
    )

with col3:
    weight = st.number_input(
        "Weight (kg):",
        min_value=1.0,
        max_value=120.0,
        value=70.0,
        step=0.1,
        format="%.3f"
    )

# Extra validation
if weight > 120:
    st.error("Weight cannot exceed 120 kg")

# Calculate BMI Button 
if st.button("Calculate BMI"):
    # Convert height to meters
    height_m = ((feet * 12) + inches) * 0.0254
    bmi = weight / (height_m ** 2)

    # Determine category
    if bmi < 18.5:
        category = "Underweight 😕"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        category = "Normal ✅"
        color = "green"
    elif 25 <= bmi < 29.9:
        category = "Overweight ⚠️"
        color = "orange"
    else:
        category = "Obese 🚨"
        color = "red"

    # Ideal weight range
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)

    #  Display Resultsz
    st.markdown("---")
    st.subheader(f"Result for {name or 'User'}:")
    st.metric(label="💪 Your BMI", value=f"{bmi:.2f}", delta=None)
    st.markdown(f"**Category:** <span style='color:{color}'>{category}</span>", unsafe_allow_html=True)
    st.write(f"✅ Healthy weight range: **{min_weight:.1f} kg – {max_weight:.1f} kg**")

    # Personalized suggestion
    if weight < min_weight:
        st.info(f"You need to **gain about {min_weight - weight:.1f} kg** to reach normal weight.")
    elif weight > max_weight:
        st.warning(f"You need to **lose about {weight - max_weight:.1f} kg** to reach normal weight.")
    else:
        st.success("Perfect! Your weight is in a healthy range. Keep it up 💪")

#  Footer 
st.markdown("---")
st.caption("Made by Mursalin Ahmad Khan ")
