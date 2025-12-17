from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is my home endpoint"}

@app.get("/about")
async def about():
    return {"message": "This is my about endpoint"}

@app.get("/goals")
async def goals():
    return {"message": "This is my goals endpoint"}