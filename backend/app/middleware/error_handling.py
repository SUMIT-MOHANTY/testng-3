from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from ..core.logger import logger

async def error_handling_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except HTTPException as exc:
        logger.error(f"HTTPException: {exc.detail}")
        return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})
    except Exception as exc:
        logger.exception('Unhandled exception')
        return JSONResponse(status_code=500, content={'detail': 'Internal Server Error'})
