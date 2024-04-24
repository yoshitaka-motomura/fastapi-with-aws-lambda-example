from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
async def about():
    return {"message": "About"}


@app.get("/contact")
async def contact():
    return {"message": "Contact"}


handler = Mangum(app)