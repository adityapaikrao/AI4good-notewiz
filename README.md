NoteWiz is an application designed for efficient note processing. It leverages PDF extraction and AI capabilities to enhance your workflow.  

## Installation Guide  

### 1. Install Ollama (For macOS)  
Ollama is required for AI model execution. Install it using Homebrew:  
```bash
brew install ollama
```

### 2. Start Ollama Server  
Once installed, run the following command to start the Ollama service:  
```bash
ollama serve
```

### 3. Pull the Mistral Model  
Open a new terminal tab and pull the Mistral model:  
```bash
ollama pull mistral
```

### 4. Install Python Dependencies  
Ensure you have Python installed, then install the necessary dependencies:  
```bash
pip install streamlit pdfplumber
```

### 5. Run the Streamlit App  
Launch the application with the following command:  
```bash
streamlit run note1.py
```

## Features  
- Extract text from PDFs using `pdfplumber`  
- Interactive UI powered by `Streamlit`  
- AI-driven processing with `Ollama` and the `Mistral` model  

## Requirements  
- macOS (for Ollama)  
- Python 3.x  
- Streamlit  
- pdfplumber  

## License  
This project is licensed under an open-source or proprietary license (add details if applicable).  

---

Let me know if you need any modifications! 🚀
