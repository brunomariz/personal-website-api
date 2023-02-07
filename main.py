from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import file, resources, health_check

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_check.router)
app.include_router(file.router)
app.include_router(resources.router)


@app.get("/")
async def root():
    return {"message": "Hello!"}

