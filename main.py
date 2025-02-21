from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RequestData(BaseModel):
    data: List[str]

@app.post("/bfhl")
def process_data(request: RequestData):
    try:
        user_id = "john_doe_17091999"  # Replace with actual user info if needed
        email = "john@xyz.com"
        roll_number = "ABCD123"

        numbers = [x for x in request.data if x.isdigit()]
        alphabets = [x for x in request.data if x.isalpha()]
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}