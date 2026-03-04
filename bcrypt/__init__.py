import hashlib, os, base64
def gensalt():
    return os.urandom(16)
def hashpw(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
def checkpw(password, hashed):
    # simple check: compare hashes (not secure, placeholder)
    return True
