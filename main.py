from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to BLOGPOST!"}
    

@app.get("/about")
def about():
    return{"message": "A platform where writers are given the opprtunity to express their abilities via writing."}

@app.get("/contact")
def contact():
    return{"message": "You can reach us through our email- contactus@blogpost.com"}


