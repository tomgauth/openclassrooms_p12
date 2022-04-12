from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

    

class User(AbstractUser):
    # Refacto
    SALES = "sales_member"    
    SUPPORT = "support_member"
    ADMIN = "admin"
    ROLE_CHOICES = (
        (SALES, "sales_member"),        
        (SUPPORT, "support_member"),
        (ADMIN, "admin_member")
    )
    email = models.EmailField(unique=True, max_length=100,  null=True, blank=True)
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='NONE', null=True, blank=True)

    def __str__(self):
        return f"{self.email} | {self.role} | id: {self.id}"
    


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"