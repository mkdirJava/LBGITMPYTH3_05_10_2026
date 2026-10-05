from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
def get_item(id: int, q: str | None = None):
    return {"id": id, "query": q}