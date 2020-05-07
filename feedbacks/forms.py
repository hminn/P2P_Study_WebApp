from django import forms
from .models import Feedback


class FeedbackForm(forms.Form):
    feedback = forms.CharField(
        label=" ",
        label_suffix=" ",
        disabled=False,
        initial="Today Feedback",
        widget=forms.Textarea,
    )

    def save(self, commit=True):
        post = Feedback(**self.cleaned_data)
        if commit:
            post.save()
        return post
