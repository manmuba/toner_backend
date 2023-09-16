from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')  # Fields to display in the user list
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # Filter options on the right sidebar
    search_fields = ('email', 'first_name', 'last_name')  # Add search functionality
    ordering = ('-date_joined',)  # Sort users by date joined, with the most recent first

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        # Add any additional fieldsets you want to display
    )

    # Customize the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    # Add any additional readonly_fields as needed
    readonly_fields = ('last_login', 'date_joined')

    # Customize the change user form
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields

admin.site.register(CustomUser, CustomUserAdmin)