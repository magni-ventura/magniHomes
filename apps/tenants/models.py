from django.db import models

# Create your models here.
from django.db import models

class Tenant(models.Model):
    """
    A model representing a tenant in the real estate application.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=255)
    employer = models.CharField(max_length=255, blank=True, null=True)
    current_address = models.TextField()
    move_in_date = models.DateField()
    lease_term_months = models.IntegerField()
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_relationship = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
