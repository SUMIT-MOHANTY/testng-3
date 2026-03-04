import os
from pydantic import BaseSettings, Field
from .core.secrets import AzureKeyVaultSecrets

class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI Azure KV Demo")
    key_vault_url: str = Field(default=os.getenv("KEY_VAULT_URL", "your-key-vault-url"))
    client_id: str = Field(default=os.getenv("CLIENT_ID", "your-client-id"))
    client_secret: str = Field(default=os.getenv("CLIENT_SECRET", "your-client-secret"))

    # Load secrets lazily from Azure Key Vault
    @property
    def secret_value(self) -> str:
        kv = AzureKeyVaultSecrets(self.key_vault_url, self.client_id, self.client_secret)
        return kv.get_secret("my-secret")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
