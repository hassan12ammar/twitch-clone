from typing import List
from ninja import Router
from twitch_clone.utlize.auth_utils import CustomAuth
from .services import (
    signup_service,
    signin_service,
    get_all_profiles_service,
    get_profile_service,
    create_profile_service,
    edit_profile_service,
)
from .schemas import (
    AuthOut,
    MessageOut,
    ProfileIn,
    ProfileOut,
    SigninIn,
    SigninUpIn,
    SigninUpOut,
)

auth_controller = Router()
profile_controller = Router()


@auth_controller.post(
    "signup",
    response={
        201: SigninUpOut,
        400: MessageOut,
    },
)
def signup(request, account_in: SigninUpIn):
    """
    Register a new user.
    """
    return signup_service(account_in)


@auth_controller.post(
    "signin",
    response={
        200: AuthOut,
        404: MessageOut,
        400: MessageOut,
    },
)
def signin(request, account_in: SigninIn):
    """
    Authenticate and sign in a user.
    """
    return signin_service(account_in)


@profile_controller.get(
    "get_all_profile",
    response={
        200: List[ProfileOut],
    },
)
def all_profile(request):
    """
    Get a list of all user profiles.
    """
    return get_all_profiles_service()


@profile_controller.get(
    "get_profile",
    response={
        200: ProfileOut,
        404: MessageOut,
        400: MessageOut,
    },
    auth=CustomAuth(),
)
def get_profile(request):
    """
    Get the profile of the authenticated user.
    """
    return get_profile_service(request)


@profile_controller.post(
    "create_profile",
    response={
        200: ProfileOut,
        404: MessageOut,
        409: MessageOut,
        400: MessageOut,
    },
    auth=CustomAuth(),
)
def create_profile(request, profile_in: ProfileIn):
    """
    Create a new profile for the authenticated user.
    """
    return create_profile_service(request, profile_in)


@profile_controller.post(
    "edit_profile",
    response={
        200: ProfileOut,
        404: MessageOut,
        400: MessageOut,
    },
    auth=CustomAuth(),
)
def edit_profile(request, profile_in: ProfileIn):
    """
    Edit the profile of the authenticated user.
    """
    return edit_profile_service(request, profile_in)
