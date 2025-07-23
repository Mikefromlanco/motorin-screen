  1: import streamlit as st
  2: from datetime import datetime
  3: 
  4: st.set_page_config(page_title="Motorin Screener", layout="centered")
  5: 
  6: # ---- LOGO (CENTERED AND ENLARGED) ----
  7: st.markdown("<div style='text-align: center;'><img src='https://i.imgur.com/1thkHWE.png' width='480'></div>", unsafe_allow_html=True)
  8: st.markdown("---")
  9: 
 10: # ---- DEMOGRAPHICS ----
 11: st.header("Screening Details")
 12: child_first_name = st.text_input("Child's First Name")
 13: child_last_name = st.text_input("Child's Last Name")
 14: dob = st.date_input("Date of Birth")
 15: date_of_screen = st.date_input("Date of Screen", datetime.today())
 16: therapist_name = st.text_input("Therapist Name")
 17: 
 18: # ---- CHRONOLOGICAL AGE CALCULATION ----
 19: if dob:
 20:     today = date_of_screen
 21:     delta = today - dob
 22:     years = delta.days // 365
 23:     months = (delta.days % 365) // 30
 24:     st.markdown(f"**Chronological Age:** {years} years, {months} months")
 25: 
 26: st.markdown("---")
 27: 
 28: # ---- SCREENER INSTRUCTIONS ----
 29: st.subheader("Instructions")
 30: st.markdown("Rate each item based on observation or parent/therapist report using the following scale:")
 31: st.markdown("- 0 = Absent")
 32: st.markdown("- 1 = Emerging")
 33: st.markdown("- 2 = Present")
 34: st.markdown("---")
 35: 
 36: # ---- SCREENER ITEMS ----
 37: st.header("Screener Items")
 38: 
 39: items_by_age = {
 40:     "1–2 Years": [
 41:         "Reaches for objects with one hand",
 42:         "Bangs two toys together",
 43:         "Places items into a container",
 44:         "Removes items from container",
 45:         "Holds crayon and scribbles",
 46:     ],
 47:     "2–3 Years": [
 48:         "Turns pages in a book",
 49:         "Builds a tower of 4+ blocks",
 50:         "Imitates vertical strokes",
 51:         "Strings large beads",
 52:         "Uses spoon with minimal spilling",
 53:     ],
 54:     "3–4 Years": [
 55:         "Copies a circle",
 56:         "Cuts paper in half with scissors",
 57:         "Buttons large buttons",
 58:         "Uses tripod grasp on crayon",
 59:         "Manipulates toys with moving parts",
 60:     ],
 61:     "4–5 Years": [
 62:         "Copies a cross",
 63:         "Cuts along a straight line",
 64:         "Traces basic shapes",
 65:         "Screws/unscrews lids",
 66:         "Uses fork independently",
 67:     ],
 68:     "5–6 Years": [
 69:         "Prints some capital letters",
 70:         "Cuts out a circle",
 71:         "Zips and unzips jacket",
 72:         "Uses pencil with controlled grasp",
 73:         "Completes simple dot-to-dot",
 74:     ],
 75:     "6–7 Years": [
 76:         "Copies triangle",
 77:         "Colors within the lines",
 78:         "Buttons and unbuttons quickly",
 79:         "Builds complex block designs",
 80:         "Writes name clearly",
 81:     ]
 82: }
 83: 
 84: score_options = {
 85:     "Absent (0)": 0,
 86:     "Emerging (1)": 1,
 87:     "Present (2)": 2
