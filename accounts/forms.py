from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from accounts.models import Helper
from django.contrib.auth.models import User
from accounts.cities import city
class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ["username", "first_name", "last_name","email", "password1", "password2"]
        model = User



class HelperCreateForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields=('phone','availability','city')


class RequestForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.ChoiceField(choices=city, required=True)

