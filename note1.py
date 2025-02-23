import streamlit as st
import pdfplumber
from prompts import *
from pages import custom_sidebar, user_dashboard, user_profile
from mistralai import Mistral
from dotenv import load_dotenv
import os
import json
load_dotenv()

api_key = os.getenv('MISTRAL_API_KEY')
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

def get_model_response(prompt, type='json'):
    if type == 'json':
        chat_response = client.chat.complete(
        model= model,
        response_format= {'type':'json_object'},
        messages = [
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ]
    )
        resp = chat_response.choices[0].message.content
        json_resp = json.loads(resp)
        return json_resp
    else:
        chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ]
    )
        resp = chat_response.choices[0].message.content
        return resp

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])



def main_app():

    if st.session_state["dark_mode"]:
        st.markdown("<style>body { background-color: black; color: white; }</style>", unsafe_allow_html=True)
    else:
        st.markdown("<style>body { background-color: white; color: black; }</style>", unsafe_allow_html=True)
    
    # Streamlit UI
    # st.set_page_config(page_title="AI Study Helper", layout="centered")
    st.title("📚 NoteWiz")
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
                prompt = SUMMARY + f"""{pdf_text}"""
                st.session_state["summary"] = get_model_response(prompt, type='not json')

            if st.session_state["selected_section"] == "Quiz" and not st.session_state["quiz"]:
                prompt = QUIZ + f""""{pdf_text} Output: """
                resp = get_model_response(prompt)
                st.session_state["quiz"] = []
                for question_dict in resp['questions']:
                    # print(question_dict)
                    question = question_dict['question']
                    options = {
                            "A": question_dict['A'],
                            "B": question_dict['B'],
                            "C": question_dict['C'],
                            "D": question_dict['D'],
                        }
                    correct_answer = question_dict['correct_option']
                    response = question_dict['response_if_wrong']
                    st.session_state["quiz"].append({"question": question, "options": options, "correct_answer": correct_answer, "response": response})

                # quiz_text = get(f"Generate 5 multiple-choice quiz questions with 4 options (A, B, C, D) and correct answer format 'Answer: A'\n{pdf_text}")
                # quiz_list = quiz_text.split("\n")
                # st.session_state["quiz"] = []
                # for i in range(0, len(quiz_list), 6):  
                #     if i + 5 < len(quiz_list):
                #         question = quiz_list[i]
                #         options = {
                #             "A": quiz_list[i + 1],
                #             "B": quiz_list[i + 2],
                #             "C": quiz_list[i + 3],
                #             "D": quiz_list[i + 4],
                #         }
                #         correct_answer = quiz_list[i + 5].replace("Answer: ", "").strip().upper()
                #         st.session_state["quiz"].append({"question": question, "options": options, "correct_answer": correct_answer})

            if st.session_state["selected_section"] == "Flashcards" and not st.session_state["flashcards"]:
                prompt = FLASHCARD + f"""{pdf_text} Output:"""
                # print(prompt) 
                flashcard_dict = get_model_response(prompt)
                # print(flashcard_dict)
                flashcards_list = [{'question':key, 'answer':value} for key,value in flashcard_dict.items()]
                if len(flashcards_list) % 2 != 0:
                    flashcards_list.append("No answer provided")
                st.session_state["flashcards"] = flashcards_list

            # Display the chosen section
            if st.session_state["selected_section"] == "Summary":
                st.subheader("📌 AI-Generated Summary")
                st.write(st.session_state["summary"])

            elif st.session_state["selected_section"] == "Quiz":
                st.subheader("📝 AI-Generated Quiz Questions")

                if st.session_state["quiz"]:
                    index = st.session_state["current_quiz_index"]
                    quiz_item = st.session_state["quiz"][index]
                    st.markdown(f"### ❓ {st.session_state["quiz"][index]['question']}")
                    
                    for key, value in quiz_item["options"].items():
                        st.markdown(f"**{key}.** {value}")

                    st.session_state["user_quiz_input"] = st.text_input("Enter your answer (A, B, C, or D):").strip().upper()

                    if st.button("✅ Submit Answer"):
                        if st.session_state["user_quiz_input"] == quiz_item["correct_answer"]:
                            st.session_state["quiz_feedback"] = "✅ Correct!"
                        else:
                            st.session_state["quiz_feedback"] = f"❌ \n{quiz_item['response']}. The correct answer is: **{quiz_item['correct_answer']}**"

                    if st.session_state["quiz_feedback"]:
                        st.markdown(st.session_state["quiz_feedback"])

                    if st.button("➡️ Next Question"):
                        if st.session_state["current_quiz_index"] < len(st.session_state["quiz"]) - 1:
                            st.session_state["current_quiz_index"] += 1
                            st.session_state["quiz_feedback"] = ""
                            st.session_state["user_quiz_input"] = ""
                            st.session_state["quiz_progress"] = ((st.session_state["current_quiz_index"] + 1) / len(st.session_state["quiz"])) * 100
                            st.rerun()
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
                            st.rerun()

                    with col2:
                        if st.button("➡️ Next", disabled=index == len(st.session_state["flashcards"]) - 1):
                            st.session_state["current_flashcard_index"] += 1
                            st.session_state["show_answer"] = False  
                            st.session_state["flashcard_progress"] = ((st.session_state["current_flashcard_index"] + 1) / len(st.session_state["flashcards"])) * 100
                            st.rerun()
                else:
                    st.warning("⚠️ No flashcards generated. Try uploading a different PDF.")


def render_pages():

    if st.session_state["page"] == "dashboard":
        user_dashboard()
    elif st.session_state["page"] == "profile":
        user_profile()
    else:
        main_app()
