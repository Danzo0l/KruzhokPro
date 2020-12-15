from .models import user
from django.forms import ModelForm, TextInput

class userform(ModelForm):
    class Meta:
        model = user
        fields = ['talent', 'mail', 'epicid', 'overwatchname']
        widgets = {
            "talent": TextInput(attrs={
                'class': 'inp',
                "placeholder": 'Enter your TalentID'
            }),
            "mail": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your mail'
            }),
            "epicid": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your epicid'
            }),
            "overwatchname": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your overwatchname'
            }),
        }