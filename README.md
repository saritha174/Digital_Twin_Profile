# 🤖 AI Digital Twin

An AI-powered digital twin that represents my professional profile and answers questions about my **career, skills, experience, and projects**.

## 🚀 Features

* Chat with an AI representation of my professional profile
* Uses my **Resume, LinkedIn profile, and professional summary**
* Answers questions about skills, projects, and experience
* Supports Groq tool calling
* Collects visitor contact information for follow-up

## 🛠️ Tech Stack

* Python
* Groq
* Llama
* Gradio
* PyPDF
* Python-dotenv

## 📁 Project Structure

```text
digital-twin/
│
├── app.py
├── context.py
├── tools.py
├── styles.py
├── linkedin.pdf
├── resume.pdf
├── summary.txt
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 3. Run the application

```bash
python app.py
```

The Gradio interface will open locally in your browser.

## 🧠 How It Works

```text
Resume + LinkedIn + Summary
            ↓
        context.py
            ↓
     System Prompt
            ↓
         Groq LLM
            ↓
        Gradio Chat
            ↓
      Digital Twin
```

## 📌 Project Status

**Proof of Concept**

Built to create an interactive AI-powered professional portfolio that allows recruiters and visitors to learn about my experience through conversation.
