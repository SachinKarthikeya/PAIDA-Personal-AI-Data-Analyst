import ollama
import json
from prompts import system_prompt, recommendation_prompt, analyst_prompt

model1_name = "llama3.2:1b"
model2_name = "gemma3:4b"

SYSTEM_PROMPT = system_prompt()
RECOMMENDATION_PROMPT = recommendation_prompt()
ANALYST_PROMPT = analyst_prompt()

def llm_query(user_query):
    response = ollama.chat(
        model=model1_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    raw_output = response['message']['content']

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from LLM", "message": raw_output}
    

def recommendation_query(dataset_metadata):
    response = ollama.chat(
        model=model1_name,
        messages=[
            {"role": "system", "content": RECOMMENDATION_PROMPT},
            {"role": "user", "content": json.dumps(dataset_metadata, indent=2)}
        ]
    )

    raw_output = response['message']['content']

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {"recommended_models": [], "error": raw_output}
    
def analyst_query(dataset_metadata):
    response = ollama.chat(
        model=model2_name,
        messages=[
            {"role": "system", "content": ANALYST_PROMPT},
            {"role": "user", "content": json.dumps(dataset_metadata, indent=2)}
        ]
    )

    return response['message']['content']
