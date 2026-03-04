from fastapi import FastAPI
from .routers import loan

app = FastAPI(title='Loan Service')
app.include_router(loan.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
