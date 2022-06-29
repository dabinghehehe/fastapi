from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    user:list[int]


def index(age: int):

    return {"age": age}


def login(data: Login):
    return data
