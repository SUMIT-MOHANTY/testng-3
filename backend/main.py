from fastapi import FastAPI
from backend.auth.security import verify_jwt
from backend.claims import claims_router

app = FastAPI()
app.include_router(claims_router, prefix="/api/v1")
