import os
from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from chatbilly.core import impersonate, get_all_names

UVICORN_HOST = os.environ.get("UVICORN_HOST", "0.0.0.0")
UVICORN_PORT = int(os.environ.get("UVICORN_PORT", 8080))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def load_prompt_template():
    """Load the prompt template on startup."""
    global all_names
    print("INFO: Loading names...")
    all_names = get_all_names()


@app.get("/api/impersonate")
async def ask(person: Union[str, None] = None):
    """Process a text query and return the SQL statement, results, and explanation."""
    impersonation = await impersonate(person)
    return {
        "response": {
            "person": person,
            "impersonation": impersonation,
        }
    }


@app.get("/api/all_names")
async def names():
    return {
        "response": {
            "names": all_names,
        }
    }


@app.get("/")
async def serve_index():
    """Serve index.html"""
    return FileResponse("index.html")


def serve():
    uvicorn.run(app, host=UVICORN_HOST, port=UVICORN_PORT)
