AI4Good-NoteWiz is a Streamlit-based application designed for efficient note processing. It leverages PDF extraction and AI capabilities to enhance your workflow.

## Installation Guide  

### 1. Set Up a Virtual Environment  

Using a virtual environment is recommended for managing dependencies.  

#### **macOS/Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **Windows (PowerShell)**  
```powershell
python -m venv venv
venv\Scripts\Activate
```

In both cases, once activated, you should see `(venv)` appear in your terminal, indicating the environment is active.  

### 2. Install Dependencies  

#### **macOS/Linux/Windows**  
Once the virtual environment is activated, install the required Python packages:  
```bash
pip install -r requirements.txt
```

### 3. Set UP your MISTRAL API key in `.env`
```
MISTRAL_API_KEY = "<YOUR API KEY>"
```

### 4. Run the Streamlit App  

#### **macOS/Linux/Windows**  
Launch the application with:  
```bash
streamlit run home.py
```

## Features  
- Extract text from PDFs using `pdfplumber`  
- Interactive UI powered by `Streamlit`  
- AI-driven processing with `Mistral`

