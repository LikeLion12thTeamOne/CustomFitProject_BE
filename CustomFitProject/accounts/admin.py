from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Keyword

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields': (
                    'keyword',
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Keyword)
