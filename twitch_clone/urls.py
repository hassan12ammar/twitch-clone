from ninja import NinjaAPI
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
# local models
from authentication.controllers import auth_controller, profile_controller
from content.controllers import video_controller
from twitch_clone.settings import MEDIA_ROOT, MEDIA_URL

api = NinjaAPI(title="Twitch-Clone Backend")

api.add_router("auth", auth_controller, tags=["Auth"])
api.add_router("profile", profile_controller, tags=["Profile"])
api.add_router("content", video_controller, tags=["Content"])

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
