from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm


# inherit from AdminUserCreationForm, not just UserCreationForm
# otherwiser you'll get missing field `usable_password` error.
# also, every fucking class can be imported but not AdminUserCreationForm
class CustomUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = get_user_model()
        fields = ["email", "username"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]
