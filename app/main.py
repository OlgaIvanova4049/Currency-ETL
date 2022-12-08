import uvicorn
from fastapi import FastAPI

from routers import api_router


def create_app():
    app_ = FastAPI()
    app_.include_router(api_router)
    return app_


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
