from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('INR', 'Indian Rupee'),
    ('UAH', 'Ukrainian Hryvnia'),
    ('PLN', 'Polish Złoty'),
]

class Account(TrackingModel):
    name = models.CharField(max_length=255)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
