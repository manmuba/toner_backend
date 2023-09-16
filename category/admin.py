from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

admin.site.register(Category, CategoryAdmin)
