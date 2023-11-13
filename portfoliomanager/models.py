from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    """Represents stocks or options"""
    underlying = models.CharField(max_length=20)
    symbol = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True) # Change this with JS. If stock->True, else False.
    strike = models.FloatField(blank=True, null=True) # Change this with JS
    quantity = models.IntegerField(default=0)
    
    SIDE = (
        ('S', 'Short'),
        ('L', 'Long'),
    )

    INSTRUMENT_TYPE = (
        ('C', 'Call'),
        ('P', 'Put'),
        ('S', 'Stock'),

    )

    side = models.CharField(
        max_length = 1,
        choices = SIDE,
        help_text = "Short or Long"
    )

    type = models.CharField(
        max_length=1,
        choices=INSTRUMENT_TYPE,
        help_text = 'Stock or Option Type: Stock, Put, or Call',
    )


    class Meta:
        ordering = ['expiration_date']



    def __str__(self):
        return f"{self.symbol} "
    
    def get_absolute_url(self):
        return reverse("model-detail-view", args=[str(self.id)])



    