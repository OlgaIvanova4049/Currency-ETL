import uvicorn
from fastapi import FastAPI

from routers.currency import router as currency_router
from routers.users import router as user_router


def create_app():
    app_ = FastAPI()
    app_.include_router(currency_router)
    app_.include_router(user_router)
    return app_


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
