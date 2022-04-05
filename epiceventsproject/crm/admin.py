from django.contrib import admin
from crm.models import Customer, Contract, EventStatus, Event

# Register your models here.
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(EventStatus)
admin.site.register(Event)
