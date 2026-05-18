from openai import OpenAI
import json

from schema import AIResponse

from dotenv import load_dotenv
from config import MODEL_NAME, TEMPERATURE, MAX_TOKENS

from json_repair import (
    clean_json_output,
    repair_json_with_llm
)

import os

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Create client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


def generate_llm_response(prompt):

    # Generate response
    response = client.chat.completions.create(

        model=MODEL_NAME,

        temperature=TEMPERATURE,

        max_tokens=MAX_TOKENS,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Raw LLM output
    raw_output = response.choices[0].message.content

    print("\nRAW OUTPUT:\n")
    print(raw_output)

    # Clean markdown formatting
    cleaned_output = clean_json_output(raw_output)

    print("\nCLEANED OUTPUT:\n")
    print(cleaned_output)

    try:

        # Convert JSON string to dictionary
        parsed_output = json.loads(cleaned_output)

        # Validate structure
        validated_output = AIResponse(**parsed_output)

        print("\nVALIDATED OUTPUT:\n")
        print(validated_output)

        return validated_output

    except Exception as e:

        print("\nJSON Parsing Failed")
        print(e)

        print("\nAttempting Auto-Repair...\n")

        repaired_json = repair_json_with_llm(
            client,
            cleaned_output
        )

        print("\nREPAIRED JSON:\n")
        print(repaired_json)

        repaired_output = json.loads(repaired_json)

        validated_output = AIResponse(**repaired_output)

        print("\nVALIDATED REPAIRED OUTPUT:\n")
        print(validated_output)

        return validated_output