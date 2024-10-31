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
        return str(self.name)
    class Meta:
        ordering=('diffrence','-curent_date')
    def save(self, *args, **kwargs):
        name,price=get_link(self.url)
        old_price=self.current_price
        self.current_price = self.price
        if self.current_price:
            if price!=old_price:
                diff=price- old_price
                self.diffrence=diff
                self.old_price=old_price
            else:
                self.old_price=0
                self.diffrence=0
        self.name=name
        self.curent_date=price
        super().save(*args, **kwargs)
        
    @classmethod
    def get_all(cls):
        # This custom method retrieves and updates the latest prices for each link
        all_links = cls.objects.all()
        for link in all_links:
            name, price = get_link(link.url)
            old_price = link.current_price
            print("#$#%$%$%#$$#$#$%%%$%$%R$%$")
            print(f"Product Name: {name}")
            print(f"Price: {price}")
            print(f"Current Price (before update): {link.current_price}")

            # Set the product properties with improved checks
            link.name = name if name else "Unknown Product"
            link.price = price if price is not None else 0.0
            link.old_price = old_price
            link.current_price = link.price  # Set current_price to updated price

            # Calculate the difference if old_price and current_price are valid
            link.diffrence = (link.old_price - link.current_price) if link.old_price is not None and link.current_price is not None and link.old_price != link.current_price else 0.0
            print(f"Difference: {link.diffrence}")

            # Save the link only if there's a change in the price
            if old_price != link.current_price:
                link.save(update_fields=['name', 'price', 'old_price', 'current_price', 'diffrence'])

        return all_links
            