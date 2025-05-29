import streamlit as st
from app.wiki_fetcher import fetch_summary
from app.generator import generate_questions
from app.utils import categorize_difficulty

st.title("🎓 Exam Question Generator")

topic = st.text_input("Enter a topic (e.g., Photosynthesis, Newton's Laws):")
question_type = st.selectbox("Question type:", ["mcq", "descriptive"])
difficulty_level = st.slider("Select difficulty level (1: Easy, 10: Hard)", 1, 10, 5)

if st.button("Generate Questions"):
    with st.spinner("Fetching content and generating questions..."):
        summary = fetch_summary(topic)
        difficulty = categorize_difficulty(difficulty_level)
        questions = generate_questions(summary, question_type, difficulty)
        
        st.subheader("Generated Questions")
        st.markdown(questions)
