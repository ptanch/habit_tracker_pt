from django.contrib import admin


from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant",
        "related_habit",
        "periodicity",
        "reward",
        "execution_time",
        "is_public",
    )
