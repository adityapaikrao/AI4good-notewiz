# NoteWiz - AI-Powered Study Plan

## Overview
NoteWiz is an AI-powered study planner that generates summaries, flashcards, and quizzes based on uploaded study materials. This project is built using HTML, CSS, and JavaScript and integrates OpenAI's GPT API for content generation.

## Features
- **User Authentication**: Login with username and password.
- **File Upload**: Upload study notes in text format.
- **AI-Generated Content**:
  - Summarization of study materials.
  - Flashcards for active recall.
  - Quiz questions for self-assessment.
- **User Profile & Progress Tracking**.

## Prerequisites
Before running this project locally, ensure you have the following installed:
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) (Recommended)
- [Python 3](https://www.python.org/) (For running a local server) or
- [Node.js](https://nodejs.org/) (For an alternative server setup)

## How to Run Locally
### Option 1: Using Live Server (Recommended)
1. Open the project folder in **VS Code**.
2. Install the **Live Server** extension from the Extensions Marketplace.
3. Right-click on `index.html` and select **"Open with Live Server"**.
4. The app will open in your default web browser at `http://127.0.0.1:5500/`.

### Option 2: Using Python HTTP Server
1. Open a terminal and navigate to the project folder:
   ```sh
   cd path/to/your/project
   ```
2. Start a local server:
   - If using **Python 3**:
     ```sh
     python -m http.server 8000
     ```
   - If using **Python 2**:
     ```sh
     python -m SimpleHTTPServer 8000
     ```
3. Open your browser and visit: `http://localhost:8000/`

### Option 3: Using Node.js (Express.js)
1. Ensure Node.js is installed on your system.
2. Open a terminal and navigate to your project folder:
   ```sh
   cd path/to/your/project
   ```
3. Install a simple static server globally:
   ```sh
   npm install -g serve
   ```
4. Start the server:
   ```sh
   serve .
   ```
5. The app will be accessible at `http://localhost:3000/` (or the port displayed).

## API Integration (OpenAI GPT)
To enable AI features, you need an OpenAI API key:
1. Sign up at [OpenAI](https://openai.com/) and generate an API key.
2. Replace `YOUR_OPENAI_API_KEY` in `index.html` with your actual API key:
   ```js
   const apiKey = 'YOUR_OPENAI_API_KEY';
   ```
3. Ensure your API key is kept **secure** and not exposed in public repositories.

## Troubleshooting
- If the app doesn’t load, check the browser console (`F12` or `Ctrl+Shift+I` → Console) for errors.
- Ensure your API key is correctly configured if using GPT-based features.
- If the local server isn’t working, try a different port (e.g., `http.server 9000`).

## Contributing
If you’d like to contribute to **NoteWiz**, feel free to fork this repository and submit a pull request.

## License
This project is licensed under the MIT License.

---
Enjoy using **NoteWiz** to supercharge your study sessions! 🚀

