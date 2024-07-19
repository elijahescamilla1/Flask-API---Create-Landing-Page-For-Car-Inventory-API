import secrets

def generate_token():
    return secrets.token_hex(16)

def verify_token(token):
    # Code to verify the token
    pass
