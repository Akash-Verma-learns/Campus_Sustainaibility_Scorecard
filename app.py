import streamlit as st
import json
from score_utils import calculate_score, get_grade

st.set_page_config(page_title="Campus Sustainability Scorecard", layout="centered")
st.title("🏫 Campus Sustainability Scorecard")

st.markdown("Enter your monthly data below:")

electricity = st.number_input("🔌 Electricity Usage (kWh)", min_value=0, value=3000)
water = st.number_input("🚰 Water Usage (litres)", min_value=0, value=20000)
transport_total = st.number_input("🚗 Total Commutes (students + staff)", min_value=1, value=1000)
green_commutes = st.number_input("🚲 Green Commutes (walk, cycle, public transport)", min_value=0, value=400)
waste = st.number_input("🗑 Waste Sent to Landfill (kg)", min_value=0, value=500)

if transport_total > 0:
    green_ratio = green_commutes / transport_total
else:
    green_ratio = 0

data = {
    "electricity": electricity,
    "water": water,
    "green_transport_ratio": green_ratio,
    "waste": waste
}

if st.button("Generate Score"):
    score = calculate_score(data)
    grade = get_grade(score)

    st.metric("Total Sustainability Score", f"{score}/100")
    st.metric("Grade", grade)

    with open("suggestions.json") as f:
        tips = json.load(f)

    st.subheader("💡 Suggestions to Improve")
    if electricity > 3000:
        st.info(tips["electricity"])
    if water > 15000:
        st.info(tips["water"])
    if green_ratio < 0.5:
        st.info(tips["transport"])
    if waste > 300:
        st.info(tips["waste"])
