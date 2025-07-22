import streamlit as st
from io import BytesIO
import base64

# Try importing docx safely
try:
    from docx import Document
    docx_available = True
except ImportError:
    docx_available = False

# Score map for radio buttons
score_map = {
    "Absent (0 points)": 0,
    "Emerging (1 point)": 1,
    "Present (2 points)": 2
}

# Screener items grouped by developmental domain
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

# Streamlit app UI
st.set_page_config(page_title="Motorin Screener", layout="centered")
st.title("Motorin Fine Motor Screener")
st.markdown("Use this tool to screen fine motor development in children ages 1–7.")

st.header("Screener Items")
user_scores = {}

# Render radio buttons for each item
for domain, items in screener_items.items():
    st.subheader(domain)
    for item in items:
        choice = st.radio(
            label=item,
            options=["Absent (0 points)", "Emerging (1 point)", "Present (2 points)"],
            index=None,
            key=item
        )
        if choice:
            user_scores[item] = score_map[choice]

# Results summary after scoring
if user_scores:
    total = sum(user_scores.values())
    max_score = len(user_scores) * 2
    percent = (total / max_score) * 100

    # Interpretation
    if percent < 50:
        result = "Needs further assessment"
    elif percent < 75:
        result = "May need further assessment"
    else:
        result = "Fine motor skills appear age-appropriate"

    # Display results
    st.markdown("## Results")
    st.markdown(f"**Total Score:** {total} / {max_score} ({percent:.1f}%)")
    st.markdown(f"**Interpretation:** {result}")

    # Summary paragraph
    summary = (
        f"The Motorin screener was completed to assess fine motor abilities across several developmental areas. "
        f"The child earned {total} out of {max_score} possible points ({percent:.1f}%), which falls into the category: "
        f"**{result}**. Additional assessment may be warranted depending on clinical judgment or developmental concerns."
    )

    st.markdown("## Summary")
    st.write(summary)

    # Word report generation if python-docx is installed
    if docx_available:
        def create_word_doc(summary, scores):
            doc = Document()
            doc.add_heading("Motorin Screener Report", 0)
            doc.add_paragraph(summary)
            doc.add_heading("Item Scores", level=1)
            for item, score in scores.items():
                doc.add_paragraph(f"{item}: {score} point(s)")
            buffer = BytesIO()
            doc.save(buffer)
            return buffer.getvalue()

        word_bytes = create_word_doc(summary, user_scores)
        b64 = base64.b64encode(word_bytes).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="motorin_screener_report.docx">📄 Download Word Report</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("To enable Word report download, please install `python-docx`.")

    # PDF placeholder
    st.markdown("*PDF export coming soon.*")

else:
    st.info("Please score at least one item to see results and generate a report.")
