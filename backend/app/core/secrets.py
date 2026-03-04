class SecretsProvider:
    def __init__(self):
        pass  # In real implementation, initialise Azure Key Vault client

    def get(self, name: str) -> str:
        raise NotImplementedError("Key Vault integration not implemented in this mock")
