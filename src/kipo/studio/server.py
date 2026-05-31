from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Kipo"}

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8080)