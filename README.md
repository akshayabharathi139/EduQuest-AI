# EduQuest-AI

# 🧠 Exam Question Generator from Topics

Automatically generate MCQs and descriptive questions with answers using LLaMA3-70B, Wikipedia API, and LangChain.

---

## 📌 Features

- 🧾 Input any topic or syllabus section
- 🌐 Fetch relevant content from Wikipedia API
- 💡 Generate MCQs or descriptive questions using LLaMA3-70B via Groq
- 🎯 Categorize questions by difficulty (Easy, Medium, Hard)
- 🧠 View and export questions with answers
- 💻 Deploy via Streamlit or FastAPI

---

## 🏗️ Tech Stack

| Component        | Technology                         |
|------------------|-------------------------------------|
| Language Model   | LLaMA3-70B via [Groq API](https://console.groq.com/) |
| Orchestration    | LangChain                          |
| Content Fetching | Wikipedia API                      |
| Backend Logic    | Python                             |
| Deployment       | Streamlit or FastAPI (optional)    |

---



Flow Chart 
![ChatGPT Image May 29, 2025, 03_53_34 PM](https://github.com/user-attachments/assets/753be44c-d421-44a6-bc50-63bcb989dd59)

Demo Video

![Streamlit and 1 more page - Personal - Microsoft_ Edge 2025-05-29 16-47-22](https://github.com/user-attachments/assets/bfe515d5-432a-4e42-8c76-44a841b9f574)




## 📂 Folder Structure


exam-question-generator/
├── app/
│ ├── init.py
│ ├── generator.py # LLM question generation
│ ├── wiki_fetcher.py # Wikipedia content fetching
│ ├── utils.py # Text parsing, formatting
│ └── prompts/ # Prompt templates
│ └── prompt_template.txt
├── config/
│ └── settings.py # API keys and model configs
├── main.py # Streamlit/FastAPI entry point
├── requirements.txt
└── README.md



---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/exam-question-generator.git
cd exam-question-generator


3. Set up your .env file
env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions




Run the App:

streamlit run main.py



📥 Example Input
Topic: "Photosynthesis"

🔄 Output:
Q1 (Easy): What are the two main stages of photosynthesis?

A1: The light-dependent reactions and the Calvin cycle.

Q2 (Medium): Describe the role of chlorophyll in photosynthesis.

Q3 (Hard): Explain how environmental factors affect the rate of photosynthesis.




💡 Future Improvements
Add PDF/CSV export

Integrate GPT-4 as fallback

UI styling and theme customization

Save user-generated quizzes

Developed by Akshaya Bharathi
my emailid:akshayabharathi139@gmail.com



