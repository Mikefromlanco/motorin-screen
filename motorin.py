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
today = date.today()
age_years = age_months = None
if dob:
    age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    age_months = (today.month - dob.month) % 12
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

# Flatten item list by age group for basal logic
all_items_flat = []
for age_group, group_data in motorin_data.items():
    for item in group_data['items']:
        all_items_flat.append((age_group, item))

# Determine index of basal start (4 items prior to chronological age band)
age_group_names = list(motorin_data.keys())
chronological_band_index = min(len(age_group_names) - 1, max(0, (age_years or 0) - 0))
basal_index = max(0, sum(len(motorin_data[ag]['items']) for ag in age_group_names[:chronological_band_index]) - 4)

scores = {}
flagged_items = []

# Scoring UI
for idx, (age_group, item) in enumerate(all_items_flat):
    data = motorin_data[age_group]
    auto_present = idx < basal_index
    st.markdown("""
        <div style='background-color:{}; padding: 10px; border-radius: 6px;'>
    """.format(data['color']), unsafe_allow_html=True)

    if item == motorin_data[age_group]['items'][0]:
        st.markdown(f"<h4 style='color:black'>{age_group}</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4, 3, 3])
    with col1:
        st.markdown(f"<span style='color:black'>{item}</span>", unsafe_allow_html=True)
    with col2:
        if auto_present:
            response = "Present (2)"
            st.radio("", options, in
