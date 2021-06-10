from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()

template = Jinja2Templates(directory="template")

@app.get("/")
def hello_name(request: Request, name: Optional[str] = None ):
    return template.TemplateResponse("index.html", {"request":request, "name":name})