from django.db import models
from link.utils import get_link
# Create your models here.
class links_model(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(max_length=200, blank=True, null=True)  # Allow null values here
    old_price = models.FloatField(max_length=200, blank=True, null=True)
    current_price = models.FloatField(max_length=200, blank=True, null=True)
    diffrence = models.FloatField(max_length=200, blank=True, null=True)
    curent_date = models.DateField(auto_now=True)
    url = models.URLField()   
    def __str__(self):
        return super().__str__()
    
    def save(self, *args, **kwargs):
        name,price=get_link(self.url)
        self.name = name if name else "Unknown Product"
        self.price = price if price is not None else 0.0
        self.current_price = self.price
        old_price=self.current_price
        if self.current_price:
            if price!=old_price:
                diff=old_price-price
                self.diffrence=diff
                self.old_price=old_price
            else:
                self.current_price=0
        self.name=name
        self.curent_date=price
        super().save(*args, **kwargs)
            