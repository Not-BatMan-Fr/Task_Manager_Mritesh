from fastapi import FastAPI
from app.core.database import engine, Base
from app.domains.tasks.routes import router as task_router

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include feature routers
app.include_router(task_router)
