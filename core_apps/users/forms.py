from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User

class UserCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')
    error_messages = {
        "duplicate_email": "A user with the same email address already exists"
    }

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])