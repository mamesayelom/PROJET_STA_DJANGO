from django.contrib import admin

from .models import Entry, Category


class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)