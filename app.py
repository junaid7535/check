from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Jenkins CI/CD after Modifiy Space"}
