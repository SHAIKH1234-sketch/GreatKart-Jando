from django.db import models
from catagory.models import Catagory
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(max_length=500,unique=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='phtos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_details',args=[self.catagory.slug,self.slug])

    def __str__(self):
        return self.product_name
