import streamlit as st
from io import BytesIO
from docx import Document
from fpdf import FPDF

# Configuration
st.set_page_config(page_title="MOTORIN Screener", layout="wide")
st.title("🧠 MOTORIN Fine Motor Screener")
st.subheader("OT-led Screener: Caregiver Interview and/or Child Participation")

# Scoring categories
options = ["Absent (0)", "Emerging (1)", "Present (2)"]
score_map = {"Absent (0)": 0, "Emerging (1)": 1, "Present (2)": 2}

# Screener data
motorin_data = {
    "6–12 Months": {
        "color": "#add8e6",
        "items": [
            "Reaches with both hands",
            "Transfers toy hand-to-hand",
            "Uses whole hand to rake small objects",
            "Bangs objects together",
            "Brings hands to midline",
            "Scribbles spontaneously when given a crayon",
            "Fisted grasp when holding a crayon"
        ]
    },
    "12–18 Months": {
        "color": "#ffa07a",
        "items": [
            "Points with index finger",
            "Releases small object into container voluntarily",
            "Stacks 2-3 blocks",
            "Turns pages in a cardboard book",
            "Uses a spoon with spills",
            "Pulls lids off containers (e.g., Play-Doh, Tupperware)",
            "Digital pronate grasp when coloring"
        ]
    },
    "18–24 Months": {
        "color": "#add8e6",
        "items": [
            "Imitates vertical stroke with crayon",
            "Places small objects into a container",
            "Builds a 4-block tower",
            "Opens Ziplock bags"
        ]
    },
    "24–30 Months": {
        "color": "#ffa07a",
        "items": [
            "Imitates horizontal stroke",
            "Turns single pages in board books",
            "Unscrews lids from containers",
            "Snips with child-safe scissors",
            "Scribbles within large shapes without crossing boundaries",
            "Attempts to copy a circle",
            "Uses fingertip grasp when coloring"
        ]
    },
    "30–36 Months": {
        "color": "#add8e6",
        "items": [
            "Copies circle independently",
            "Begins to draw a person with head and limbs (2-4 parts)",
            "Builds 6-8 block tower",
            "Uses spoon and fork with moderate spill",
            "Tripod grasp emerges when coloring"
        ]
    },
    "3–4 Years": {
        "color": "#ffa07a",
        "items": [
            "Copies cross",
            "Cuts across a piece of paper with scissors",
            "Strings large beads",
            "Buttons large buttons",
            "Begins drawing a square"
        ]
    },
    "4–5 Years": {
        "color": "#add8e6",
        "items": [
            "Copies square",
            "Begins drawing triangle",
            "Cuts on a line with scissors",
            "Writes some letters in their name",
            "Dresses self with supervision (zippers/buttons)"
        ]
    },
    "5–6 Years": {
        "color": "#ffa07a",
        "items": [
            "Copies triangle",
            "Begins copying diamond",
            "Draws person with 6+ parts",
            "Prints first and last name",
            "Ties shoelaces (attempts)",
            "Buttons and unbuttons without help"
        ]
    },
    "6–7 Years": {
        "color": "#add8e6",
        "items": [
            "Copies diamond",
            "Writes legibly within lines",
            "Cuts out complex shapes accurately",
            "Ties shoelaces independently",
            "Demonstrates refined tripod grasp"
        ]
    }
}

scores = {}

# UI for scoring
for age_group, data in motorin_data.items():
    st.markdown(f"### <span style='color:{data['color']}'>{age_group}</span>", unsafe_allow_html=True)
    for item in data['items']:
        choice = st.radio(item, options, horizontal=True, key=f"{age_group}_{item}")
        scores[f"{age_group}: {item}"] = score_map[choice]

# Generate report
if st.button("Generate Report"):
    total_score = sum(scores.values())
    doc = Document()
    doc.add_heading("MOTORIN Screener Report", 0)
    doc.add_paragraph(f"Total Score: {total_score}")

    for age_group in motorin_data:
        doc.add_heading(age_group, level=1)
        for item in motorin_data[age_group]['items']:
            key = f"{age_group}: {item}"
            val = scores[key]
            doc.add_paragraph(f"{item}: {val} ({[k for k,v in score_map.items() if v == val][0]})")

    # Save as Word
    word_stream = BytesIO()
    doc.save(word_stream)
    st.download_button("Download Word Report", word_stream.getvalue(), file_name="motorin_report.docx")

    # Save as PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="MOTORIN Screener Report\n\n")
    pdf.multi_cell(0, 10, txt=f"Total Score: {total_score}\n")
    for age_group in motorin_data:
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, txt=age_group, ln=True)
        pdf.set_font("Arial", size=12)
        for item in motorin_data[age_group]['items']:
            key = f"{age_group}: {item}"
            val = scores[key]
            label = [k for k,v in score_map.items() if v == val][0]
            pdf.multi_cell(0, 10, txt=f"{item}: {val} ({label})")

    pdf_stream = BytesIO()
    pdf.output(pdf_stream)
    st.download_button("Download PDF Report", pdf_stream.getvalue(), file_name="motorin_report.pdf")
