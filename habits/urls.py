from django.urls import path
from rest_framework.urls import app_name

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = "habits"


urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/", HabitListAPIView.as_view(), name="habit-list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habit/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
