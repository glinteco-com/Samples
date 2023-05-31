from pydantic import BaseModel

fake_users_db = {
    "joevu": {
        "username": "joevu",
        "full_name": "Joe Vu",
        "email": "joevu@glinteco.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "snowy": {
        "username": "snowy",
        "full_name": "Alice Wonderson",
        "email": "snowy@glinteco.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


def fake_hash_password(password: str):
    return "fakehashed" + password
