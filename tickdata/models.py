from django.db import models

# Create your models here.


class StockIndex(models.Model):
    name = models.CharField(max_length=255)


class DailyPrice(models.Model):
    index = models.ForeignKey(StockIndex, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()
