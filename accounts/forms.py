from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AdminUserCreationForm,
)
from .models import CustomUser


# the book is outdated here as well, i needed to subclass AdminuserCreationForm instead of UserCreationForm:
# link to the stack_overflow code below:
# https://stackoverflow.com/questions/79333449/django-fielderror-unknown-fields-usable-password-specified
class CustomUserCreationForm(AdminUserCreationForm):

    # inherit parent Meta class
    class Meta(UserCreationForm.Meta):
        model = CustomUser

        # add custom field to default fields
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = "__all__"
