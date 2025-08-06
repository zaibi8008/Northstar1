from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Configure OpenAI API key (replace with your key)
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    chat_input: str

def generate_tasks(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Based on this input: '{prompt}', return ONLY a valid JSON structure with a 'project' name and a 'tasks' list. Each task should have a 'name' and a 'subtasks' list, where each subtask has 'name', 'start', and 'finish' dates in 'YYYY-MM-DD' format, starting from 2025 or later. Example: {{'project': 'Project Name', 'tasks': [{{'name': 'Task 1', 'subtasks': [{{'name': 'Subtask 1', 'start': '2025-08-06', 'finish': '2025-08-10'}}]}}]}}."}]
    )
    json_str = response.choices[0].message.content.strip()
    import json
    return json.loads(json_str)

@app.post("/get-tasks")
async def get_tasks(chat: ChatRequest):
    try:
        return generate_tasks(chat.chat_input)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
