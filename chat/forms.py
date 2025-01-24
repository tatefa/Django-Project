from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    """
    Custom form for user registration, extending Django's default UserCreationForm.
    """
    pass

class LoginForm(AuthenticationForm):
    """
    Custom form for user login, extending Django's default AuthenticationForm.
    """
    pass
