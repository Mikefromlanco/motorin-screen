import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Motorin Screener", layout="centered")

# ---- LOGO (CENTERED AND ENLARGED) ----
st.markdown("<div style='text-align: center;'><img src='https://i.imgur.com/1thkHWE.png' width='480'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---- DEMOGRAPHICS ----
st.header("Screening Details")
child_first_name = st.text_input("Child's First Name")
child_last_name = st.text_input("Child's Last Name")
dob = st.date_input("Date of Birth")
date_of_screen = st.date_input("Date of Screen", datetime.today())
therapist_name = st.text_input("Therapist Name")

# ---- CHRONOLOGICAL AGE CALCULATION ----
if dob:
    today = date_of_screen
    delta = today - dob
    years = delta.days // 365
    months = (delta.days % 365) // 30
    st.markdown(f"**Chronological Age:** {years} years, {months} months")

st.markdown("---")

# ---- SCREENER INSTRUCTIONS ----
st.subheader("Instructions")
st.markdown("Rate each item based on observation or parent/therapist report using the following scale:")
st.markdown("- 0 = Absent")
st.markdown("- 1 = Emerging")
st.markdown("- 2 = Present")
st.markdown("---")

# ---- SCREENER ITEMS ----
st.header("Screener Items")

items_by_age = {
    "1–2 Years": [
        "Reaches for objects with one hand",
        "Bangs two toys together",
        "Places items into a container",
        "Removes items from container",
        "Holds crayon and scribbles",
    ],
    "2–3 Years": [
        "Turns pages in a book",
        "Builds a tower of 4+ blocks",
        "Imitates vertical strokes",
        "Strings large beads",
        "Uses spoon with minimal spilling",
    ],
    "3–4 Years": [
        "Copies a circle",
        "Cuts paper in half with scissors",
        "Buttons large buttons",
        "Uses tripod grasp on crayon",
        "Manipulates toys with moving parts",
    ],
    "4–5 Years": [
        "Copies a cross",
        "Cuts along a straight line",
        "Traces basic shapes",
        "Screws/unscrews lids",
        "Uses fork independently",
    ],
    "5–6 Years": [
        "Prints some capital letters",
        "Cuts out a circle",
        "Zips and unzips jacket",
        "Uses pencil with controlled grasp",
        "Completes simple dot-to-dot",
    ],
    "6–7 Years": [
        "Copies triangle",
        "Colors within the lines",
        "Buttons and unbuttons quickly",
        "Builds complex block designs",
        "Writes name clearly",
    ]
}

score_options = {
    "Absent (0)": 0,
    "Emerging (1)": 1,
    "Present (2)": 2
}

item_number = 1
scores = {}

for age_range, items in items_by_age.items():
    st.markdown(f"<hr><h4>{age_range}</h4>", unsafe_allow_html=True)
    for item in items:
        score = st.radio(f"{item_number}. {item}", list(score_options.keys()), horizontal=True, key=f"item_{item_number}")
        scores[f"{item_number}. {item}"] = score_options[score]
        item_number += 1

st.markdown("---")
st.success("✅ Screening complete! Scroll up to review or edit responses.")
