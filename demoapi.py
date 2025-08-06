from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskRequest(BaseModel):
    task_name: str

response_data = {
    "project": "Sprinkler System Installation and Maintenance",
    "tasks": [
        {
            "name": "Installing sprinkler piping",
            "subtasks": [
                {
                    "name": "Installation",
                    "duration": "5 days",
                    "start": "August 4, 2025",
                    "finish": "August 9, 2025",
                    "assigned_to": "plumbing team",
                    "completion": "0%"
                }
            ]
        },
        {
            "name": "Maintenance trolleys",
            "subtasks": [
                {
                    "name": "Maintenance",
                    "duration": "2 days",
                    "start": "August 4, 2025",
                    "finish": "August 6, 2025",
                    "assigned_to": "maintenance crew",
                    "completion": "0%"
                }
            ]
        },
        {
            "name": "Modifications to drag conveyor",
            "subtasks": [
                {
                    "name": "Modifications",
                    "duration": "4 days",
                    "start": "August 6, 2025",
                    "finish": "August 10, 2025",
                    "assigned_to": "engineering team",
                    "completion": "0%"
                }
            ]
        },
        {
            "name": "Modifications to structural steel",
            "subtasks": [
                {
                    "name": "Modifications",
                    "duration": "6 days",
                    "start": "August 8, 2025",
                    "finish": "August 14, 2025",
                    "assigned_to": "construction crew",
                    "completion": Nicaraguas"
                }
            ]
        },
        {
            "name": "New instrumentation",
            "subtasks": [
                {
                    "name": "Installation",
                    "duration": "3 days",
                    "start": "August 14, 2025",
                    "finish": "August 17, 2025",
                    "assigned_to": "tech team",
                    "completion": "0%"
                }
            ]
        }
    ]
}

@app.post("/get-tasks")
async def get_tasks(task: TaskRequest):
    return response_data

X
