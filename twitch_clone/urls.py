from ninja import NinjaAPI
from django.urls import path
from django.contrib import admin
# local models
from authentication.controllers import auth_controller, profile_controller

api = NinjaAPI(title="Twitch-Clone Backend")

api.add_router("auth", auth_controller, tags=["Auth"])
api.add_router("profile", profile_controller, tags=["Profile"])

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
