from starlette.requests import Request
from starlette.responses import Response
import time
from ..core.logger import logger

async def logging_middleware(request: Request, call_next):
    start = time.time()
    response: Response = await call_next(request)
    process_time = (time.time() - start) * 1000
    logger.info(
        f"{request.method} {request.url.path} completed in {process_time:.2f}ms "
        f"status={response.status_code}")
    return response
