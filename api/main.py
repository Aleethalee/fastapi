from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return{"Hai! welcome to my little world..."}