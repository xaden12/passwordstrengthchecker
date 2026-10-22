import streamlit as st
import string

# Page settings
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Main heading
st.title("🔐 Password Strength Checker")
st.write("Check your password and learn how to make it stronger.")

st.info("Use a sample password for testing. Never enter your actual password.")

# Password input
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter a sample password..."
)

if password:
    # Check all five criteria
    checks = {
        "At least 8 characters": len(password) >= 8,
        "One uppercase letter (A-Z)": any(c.isupper() for c in password),
        "One lowercase letter (a-z)": any(c.islower() for c in password),
        "At least one number (0-9)": any(c.isdigit() for c in password),
        "One special character": any(
            c in string.punctuation for c in password
        )
    }

    # Calculate score
    score = sum(checks.values())

    st.subheader("📊 Password Strength Analysis")

    # Display checklist
    st.write("### Criteria Checklist")

    for criterion, passed in checks.items():
        if passed:
            st.success("✅ " + criterion)
        else:
            st.error("❌ " + criterion)

    # Display score and progress bar
    st.write("### Strength Score")
    st.progress(score / 5)
    st.write(f"**Your score: {score}/5**")

    # Determine strength
    if score <= 2:
        st.error("🔴 Weak Password")
    elif score <= 4:
        st.warning("🟠 Moderate Password")
    else:
        st.success("🟢 Strong Password")

    # Suggestions
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(c.islower() for c in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include at least one number.")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Include at least one special character.")

    st.subheader("💡 Suggestions for Improvement")

    if suggestions:
        for suggestion in suggestions:
            st.write("- " + suggestion)
    else:
        st.success("Excellent! All five criteria are satisfied.")

else:
    st.caption("Enter a sample password above to begin the analysis.")
