import os
from fastapi import APIRouter
from typing import List, Dict, Any
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient, errors
from pydantic import BaseModel
from .text import TextPrompt
from .data_source import Data_Source
from .vector_store import Vector_Store
from .request_data import PromptBody
# fastapi router
router = APIRouter()

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

@router.post("/vector/store")
def vector_store(name: str):
    vector_reply = Vector_Store.create(name=name)
    return(
        {"vector_store": vector_reply,
        }
    )


@router.get("/datasource/list")
def datasource():
    
    # get prompt answer
    ds_reply = Data_Source.list()

    return ds_reply