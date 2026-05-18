import json

def clean_json_output(raw_text):

    cleaned_text = raw_text.replace("```json", "")
    cleaned_text = cleaned_text.replace("```", "")

    return cleaned_text.strip()

def repair_json_with_llm(client, raw_json):

    repair_prompt = f"""
You are a JSON repair system.

TASK:
Fix the malformed JSON below.

CONSTRAINTS:
- Return ONLY valid JSON
- Do not add explanations
- Preserve original meaning

MALFORMED JSON:
{raw_json}
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        temperature=0,

        max_tokens=300,

        messages=[
            {
                "role": "user",
                "content": repair_prompt
            }
        ]
    )

    return response.choices[0].message.content