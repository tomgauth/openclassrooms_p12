from django.contrib import admin
from crm.models import Contract, EventStatus, Event

# Register your models here.
admin.site.register(Contract)
admin.site.register(EventStatus)
admin.site.register(Event)
