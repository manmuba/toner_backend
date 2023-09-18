from django.contrib import admin
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import PersonalInformation

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('display_user_emails', 'name', 'address_type', 'phone')
    search_fields = ( 'user__email', 'name', 'address_type', 'phone')
    list_filter = ('user__email', 'name', 'address_type', 'phone')
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

    def display_user_emails(self, obj):
        return obj.user.email

    display_user_emails.short_description = 'User Emails'

admin.site.register(PersonalInformation, PersonalInfoAdmin)