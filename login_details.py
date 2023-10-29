from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Login():
    username: str
    password: str

#CRUD operation

#Home
@app.get('/')
def home():
  return("Welcome")

#Login endpoint
@app.post("/login/")
async def login(
    username: Annotated [str, Form()],
    password: Annotated [str, Form()],
):
 if username == "afenokoatabo" and password == "admin121":
    return("Welcome, Afenoko")

 else:
    return("Oops, Login failed")
   

@app.post("/login/")
async def login(
    username: Annotated [str, Form()],
    password: Annotated [str, Form()],
):
 if username == "stellainabo" and password == "admin122":
    return("Welcome, Stella")
 else:
    return("Oops, Login failed")
 

@app.post("/login/")
async def login(
    username: Annotated [str, Form()],
    password: Annotated [str, Form()],
):
 if username == "franzkati" and password == "admin123":
    return("Welcome, Franz")
 else:
    return("Oops, Login failed")
 

@app.post("/login/")
async def login(
    username: Annotated [str, Form()],
    password: Annotated [str, Form()],
):
 if username == "sandrabajon" and password == "admin124":
    return("Welcome, Sandra")
 else:
    return("Oops, Login failed")


@app.post("/login/")
async def login(
    username: Annotated [str, Form()],
    password: Annotated [str, Form()],
):
 if username == "stephmoses" and password == "admin125":
    return("Welcome, Stephanie")
 else:
    return("Oops, Login failed")

   

