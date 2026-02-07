import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_sql_query_from_nl(prompt, schema):
    schema_text = "\n".join([f"{table}: {', '.join(cols)}" for table, cols in schema.items()])
    full_prompt = f"""
You are an expert SQL assistant. Based on the database schema below, write a valid MySQL query.

Schema:
{schema_text}

Question: {prompt}
Return only the SQL query, no explanation.
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": full_prompt}],
            "temperature": 0.2
        }
    )

    try:
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error generating SQL: {e}"
