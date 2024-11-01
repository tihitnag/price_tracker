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
    image_url = models.URLField(null=True,blank=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=('diffrence','-curent_date')
    def save(self, *args, **kwargs):
       # Fetch name and price using the get_link method
        name, price,image_url = get_link(self.url)
        self.name = name if name else "Unknown Product"
        self.image_url = image_url
        self.price = price if price is not None else 0.0
        self.old_price = self.current_price
        
        self.current_price = self.price
        if self.old_price is not None: 
            if self.current_price != self.old_price:  
                self.diffrence = self.old_price - self.current_price   
            else:
                self.diffrence = 0.0  
        else:
            self.diffrence = 0.0 

        self.name=name
        self.curent_date=price
        super().save(*args, **kwargs)
        
    @classmethod
    def get_all(cls):
        # This custom method retrieves and updates the latest prices for each link
        all_links = cls.objects.all()
        updated_links = []  # Collect links that need to be saved

        for link in all_links:
            name, price, image_url = get_link(link.url)  # Fetch the latest name and price
            
            # Update the link's properties only if there's a change
            if name and link.name != name:
                link.name = name
            
            if price is not None and link.current_price != price:
                link.old_price = link.current_price  # Store old price before update
                link.current_price = price  # Update current price
                
                # Calculate the difference
                link.diffrence = link.old_price - link.current_price
                
                updated_links.append(link)  # Mark for saving

        # Save all updated links in one go to reduce database hits
        if updated_links:
            cls.objects.bulk_update(updated_links, ['name', 'current_price', 'old_price', 'diffrence', 'image_url'])

        return all_links
                    