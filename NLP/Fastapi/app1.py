from fastapi import FastAPI

# Initialize the FastAPI instance
app = FastAPI(title="AI Engineer Entrypoint")

@app.get("/")
def home():
    return {"message": "AI Inference Server is live!"}
