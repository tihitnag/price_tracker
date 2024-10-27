from django.db import models
from link.utils import get_link
# Create your models here.
class links_model(models.Model):
    name = models.CharField(max_length=200, blank=True)
    price = models.FloatField(max_length=200, blank=True)
    old_price = models.FloatField(max_length=200, blank=True)
    current_price = models.FloatField(max_length=200, blank=True)
    diffrence = models.FloatField(max_length=200, blank=True)
    curent_date=models.DateField(auto_now=True)
    url=models.URLField()
    
    def __str__(self):
        return super().__str__()
    
    def save(self, *args, **kwargs):
        name,price=get_link(self.url)
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
            