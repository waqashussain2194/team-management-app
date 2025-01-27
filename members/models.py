from django.db import models
from django.core.validators import RegexValidator

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
            message="Phone number must be entered in the format: '(999) 999-9999' or '999-999-9999' or '9999999999'. Up to 10 digits allowed."
        )]
    )
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
