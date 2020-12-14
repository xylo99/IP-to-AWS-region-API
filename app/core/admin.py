from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'region']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'region')}),
        (
            'Permissions',
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        )
    )


add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2', 'region')
    }),
)

admin.site.register(models.User, UserAdmin)
