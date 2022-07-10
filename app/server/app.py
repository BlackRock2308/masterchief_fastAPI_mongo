from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.recipe import router as RecipeRouter


app = FastAPI()

app.include_router(RecipeRouter, tags=["Recipe"], prefix="/recipe")



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


