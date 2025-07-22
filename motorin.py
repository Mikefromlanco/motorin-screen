import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-header {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }
        .section {
            border: 2px solid #ddd;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 40px;
            background-color: #f9f9f9;
        }
        .item-label {
            font-size: 20px;
            font-weight: 500;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="big-header">🧠 MOTORIN Fine Motor Screener</div>', unsafe_allow_html=True)
st.write("")

# Define test items by age group
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

# Render each section
for age_range, items in screener_items.items():
    with st.container():
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader(age_range)
        for item in items:
            st.markdown(f'<div class="item-label">{item}</div>', unsafe_allow_html=True)
            st.radio(f"{item}", ["Absent (0)", "Emerging (1)", "Present (2)"], key=item)
        st.markdown('</div>', unsafe_allow_html=True)
