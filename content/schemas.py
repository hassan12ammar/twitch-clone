# serializers.py
from ninja import Schema

from authentication.schemas import ProfileOut


class VideoIn(Schema):
    title: str
    description: str

class VideoUpdate(VideoIn):
    id: int

class VideoOut(VideoIn):
    id: int

    profile: ProfileOut
    video_file: str
