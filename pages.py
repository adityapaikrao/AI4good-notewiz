import streamlit as st

def user_dashboard():
    st.title("📊 User Dashboard")
    st.subheader("Your Study Progress")
    st.progress(st.session_state["progress"] / 100)
    st.write(f"Progress: {st.session_state['progress']}%")
    if st.button("🔙 Back to Study Helper"):
        st.session_state["page"] = "main"

# User Profile Page
def user_profile():
    st.title("👤 User Profile")
    if st.button("🔄 Change Username/Password"):
        st.write("Feature to change username/password coming soon!")
    if st.button("🔙 Back"):
        st.session_state["page"] = "main"

# Sidebar Customization
def custom_sidebar():
    st.sidebar.markdown("<style>.css-1d391kg {width: 200px !important;}</style>", unsafe_allow_html=True)
    if st.sidebar.button("👤 User Profile"):
        st.session_state["page"] = "profile"
    
    with st.sidebar.expander("📊 Progress Tracker"):
        st.write("📖 Flashcards Progress")
        st.progress(st.session_state["flashcard_progress"] / 100)
        st.write(f"Flashcards Progress: {st.session_state['flashcard_progress']}%")
        
        st.write("📝 Quiz Progress")
        st.progress(st.session_state["quiz_progress"] / 100)
        st.write(f"Quiz Progress: {st.session_state['quiz_progress']}%")
    
    with st.sidebar.expander("🏆 Leaderboard"):
        leaderboard_data = {
            "User": ["Aditya", "Nikhil", "Kanika", "Ebube", "Mint"],
            "Points": [50, 45, 45, 40, 40]
        }
        st.table(leaderboard_data)
