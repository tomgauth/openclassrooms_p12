from django.db import models
from accounts.models import User, Client



# Create your models here.
class Contract(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return f"{self.client} | €{self.amount} | {self.payment_due}"


class EventStatus(models.Model):

    EVENT_STATUS = [
        ('incoming', 'incoming'),
        ('past', 'past')
    ]

    status = models.CharField(choices=EVENT_STATUS, max_length=25)

    def __str__(self):
        return f"{self.status}"


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()


    def __str__(self):
        return f"{self.client} | {self.event_date} | {self.notes}"