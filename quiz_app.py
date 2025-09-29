import streamlit as st
import time
from questions import questions  # Make sure your questions list is imported correctly

# Define sections with slices of questions (adjust slices as per your questions list)
sections = {
    "Section A – Verbal Ability": questions[0:20],
    "Section B – Numerical Ability": questions[20:40],
    "Section C – Analytical Ability": questions[40:60]
}

# Initialize session state variables
if "section_index" not in st.session_state:
    st.session_state.section_index = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

section_names = list(sections.keys())

# If quiz finished, show results and restart option
if st.session_state.quiz_finished:
    st.title("🎉 Quiz Completed!")
    total_correct = 0
    total_questions = 0

    for sec_i, sec_name in enumerate(section_names):
        st.header(sec_name)
        for q_i, q in enumerate(sections[sec_name]):
            total_questions += 1
            key = (sec_i, q_i)
            selected = st.session_state.answers.get(key, None)
            correct = (selected == q['answer'])
            if correct:
                total_correct += 1
            st.write(f"Q{q_i+1}: {q['question']}")
            st.write(f"Your answer: {selected}")
            st.write(f"Correct answer: {q['answer']}")
            st.write(f"{'✅ Correct' if correct else '❌ Incorrect'}")
            st.markdown("---")

    st.subheader(f"Your Score: {total_correct} / {total_questions}")

    if st.button("Restart Quiz"):
        for key in ["section_index", "question_index", "start_time", "answers", "quiz_finished"]:
            if key in st.session_state:
                del st.session_state[key]
        try:
            st.experimental_rerun()
        except AttributeError:
            pass
    st.stop()

# Get current section and questions
current_section = section_names[st.session_state.section_index]
current_questions = sections[current_section]

# Ensure question index in valid range
q_idx = st.session_state.question_index
max_index = len(current_questions) - 1

if q_idx < 0:
    q_idx = 0
elif q_idx > max_index:
    q_idx = max_index
st.session_state.question_index = q_idx

q = current_questions[q_idx]

# Timer: 60 seconds per question
elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, 60 - elapsed)

# Display section and question
st.title(current_section)
st.markdown(f"Question {q_idx + 1} of {len(current_questions)}")
st.write(q['question'])

# Radio options with unique key
selected = st.radio("Choose one:", q['options'], key=f"sec{st.session_state.section_index}_q{q_idx}")

# Save selected answer
if selected:
    st.session_state.answers[(st.session_state.section_index, q_idx)] = selected

# Show remaining time
st.info(f"⏳ Time remaining: {remaining} seconds")

rerun_called = False

# Navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Previous"):
        if q_idx > 0:
            st.session_state.question_index -= 1
        elif st.session_state.section_index > 0:
            st.session_state.section_index -= 1
            prev_section = section_names[st.session_state.section_index]
            st.session_state.question_index = len(sections[prev_section]) - 1
        st.session_state.start_time = time.time()
        rerun_called = True

with col3:
    if st.button("Next ➡️"):
        if q_idx < max_index:
            st.session_state.question_index += 1
        else:
            if st.session_state.section_index < len(section_names) - 1:
                st.session_state.section_index += 1
                st.session_state.question_index = 0
            else:
                st.session_state.quiz_finished = True
        st.session_state.start_time = time.time()
        rerun_called = True

# Auto move to next question when timer ends
if remaining == 0:
    if q_idx < max_index:
        st.session_state.question_index += 1
    else:
        if st.session_state.section_index < len(section_names) - 1:
            st.session_state.section_index += 1
            st.session_state.question_index = 0
        else:
            st.session_state.quiz_finished = True
    st.session_state.start_time = time.time()
    rerun_called = True

# Rerun app if needed
if rerun_called:
    try:
        st.experimental_rerun()
    except AttributeError:
        pass
