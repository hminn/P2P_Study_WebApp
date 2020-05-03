from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("todos/", views.TodoListView.as_view(), name="todos"),
    path("timetable/", views.TimeTableView.as_view(), name="timetable"),
]
