
import os
import json

from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()


# Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")


# Gemini client
client = genai.Client(api_key=api_key)


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a senior software engineer and hiring manager.

Evaluate the following resume based on the user's career goal.

USER GOAL:
{user_goal}

STRICT RULES:
- Extract only skills relevant to the user's goal.
- Remove irrelevant skills.
- Identify missing skills required for the goal.
- Create a roadmap only for the missing skills.
- Make the analysis different depending on the user's goal.
- Give practical interview questions relevant to the goal.
- Return ONLY valid JSON.
- Do not use markdown.
- Do not add explanations outside the JSON.

Return exactly this structure:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}

RESUME:
{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        return json.loads(response.text)

    except Exception as e:
        error_message = str(e)

        if "503" in error_message or "UNAVAILABLE" in error_message:
            return {
                "skills": [],
                "missing_skills": [],
                "roadmap": [],
                "interview_questions": [],
                "error": "Gemini AI is temporarily busy. Please try again in a few seconds."
            }

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": error_message
        }

