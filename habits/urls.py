from django.urls import path

from habits.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = "habits"


urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
