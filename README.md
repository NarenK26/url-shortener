# URL Shortener API

## Project Description

This project is a simple URL Shortener API built using Python and FastAPI. It converts a long URL into a short URL. When someone opens the short URL, the application redirects them to the original URL.

The application uses SQLite to store URLs so that the short links continue to work even after the server is restarted.

## Features

- Create short URLs from original URLs.
- Redirect short URLs to their original destinations.
- Store URL mappings in an SQLite database.
- Check application health using a health endpoint.
- Handle invalid or unknown short codes.
- Run automated unit tests using pytest.

## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pytest




## Project Structure

- `main.py` — Contains the FastAPI application and API endpoints.
- `database.py` — Handles database creation and URL storage and retrieval.
- `test_main.py` — Contains automated tests.
- `urls.db` — SQLite database file created by the application.

## Installation

Install the required packages:

```bash
python -m pip install fastapi uvicorn pytest httpx
```

## Run the Application

Start the application using:

```bash
python -m uvicorn main:app --reload
```





The application will run at:

`http://127.0.0.1:8000`

## API Documentation

Open the following URL in your browser to explore and test the API:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks that the application is running. |
| GET | `/health` | Returns the health status. |
| POST | `/shorten` | Creates a short URL. |
| GET | `/{short_code}` | Redirects to the original URL. |

## Run Automated Tests

Run all tests using:

```bash
python -m pytest -v
```

## Database Persistence

The application stores short codes and their original URLs in an SQLite database. The saved mappings remain available after restarting the application.

## Future Improvements

- Add custom short codes.
- Add URL expiration.
- Add Docker support.
- Set up a CI/CD pipeline.
- Deploy the application to a cloud platform.