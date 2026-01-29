import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Decision-Making Copilot",
    layout="centered"
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1>🧠 Decision-Making Copilot</h1>
    <p style="color:#6b7280;">
    For introverts & early professionals — think before you speak.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- Scenario Presets ----------------
st.markdown("### Quick scenarios (optional)")
preset = st.selectbox(
    "",
    [
        "— Select a common situation —",
        "First day at work, unsure what to say",
        "Manager set an unrealistic deadline",
        "Need to push back politely",
        "Disagree with a senior colleague",
        "Asking for clarity without sounding dumb"
    ]
)

preset_map = {
    "First day at work, unsure what to say":
        "Today is my first day and there was no formal introduction. What should I say?",
    "Manager set an unrealistic deadline":
        "My manager has set a very urgent and unrealistic deadline. I’m not sure how to push back.",
    "Need to push back politely":
        "I disagree with the decision but don’t want to sound confrontational.",
    "Disagree with a senior colleague":
        "I think there’s a flaw in the plan proposed by a senior colleague.",
    "Asking for clarity without sounding dumb":
        "I don’t fully understand the task but I’m afraid of asking."
}

# ---------------- Input ----------------
st.markdown("### What situation are you stuck in?")
situation = st.text_area(
    "",
    value=preset_map.get(preset, ""),
    placeholder="Describe your situation in your own words…",
    height=120
)

tone = st.selectbox(
    "Preferred communication style",
    ["Calm & respectful", "Assertive but polite", "Logical & structured"]
)

# ---------------- Action ----------------
if st.button("Craft a response"):
    if situation.strip() == "":
        st.warning("Please describe your situation first.")
    else:
        st.divider()

        # ---------------- Chat Bubble: User ----------------
        st.markdown(
            f"""
            <div style="background:#f1f5f9; padding:14px; border-radius:12px; margin-bottom:10px;">
            <strong>You</strong><br>
            {situation}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- How to Think ----------------
        st.markdown(
            """
            <div style="background:#fff7ed; padding:16px; border-radius:12px; margin-bottom:12px;">
            <strong>🧩 How to think about this</strong>
            <ul>
                <li>Assume positive intent — not pressure or judgment.</li>
                <li>Separate facts from emotions.</li>
                <li>Your goal is alignment, not winning.</li>
                <li>Clarity > cleverness.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- Chat Bubble: Copilot ----------------
        st.markdown(
            f"""
            <div style="background:#eef2ff; padding:16px; border-radius:12px;">
            <strong>🤖 Copilot ({tone})</strong><br><br>
            “I want to make sure I approach this the right way.
            Based on my current understanding, I see a potential risk here.
            Could we align on priorities or expectations so I can move forward confidently?”
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            "This copilot helps you think clearly before you speak — not tell you what to do."
        )

st.divider()
st.caption("Built by Shreya • Product thinking × AI")
