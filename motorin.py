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
    "6–12 Months": {"color": "#add8e6", "items": [
        "Reaches with both hands", "Transfers toy hand-to-hand", "Uses whole hand to rake small objects",
        "Bangs objects together", "Brings hands to midline", "Scribbles spontaneously when given a crayon",
        "Fisted grasp when holding a crayon"]},
    "12–18 Months": {"color": "#ffa07a", "items": [
        "Points with index finger", "Releases small object into container voluntarily", "Stacks 2-3 blocks",
        "Turns pages in a cardboard book", "Uses a spoon with spills", "Pulls lids off containers",
        "Digital pronate grasp when coloring"]},
    "18–24 Months": {"color": "#add8e6", "items": [
        "Imitates vertical stroke with crayon", "Places small objects into a container", "Builds a 4-block tower",
        "Opens Ziplock bags"]},
    "24–30 Months": {"color": "#ffa07a", "items": [
        "Imitates horizontal stroke", "Turns single pages in board books", "Unscrews lids from containers",
        "Snips with child-safe scissors", "Scribbles within large shapes without crossing boundaries",
        "Attempts to copy a circle", "Uses fingertip grasp when coloring"]},
    "30–36 Months": {"color": "#add8e6", "items": [
        "Copies circle independently", "Begins to draw a person with head and limbs (2-4 parts)",
        "Builds 6-8 block tower", "Uses spoon and fork with moderate spill", "Tripod grasp emerges when coloring"]},
    "3–4 Years": {"color": "#ffa07a", "items": [
        "Copies cross", "Cuts across a piece of paper with scissors", "Strings large beads",
        "Buttons large buttons", "Begins drawing a square"]},
    "4–5 Years": {"color": "#add8e6", "items": [
        "Copies square", "Begins drawing triangle", "Cuts on a line with scissors",
        "Writes some letters in their name", "Dresses self with supervision"]},
    "5–6 Years": {"color": "#ffa07a", "items": [
        "Copies triangle", "Begins copying diamond", "Draws person with 6+ parts",
        "Prints first and last name", "Ties shoelaces (attempts)", "Buttons and unbuttons without help"]},
    "6–7 Years": {"color": "#add8e6", "items": [
        "Copies diamond", "Writes legibly within lines", "Cuts out complex shapes accurately",
        "Ties shoelaces independently", "Demonstrates refined tripod grasp"]}
}

scores = {}
flagged_items = []

# Scoring UI
for age_group, data in motorin_data.items():
    st.markdown(f"### <span style='color:{data['color']}'>{age_group}</span>", unsafe_allow_html=True)
    for item in data['items']:
        col1, col2, col3 = st.columns([4, 3, 3])
        with col1:
            st.markdown(f"<span style='color:{data['color']}'>{item}</span>", unsafe_allow_html=True)
        with col2:
            response = st.radio("", options, key=f"{age_group}_{item}", horizontal=True, label_visibility="collapsed")
        scores[f"{age_group}: {item}"] = score_map[response]
        if score_map[response] == 0:
            flagged_items.append(f"{item} ({age_group})")

# Report
if st.button("Generate Report"):
    total_score = sum(scores.values())

    # Word report
    doc = Document()
    doc.add_heading("MOTORIN Screener Report", 0)
    doc.add_paragraph(f"Name: {child_name}")
    doc.add_paragraph(f"Therapist: {therapist_name}")
    doc.add_paragraph(f"Session Date: {session_date.strftime('%B %d, %Y')}")
    if age_years is not None:
        doc.add_paragraph(f"Chronological Age: {age_years} years, {age_months} months")
    doc.add_paragraph(f"Total Score: {total_score}")

    if flagged_items:
        doc.add_heading("⚠️ Flagged Items (Marked Absent)", level=2)
        for flag in flagged_items:
            doc.add_paragraph(f"- {flag}")

    for age_group in motorin_data:
        doc.add_heading(age_group, level=2)
        for item in motorin_data[age_group]['items']:
            key = f"{age_group}: {item}"
            val = scores[key]
            label = [k for k, v in score_map.items() if v == val][0]
            doc.add_paragraph(f"{item}: {label}")

    if notes:
        doc.add_heading("Therapist Notes", level=2)
        doc.add_paragraph(notes)

    word_stream = BytesIO()
    doc.save(word_stream)
    st.download_button("Download Word Report", word_stream.getvalue(), file_name="motorin_report.docx")

    # PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="MOTORIN Screener Report")
    pdf.multi_cell(0, 10, txt=f"Name: {child_name}")
    pdf.multi_cell(0, 10, txt=f"Therapist: {therapist_name}")
    pdf.multi_cell(0, 10, txt=f"Session Date: {session_date.strftime('%B %d, %Y')}")
    if age_years is not None:
        pdf.multi_cell(0, 10, txt=f"Chronological Age: {age_years} years, {age_months} months")
    pdf.multi_cell(0, 10, txt=f"Total Score: {total_score}\n")

    if flagged_items:
        pdf.set_font("Arial", style='B', size=12)
        pdf.multi_cell(0, 10, txt="Flagged Items (Marked Absent):")
        pdf.set_font("Arial", size=12)
        for flag in flagged_items:
            clean_flag = flag.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, txt=f"- {clean_flag}")

    for age_group in motorin_data:
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, txt=age_group.encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.set_font("Arial", size=12)
        for item in motorin_data[age_group]['items']:
            key = f"{age_group}: {item}"
            val = scores[key]
            label = [k for k, v in score_map.items() if v == val][0]
            clean_item = item.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, txt=f"{clean_item}: {label}")

    if notes:
        pdf.set_font("Arial", style='B', size=12)
        pdf.multi_cell(0, 10, txt="\nTherapist Notes")
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=notes.encode('latin-1', 'replace').decode('latin-1'))

    pdf_stream = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    pdf_stream.write(pdf_bytes)
    st.download_button("Download PDF Report", pdf_stream.getvalue(), file_name="motorin_report.pdf")
