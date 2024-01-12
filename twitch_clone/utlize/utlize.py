from typing import Union
from rest_framework import status
from django.contrib.auth import get_user_model
from .custom_classes import Error
from authentication.models import Profile
from authentication.schemas import MessageOut

User = get_user_model()


def get_user(email: str) -> Union[User, Error]:
    """
    Get user by email.
    Returns:
    - User object if user exists.
    - Error object (HTTP status, message dictionary) if user does not exist.
    """
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return Error(status.HTTP_404_NOT_FOUND, MessageOut(detail="User not found"))


def get_user_profile(email: str) -> Union[Profile, Error]:
    """
    Get user profile by email.
    Returns:
    - Profile object if user and profile exist.
    - Error object (HTTP status, message dictionary) if user or profile does not exist.
    """
    try:
        user = User.objects.get(email=email)
        user_profile = user.profile_user
        return user_profile
    except User.DoesNotExist:
        return Error(status.HTTP_404_NOT_FOUND, MessageOut(detail="User not found"))
    except Profile.DoesNotExist:
        return Error(status.HTTP_404_NOT_FOUND, MessageOut(detail="Profile not found"))


def normalize_email(email: str) -> str:
    """
    Normalize email by stripping, lowercasing, and removing spaces.
    """
    return email.strip().lower().replace(" ", "")
