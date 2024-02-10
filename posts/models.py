from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils.timezone

# Create your models here.
class car_model(models.Model):
    car_image=models.ImageField( upload_to='posts/media/uploads', blank=True,null=True)
    car_name = models.CharField(max_length=50)
    car_price= models.IntegerField()
    car_brand_name = models.ForeignKey('brand_model', on_delete=models.CASCADE)
    car_description = models.TextField(default="it is a good car")
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'car model:{self.car_name} , brand: {self.car_brand_name}'


class brand_model(models.Model):
    # brand_relation= models.OneToOneField("car_model", on_delete=models.CASCADE)
    brand_name = models.CharField( max_length=50)
    slug = models.SlugField(blank=True,null=True,unique=True)
    def __str__(self) -> str:
        return f'{self.brand_name}'
    
class comments_Model(models.Model):
    relation_with_car_model = models.ForeignKey(car_model,  on_delete=models.CASCADE,related_name="comments")
    name= models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created_one = models.DateTimeField( auto_now_add=True)

    def __str__(self) -> str:
        return f' {self.name} ,  {self.body}'
    

# handling purchase option 
class purchase(models.Model):
    relation_with_user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation_with_car_model= models.ForeignKey(car_model,  on_delete=models.CASCADE)
    purchased_car_model_name = models.TextField(blank=True)
    purchased_car_brand_name = models.TextField(blank=True)
    who_purchased_user_name= models.CharField(max_length=50,blank=True,null=True)
    purchase_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self) -> str:
        return f'{self.who_purchased_user_name}--bought:{self.purchased_car_model_name}'






    