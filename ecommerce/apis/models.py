from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.FileField(upload_to="category_img/", null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
class Attribute(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)        
    image = models.FileField(upload_to="brand_img/", null=True, blank=True)

    def __str__(self):
        return self.name
    
product_type = (
        ('digital', 'Digital'),
        ('physical', 'Physical'),
    )
    
discount_type = (
        ('flat', 'Flat'),
        ('percent', 'Percent'),
    )
    
products_unit = (
        ('psc', 'psc'),
        ('kg', 'kg'),
        ('ltrs', 'ltrs'),
        ('gms', 'gms'),
    )

    
class InHouseProducts(models.Model):
    name = models.CharField(max_length=200)    
    description = models.TextField()
    product_type = models.CharField(max_length=200, choices=product_type)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.PositiveIntegerField()
    unit = models.CharField(max_length=100, choices=products_unit)
    color = models.CharField(max_length=150)
    unit_price = models.FloatField()
    purchase_price = models.FloatField()
    tax = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(max_length=200, choices=discount_type, null=True, blank=True)
    total_quantity = models.PositiveIntegerField()
    minimum_order_quantity = models.PositiveBigIntegerField()
    shipping_cost = models.FloatField(null=True, blank=True)
    meta_title = models.TextField()
    meta_description = models.TextField()
    meta_image = models.FileField(upload_to="meta_image/", null=True, blank=True)
    product_images = models.FileField(upload_to="products_img", null=True, blank=True)
    product_thumbnail = models.FileField(upload_to="product_thumbnail/", null=True, blank=True)


    def __str__(self):
        return self.name
    

    def get_price(self):
        price = self.unit_price - (self.unit_price * (self.discount / 100))
        return price
    