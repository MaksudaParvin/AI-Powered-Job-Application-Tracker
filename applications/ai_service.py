from google import genai
from google.genai import types
from django.conf import settings
import json


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def analyze_job_description(job_description):

    prompt = f"""
You are an expert technical recruiter.

Analyze this job description and provide useful information
for a job seeker.

JOB DESCRIPTION:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,

        config=types.GenerateContentConfig(
            response_mime_type="application/json",

            response_schema={
                "type": "object",

                "properties": {

                    "summary": {
                        "type": "string"
                    },

                    "required_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },

                    "required_experience": {
                        "type": "string"
                    },

                    "technologies": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },

                    "interview_preparation": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },

                "required": [
                    "summary",
                    "required_skills",
                    "required_experience",
                    "technologies",
                    "interview_preparation"
                ]
            }
        )
    )

    return json.loads(response.text)