import streamlit as st

st.set_page_config(page_title="MOTORIN Screener", layout="wide")

st.title("🧠 MOTORIN Fine Motor Screener")
st.subheader("For Occupational Therapists: Caregiver Interview or Child Participation")

age_brackets = {
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
            "Stacks 2–3 blocks",
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
            "Begins to draw a person with head and limbs (2–4 parts)",
            "Builds 6–8 block tower",
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

# Render checkboxes by age bracket
for age_group, data in age_brackets.items():
    st.markdown(f"### <span style='color:{data['color']}'>{age_group}</span>", unsafe_allow_html=True)
    for item in data["items"]:
        st.checkbox(item, key=f"{age_group}_{item}")
