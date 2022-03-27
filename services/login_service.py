from fastapi import HTTPException
from models.login import Login
from models.user import User

fake_login_table = {"username": ["admin"], "password": ["admin_"]}


def example_login_service():
    return {"message": "login screen"}


def login(login_info: Login):
    if (
        login_info.username == fake_login_table["username"][0]
        and login_info.password == fake_login_table["password"][0]
    ):
        return User(username="admin")
    else:
        raise HTTPException(status_code=400, detail="invalid login")
