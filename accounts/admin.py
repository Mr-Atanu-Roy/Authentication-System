from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'created_at', 'updated_at')
    search_fields = ['user']
    
class ProfileInline(admin.TabularInline):
    model = Profile
    
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'is_staff', 'date_joined')
    
    fieldsets = (
        ("User Details", {
            "fields": (
                ['email', 'first_name', 'last_name']
            ),
        }),
        ("More Details", {
            "fields": (
                ['date_joined', 'last_login']
            ), 'classes': ['collapse']
        }),
        ("Permissions", {
            "fields": (
                ['is_staff', 'is_superuser', 'is_active', 'user_permissions', 'groups']
            ),
        }),
    )
    
    inlines = [ProfileInline]

    search_fields = ['username', 'first_name']


admin.site.register(ResetPassword)

admin.site.register(Profile, AdminProfile)

admin.site.unregister(User)
admin.site.register(User, AdminUser)