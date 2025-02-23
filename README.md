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
pip install streamlit pdfplumber
```

### 3. Install Ollama  

Ollama is required for AI model execution.  

#### **macOS (via Homebrew)**  
```bash
brew install ollama
```

#### **Windows**  
1. Download the **Ollama Windows installer** from [Ollama's official site](https://ollama.com)  
2. Run the installer and follow the setup instructions  

### 4. Start Ollama Server  

#### **macOS/Linux/Windows**  
Once installed, start the Ollama server:  
```bash
ollama serve
```

### 5. Open a New Terminal Tab and Pull the Mistral Model  

In a **new terminal tab**, activate the same virtual environment:  

#### **macOS/Linux**  
```bash
source venv/bin/activate
```

#### **Windows (PowerShell)**  
```powershell
venv\Scripts\Activate
```

Then, pull the Mistral model:  

```bash
ollama pull mistral
```

### 6. Run the Streamlit App  

#### **macOS/Linux/Windows**  
Launch the application with:  
```bash
streamlit run note1.py
```

## Features  
- Extract text from PDFs using `pdfplumber`  
- Interactive UI powered by `Streamlit`  
- AI-driven processing with `Ollama` and the `Mistral` model  

## Requirements  
- macOS or Windows  
- Python 3.x  
- Streamlit  
- pdfplumber  
- Virtual environment (recommended)  
- Ollama installed  

## License  
This project is licensed under an open-source or proprietary license.  
