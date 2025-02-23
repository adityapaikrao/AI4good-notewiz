import streamlit as st
from note1 import main_app

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
        main_app()
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
