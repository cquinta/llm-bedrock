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
from .vector_index import Vector_Index
from .knowledge_base import Knowledge_Base
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

@router.post("/knowledge_base/create")
def knowledge_base(name: str):
    knowledge_base_reply = Knowledge_Base.create(knowledge_base_name=name)
    return(
        {"vector_store": knowledge_base_reply[0], 
         "vector_index": knowledge_base_reply[1],
        }
    )


    
    # get prompt answer
    ds_reply = Data_Source.list()

    return ds_reply