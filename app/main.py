"""The main script for the app"""
from fastapi import FastAPI


app = FastAPI(title="MySQL CRUD", description="A simple app to perform CRUD operations on MySQL")


@app.get("/", name="Root", description="The root endpoint for the app", tags=['Root'])
async def root_endpoint() -> dict[str, str]:
    """The root endpoint for the app"""
    return {"message": "Hello World"}