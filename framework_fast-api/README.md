```
pip install fastapi
pip install uvicorn

  WARNING: The script uvicorn is installed in '/home/k/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
create a main.py
```
#main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, Main Page"}

@app.get("/hello")
async def root():
    return {"message": "Hello"}
```

Run the following command in a terminal 
```
uvicorn main:app --reload
```

URLs
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/openapi.json
```
