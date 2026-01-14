from fastapi import FastAPI
import uvicorn
from api import controller

app = FastAPI(title="UK Rock Assistant Model", version="0.0.1")
app.include_router(controller.router, prefix="/api/v1")
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
