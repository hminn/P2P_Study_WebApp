from django.urls import path
from . import views

app_name = "feedbacks"
urlpatterns = [
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    path("feedback/<str:user_id>/", views.avatar_detail, name="avatar_feedback"),
]
