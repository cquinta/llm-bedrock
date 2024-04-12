import os
from fastapi import APIRouter
from typing import List, Dict, Any
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient, errors
from pydantic import BaseModel
from .text import TextPrompt
from .request_data import PromptBody

# fastapi router
router = APIRouter()

# connect to mongo
client = MongoClient(os.getenv("MongoURI"))

# check the loaded env vars
all_values = dotenv_values(".env")
# print(all_values)



# generate text prompts
# expects a prompt in the post body
@router.post("/text/prompt")
def prompt(prompt: PromptBody):
    
    # get prompt answer
    prompt_reply = TextPrompt.generate(prompt=prompt.prompt)

    return {
        "reply": prompt_reply,
        "prompt": prompt,
    }