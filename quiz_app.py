import streamlit as st
import time
from questions import questions

# Split questions into sections
verbal = questions[0:20]
numerical = questions[20:40]
analytical = questions[40:60]

sections = {
    "Section A – Verbal Ability": verbal,
    "Section B – Numerical Ability": numerical,
    "Section C – Analytical Ability": analytical
}

# Initialize session state variables
if 'section' not in st.session_state:
    st.session_state.section = list(sections.keys())[0]
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'quiz_over' not in st.session_state:
    st.session_state.quiz_over = False

# Section selection — only at the beginning
if st.session_state.question_index == 0 and not st.session_state.answers:
    st.session_state.section = st.selectbox("Choose Section", list(sections.keys()))

current_questions = sections[st.session_state.section]

# Stop if quiz is over
if st.session_state.quiz_over:
    st.title("✅ Section Completed!")
    st.subheader("Your Answers:")
    for idx, ans in st.session_state.answers.items():
        st.write(f"Q{idx + 1}: {ans}")
    st.stop()

# Timer logic (60s per question)
elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, 60 - elapsed)

# Display current question
q_index = st.session_state.question_index
q = current_questions[q_index]

st.title(st.session_state.section)
st.markdown(f"**Question {q_index + 1} of 20**")
st.write(q['question'])

selected = st.radio("Choose one:", q['options'], key=f"q_{q_index}")
st.write(f"⏳ Time remaining: **{remaining} seconds**")

# Save answer
st.session_state.answers[q_index] = selected

# When timer hits 0 or user clicks "Next", go to next question
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("Next ➡️") or remaining == 0:
        if q_index < 19:
            st.session_state.question_index += 1
            st.session_state.start_time = time.time()
            st.experimental_rerun()
        else:
            st.session_state.quiz_over = True
            st.experimental_rerun()
