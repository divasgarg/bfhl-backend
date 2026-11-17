# BFHL API

A FastAPI service that separates a list of strings into numbers and alphabetic entries. `POST /bfhl` accepts a JSON body such as `{"data":["M","1","334","4","B"]}` and returns both groups plus the highest alphabetic entry. `GET /bfhl` returns the operation code.

## Run locally

In a Python virtual environment, run `pip install -r requirements.txt`, then `uvicorn main:app --reload`. Open `/docs` on the local server to try the endpoints.

[React frontend](https://github.com/divasgarg/bfhl-frontend) · [API implementation](main.py)
