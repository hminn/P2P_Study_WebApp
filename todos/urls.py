from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("todolist/", views.TodoListView.as_view(), name="todolist"),
    path("timetable/", views.TimeTableView.as_view(), name="timetable"),
    path("timetable/<str:user_id>/", views.avatar_detail, name="avatar_timetable"),
]
