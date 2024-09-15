from django import forms
from app.models import UrlModel

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url']
