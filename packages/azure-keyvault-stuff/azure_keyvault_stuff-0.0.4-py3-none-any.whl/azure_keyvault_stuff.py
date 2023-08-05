def getClient(vault_name, credential):
    """
    Returns a SecretClient object for the specified vault.

    Args:
        vault_name (str): The name of the vault.
        credential (TokenCredential): The credential to use for authentication. Should usually be from azure.identity.DefaultAzureCredential().
    Returns:
        SecretClient: A SecretClient object for the specified vault.
        
    """
    from azure.keyvault.secrets import SecretClient
    
    KVUri = f"https://{vault_name}.vault.azure.net"
    return SecretClient(vault_url=KVUri, credential=credential)

def getSecret(client, secret_name):
    """
    Returns the value of the specified secret.
    
    Args:
        client (SecretClient): The SecretClient object to use.
        secret_name (str): The name of the secret.
    Returns:
        str: The value of the secret.
    
    """
    secret = client.get_secret(secret_name)
    return secret.value

def setSecret(client, secret_name, secret_value):
    """
    Sets the value of the specified secret.

    Args:
        client (SecretClient): The SecretClient object to use.
        secret_name (str): The name of the secret.
        secret_value (str): The value of the secret.
    Returns:
        str: The value of the secret.
    
    """
    client.set_secret(secret_name, secret_value)
    return secret_value

def deleteSecret(client, secret_name):
    """
    Deletes the specified secret.

    Args:
        client (SecretClient): The SecretClient object to use.
        secret_name (str): The name of the secret.
    Returns:
        DeletedSecret: The deleted secret.

    """
    poller = client.begin_delete_secret(secret_name)
    deleted_secret = poller.result()
    return deleted_secret