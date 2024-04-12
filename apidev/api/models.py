from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentage=models.DecimalField(max_digits=10, decimal_places=2)
    rating=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    image_urls = models.TextField() 
    def get_image_urls_list(self):
        # Split the stored URLs into a list
        return self.image_urls.split('\n')

    def __str__(self):
        return self.name
    
    


    
     
    
      
      
      
