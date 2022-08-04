from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # set hashing algorithm

def hash(password: str):
    return pwd_context.hash(password)