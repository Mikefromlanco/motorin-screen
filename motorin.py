}

item_number = 1
scores = {}

for age_range, items in items_by_age.items():
    st.markdown(f"<hr><h4>{age_range}</h4>", unsafe_allow_html=True)
    for item in items:
        score = st.radio(f"{item_number}. {item}", list(score_options.keys()), horizontal=True, key=f"item_{item_number}")
        scores[f"{age_range} - {item_number}. {item}"] = score_options[score]
        item_number += 1

st.markdown("---")

# ---- AGE EQUIVALENCY CALCULATION ----
st.header("Summary & Age Equivalency")

age_midpoints = {
    "1–2 Years": 18,
    "2–3 Years": 30,
    "3–4 Years": 42,
    "4–5 Years": 54,
    "5–6 Years": 66,
    "6–7 Years": 78
}

total_points = 0
valid_items = 0

for item_label, score in scores.items():
    for age_range, midpoint in age_midpoints.items():
        if age_range in item_label:
            anchor_age = midpoint
            break
    else:
        anchor_age = 0

    if score == 1:
        total_points += 0.5 * anchor_age
        valid_items += 1
    elif score == 2:
        total_points += anchor_age
        valid_items += 1

if valid_items > 0:
    avg_months = total_points / valid_items
    ae_years = int(avg_months // 12)
    ae_months = int(avg_months % 12)
    st.subheader(f"🧠 Fine Motor Age Equivalency: {ae_years} years, {ae_months} months")

    if dob:
        ca_months = (date_of_screen - dob).days // 30
        gap = ca_months - avg_months

        if gap <= 0:
            recommendation = "✅ Age-appropriate fine motor skills"
        elif gap <= 6:
            recommendation = "⚠️ Mild delay – Monitor"
        else:
            recommendation = "❌ Delay – Further evaluation recommended"
        st.markdown(f"**Clinical Impression:** {recommendation}")
else:
    st.warning("Insufficient data to calculate age equivalency.")
