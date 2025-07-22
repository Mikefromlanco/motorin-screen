import streamlit as st

st.set_page_config(layout="wide")
st.title("MOTORIN Fine Motor Screener")

# Define screener items grouped by age
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

# Custom spacing styles
st.markdown("""
    <style>
    .stRadio > div {
        flex-direction: row;
        gap: 32px !important;
        margin-top: -15px;
    }
    .stRadio label {
        font-size: 16px;
    }
    .item-block {
        margin-bottom: 35px;
    }
    hr {
        margin-top: 50px;
        margin-bottom: 50px;
        border: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# Display numbered items with improved spacing and dividers
item_num = 1
for idx, (age_group, items) in enumerate(screener_items.items()):
    if idx > 0:
        st.markdown("<hr>", unsafe_allow_html=True)
    st.header(age_group)
    for item in items:
        st.markdown(f"<div class='item-block'><strong>{item_num}. {item}</strong></div>", unsafe_allow_html=True)
        st.radio(
            label="",
            options=["Absent (0)", "Emerging (1)", "Present (2)"],
            key=f"{item_num}_{item}",
            horizontal=True
        )
        item_num += 1
