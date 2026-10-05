from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/items")
def get_items():
    return []

@app.post("/items")
def create_item():
    return {"status": "created"}

@app.post("/items", status_code=201)
def create_item():
    return {"message": "Item created"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)