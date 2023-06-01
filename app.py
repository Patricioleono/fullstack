from fastapi import FastAPI
from routes.images import images
from routes.cats import cats


app = FastAPI()

app.include_router(images)
app.include_router(cats)