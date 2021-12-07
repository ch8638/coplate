from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)  # UserAdmin class는 User 모델에 대해서 특별한 인터페이스를 제공한다.
# User 모델의 추가 field는 기본적으로 admin 페이지에 나타나지 않기 때문에 따로 추가해야 한다.
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)  # custom fields 섹션 아래에 nickname field 추가
