from django.contrib import admin
from .models import User, Permission
from django.utils.translation import ugettext_lazy as _


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('nome', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass
