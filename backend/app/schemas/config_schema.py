from pydantic import BaseModel

class ConfigResponse(BaseModel):
    app_name: str
    key_vault_url: str
