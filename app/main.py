from fastapi import FastAPI
from app.routers import router

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"status": "alive"}

subapi =  FastAPI()
subapi.include_router(router.router)
app.mount("/v1",subapi)

