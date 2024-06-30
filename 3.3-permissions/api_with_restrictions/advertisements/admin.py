from django.contrib import admin

# Register your models here.

from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', "description", "creator", "status", "created_at"]
    list_filter = ["title", "status", "created_at"]
    readsonly_fields = ["creator"]

