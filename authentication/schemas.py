from ninja import Schema
from typing import Optional
from pydantic import EmailStr, Field


# General Schemas
class MessageOut(Schema):
    detail: str


# Authentication Schemas
class UserIn(Schema):
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str = Field(min_length=8)


class TokenOut(Schema):
    access: str


class UserOut(Schema):
    email: EmailStr


class AuthOut(Schema):
    token: TokenOut
    user: UserOut


class SigninIn(Schema):
    email: EmailStr
    password: str


class SigninUpIn(UserIn):
    name: str


class SigninUpOut(AuthOut):
    name: str


# Profile Schemas
class ProfileSchema(Schema):
    name: str


class ProfileIn(ProfileSchema):
    ...


class ProfileOut(ProfileIn):
    name: str
    user: UserOut


class ProfileSchemaUpdate(ProfileIn):
    pass


class ProfileDelete(Schema):
    pass
