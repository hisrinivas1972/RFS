import streamlit as st
import time
from questions import questions

# Constants
TOTAL_QUESTIONS = len(questions)
TIME_PER_QUESTION = 60  # seconds

# Session State Setup
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Timer logic
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = TOTAL_QUESTIONS * TIME_PER_QUESTION - elapsed_time

st.title("🧠 1-Hour Multiple Choice Quiz")
st.markdown(f"**⏳ Time Left:** {remaining_time // 60}:{remaining_time % 60:02d} mins")

if remaining_time <= 0:
    st.warning("⏰ Time's up!")
    st.success(f"✅ Final Score: {st.session_state.score}/{TOTAL_QUESTIONS}")
    st.stop()

# Display current question
q = questions[st.session_state.q_index]
st.markdown(f"**Q{st.session_state.q_index + 1}.** {q['question']}")
user_answer = st.radio("Select an option:", q['options'], key=st.session_state.q_index)

if st.button("Next"):
    if user_answer == q['answer']:
        st.session_state.score += 1
    st.session_state.q_index += 1
    if st.session_state.q_index >= TOTAL_QUESTIONS:
        st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.score}/{TOTAL_QUESTIONS}")
        st.stop()
    st.rerun()
