import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.markdown("""
<div style='text-align: center;'>
    <img src='https://i.imgur.com/yDtdR8y.png' style='width: 30%; max-width: 350px; height: auto;'>
</div>
""", unsafe_allow_html=True)

# Child and therapist info
child_fn = st.text_input("Child's First Name")
child_ln = st.text_input("Child's Last Name")
screen_date = st.date_input("Date of Screen")
dob = st.date_input("Child's Date of Birth")
therapist_name = st.text_input("Therapist's Name")

# Calculate chronological age
if dob:
    today = date.today()
    age = relativedelta(today, dob)
    st.markdown(f"**Chronological Age:** {age.years} years, {age.months} months")

# Define age groups and items
screener_items = {
    "6–12 Months": [
        "Reaches with both hands",
        "Transfers toy hand-to-hand",
        "Uses whole hand to rake small objects",
        "Bangs objects together",
        "Brings hands to midline",
        "Scribbles spontaneously when given a crayon",
        "Fisted grasp when holding a crayon"
    ],
    "12–18 Months": [
        "Points with index finger",
        "Releases small object into container voluntarily",
        "Stacks 2–3 blocks",
        "Turns pages in a cardboard book",
        "Uses a spoon with spills",
        "Pulls lids off containers (e.g., Play-Doh, Tupperware)",
        "Digital pronate grasp when coloring"
    ],
    "18–24 Months": [
        "Imitates vertical stroke with crayon",
        "Places small objects into a container",
        "Builds a 4-block tower",
        "Opens Ziplock bags"
    ],
    "24–30 Months": [
        "Imitates horizontal stroke",
        "Turns single pages in board books",
        "Unscrews lids from containers",
        "Snips with child-safe scissors",
        "Scribbles within large shapes without crossing boundaries",
        "Makes approximations of circles (endpoints overlap, looks more like an oval/circular scribble)",
        "Uses fingertip grasp when coloring"
    ],
    "30–36 Months": [
        "Copies circle independently",
        "Draws a person with limbs and facial features (5 plus parts)",
        "Builds 6–8 block tower",
        "Uses spoon and fork with moderate spill",
        "Tripod grasp emerges when coloring"
    ],
    "3–4 Years": [
        "Copies cross",
        "Cuts across a piece of paper with scissors",
        "Strings large beads",
        "Buttons large buttons",
        "Begins drawing a square"
    ],
    "4–5 Years": [
        "Copies square",
        "Begins drawing triangle",
        "Cuts on a line with scissors",
        "Writes some letters in their name",
        "Dresses self with supervision (zippers/buttons)"
    ],
    "5–6 Years": [
        "Copies triangle",
        "Begins copying diamond",
        "Draws person with 6+ parts",
        "Prints first and last name",
        "Ties shoelaces (attempts)",
        "Buttons and unbuttons without help"
    ],
    "6–7 Years": [
        "Copies diamond",
        "Writes legibly within lines",
        "Cuts out complex shapes accurately",
        "Ties shoelaces independently",
        "Demonstrates refined tripod grasp"
    ]
}

# Display demographics and screener items
st.markdown("""
---
### Screening Details
**Child's First Name:** {}

**Child's Last Name:** {}

**Date of Birth:** {}

**Chronological Age:** {} years, {} months

**Therapist Name:** {}

**Date of Screen:** {}
---
""".format(child_fn, child_ln, dob.strftime('%m/%d/%Y'), age.years if dob else '', age.months if dob else '', therapist_name, screen_date.strftime('%m/%d/%Y')))
for age_group, items in screener_items.items():
    st.markdown(f"### {age_group}")
    for item in items:
        st.radio(label=item, options=["Absent (0)", "Emerging (1)", "Present (2)"], horizontal=True, key=item)
