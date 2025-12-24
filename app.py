from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI(title="Student Performance Prediction API", version="1.0")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_model=None, status_code=200, tags=["Home"], summary="Render Home Page", description="Renders the home page of the Student Performance Prediction API.")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)