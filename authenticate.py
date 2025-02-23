import streamlit as st

# Function to display the login form
def login_form():
    st.subheader("Login", anchor="login")
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type='password', placeholder="Enter your password")
    
    if st.button("Login"):
        # Simulate a login action
        if username and password:
            # we will call the main page here
            # note1_main()
            st.success("Logged in successfully!")

        else:
            st.error("Please enter both username and password.")

# Function to display the registration form
def registration_form():
    st.subheader("Register", anchor="register")
    new_username = st.text_input("New Username", placeholder="Choose a username")
    new_password = st.text_input("New Password", type='password', placeholder="Choose a password")
    
    if st.button("Register"):
        # Simulate a registration action
        if new_username and new_password:
            st.success("Registered successfully! You can now log in.")
        else:
            st.error("Please enter both username and password.")

# Main function to control the flow of the app
def main():
    st.set_page_config(page_title="NoteWiz Authentication", page_icon="🔒", layout="centered")
    
    # Add a title and some styling
    st.markdown("<h1 class='title'>NoteWiz</h1>", unsafe_allow_html=True)
    st.markdown("<h5 class='login-message'>Please log in to continue</h5>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            color: #4B0082;
            font-size: 2.5em;
            font-weight: bold;
        }
        .login-message {
            text-align: center;
            color: #6A5ACD;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .subheader {
            text-align: center;
            color: #4B0082;
            font-size: 1.5em;
        }
        .button {
            background-color: #4B0082;
            color: white;
            border: None;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #6A5ACD;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Create a radio button for selecting login or registration
    option = st.radio("Select an option:", ("Login", "Register"), index=0, label_visibility="collapsed")
    
    if option == "Login":
        login_form()
    else:
        registration_form()

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    # st.markdown("Made with ❤️ by The Guardians of ", unsafe_allow_html=True)

if __name__ == "__main__":
    main()