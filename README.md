# AI Interview OS

A modular GenAI backend project built using Python and Groq API.

## Features

- Prompt Engineering
- Structured JSON Outputs
- Pydantic Validation
- Auto JSON Repair Pipeline
- Retry Handling
- Modular LLM Architecture

## Tech Stack

- Python
- Groq API
- OpenAI SDK
- Pydantic
- dotenv

## Project Structure

```bash
app.py
llm_engine.py
prompt_builder.py
schema.py
json_repair.py
config.py
.env
```

## Setup

### 1. Clone Repository

```bash
git clone <your_repo_url>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add API Key

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

### 6. Run Project

```bash
python app.py
```

## Example

Input:

```text
Prompt Engineering
```

Output:

```json
{
  "topic": "Prompt Engineering",
  "difficulty": "Beginner",
  "answer": "..."
}
```

## Author

Siddhant Chandorkar