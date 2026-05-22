import json
import os
import requests
from dotenv import load_dotenv
from prompts import REVIEW_PROMPT

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


def review_code(code):
    prompt = REVIEW_PROMPT.format(code=code)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    text = result["candidates"][0]["content"]["parts"][0]["text"]

    try:
        return json.loads(text)
    except:
        return {
            "comments": [
                {
                    "issue": "Could not parse response",
                    "severity": "Medium",
                    "confidence": 50,
                    "suggestion": text
                }
            ]
        }