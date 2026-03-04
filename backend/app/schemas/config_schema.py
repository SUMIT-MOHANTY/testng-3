from pydantic import BaseModel

class ConfigResponse(BaseModel):
    LOG_ENDPOINT: str
