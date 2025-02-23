import streamlit as st
import pdfplumber
import subprocess
import random

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Function to query Mistral via Ollama
def generate_ai_content(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

# Initialize session state
if "summary" not in st.session_state:
    st.session_state["summary"] = None
if "quiz" not in st.session_state:
    st.session_state["quiz"] = []
if "flashcards" not in st.session_state:
    st.session_state["flashcards"] = []
if "selected_section" not in st.session_state:
    st.session_state["selected_section"] = None
if "current_flashcard_index" not in st.session_state:
    st.session_state["current_flashcard_index"] = 0
if "show_answer" not in st.session_state:
    st.session_state["show_answer"] = False
if "current_quiz_index" not in st.session_state:
    st.session_state["current_quiz_index"] = 0
if "user_quiz_input" not in st.session_state:
    st.session_state["user_quiz_input"] = ""
if "quiz_feedback" not in st.session_state:
    st.session_state["quiz_feedback"] = ""

# Streamlit UI
st.set_page_config(page_title="AI Study Helper", layout="centered")
st.title("📚 AI Study Helper (Mistral)")
st.write("Upload a PDF to generate **Summaries, Quiz Questions, and Flashcards!**")

# Upload PDF
uploaded_file = st.file_uploader("📂 Choose a PDF file", type="pdf")

if uploaded_file:
    st.success("✅ PDF Uploaded Successfully!")
    pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text and pdf_text != st.session_state.get("current_pdf_text"):
        st.session_state["current_pdf_text"] = pdf_text
        st.session_state["summary"] = None
        st.session_state["quiz"] = []
        st.session_state["flashcards"] = []
        st.session_state["selected_section"] = None

    if pdf_text:
        st.markdown("### Select an Option Below:")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📌 Summary"):
                st.session_state["selected_section"] = "Summary"
        with col2:
            if st.button("📝 Quiz"):
                st.session_state["selected_section"] = "Quiz"
        with col3:
            if st.button("📖 Flashcards"):
                st.session_state["selected_section"] = "Flashcards"

        # Generate responses when needed
        if st.session_state["selected_section"] == "Summary" and st.session_state["summary"] is None:
            st.session_state["summary"] = generate_ai_content(f"Summarize this:\n{pdf_text}")

        if st.session_state["selected_section"] == "Quiz" and not st.session_state["quiz"]:
            quiz_text = generate_ai_content(f"Generate 5 multiple-choice quiz questions with 4 options (A, B, C, D) and correct answer format 'Answer: A'\n{pdf_text}")
            quiz_list = quiz_text.split("\n")
            st.session_state["quiz"] = []
            for i in range(0, len(quiz_list), 6):  
                if i + 5 < len(quiz_list):
                    question = quiz_list[i]
                    options = {
                        "A": quiz_list[i + 1],
                        "B": quiz_list[i + 2],
                        "C": quiz_list[i + 3],
                        "D": quiz_list[i + 4],
                    }
                    correct_answer = quiz_list[i + 5].replace("Answer: ", "").strip().upper()
                    st.session_state["quiz"].append({"question": question, "options": options, "correct_answer": correct_answer})

        if st.session_state["selected_section"] == "Flashcards" and not st.session_state["flashcards"]:
            flashcards_text = generate_ai_content(f"Create flashcards from this text:\n{pdf_text}")
            flashcards_list = flashcards_text.split("\n")
            if len(flashcards_list) % 2 != 0:
                flashcards_list.append("No answer provided")
            st.session_state["flashcards"] = [
                {"question": flashcards_list[i], "answer": flashcards_list[i + 1]}
                for i in range(0, len(flashcards_list), 2)
            ]

        # Display the chosen section
        if st.session_state["selected_section"] == "Summary":
            st.subheader("📌 AI-Generated Summary")
            st.write(st.session_state["summary"])

        elif st.session_state["selected_section"] == "Quiz":
            st.subheader("📝 AI-Generated Quiz Questions")

            if st.session_state["quiz"]:
                index = st.session_state["current_quiz_index"]
                quiz_item = st.session_state["quiz"][index]
                st.markdown(f"### ❓ {quiz_item['question']}")
                
                for key, value in quiz_item["options"].items():
                    st.markdown(f"**{key}.** {value}")

                st.session_state["user_quiz_input"] = st.text_input("Enter your answer (A, B, C, or D):").strip().upper()

                if st.button("✅ Submit Answer"):
                    if st.session_state["user_quiz_input"] == quiz_item["correct_answer"]:
                        st.session_state["quiz_feedback"] = "✅ Correct!"
                    else:
                        st.session_state["quiz_feedback"] = f"❌ Incorrect! The correct answer is: **{quiz_item['correct_answer']}**"

                if st.session_state["quiz_feedback"]:
                    st.markdown(st.session_state["quiz_feedback"])

                if st.button("➡️ Next Question"):
                    if st.session_state["current_quiz_index"] < len(st.session_state["quiz"]) - 1:
                        st.session_state["current_quiz_index"] += 1
                        st.session_state["quiz_feedback"] = ""
                        st.session_state["user_quiz_input"] = ""
                    else:
                        st.success("🎉 You've completed all questions!")

        elif st.session_state["selected_section"] == "Flashcards":
            st.subheader("📖 AI-Generated Flashcards")

            if st.session_state["flashcards"]:
                index = st.session_state["current_flashcard_index"]
                flashcard = st.session_state["flashcards"][index]

                st.markdown(f"### ❓ {flashcard['question']}")
                
                if st.button("🔄 Flip Flashcard"):
                    st.session_state["show_answer"] = not st.session_state["show_answer"]

                if st.session_state["show_answer"]:
                    st.markdown(f"### 🏆 Answer: {flashcard['answer']}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⬅️ Previous", disabled=index == 0):
                        st.session_state["current_flashcard_index"] -= 1
                        st.session_state["show_answer"] = False  

                with col2:
                    if st.button("➡️ Next", disabled=index == len(st.session_state["flashcards"]) - 1):
                        st.session_state["current_flashcard_index"] += 1
                        st.session_state["show_answer"] = False  
            else:
                st.warning("⚠️ No flashcards generated. Try uploading a different PDF.")

