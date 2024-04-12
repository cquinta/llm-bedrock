import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv, dotenv_values


# load env vars
load_dotenv()

# import router
from prompts.controllers import router


# create server instance
app = FastAPI(desc="Yoda AI")

# include the prompts routes
app.include_router(router)


@app.get("/")
def index():
    return {
        "page": "home",
        "version": "v2"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)