import time
from fastapi import Request, HTTPException

# Simple in‑memory sliding window - NOT production ready
RATE_LIMIT = 5  # requests per minute per client IP
_clients = {}

async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    now = time.time()
    timestamps = _clients.get(client_ip, [])
    # keep only timestamps within last 60 seconds
    timestamps = [t for t in timestamps if now - t < 60]
    if len(timestamps) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail='Rate limit exceeded')
    timestamps.append(now)
    _clients[client_ip] = timestamps
    return await call_next(request)
