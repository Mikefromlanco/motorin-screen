import streamlit as st
from io import BytesIO
from docx import Document
from fpdf import FPDF
from datetime import date
from dateutil.relativedelta import relativedelta

# Setup
st.set_page_config(page_title="MOTORIN Screener", layout="wide")
st.title("🧠 MOTORIN Fine Motor Screener")

# Child and therapist info
child_name = st.text_input("Child's Name", placeholder="Enter name or initials")

import datetime
st.markdown("**Child's Date of Birth**")
day = st.selectbox("Day", list(range(1, 32)), index=0)
month = st.selectbox("Month", list(range(1, 13)), index=0)
year = st.selectbox("Year", list(range(2000, datetime.datetime.now().year + 1)), index=20)

dob = datetime.date(year, month, day)
age = relativedelta(date.today(), dob)
age_years = age.years
age_months = age.months
st.markdown(f"**Chronological Age:** {age_years} years, {age_months} months")

therapist_name = st.text_input("Therapist Name", placeholder="Enter therapist name")
session_date = st.date_input("Session Date", value=date.today())
notes = st.text_area("Therapist Notes / Impressions")





# Scoring
options = ["Absent (0)", "Emerging (1)", "Present (2)"]
score_map = {"Absent (0)": 0, "Emerging (1)": 1, "Present (2)": 2}

motorin_data = {
    "6–12 Months": {"items": [
        "Reaches with both hands", "Transfers toy hand-to-hand", "Uses whole hand to rake small objects",
        "Bangs objects together", "Brings hands to midline", "Scribbles spontaneously when given a crayon",
        "Fisted grasp when holding a crayon"]},
    "12–18 Months": {"items": [
        "Points with index finger", "Releases small object into container voluntarily", "Stacks 2-3 blocks",
        "Turns pages in a cardboard book", "Uses a spoon with spills", "Pulls lids off containers",
        "Digital pronate grasp when coloring"]},
    "18–24 Months": {"items": [
        "Imitates vertical stroke with crayon", "Places small objects into a container", "Builds a 4-block tower",
        "Opens Ziplock bags"]},
    "24–30 Months": {"items": [
        "Imitates horizontal stroke", "Turns single pages in board books", "Unscrews lids from containers",
        "Snips with child-safe scissors", "Scribbles within large shapes without crossing boundaries",
        "Attempts to copy a circle", "Uses fingertip grasp when coloring"]},
    "30–36 Months": {"items": [
        "Copies circle independently", "Begins to draw a person with head and limbs (2-4 parts)",
        "Builds 6-8 block tower", "Uses spoon and fork with moderate spill", "Tripod grasp emerges when coloring"]},
    "3–4 Years": {"items": [
        "Copies cross", "Cuts across a piece of paper with scissors", "Strings large beads",
        "Buttons large buttons", "Begins drawing a square"]},
    "4–5 Years": {"items": [
        "Copies square", "Begins drawing triangle", "Cuts on a line with scissors",
        "Writes some letters in their name", "Dresses self with supervision"]},
    "5–6 Years": {"items": [
        "Copies triangle", "Begins copying diamond", "Draws person with 6+ parts",
        "Prints first and last name", "Ties shoelaces (attempts)", "Buttons and unbuttons without help"]},
    "6–7 Years": {"items": [
        "Copies diamond", "Writes legibly within lines", "Cuts out complex shapes accurately",
        "Ties shoelaces independently", "Demonstrates refined tripod grasp"]}
}

# Flatten the list of items with metadata
flat_items = []
for group_idx, (age_group, data) in enumerate(motorin_data.items()):
    for item in data['items']:
        flat_items.append({
            "age_group": age_group,
            "group_idx": group_idx,
            "item": item
        })

# Generate report
if child_name:
    document = Document()
    document.add_heading("MOTORIN Screener Report", 0)
    document.add_paragraph(f"Name: {child_name}")
    document.add_paragraph(f"Session Date: {session_date.strftime('%B %d, %Y')}")
document.add_paragraph(f"Date of Birth: {dob.strftime('%d/%m/%Y')}")
document.add_paragraph(f"Chronological Age: {age_years} years, {age_months} months")
        if therapist_name:
        document.add_paragraph(f"Therapist: {therapist_name}")
    if notes:
        document.add_paragraph("Therapist Notes:")
        document.add_paragraph(notes)

    document.add_paragraph("⚠️ Items flagged for review:")
    for item in flagged_items:
        document.add_paragraph(f"- {item}")

    document.add_paragraph("Scoring Summary:")
    for item, score in scores.items():
        document.add_paragraph(f"{item}: {score}")

    buffer = BytesIO()
    document.save(buffer)
    buffer.seek(0)
    st.download_button("📥 Download Report (.docx)", buffer, file_name="motorin_report.docx")


# Show items and implement basal logic
scores = {}
flagged_items = []
present_streak = 0
basal_triggered = False
basal_index = None

for idx, entry in enumerate(flat_items):
    age_group = entry['age_group']
    item = entry['item']
    key = f"{age_group}_{item}"

    show_header = item == motorin_data[age_group]['items'][0]
    if show_header:
        st.markdown(f"<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:black'>{age_group}</h4>", unsafe_allow_html=True)

    col1, col2, _ = st.columns([4, 6, 1])
    with col1:
        st.markdown(f"<span style='color:black'>{item}</span>", unsafe_allow_html=True)

    with col2:
        if basal_triggered and idx < basal_index:
            default_index = 2  # default to "Present (2)"
        else:
            default_index = None

        response = st.radio("", options, key=key, horizontal=True, index=default_index, label_visibility="collapsed")
        score = score_map.get(response, 0)

        if score == 2:
            present_streak += 1
            if present_streak >= 4 and not basal_triggered:
                basal_index = idx - 3
                basal_triggered = True
        else:
            present_streak = 0

    scores[f"{age_group}: {item}"] = score
    if score == 0:
        flagged_items.append(f"{item} ({age_group})")
