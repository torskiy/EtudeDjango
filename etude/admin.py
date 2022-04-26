from django.contrib import admin
from .models import *


# Register your models here.


class CasePhotoInline(admin.TabularInline):
    model = CasePhoto
    extra = 3


class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        ('Превью', {'fields': ['description', 'title_image']}),
        ('Контент', {'fields': ['video', 'content']}),
        (None, {'fields': ['is_published']})
    ]
    inlines = [CasePhotoInline]
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'position', 'is_published', 'main_contact')
    list_display_links = ('name', 'second_name', 'position')
    list_editable = ('is_published', 'main_contact')


admin.site.register(Case, CaseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(StaticData)
