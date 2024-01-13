# controllers.py

from typing import List, Optional
from ninja import File, Router, UploadedFile
from authentication.schemas import MessageOut

from twitch_clone.utlize.auth_utils import CustomAuth

from .services import (
    create_video_service,
    get_all_videos_service,
    get_video_service,
    update_video_service,
    delete_video_service,
)
from .schemas import (
    VideoIn,
    VideoOut,
)

video_controller = Router()


@video_controller.post(
    "create_video",
    response={
        201: VideoOut,
        400: MessageOut,
        404: MessageOut,
    },
    auth=CustomAuth(),
)
def create_video(request, video_in: VideoIn, file: UploadedFile):
    return create_video_service(request, video_in, file)


@video_controller.get(
    "get_all_videos",
    response={
        200: List[VideoOut],
    },
    # auth=CustomAuth(),
)
def get_all_videos(request):
    return get_all_videos_service(request)


@video_controller.get(
    "get_video/{video_id}",
    response={
        200: VideoOut,
        404: MessageOut,
    },
    # auth=CustomAuth(),
)
def get_video(request, video_id: int):
    return get_video_service(request, video_id)


@video_controller.patch(
    "update_video/{video_id}",
    response={
        200: VideoOut,
        404: MessageOut,
        400: MessageOut,
    },
    auth=CustomAuth(),
)
def update_video(request, video_id: int, video_in: VideoIn, file: Optional[UploadedFile]=File(...)):
    return update_video_service(request, video_id, video_in, file)


@video_controller.delete(
    "delete_video/{video_id}",
    response={
        200: MessageOut,
        404: MessageOut,
    },
    auth=CustomAuth(),
)
def delete_video(request, video_id: int):
    return delete_video_service(request, video_id)
