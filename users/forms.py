from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]