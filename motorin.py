import streamlit as st

st.set_page_config(page_title="Motorin Screener", layout="centered")

st.title("🧠 Motorin Fine Motor Screener (Ages 1–7)")
st.write("Quick screening tool using a 3-point scale.\n\n**0 = Not Observed**, **1 = Emerging**, **2 = Functional**")

items = {
    "Finger Isolation: Points with index finger": None,
    "Strength: Squeezes soft toy with hand": None,
    "Trunk Tone: Maintains posture in prone suspension": None,
    "Bilateral Coordination: Brings hands together at midline": None
}

desc = {0: "Not Observed", 1: "Emerging", 2: "Functional"}

total = 0
max_score = len(items) * 2
for item in items:
    score = st.radio(item, options=[0, 1, 2], format_func=lambda x: f"{x} – {desc[x]}")
    items[item] = score
    total += score

st.markdown("---")
st.subheader("📊 Screening Summary")
pct = (total / max_score) * 100
st.write(f"**Total Score:** {total} / {max_score} ({pct:.0f}%)")

if pct >= 85:
    st.success("✅ Motor skills appear age-appropriate.")
elif pct >= 60:
    st.warning("⚠️ Emerging motor skills. Monitor or consider follow-up.")
else:
    st.error("❗ Motor concerns noted. Recommend full evaluation.")

