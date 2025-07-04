import streamlit as st

st.set_page_config(page_title="Personal Carbon Calculator App", layout="centered")

st.markdown("## Personal Carbon Calculator App ⚠️")

st.markdown("### 🌍 Your Country")
country = st.selectbox("Select", ["India", "USA", "UK", "Germany", "Australia", "Other"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚗 Daily commute distance (in km)")
    commute_km = st.slider("Distance", min_value=0.0, max_value=100.0, value=6.0)

with col2:
    st.markdown("### 🍽️ Waste generated per week (in kg)")
    waste_kg = st.slider("Waste", min_value=0.0, max_value=100.0, value=6.0)

with col1:
    st.markdown("### ⚡ Monthly electricity consumption (in kWh)")
    electricity_kwh = st.slider("Electricity", min_value=0.0, max_value=1800.0, value=6.0)

with col2:
    st.markdown("### 🍛 Number of meals per day")
    meals = st.number_input("Meals", min_value=0, max_value=10, value=0)

if st.button("Calculate CO2 Emissions"):
    total_emissions = (commute_km * 0.21 * 30) + (waste_kg * 4) + (electricity_kwh * 0.7) + (meals * 0.5 * 30)
    
    st.success(f"Estimated CO₂ emissions per month: **{total_emissions:.2f} kg CO₂**")
