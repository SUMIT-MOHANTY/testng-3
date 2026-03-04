from typing import Optional
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

class AzureKeyVaultSecrets:
    def __init__(self, vault_url: str, client_id: str, client_secret: str):
        self.vault_url = vault_url
        self.credential = ClientSecretCredential(
            tenant_id=os.getenv("TENANT_ID", "your-tenant-id"),
            client_id=client_id,
            client_secret=client_secret,
        )
        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)

    def get_secret(self, name: str) -> Optional[str]:
        try:
            secret = self.client.get_secret(name)
            return secret.value
        except Exception:
            return None
