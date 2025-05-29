import requests
from config.settings import GROQ_API_URL, HEADERS

def generate_questions(content: str, question_type: str = "mcq", difficulty: str = "medium") -> str:
    prompt = f"""
You are an exam question generator AI.

Topic content:
\"\"\"
{content}
\"\"\"

Generate 3 {question_type.upper()} questions on the above topic. 
Difficulty: {difficulty}. 
Also include correct answers and explanations.
Format output as:

Q1: ...
A. ...
B. ...
C. ...
D. ...
Answer: ...
Explanation: ...

Only include questions.
"""
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
    return response.json()["choices"][0]["message"]["content"]
