from django.db import models
from django.urls import reverse


class Instrument(models.Model):
    """Represents stocks or options"""
    underlying = models.CharField(max_length=20)
    symbol = models.CharField(max_length=32)
    expiration_date = models.DateField()
    strike = models.FloatField()

    INSTRUMENT_TYPE = (
        ('C', 'Call'),
        ('P', 'Put'),
        ('S', 'Stock'),

    )

    type = models.CharField(
        max_length=1,
        choices=INSTRUMENT_TYPE,
        help_text = 'Stock or Option Type: Stock, Put, or Call',
    )


    class Meta:
        ordering = ['expiration_date']

    

    def __str__(self):
        return f"{self.underlying} {type} : {self.strike} {self.expiration_date} "
    
    def get_absolute_url(self):
        return reverse("model-detail-view", args=[str(self.id)])
    
class Portfolio(models.Model):
    
    name = models.CharField(max_length=32, default='Default Portfolio', unique=True)
    instrument = models.ManyToManyField(Instrument)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        pass


    