import streamlit as st
from datetime import date

# Updated MOTORIN screener item list (Birth to 7 Years)
motorin_items = {
    "0-3 Months": [
        "Tracks rattle side to side",
        "Brings hands to midline",
        "Briefly brings hands to mouth",
        "Grips caregiver's finger",
        "Opens fingers during touch/play",
        "Shows alertness to visual stimuli"
    ],
    "4-6 Months": [
        "Reaches for toy with both hands",
        "Holds a rattle briefly with one or both hands",
        "Brings toy to mouth",
        "Swipes at toy dangling in front of them",
        "Maintains grasp when toy is gently pulled",
        "Purposefully turns head to look at sounds"
    ],
    "7-9 Months": [
        "Transfers toy between hands",
        "Bangs two toys together",
        "Rakes small object with fingers",
        "Grasps cube with radial-palmar grasp",
        "Shakes toy purposefully",
        "Reaches in different directions with control"
    ],
    "10-12 Months": [
        "Releases block into container",
        "Uses a pincer grasp to pick up tiny objects",
        "Opens hand to drop object without cue",
        "Pokes with index finger",
        "Takes rings off of a stacker"
    ],
    "13-18 Months": [
        "Turns pages in cardboard book (multiple at once)",
        "Scribbles with crayon (full-arm motion)",
        "Places 1 shape into shape sorter",
        "Removes pegs from pegboard",
        "Places toy in/out of container",
        "Uses both hands in midline play",
        "Puts 4 rings onto a stacker"
    ],
    "19-24 Months": [
        "Builds tower of 4+ blocks",
        "Places lid on container",
        "Unscrews or pulls off container lid",
        "Scribbles spontaneously (in all directions)",
        "Places 3+ shapes in sorter",
        "Inserts coin into slot",
        "Takes apart pop beads",
        "Imitates forming vertical strokes"
    ],
    "25-36 Months (2-3 Years)": [
        "Draws vertical stroke",
        "Builds 6-block tower",
        "Opens simple flip-top container",
        "Strings 1–2 large beads",
        "Imitates circular scribble",
        "Begins to show hand preference",
        "Puts together pop beads",
        "Imitates forming horizontal strokes"
    ],
    "37-48 Months (3-4 Years)": [
        "Snips paper with child scissors",
        "Imitates forming a circle",
        "Strings 4–5 beads",
        "Cuts across paper with moderate control",
        "Builds 9–10 block tower",
        "Screws lid onto container",
        "Imitates forming a cross"
    ],
    "49-60 Months (4-5 Years)": [
        "Imitates forming a square",
        "Draws simple person (head + limbs)",
        "Cuts on thick line with control",
        "Colors inside simple shape (e.g., circle)",
        "Uses mature tripod grasp (emerging)",
        "Places clothespin onto object"
    ],
    "61-72 Months (5-6 Years)": [
        "Imitates forming a triangle",
        "Draws complete person (head, limbs, facial features)",
        "Cuts simple shapes (circle, square)",
        "Writes name or letters with legibility",
        "Strings 3 small beads onto a string",
        "Imitates and reproduces 3-step visual patterns",
        "Opens food packages"
    ],
    "73-84 Months (6-7 Years)": [
        "Copies diamond",
        "Writes full name with legible spacing",
        "Cuts out a square accurately",
        "Writes short sentence",
        "Folds paper in half with symmetry",
        "Completes dot-to-dot picture with precision"
    ]
}

st.markdown("<div style='text-align: center;'><img src='https://i.imgur.com/1thkHWE.png' width='480'></div>", unsafe_allow_html=True)
st.markdown("---")

# Child’s First Name (left) and Today’s Date (right)
col1, col2 = st.columns([2, 1])
with col1:
    child_name = st.text_input("Child's First Name")
with col2:
    screen_date = st.date_input("Screen Date", value=date.today())

# Additional info
child_last_name = st.text_input("Child's Last Name")
therapist_name = st.text_input("Therapist Name")
dob = st.date_input("Date of Birth")
today = screen_date

# Chronological age in months (and Y/M format)
age_months = (today.year - dob.year) * 12 + today.month - dob.month
age_years = age_months // 12
age_remaining_months = age_months % 12
st.write(f"Chronological Age: {age_months} months ({age_years} Y, {age_remaining_months} M)")

# Screener responses
responses = {}

for band, items in motorin_items.items():
    st.subheader(band)
    for item in items:
        key = f"{band}_{item}"
        response = st.radio(
            label=item,
            options=["Absent", "Emerging", "Present"],
            key=key,
            horizontal=True
        )
        responses[key] = response

if st.button("Submit"):
    st.success("Screening complete! Generating summary...")
    passed = sum(1 for r in responses.values() if r == "Present")
    total = len(responses)
    st.write(f"Items marked 'Present': {passed} / {total}")

    # Calculate percentages per bracket
    bracket_results = {}
    for band, items in motorin_items.items():
        present_count = sum(1 for item in items if responses.get(f"{band}_{item}") == "Present")
        percentage = round((present_count / len(items)) * 100)
        bracket_results[band] = percentage

    # Display chart
    st.markdown("---")
    st.subheader("Summary by Age Band")
    st.bar_chart(bracket_results)
