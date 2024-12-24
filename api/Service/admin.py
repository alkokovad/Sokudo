from django.contrib import admin
from .models import Meet


@admin.register(Meet)
class MeetAdmin(admin.ModelAdmin):
    pass
