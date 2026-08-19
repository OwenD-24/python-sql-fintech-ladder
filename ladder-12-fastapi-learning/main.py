from fastapi import FastAPI # imports the FastAPI class from the package.

app = FastAPI() # creates your API application object.
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/validate")
def validation():
    return {
        "total": 5,
        "valid": 1,
        "review": 1,
        "invalid": 3
    }

# Python handles the validation, 
# n8n activates the workflow and 
# the LLM summarieses the results before the email is sent.