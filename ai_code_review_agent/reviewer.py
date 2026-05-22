import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import REVIEW_PROMPT

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-pro")


def review_code(code):
    prompt = REVIEW_PROMPT.format(code=code)

    try:
        response = model.generate_content(prompt)

        # Gemini response text
        text = response.text

        # Convert AI response into JSON
        try:
            return json.loads(text)

        except:
            return {
                "comments": [
                    {
                        "issue": "Could not parse AI response",
                        "severity": "Medium",
                        "confidence": 70,
                        "suggestion": text
                    }
                ]
            }

    except Exception as e:
        return {
            "comments": [
                {
                    "issue": str(e),
                    "severity": "High",
                    "confidence": 95,
                    "suggestion": "Check Gemini API key or model configuration"
                }
            ]
        }