from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    financial_institution = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    asset = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rate = models.FloatField()
    maturity_date = models.DateField()
    amount = models.FloatField()

    def amount_in_aed(self):
        # Fetch latest AED conversion rate (you can use an API)
        aed_rate = 3.67  # Example rate
        return self.amount * aed_rate

    def amount_in_inr(self):
        # Fetch latest INR conversion rate (you can use an API)
        inr_rate = 75.0  # Example rate
        return self.amount * inr_rate

    def __str__(self):
        return self.title