from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("base/", views.TodoListingView.as_view(), name="base"),
]
