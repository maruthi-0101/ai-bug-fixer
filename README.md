
# 🐞 AI Bug Fixer

AI Bug Fixer is an AI-powered web application that helps developers understand and fix Python code errors.
Users paste buggy Python code along with the error message, and the AI explains the issue and suggests corrected code.

This project demonstrates how to build an end-to-end **GenAI application** using a pretrained Large Language Model (LLM), without training or fine-tuning.

---

## 🚀 Features

- 🧠 Explains Python errors in simple language  
- 🛠️ Suggests corrected, runnable Python code  
- 🌐 Interactive web UI built with Gradio  
- ⚡ Uses pretrained LLM (no training required)  
- 📦 Clean, beginner-friendly project structure  

---

## 🏗️ Project Architecture

```
User Input (Code + Error)
        ↓
Gradio UI (app.py)
        ↓
AI Logic (bug_fixer.py)
        ↓
Prompt + LLM Inference
        ↓
Explanation + Fixed Code
        ↓
Output shown in UI
```

---

## 📁 Project Structure

```
ai-bug-fixer/
├── app.py                  # Gradio web application (UI)
├── bug_fixer.py            # Core AI bug-fixing logic
├── prompts.py              # Prompt templates for the LLM
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── data/
    └── python_errors.txt   # Sample Python errors (optional testing)
```

---

## ⚙️ Tech Stack

- **Python**
- **Gradio** – Web interface
- **Hugging Face Transformers**
- **google/flan-t5-base** – Pretrained LLM
- **PyTorch**

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-link>
cd ai-bug-fixer
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

After running, open your browser and go to:
```
http://127.0.0.1:7860
```

---

## 🧪 Example Usage

**Buggy Code**
```python
for i in range(5)
    print(i)
```

**Error Message**
```
SyntaxError: invalid syntax
```

**AI Output**
- Explanation of the syntax error
- Corrected code:
```python
for i in range(5):
    print(i)
```

---

## 🧠 Key Learnings

- Difference between **training** and **inference**
- Prompt engineering for LLMs
- Building AI-powered applications end-to-end
- Integrating LLMs with web UIs
- Handling edge cases (missing error messages)

---

## ⚠️ Limitations

- The model does not execute code
- Users must paste the error message manually
- Response quality depends on the LLM (flan-t5-base is lightweight)

---

## 📌 Future Improvements

- Automatic error detection by executing code safely
- Support for more programming languages
- Stronger models or API-based LLMs
- RAG-based error pattern retrieval

---

## 📄 License

This project is for educational and portfolio purposes.
