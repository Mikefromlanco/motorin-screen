import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# Page setup

st.set_page_config(page_title="MOTORIN Screener")
st.markdown("<h1 style='text-align: center;'><img src='https://i.imgur.com/CFwRkK8.png' width='60' style='vertical-align: middle;'> MOTORIN Fine Motor Screener</h1>", unsafe_allow_html=True)


first_name = st.text_input("Child's First Name")
last_name = st.text_input("Child's Last Name")
therapist_name = st.text_input("Therapist's Name")

# Child DOB and Chronological Age Calculation
dob = st.date_input("Child's Date of Birth", value=date.today())
age = relativedelta(date.today(), dob)
st.markdown(f"**Chronological Age:** {age.years} years, {age.months} months")

# Scoring setup
options = ["Absent (0)", "Emerging (1)", "Present (2)"]
score_map = {"Absent (0)": 0, "Emerging (1)": 1, "Present (2)": 2}

# Motorin data (test items only)
motorin_data = {
    "6–12 Months": [
        "Reaches with both hands", "Transfers toy hand-to-hand", "Uses whole hand to rake small objects",
        "Bangs objects together", "Brings hands to midline", "Scribbles spontaneously when given a crayon",
        "Fisted grasp when holding a crayon"
    ],
    "12–18 Months": [
        "Points with index finger", "Releases small object into container voluntarily", "Stacks 2–3 blocks",
        "Turns pages in a cardboard book", "Uses a spoon with spills", "Pulls lids off containers",
        "Digital pronate grasp when coloring"
    ],
    "18–24 Months": [
        "Imitates vertical stroke with crayon", "Places small objects into a container", "Builds a 4-block tower",
        "Opens Ziplock bags"
    ],
    "24–30 Months": [
        "Imitates horizontal stroke", "Turns single pages in board books", "Unscrews lids from containers",
        "Snips with child-safe scissors", "Scribbles within large shapes without crossing boundaries",
        "Makes approximations of circles (endpoints overlap, looks more like an oval/circular scribble)", "Uses fingertip grasp when coloring"
    ],
    "30–36 Months": [
        "Copies circle independently", "Draws a person with limbs and facial features (5 plus parts)",
        "Builds 6–8 block tower", "Uses spoon and fork with moderate spill", "Tripod grasp emerges when coloring"
    ],
    "3–4 Years": [
        "Copies cross", "Cuts across a piece of paper with scissors", "Strings large beads",
        "Buttons large buttons", "Begins drawing a square"
    ],
    "4–5 Years": [
        "Copies square", "Begins drawing triangle", "Cuts on a line with scissors",
        "Writes some letters in their name", "Dresses self with supervision"
    ],
    "5–6 Years": [
        "Copies triangle", "Begins copying diamond", "Draws person with 6+ parts",
        "Prints first and last name", "Ties shoelaces (attempts)", "Buttons and unbuttons without help"
    ],
    "6–7 Years": [
        "Copies diamond", "Writes legibly within lines", "Cuts out complex shapes accurately",
        "Ties shoelaces independently", "Demonstrates refined tripod grasp"
    ]
}

# Render items
for age_group, items in motorin_data.items():
    st.markdown(f"---\n### {age_group}")
    for item in items:
        response = st.radio(f"{item}", options, horizontal=True, key=f"{age_group}_{item}")
