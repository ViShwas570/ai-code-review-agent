import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import REVIEW_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def review_code(code):
    prompt = REVIEW_PROMPT.format(code=code)

    response = model.generate_content(prompt)

    text = response.text

    try:
        return json.loads(text)
    except:
        return {
            "comments": [
                {
                    "issue": text,
                    "severity": "High",
                    "confidence": 95,
                    "suggestion": "Check Gemini API response formatting"
                }
            ]
        }