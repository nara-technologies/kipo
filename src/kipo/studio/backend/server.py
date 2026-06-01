from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return (FRONTEND_DIR / "index.html").read_text(
        encoding="utf-8"
    )

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8080)