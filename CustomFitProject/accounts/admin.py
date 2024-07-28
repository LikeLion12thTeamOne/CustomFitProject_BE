from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'gender', 'disease', 'height', 'weight', 'average_rating')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('age', 'gender', 'disease', 'height', 'weight')

admin.site.register(CustomUser, CustomUserAdmin)
