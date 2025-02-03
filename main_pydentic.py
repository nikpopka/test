from pydantic import BaseModel, Field, EmailStr, ConfigDict

from fastapi import FastAPI

data = {
    "email": "acb@mail.ru",
    "bio": "qwdqwdqdw",
    "age": 12,
    "name": "nik"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=100)


user = UserSchema(**data)

print(repr(user))
