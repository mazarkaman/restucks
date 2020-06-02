from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from users.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["-id"]
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('email',)
    search_fields = ['email', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
                                         'last_name',
                                         )}),
        (_('Permissions'), {
            'fields': (
                'role',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'),
        }),
        (_('Dates'), {'fields': ['register_date', 'last_login']}),
    )
    add_fieldsets = (
        (None, {
            'classes': ['wide'],
            'fields': ('email',
                       'password1',
                       'password2',
                       'first_name',
                       'last_name',
                       'is_mobile_verified')}),
    )
    readonly_fields = ('last_login', 'register_date')
    exclude = ['']


admin.site.register(User, UserAdmin)
