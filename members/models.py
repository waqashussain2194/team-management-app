from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
