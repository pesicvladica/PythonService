from fastapi import FastAPI
from app.api.v1.routes import users
from app.core.database import Base, engine

# Initialize database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/api/v1", tags=["users"])
