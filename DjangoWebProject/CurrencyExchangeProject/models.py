from django.db import models
    
class Currencies(models.Model):
  code = models.CharField(max_length=3)
  
  def __str__(self):
        return self.code
  

class CurrencyPairs(models.Model):
  exchange_date = models.DateField()
  currency_pairs = models.CharField(max_length=8)
  exchange_rates = models.FloatField()
  
  def __str__(self):
      return self.currency_pairs
  