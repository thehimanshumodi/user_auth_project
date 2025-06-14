from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(required=True, help_text='Required.')
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email', 'profile_picture',
            'address_line1', 'city', 'state', 'pincode', 'user_type'
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    # No extra fields needed, Django's default AuthenticationForm handles username/password
    pass