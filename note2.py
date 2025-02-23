# import streamlit as st
# import pdfplumber
# import subprocess
# import random

# # Ensure required modules are installed
# try:
#     import streamlit as st
#     import pdfplumber
# except ModuleNotFoundError:
#     st.error("Missing required modules. Please install them using 'pip install streamlit pdfplumber'.")

# # Function to extract text from PDF
# def extract_text_from_pdf(uploaded_file):
#     with pdfplumber.open(uploaded_file) as pdf:
#         return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# # Function to query Mistral via Ollama
# def generate_ai_content(prompt):
#     try:
#         result = subprocess.run(
#             ["ollama", "run", "mistral", prompt],
#             capture_output=True,
#             text=True
#         )
#         return result.stdout.strip()
#     except Exception as e:
#         return f"Error: {e}"

# # Initialize session state
# if "page" not in st.session_state:
#     st.session_state["page"] = "main"
# if "summary" not in st.session_state:
#     st.session_state["summary"] = None
# if "quiz" not in st.session_state:
#     st.session_state["quiz"] = []
# if "flashcards" not in st.session_state:
#     st.session_state["flashcards"] = []
# if "progress" not in st.session_state:
#     st.session_state["progress"] = 0  # Progress tracker (0 to 100)

# # User Dashboard Page
# def user_dashboard():
#     st.title("📊 User Dashboard")
#     st.subheader("Your Study Progress")
#     st.progress(st.session_state["progress"] / 100)
#     st.write(f"Progress: {st.session_state['progress']}%")
#     if st.button("🔙 Back to Study Helper"):
#         st.session_state["page"] = "main"

# # Main Page
# def main_page():
#     st.sidebar.button("👤 User Profile", on_click=lambda: st.session_state.update({"page": "dashboard"}))
#     st.title("NoteWiz 📚")
#     st.write("Upload a PDF to generate **Summaries, Quiz Questions, and Flashcards!**")
#     uploaded_file = st.file_uploader("📂 Choose a PDF file", type="pdf")

#     if uploaded_file:
#         st.success("✅ PDF Uploaded Successfully!")
#         pdf_text = extract_text_from_pdf(uploaded_file)

#         if pdf_text and pdf_text != st.session_state.get("current_pdf_text"):
#             st.session_state["current_pdf_text"] = pdf_text
#             st.session_state["summary"] = None
#             st.session_state["quiz"] = []
#             st.session_state["flashcards"] = []

#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("📌 Summary"):
#                 st.session_state["summary"] = generate_ai_content(f"Summarize this:\n{pdf_text}")
#                 st.session_state["progress"] += 10
#         with col2:
#             if st.button("📝 Quiz"):
#                 st.session_state["quiz"] = ["Sample Quiz Question"]
#                 st.session_state["progress"] += 10
#         with col3:
#             if st.button("📖 Flashcards"):
#                 st.session_state["flashcards"] = ["Sample Flashcard"]
#                 st.session_state["progress"] += 10

#         if st.session_state["summary"]:
#             st.subheader("📌 AI-Generated Summary")
#             st.write(st.session_state["summary"])
        
#         if st.session_state["quiz"]:
#             st.subheader("📝 AI-Generated Quiz Questions")
#             st.write(st.session_state["quiz"])
        
#         if st.session_state["flashcards"]:
#             st.subheader("📖 AI-Generated Flashcards")
#             st.write(st.session_state["flashcards"])

# # Render pages
# if st.session_state["page"] == "dashboard":
#     user_dashboard()
# else:
#     main_page()
import streamlit as st
import pdfplumber
import subprocess
import random

# Ensure required modules are installed
try:
    import streamlit as st
    import pdfplumber
except ModuleNotFoundError:
    st.error("Missing required modules. Please install them using 'pip install streamlit pdfplumber'.")

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

# User Dashboard Page
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
    
    st.sidebar.markdown("<div style='position: absolute; bottom: 10px; left: 10px;'>", unsafe_allow_html=True)
    if st.sidebar.button("☀️ Light Mode"):
        st.session_state["dark_mode"] = False
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Main Page
def main_page():
    custom_sidebar()
    
    # Theme switching
    if st.session_state["dark_mode"]:
        st.markdown("<style>body { background-color: black; color: white; }</style>", unsafe_allow_html=True)
    else:
        st.markdown("<style>body { background-color: white; color: black; }</style>", unsafe_allow_html=True)
    
    st.title("NoteWiz 📚")
    st.write("Upload a PDF to generate **Summaries, Quiz Questions, and Flashcards!**")
    uploaded_file = st.file_uploader("📂 Choose a PDF file", type="pdf")

    if uploaded_file:
        st.success("✅ PDF Uploaded Successfully!")
        pdf_text = extract_text_from_pdf(uploaded_file)

        if pdf_text and pdf_text != st.session_state.get("current_pdf_text"):
            st.session_state["current_pdf_text"] = pdf_text
            st.session_state["summary"] = None
            st.session_state["quiz"] = []
            st.session_state["flashcards"] = []

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📌 Summary"):
                st.session_state["summary"] = generate_ai_content(f"Summarize this:\n{pdf_text}")
                st.session_state["progress"] += 10
        with col2:
            if st.button("📝 Quiz"):
                st.session_state["quiz"] = ["Sample Quiz Question"]
                st.session_state["progress"] += 10
                st.session_state["quiz_progress"] += 10
        with col3:
            if st.button("📖 Flashcards"):
                st.session_state["flashcards"] = ["Sample Flashcard"]
                st.session_state["progress"] += 10
                st.session_state["flashcard_progress"] += 10

        if st.session_state["summary"]:
            st.subheader("📌 AI-Generated Summary")
            st.write(st.session_state["summary"])
        
        if st.session_state["quiz"]:
            st.subheader("📝 AI-Generated Quiz Questions")
            st.write(st.session_state["quiz"])
        
        if st.session_state["flashcards"]:
            st.subheader("📖 AI-Generated Flashcards")
            st.write(st.session_state["flashcards"])

# Render pages
if st.session_state["page"] == "dashboard":
    user_dashboard()
elif st.session_state["page"] == "profile":
    user_profile()
else:
    main_page()


