import streamlit as st
from io import BytesIO
from docx import Document
from fpdf import FPDF
from datetime import date

# Setup
st.set_page_config(page_title="MOTORIN Screener", layout="wide")
st.title("🧠 MOTORIN Fine Motor Screener")

# Child and therapist info
child_name = st.text_input("Child's Name", placeholder="Enter name or initials")
dob = st.date_input("Child's Date of Birth")
therapist_name = st.text_input("Therapist Name", placeholder="Enter therapist name")
session_date = st.date_input("Session Date", value=date.today())
notes = st.text_area("Therapist Notes / Impressions")

# Calculate age
age_years = age_months = None
if dob:
    today = date.today()
    age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    age_months = (today.month - dob.month - (today.day < dob.day)) % 12
    st.markdown(f"**Chronological Age:** {age_years} years, {age_months} months")

# Scoring
options = ["Absent (0)", "Emerging (1)", "Present (2)"]
score_map = {"Absent (0)": 0, "Emerging (1)": 1, "Present (2)": 2}

motorin_data = {
    "6–12 Months": {"color": "#e6f2ff", "items": [
        "Reaches with both hands", "Transfers toy hand-to-hand", "Uses whole hand to rake small objects",
        "Bangs objects together", "Brings hands to midline", "Scribbles spontaneously when given a crayon",
        "Fisted grasp when holding a crayon"]},
    "12–18 Months": {"color": "#ffe5cc", "items": [
        "Points with index finger", "Releases small object into container voluntarily", "Stacks 2-3 blocks",
        "Turns pages in a cardboard book", "Uses a spoon with spills", "Pulls lids off containers",
        "Digital pronate grasp when coloring"]},
    "18–24 Months": {"color": "#e6f2ff", "items": [
        "Imitates vertical stroke with crayon", "Places small objects into a container", "Builds a 4-block tower",
        "Opens Ziplock bags"]},
    "24–30 Months": {"color": "#ffe5cc", "items": [
        "Imitates horizontal stroke", "Turns single pages in board books", "Unscrews lids from containers",
        "Snips with child-safe scissors", "Scribbles within large shapes without crossing boundaries",
        "Attempts to copy a circle", "Uses fingertip grasp when coloring"]},
    "30–36 Months": {"color": "#e6f2ff", "items": [
        "Copies circle independently", "Begins to draw a person with head and limbs (2-4 parts)",
        "Builds 6-8 block tower", "Uses spoon and fork with moderate spill", "Tripod grasp emerges when coloring"]},
    "3–4 Years": {"color": "#ffe5cc", "items": [
        "Copies cross", "Cuts across a piece of paper with scissors", "Strings large beads",
        "Buttons large buttons", "Begins drawing a square"]},
    "4–5 Years": {"color": "#e6f2ff", "items": [
        "Copies square", "Begins drawing triangle", "Cuts on a line with scissors",
        "Writes some letters in their name", "Dresses self with supervision"]},
    "5–6 Years": {"color": "#ffe5cc", "items": [
        "Copies triangle", "Begins copying diamond", "Draws person with 6+ parts",
        "Prints first and last name", "Ties shoelaces (attempts)", "Buttons and unbuttons without help"]},
    "6–7 Years": {"color": "#e6f2ff", "items": [
        "Copies diamond", "Writes legibly within lines", "Cuts out complex shapes accurately",
        "Ties shoelaces independently", "Demonstrates refined tripod grasp"]}
}

# Calculate total items up to current age group
total_items = []
basal_flag = False

scores = {}
flagged_items = []
found_basal = False
present_streak = 0

for age_group, group_data in motorin_data.items():
    group_color = group_data['color']
    st.markdown(f"<div style='background-color:{group_color}; padding: 10px; border-radius: 6px;'>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:black'>{age_group}</h4>", unsafe_allow_html=True)

    for item in group_data['items']:
        col1, col2, _ = st.columns([4, 6, 1])
        with col1:
            st.markdown(f"<span style='color:black'>{item}</span>", unsafe_allow_html=True)

        key = f"{age_group}_{item}"

        # Automatically assign Present (2) for all items before basal
        if not found_basal:
            default_idx = 2  # Present
            disabled = True
            present_streak += 1
            if present_streak >= 4:
                found_basal = True
        else:
            default_idx = 0
            disabled = False

        with col2:
            response = st.radio("", options, index=default_idx, key=key, horizontal=True, label_visibility="collapsed", disabled=disabled)

        score = score_map[response]
        scores[f"{age_group}: {item}"] = score
        if score == 0:
            flagged_items.append(f"{item} ({age_group})")

    st.markdown("</div>", unsafe_allow_html=True)
