import streamlit as st

st.set_page_config(layout="wide")
st.title("MOTORIN Fine Motor Screener")

# Test items grouped by age range
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
        "Stacks 2-3 blocks",
        "Turns pages in a cardboard book"
    ],
    "18–24 Months": [
        "Imitates vertical stroke",
        "Builds tower of 4-6 blocks",
        "Places shape in puzzle board (circle/square/triangle)",
        "Turns knob or cap"
    ],
    "24–30 Months": [
        "Imitates horizontal stroke",
        "Strings 1-inch beads",
        "Builds tower of 6+ blocks",
        "Uses pronated or fingertip grasp when scribbling"
    ],
    "30–36 Months": [
        "Imitates circle",
        "Snips with scissors",
        "Builds train of 3+ blocks",
        "Turns pages one at a time",
        "Completes simple inset puzzle"
    ],
    "3–4 Years": [
        "Draws person with head and at least one body part",
        "Imitates cross",
        "Cuts across paper with scissors",
        "Screws/unscrews lid",
        "Holds crayon with tripod grasp"
    ],
    "4–5 Years": [
        "Cuts on line",
        "Draws square",
        "Prints some capital letters",
        "Buttons and unbuttons clothing",
        "Copies first name"
    ],
    "5–6 Years": [
        "Draws triangle",
        "Ties shoelaces",
        "Colors within lines",
        "Cuts out circle",
        "Prints numbers 1–5"
    ],
    "6–7 Years": [
        "Forms all capital and lowercase letters",
        "Uses appropriate spacing when writing",
        "Uses functional grasp with pencil",
        "Cuts complex shapes accurately",
        "Writes full name"
    ]
}

# Display items
for age_group, items in screener_items.items():
    st.header(age_group)
    for item in items:
        st.radio(f"{item}", ["Absent (0)", "Emerging (1)", "Present (2)"], key=item)
