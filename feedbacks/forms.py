from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "contents",
        ]
        labels = {
            "contents": "",
        }
        widgets = {
            "contents": forms.Textarea(attrs={"placeholder": "피드백을 입력해주세요."}),
        }
