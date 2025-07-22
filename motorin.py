import streamlit as st
from io import BytesIO
from docx import Document
import base64

# --- Score values ---
score_map = {
    "Absent (0 points)": 0,
    "Emerging (1 point)": 1,
    "Present (2 points)": 2
}

# --- Screener Items Organized by Subdomain ---
screener_items = {
    "Prewriting & Drawing": [
        "Scribbles or Draws",
        "Pencil Grasp"
    ],
    "Tool Use": [
        "Uses Spoon/Fork",
        "Snips with Scissors",
        "Cuts Playdough or Putty"
    ],
    "Manipulation": [
        "Strings Beads",
        "Turns Lid or Cap",
        "Fastens Zipper",
        "Isolates Finger to Point or Tap"
    ],
    "Construction": [
        "Stacks Blocks"
    ]
}

# --- App Header ---
st.title("Motorin Fine Motor Screener")
st.markdown("Screening tool for fine motor development in children ages 1–7.")

# --- Scoring Form ---
st.header("Screener Items")
user_scores = {}

for domain, items in screener_items.items():
    st.subheader(domain)
    for item in items:
        response = st.radio(
            label=item,
            options=["Absent (0 points)", "Emerging (1 point)", "Present (2 points)"],
            index=None,
            key=item
        )
        if response:
            user_scores[item] = score_map[response]

# --- Results ---
if user_scores:
    total_score = sum(user_scores.values())
    max_score = len(user_scores) * 2
    percent = (total_score / max_score) * 100

    # --- Interpretation ---
    if percent < 50:
        interpretation = "Needs further assessment"
    elif percent < 75:
        interpretation = "May need further assessment"
    else:
        interpretation = "Fine motor skills appear age-appropriate"

    st.markdown("## Results")
    st.markdown(f"**Total Score:** {total_score} / {max_score} ({percent:.1f}%)")
    st.markdown(f"**Interpretation:** {interpretation}")

    # --- Summary Text ---
    summary_text = (
        f"The Motorin screener was used to assess fine motor abilities across domains such as prewriting, tool use, manipulation, and construction. "
        f"The child earned {total_score} out of {max_score} possible points, or {percent:.1f}%. "
        f"This performance falls into the category: **{interpretation}**. "
        f"Consider further evaluation if there are additional developmental concerns."
    )

    st.markdown("## Summary")
    st.write(summary_text)

    # --- Generate Word Report ---
    def generate_word_doc(summary, scores):
        doc = Document()
        doc.add_heading("Motorin Fine Motor Screener Report", 0)
        doc.add_paragraph(summary)
        doc.add_heading("Item Scores", level=1)
        for item, val in scores.items():
            doc.add_paragraph(f"{item}: {val} point(s)")
        byte_stream = BytesIO()
        doc.save(byte_stream)
        return byte_stream.getvalue()

    word_file = generate_word_doc(summary_text, user_scores)
    b64 = base64.b64encode(word_file).decode()
    download_link = f'<a href="data:application/octet-stream;base64,{b64}" download="motorin_screener_report.docx">📄 Download Word Report</a>'
    st.markdown(download_link, unsafe_allow_html=True)

    # --- PDF Placeholder ---
    st.markdown("*PDF export coming soon*")

else:
    st.info("Please complete the screener to view results and generate a report.")
