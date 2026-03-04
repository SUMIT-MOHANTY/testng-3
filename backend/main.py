import uvicorn
from .app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('backend.main:app', host='0.0.0.0', port=8000, reload=False)
    uvicorn.run(app, host='0.0.0.0', port=8000)
from fastapi import FastAPI
from backend.auth.security import verify_jwt
from backend.claims import claims_router

app = FastAPI()
app.include_router(claims_router, prefix="/api/v1")
