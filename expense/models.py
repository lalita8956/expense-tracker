from django.db import models
from django.utils import timezone

class Expense(models.Model):
    UNIT_CHOICES = [
        ('Kilogram', 'Kilogram'),
        ('Gram', 'Gram'),
        ('Litre', 'Litre'),
        ('Millilitre', 'Millilitre'),
        ('Pieces', 'Pieces'),
        ('Meter', 'Meter'),
        ('Centimeter', 'Centimeter'),
        ('Nos', 'Nos'),
    ]

    CATEGORY_CHOICES = [
        ('food', 'Food & Drinks'),
        ('transport', 'Transport'),
        ('bills', 'Bills & Utilities'),
        ('entertainment', 'Entertainment'),
        ('shopping', 'Shopping'),
        ('health', 'Health & Fitness'),
        ('education', 'Education'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)           
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create = models.DateTimeField(default=timezone.now)

    @property
    def total(self):
        return self.quantity * self.amount

    def __str__(self):
        return f"{self.name} - ₹{self.total}"

    