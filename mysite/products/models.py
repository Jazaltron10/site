from django.db import models

# Create your models here.
class Product(models.Model):
    # Represents a product entity
    name = models.CharField(max_length=100) # The name of the product 
    price = models.DecimalField(max_digits=10, decimal_places=2) # The price of the product
    
    def __str__(self) -> str:
        return self.name # Returns the product name for easy identification
    
class ProductDetail(models.Model):
    # Represents detailed information about a product 
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE
    ) # Links to the product, deletes the detail if the product is deleted
    description = models.TextField() # A detailed description of the product
    warranty = models.CharField(max_length=100) # The warranty details of the product
    
    def __str__(self):
        return f"{self.product.name} - Details" # Returns product name followed by 'Details' for easy identification
    