from typing import List, Optional
from django.db import transaction
from ninja import UploadedFile
from rest_framework import status
from django.shortcuts import get_object_or_404
from authentication.schemas import MessageOut
from django.core.files.base import ContentFile

#
from content.models import Video
from content.schemas import VideoIn, VideoOut
from twitch_clone.utlize.custom_classes import Error
from twitch_clone.utlize.utlize import get_user_profile, normalize_email


def create_video_service(request, video_in: VideoIn, video_file: UploadedFile):
    email = normalize_email(request.auth)
    profile = get_user_profile(email)

    if isinstance(profile, Error):
        return profile.status, profile.message

    video = Video.objects.create(
        title=video_in.title, description=video_in.description, profile=profile
    )

    file_name = f"{video.id}_{video_file.name}"
    video.video_file.save(file_name, ContentFile(video_file.read()))
    video.save()

    return status.HTTP_201_CREATED, video


def get_all_videos_service(request) -> List[VideoOut]:
    return status.HTTP_200_OK, Video.objects.all().select_related("profile")


def get_video_service(request, video_id: int) -> VideoOut:
    return status.HTTP_200_OK, get_object_or_404(Video, pk=video_id)


def update_video_service(request, video_id: int, video_in: VideoIn, video_file: Optional[UploadedFile]) -> VideoOut:
    email = normalize_email(request.auth)
    user_prfile = get_user_profile(email)

    video_profile = get_object_or_404(Video, pk=video_id).profile

    if video_profile != user_prfile:
        return status.HTTP_401_UNAUTHORIZED, MessageOut(
            message="UNAUTHORIZED to update the specified content"
        )
    
    Video.objects.update(title=video_in.title, description=video_in.description)
    video = Video.objects.filter(id=video_id).first()

    if video:
        file_name = f"{video.id}_{video_file.name[:10]}{video_file.name[-5:]}"
        video.video_file.save(file_name, ContentFile(video_file.read()))
        video.save()

    return status.HTTP_200_OK, video


def delete_video_service(request, video_id: int) -> MessageOut:
    video = get_object_or_404(Video, pk=video_id)
    video.delete()
    return status.HTTP_200_OK, MessageOut(detail="Video deleted successfully")

