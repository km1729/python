from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, Main Page"}

@app.get("/hello")
async def root():
    return {"message": "Hello"}