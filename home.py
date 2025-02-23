import streamlit as st
from note1 import render_pages
from pages import *

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
if "page" not in st.session_state:
    st.session_state['page'] = "main"
# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "main"
if "summary" not in st.session_state:
    st.session_state["summary"] = None
if "quiz" not in st.session_state:
    st.session_state["quiz"] = []
if "flashcards" not in st.session_state:
    st.session_state["flashcards"] = []
if "progress" not in st.session_state:
    st.session_state["progress"] = 0  # Overall Progress tracker (0 to 100)
if "flashcard_progress" not in st.session_state:
    st.session_state["flashcard_progress"] = 0
if "quiz_progress" not in st.session_state:
    st.session_state["quiz_progress"] = 0
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False


# Function to display the login form
def login_form():
    st.subheader("Login", anchor="login")
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type='password', placeholder="Enter your password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True  # Set login state
            st.rerun()
  # Refresh the app to reflect changes
        else:
            st.error("Please enter both username and password.")

# Function to display the registration form
def registration_form():
    st.subheader("Register", anchor="register")
    new_username = st.text_input("New Username", placeholder="Choose a username")
    new_password = st.text_input("New Password", type='password', placeholder="Choose a password")

    if st.button("Register"):
        if new_username and new_password:
            st.success("Registered successfully! You can now log in.")
        else:
            st.error("Please enter both username and password.")

# Main function
def main():
    st.set_page_config(page_title="NoteWiz Authentication", page_icon="🔒", layout="centered")

    # If logged in, show main app
    if st.session_state.logged_in:
        custom_sidebar()
        render_pages()
        return  # Prevent further execution of login/register UI

    # Otherwise, show login/register UI
    st.markdown("<h1 class='title'>NoteWiz</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='login-message'>Please log in to continue</h5>", unsafe_allow_html=True)

    # Styling
    st.markdown(
        """
        <style>
        .title { text-align: center; color: #4B0082; font-size: 2.5em; font-weight: bold; }
        .login-message { text-align: center; color: #6A5ACD; font-size: 1.2em; margin-bottom: 20px; }
        .subheader { text-align: center; color: #4B0082; font-size: 1.5em; }
        .button { background-color: #4B0082; color: white; border: None; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
        .button:hover { background-color: #6A5ACD; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Login/Register selection
    option = st.radio("Select an option:", ("Login", "Register"), index=0, label_visibility="collapsed")

    if option == "Login":
        login_form()
    else:
        registration_form()

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
