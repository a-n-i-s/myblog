from django.contrib import admin

from .models import UserSetting,AdminSetting,AuthorSetting

# Register your models here.
@admin.register(UserSetting)
class UserSettingAdmin(admin.ModelAdmin):
    pass
 
@admin.register(AdminSetting)
class AdminSettingAdmin(admin.ModelAdmin):
    pass
 
@admin.register(AuthorSetting)
class AuthorSettingAdmin(admin.ModelAdmin):
    pass
  