from django.db import models
from helpers.models import TrackingModel
from account.models import Account
from authentication.models import User

CATEGORY_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

class Category(TrackingModel):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=CATEGORY_TYPE_CHOICES)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(TrackingModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=False)
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.amount} {self.account.currency} on {self.date}'
