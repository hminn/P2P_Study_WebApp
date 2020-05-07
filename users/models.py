from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    total_penalty = models.PositiveIntegerField(default=0, null=True)
    today_penalty = models.PositiveIntegerField(default=0, null=True)
    penalty_checked = models.BooleanField(default=False)

    # 벌금 집계를 위한 메소드 : 전체 벌금에 오늘 벌금을 반영
    # (1) Feedback Page : check 버튼을 눌렀을 때 실행
    def reset_penalty(self):
        if not self.penalty_checked:
            self.total_penalty += self.today_penalty
            self.today_penalty = 0
            self.save()
        return
