from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from core.config import settings
from routers import story, job
from db.database import create_tables

create_tables()

app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="api to create cool stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix="/api")
app.include_router(job.router, prefix="/api")

if __name__ == "__main__":
    import os
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
    # port = int(os.getenv("PORT", 8001))  # default 8000, can override with env var
    # uvicorn.run(app, host="0.0.0.0", port=port)