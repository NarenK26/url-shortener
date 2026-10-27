from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from uuid import uuid4
from fastapi.responses import RedirectResponse
from database import create_database, save_url, get_url

app = FastAPI(title="URL Shortener API")

# Create the database table
create_database()
# Request model
class URLRequest(BaseModel):
    url: HttpUrl
# Health-check API
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "URL Shortener API is running"
    }
# Root API
@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running"}

# Create a short URL
@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = uuid4().hex[:6]

    # Check whether the short code already exists
    while get_url(short_code) is not None:
        short_code = uuid4().hex[:6]

    original_url = str(request.url)

    # Save the URL in the database
    save_url(short_code, original_url)

    return {
        "short_code": short_code,
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "original_url": original_url
    }

# Redirect to the original URL
@app.get("/{short_code}")
def redirect_url(short_code: str):
    original_url = get_url(short_code)

    if not original_url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(
        url=original_url,
        status_code=307
    )