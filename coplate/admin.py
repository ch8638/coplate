from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)  # UserAdmin class는 User 모델에 대해서 특별한 인터페이스를 제공한다.
