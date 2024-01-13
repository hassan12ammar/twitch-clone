from django.db import models
from authentication.models import Profile


class Video(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title
