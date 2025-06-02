



import streamlit as st
import json

# Load the JSON file    u
with open('PGCET2016_Questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Streamlit UI setup
st.set_page_config(page_title="Quiz App", layout="centered")
st.title("🧠 Quiz - PGCET Prep")
st.markdown("Test your knowledge on C programming for the PGCET exam.")

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(questions)
if "selections" not in st.session_state:
    st.session_state.selections = [None] * len(questions)

# Quiz rendering
st.markdown("---")
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    user_ans = st.radio(
        "Choose one:", 
        q["options"], 
        key=f"q{i}", 
        index=st.session_state.selections[i] if st.session_state.selections[i] is not None else 0
    )

    if not st.session_state.answered[i]:
        if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
            selected_index = q["options"].index(user_ans)
            correct_index = q["answer"]
            st.session_state.selections[i] = selected_index
            if selected_index == correct_index:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! You chose '{user_ans}'\n\n✅ Correct answer: '{q['options'][correct_index]}'")
            st.session_state.answered[i] = True
    else:
        selected_index = st.session_state.selections[i]
        st.info("Already answered.")
        st.write(f"Your Answer: **{q['options'][selected_index]}**")
        st.write(f"Correct Answer: **{q['options'][q['answer']]}**")

    st.markdown("---")

# Show score
st.write(f"### Final Score: {st.session_state.score} / {len(questions)}")


