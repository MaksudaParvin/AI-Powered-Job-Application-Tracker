import json

from django.conf import settings
from openai import OpenAI


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def analyze_job_description(job_description):

    prompt = f"""
You are an expert career assistant.

Analyze the following job description.

Return ONLY valid JSON with exactly these fields:

{{
    "summary": "",
    "required_skills": [],
    "required_experience": "",
    "technologies": [],
    "interview_preparation": []
}}

Rules:

- summary: concise summary of the role
- required_skills: important skills required for the job
- required_experience: experience requirements
- technologies: programming languages, frameworks, tools, databases, platforms, etc.
- interview_preparation: practical topics the candidate should prepare for
- Do not invent information that is not reasonably supported by the job description.

Job Description:

{job_description}
"""


    response = client.responses.create(

        model="gpt-5.6-luna",

        input=prompt
    )


    result = response.output_text.strip()


    try:

        return json.loads(result)

    except json.JSONDecodeError:

        raise ValueError(
            "AI returned an invalid response format."
        )