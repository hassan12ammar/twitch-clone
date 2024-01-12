from rest_framework import status
from django.contrib.auth import get_user_model
# local files
from twitch_clone.utlize.auth_utils import create_token
from twitch_clone.utlize.custom_classes import Error
from twitch_clone.utlize.utlize import (
    get_user_profile,
    normalize_email,
)
from .models import Profile
from .schemas import (
    AuthOut,
    MessageOut,
    ProfileIn,
    ProfileOut,
    SigninIn,
    SigninUpIn,
    SigninUpOut,
)

User = get_user_model()


def signup_service(account_in: SigninUpIn):
    if account_in.password1 != account_in.password2:
        return status.HTTP_400_BAD_REQUEST, MessageOut(detail="Passwords do not match")

    email = normalize_email(account_in.email)

    if User.objects.filter(email=account_in.email).exists():
        return status.HTTP_400_BAD_REQUEST, MessageOut(detail="Email is already in use")

    user = User.objects.create_user(email=email, password=account_in.password1)
    profile = Profile.objects.create(user=user, name=account_in.name)
    token = create_token(user)

    return status.HTTP_201_CREATED, SigninUpOut(token=token, user=user, name=profile.name)


def signin_service(account_in: SigninIn):
    email = normalize_email(account_in.email)

    user_exists = User.objects.filter(email=email).exists()
    if not user_exists:
        return status.HTTP_404_NOT_FOUND, MessageOut(detail="User is not registered or Email is wrong")

    user = User.objects.filter(email=email).first()

    valid_password = user.check_password(account_in.password)
    if not valid_password:
        return status.HTTP_400_BAD_REQUEST, MessageOut(detail="Wrong password")

    token = create_token(user)
    return status.HTTP_200_OK, AuthOut(token=token, user=user)


def get_all_profiles_service():
    return status.HTTP_200_OK, Profile.objects.all().select_related("user")


def get_profile_service(request):
    email = normalize_email(request.auth)
    profile = get_user_profile(email)

    if isinstance(profile, Error):
        return profile.status, profile.message

    return status.HTTP_200_OK, profile


def create_profile_service(request, profile_in: ProfileIn):
    email = normalize_email(request.auth)

    user_exists = User.objects.filter(email=email).exists()
    if not user_exists:
        return status.HTTP_404_NOT_FOUND, MessageOut(detail="User is not registered or Email is wrong")

    user = User.objects.filter(email=email).first()

    profile_exists = Profile.objects.filter(user=user).exists()
    if profile_exists:
        return status.HTTP_409_CONFLICT, MessageOut(detail="Profile already exists")

    profile = Profile.objects.create(user=user, name=profile_in.name)
    profile.save()

    return status.HTTP_200_OK, profile


def edit_profile_service(request, profile_in: ProfileIn):
    email = normalize_email(request.auth)
    profile = get_user_profile(email)

    if isinstance(profile, Error):
        return profile.status, profile.message

    profile.name = profile_in.name
    profile.save()

    return status.HTTP_200_OK, profile
