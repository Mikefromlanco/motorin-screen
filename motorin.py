import streamlit as st

st.title("MOTORIN Fine Motor Screener")

# Test items grouped by age
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
    ]
}

# Display items
for age_group, items in screener_items.items():
    st.header(age_group)
    for item in items:
        st.radio(f"{item}", ["Absent (0)", "Emerging (1)", "Present (2)"], key=item)
