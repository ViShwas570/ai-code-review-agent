import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import REVIEW_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(code):
    prompt = REVIEW_PROMPT.format(code=code)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior software engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    text = response.choices[0].message.content

    try:
        return json.loads(text)
    except:
        return {
            "comments": [
                {
                    "issue": "Could not parse structured response",
                    "severity": "Medium",
                    "confidence": 40,
                    "suggestion": "Verify manually"
                }
            ]
        }