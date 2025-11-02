from django.urls import path
from . import views

urlpatterns = [
    path('', views.reaper_profile, name="reaper_profile")
]
