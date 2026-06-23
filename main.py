from fastapi import FastAPI, status
from openai import OpenAI
from dotenv import load_dotenv
import os
from utils import createUser
from fastapi.responses import RedirectResponse

load_dotenv()

## Defining App
app = FastAPI()
openai_client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


@app.get("/healthcheck")
def root_controller():
    return {"status":"healthy"}

@app.get("/",include_in_schema=False)
def docs_redirect_controller():
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/chat")
def chat_controller(prompt: str="Inpire me to learn AI"):
    response = openai_client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role":"system", "content": "You are intelligent and helpfull assistant"},
            {"role": "user", "content": prompt}
        ],
    )
    statement = response.choices[0].message.content
    return {"statement": statement}

@app.post("/users")
async def create_user_controller(user:createUser):
    return {"name": user.username, "message": "Account Succesfully Created"}