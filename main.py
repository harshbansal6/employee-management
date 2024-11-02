from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from core import config
from app.routes.routes import router
from core.middlewares.database import database_middleware
from core.middlewares.settings import settings_middleware

app = FastAPI(title=config.PROJECT_NAME)


def get_application() -> FastAPI:
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app.include_router(router, prefix='/api')

app.middleware('http')(settings_middleware(app))
app.middleware('http')(database_middleware(app))


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=7800)