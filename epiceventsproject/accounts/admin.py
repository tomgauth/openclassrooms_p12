from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.




admin.site.register(User, UserAdmin)