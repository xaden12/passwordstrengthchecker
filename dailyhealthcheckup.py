
import streamlit as st

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------
st.set_page_config(
    page_title="Daily Health Checker",
    page_icon="🏥",
    layout="centered"
)

# ----------------------------------
# APPLICATION TITLE
# ----------------------------------
st.title("🏥 Daily Health Checker")
st.subheader("Your Personal Daily Wellness Assistant")
st.write(
    "Enter your daily health details below to check "
    "your lifestyle and receive personalized suggestions."
)

st.divider()

# ----------------------------------
# RESET FUNCTION
# ----------------------------------
def reset_inputs():
    st.session_state.name = ""
    st.session_state.age = 18
    st.session_state.sleep = 8.0
    st.session_state.water = 8
    st.session_state.exercise = 30
    st.session_state.screen = 3.0
    st.session_state.mood = "Happy"

# ----------------------------------
# USER INPUT SECTION
# ----------------------------------
st.header("📝 Enter Your Daily Health Details")

name = st.text_input(
    "Enter your Name",
    key="name",
    placeholder="Your name"
)

age = st.number_input(
    "Enter your Age",
    min_value=1,
    max_value=120,
    value=18,
    key="age"
)

sleep = st.number_input(
    "Hours of Sleep",
    min_value=0.0,
    max_value=24.0,
    value=8.0,
    step=0.5,
    key="sleep"
)

water = st.number_input(
    "Glasses of Water Consumed",
    min_value=0,
    max_value=30,
    value=8,
    key="water"
)

exercise = st.number_input(
    "Daily Exercise Duration (minutes)",
    min_value=0,
    max_value=600,
    value=30,
    key="exercise"
)

screen = st.number_input(
    "Daily Screen Time (hours)",
    min_value=0.0,
    max_value=24.0,
    value=3.0,
    step=0.5,
    key="screen"
)

mood = st.selectbox(
    "How is your Mood Today?",
    ["Happy", "Sad", "Stressed", "Energetic"],
    key="mood"
)

st.divider()

# ----------------------------------
# WELLNESS ANALYSIS BUTTON
# ----------------------------------
if st.button("🔍 Check My Daily Health", type="primary"):

    if name.strip() == "":
        st.error("Please enter your name first!")

    else:
        # ----------------------------------
        # WELLNESS SCORE CALCULATION
        # ----------------------------------

        score = 0

        # Sleep score (25 points)
        if 7 <= sleep <= 9:
            score += 25
        elif 6 <= sleep < 7 or 9 < sleep <= 10:
            score += 15
        else:
            score += 5

        # Water score (20 points)
        if water >= 8:
            score += 20
        elif water >= 5:
            score += 12
        else:
            score += 5

        # Exercise score (25 points)
        if exercise >= 30:
            score += 25
        elif exercise >= 15:
            score += 15
        else:
            score += 5

        # Screen time score (15 points)
        if screen <= 2:
            score += 15
        elif screen <= 4:
            score += 10
        elif screen <= 6:
            score += 5
        else:
            score += 0

        # Mood score (15 points)
        if mood == "Happy" or mood == "Energetic":
            score += 15
        elif mood == "Sad":
            score += 8
        else:
            score += 10

        # ----------------------------------
        # DISPLAY HEALTH SUMMARY
        # ----------------------------------
        st.divider()
        st.header("📊 Your Daily Health Report")

        st.success(f"Hello {name}! Here is your health report.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Age", f"{age} years")
            st.metric("Sleep", f"{sleep} hours")
            st.metric("Water", f"{water} glasses")

        with col2:
            st.metric("Exercise", f"{exercise} minutes")
            st.metric("Screen Time", f"{screen} hours")
            st.metric("Mood", mood)

        # ----------------------------------
        # DISPLAY WELLNESS SCORE
        # ----------------------------------
        st.subheader("⭐ Daily Wellness Score")

        st.progress(score / 100)
        st.metric("Your Wellness Score", f"{score}/100")

        if score >= 80:
            st.success("Excellent! You have healthy daily habits. Keep it up!")
        elif score >= 60:
            st.info("Good job! There is still some room for improvement.")
        elif score >= 40:
            st.warning("Your lifestyle needs some improvement. Start with small changes.")
        else:
            st.error("Your wellness habits need attention. Try to build a healthier routine.")

        # ----------------------------------
        # PERSONALIZED FEEDBACK
        # ----------------------------------
        st.divider()
        st.header("💡 Personalized Health Feedback")

        recommendations = []

        # Sleep analysis
        if sleep < 7:
            recommendations.append(
                "😴 Try to get more sleep and maintain a regular sleep schedule."
            )
        elif sleep > 9:
            recommendations.append(
                "😴 Your sleep duration is above the usual adult recommendation. "
                "Monitor your sleep quality and energy levels."
            )
        else:
            recommendations.append(
                "✅ Your sleep duration is within the recommended adult range."
            )

        # Water analysis
        if water < 8:
            recommendations.append(
                "💧 Remember to drink water regularly throughout the day."
            )
        else:
            recommendations.append(
                "✅ Good job staying hydrated! Adjust your fluid intake "
                "according to your activity and needs."
            )

        # Exercise analysis
        if exercise < 30:
            recommendations.append(
                "🏃 Try to include more physical activity in your daily routine."
            )
        else:
            recommendations.append(
                "✅ Great work! You are maintaining an active lifestyle."
            )

        # Screen time analysis
        if screen > 4:
            recommendations.append(
                "📱 Reduce unnecessary screen time and take regular screen breaks."
            )
        else:
            recommendations.append(
                "✅ Your reported screen time is relatively low."
            )

        # Mood analysis
        if mood == "Happy":
            recommendations.append(
                "😊 Keep doing activities that make you happy."
            )
        elif mood == "Energetic":
            recommendations.append(
                "⚡ Great energy! Use it for productive and healthy activities."
            )
        elif mood == "Sad":
            recommendations.append(
                "💚 Take time for yourself, connect with someone you trust, "
                "and consider seeking support if sadness continues."
            )
        elif mood == "Stressed":
            recommendations.append(
                "🧘 Try relaxation, deep breathing, meditation, or a short walk."
            )

        # Display recommendations
        st.subheader("Your Health Recommendations")

        for recommendation in recommendations:
            st.write(recommendation)

        # ----------------------------------
        # FINAL MESSAGE
        # ----------------------------------
        st.divider()
        st.header("🌟 Final Health Message")

        if score >= 80:
            st.balloons()
            st.success(
                f"Congratulations {name}! You are doing great. "
                "Continue maintaining your healthy habits!"
            )
        else:
            st.info(
                f"Keep going {name}! Small healthy changes every day "
                "can make a big difference."
            )

        st.caption(
            "Note: This app provides general lifestyle feedback, "
            "not a medical diagnosis."
        )

# ----------------------------------
# RESET BUTTON
# ----------------------------------
st.divider()

st.button(
    "🔄 Reset / Clear All Inputs",
    on_click=reset_inputs
)

# ----------------------------------
# FOOTER
# ----------------------------------
st.divider()
st.caption("Daily Health Checker App | Created using Python & Streamlit")
st.caption("Stay Healthy • Stay Active • Stay Happy ❤️")

