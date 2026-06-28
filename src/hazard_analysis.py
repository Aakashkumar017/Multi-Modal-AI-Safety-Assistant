import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # loads GROQ_API_KEY from your .env file

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_hazard(query: str, caption: str) -> str:
    """
    Takes an image caption and a user question, then returns
    a plain-language safety assessment using Llama 3.3 via Groq.
    """

    prompt = f"""You are a no-nonsense safety expert. A user has uploaded an image and asked a question.

Image description (auto-generated):
"{caption}"

User's question:
"{query}"

Give a clear, human-friendly safety report. Structure it like this:

⚠️ Main Danger:
[One sentence — what is the actual risk?]

🔍 Why It's Dangerous:
[Two or three sentences explaining the hazard in plain terms. No jargon.]

✅ What To Do:
[Two or three actionable steps the person should take right now.]

Keep the tone calm but urgent. Write as if you're talking to someone who just found this hazard at home.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=512,
    )

    return response.choices[0].message.content