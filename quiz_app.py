import streamlit as st
import time
from questions import questions

# Split questions by section
verbal = questions[0:20]
numerical = questions[20:40]
analytical = questions[40:60]

sections = {
    "Section A – Verbal Ability": verbal,
    "Section B – Numerical Ability": numerical,
    "Section C – Analytical Ability": analytical
}

# Initialize session state
if 'section' not in st.session_state:
    st.session_state.section = list(sections.keys())[0]

if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Sidebar for section selection (only if question_index is 0)
if st.session_state.question_index == 0:
    st.session_state.section = st.selectbox("Choose Section", list(sections.keys()))

# Get questions of current section
current_questions = sections[st.session_state.section]

# Show current question
q = current_questions[st.session_state.question_index]
st.markdown(f"### Question {st.session_state.question_index + 1}")
st.write(q['question'])
selected = st.radio("Choose one:", q['options'], key=st.session_state.question_index)

# Save answer
st.session_state.answers[st.session_state.question_index] = selected

# Timer logic (60 seconds per question)
elapsed = int(time.time() - st.session_state.start_time)
remaining = 60 - elapsed
if remaining > 0:
    st.info(f"⏳ Time Remaining: {remaining} seconds")
    time.sleep(1)
    st.experimental_rerun()
else:
    # Move to next question
    if st.session_state.question_index < 19:
        st.session_state.question_index += 1
        st.session_state.start_time = time.time()
        st.experimental_rerun()
    else:
        st.success("✅ Section completed!")
        st.write("Your Answers:")
        for idx, ans in st.session_state.answers.items():
            st.write(f"Q{idx+1}: {ans}")
