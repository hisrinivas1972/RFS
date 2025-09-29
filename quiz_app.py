import streamlit as st
import time
from questions import questions

# Paste your questions list here or import from questions.py
questions = [
    # Your 60 questions go here (the ones you provided)
]

# Split questions into sections
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
    st.session_state.answers = {}  # key: (section_idx, question_idx), value: selected option
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

section_names = list(sections.keys())

# If quiz is finished, show summary
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
    st.stop()

# Show current section and question
current_section = section_names[st.session_state.section_index]
current_questions = sections[current_section]
q_idx = st.session_state.question_index
q = current_questions[q_idx]

elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, 60 - elapsed)  # 60 seconds per question

st.title(current_section)
st.markdown(f"Question {q_idx + 1} of 20")
st.write(q['question'])

selected = st.radio("Choose one:", q['options'], key=f"sec{st.session_state.section_index}_q{q_idx}")

if selected:
    # Save answer
    st.session_state.answers[(st.session_state.section_index, q_idx)] = selected

st.info(f"⏳ Time remaining: {remaining} seconds")

# Move to next question automatically when time runs out
if remaining == 0:
    if q_idx < 19:
        st.session_state.question_index += 1
    else:
        # Last question of this section done
        if st.session_state.section_index < 2:
            st.session_state.section_index += 1
            st.session_state.question_index = 0
        else:
            # Quiz finished
            st.session_state.quiz_finished = True
    st.session_state.start_time = time.time()
    st.experimental_rerun()

# Manual Next button
if st.button("Next ➡️"):
    if q_idx < 19:
        st.session_state.question_index += 1
    else:
        if st.session_state.section_index < 2:
            st.session_state.section_index += 1
            st.session_state.question_index = 0
        else:
            st.session_state.quiz_finished = True
    st.session_state.start_time = time.time()
    st.experimental_rerun()
