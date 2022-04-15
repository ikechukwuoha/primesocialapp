from django import forms
from .models import Prime

class PrimeForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "What's on your mind...",
                "class": "textarea is-success is-small",
            }
        ),
        label="",
    )

    class Meta:
        model = Prime
        exclude = ("user", )