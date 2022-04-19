from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str
    disabled: bool

