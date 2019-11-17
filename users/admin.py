from django.contrib import admin

# Register your models here.
# from .models import Profile
#
# admin.site.register(Profile)
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'image']


admin.site.register(CustomUser, CustomUserAdmin)
