from fastapi import Header

def get_user(x_user: str = Header(default="anonymous")):
    return x_user