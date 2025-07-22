import streamlit as st

# Page setup
st.set_page_config(page_title="MOTORIN Screener")
st.title("🧠 MOTORIN Fine Motor Screener")

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
        "Attempts to copy a circle", "Uses fingertip grasp when coloring"
    ],
    "30–36 Months": [
        "Copies circle independently", "Begins to draw a person with head and limbs (2–4 parts)",
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
