from backend.api.v1 import policies, claims
app.include_router(policies.router)
app.include_router(claims.router)
