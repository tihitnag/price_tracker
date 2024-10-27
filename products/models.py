from django.db import models

class Product(models.Model) :
    url = models.TextField()
    old_price = models.FloatField()
    name = models.CharField(max_length=100)
    
    
