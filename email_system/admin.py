from django.contrib import admin
from email_system.models import Event, Employee, EventType

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)

    admin.site.register(Event)
    admin.site.register(Employee)
    admin.site.register(EventType)
