
from django.contrib import admin

from .models import Tag, Scope


class RelationshipInline(admin.TabularInline):
    model = Scope


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]