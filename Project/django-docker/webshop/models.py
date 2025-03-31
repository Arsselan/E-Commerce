# edited by Miles Sasportas
from typing import Any
from django.db import models
from django.contrib.auth.models import  AbstractUser , PermissionsMixin, UserManager


# Create your database models here.
# By default, Django automatically creates a primary key field
# früher war das Abstractu

#author: Junior Woguia
from django.utils import timezone
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address , it is mendatory ")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):  # only for buyers 
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_buyer' , True)
        extra_fields.setdefault('is_seller' , False)
        
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):    # for sellers and staff
        extra_fields.setdefault('is_seller', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
#author: Junior Woguia 
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(blank=False, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    bio = models.CharField(max_length= 500, blank=True , default='I am happy to use Fitiness , I can only recommend it to you')
    
    
    street = models.CharField(max_length=255, blank=False, default='not provided: Anonimous')
    house_number = models.CharField(max_length=255, blank=False, default='not provided: Anonimous')
    country = models.CharField(max_length=255, blank=False, default='not provided: Anonimous')
    complement_adress = models.CharField(max_length=255, blank=True, default='')
    telnumber=models.CharField(max_length=20, null=True)
    email_paiement = models.EmailField(blank=True, null=True)  # could be diffferent from the login email.

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)    # for our Buyers 
    is_seller = models.BooleanField(default=False)   # for our Sellers 
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False) # admin 

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # now we want to login with our email and the password, like on amazon.com :) , not with the username from django by default 
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']    # we dont want additional field while creating a new user in the command prompt 

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
'''
class Buyer(models.Model):
   # We already have all the basics like username ,first_name , last_name , email , is_staff , is_active = false , date_joined 
   # lets just extend with what we need 
   account = models.OneToOneField(User, on_delete=models.CASCADE)  # now we just link each Buyer  to his account in the actor's models
   
   telnumber=models.CharField(max_length=20, null=True)
   street=models.CharField(max_length=200, null=True)
   house_number=models.CharField(max_length=200, null=True)
   city=models.CharField(max_length=255 , null=True)
   country=models.CharField(max_length=255 , null=True)
   complement=models.CharField(max_length=255, null=True)
   email_paiement = models.EmailField(blank=True, null=True)
   '''
#author: Junior Woguia 
co author . Arsslan 
class Seller(models.Model):
   account = models.OneToOneField(User, on_delete=models.CASCADE)  # we link each Seller to his account in the actor's models
   
   company_name=models.CharField(max_length=255, null=True)
   company_desc=models.CharField(max_length=255, null=True)
   



# class Seller(models.Model):
# user = models.OneToOneField(User, on_delete=models.CASCADE)
#author: Junior Woguia

class Buyer(models.Model):
   account = models.OneToOneField(User, on_delete=models.CASCADE)
#author: Arsselan
class Order(models.Model):
   id=models.AutoField(primary_key=True)
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   date=models.DateTimeField()
   totalsum=models.FloatField()
#author: Sarish
def upload_to(instance, filename):
   return '{filename}'.format(filename=filename)
#author: Arsselan
class Product(models.Model):
   id=models.AutoField(primary_key=True)
   seller=models.ForeignKey(Seller, null=True,on_delete=models.CASCADE)
   name=models.CharField(max_length=128)
   desc=models.CharField()
   price=models.FloatField()
   stock=models.IntegerField()
   image=models.ImageField(upload_to=upload_to, default='default_image.png')
   #img=models.CharField()
   def __str__(self):
      return self.name
#author: Sarish   
#co-author: Arsselan   
   def get_image(self):
        if self.image:
            return 'https://localhost:8000' + self.image.url
        return 'https://localhost:8000' + '/media/default_image.png'
   
#author: Arsselan  
class OrderPosition(models.Model):
   id=models.AutoField(primary_key=True)
   oid=models.ForeignKey(Order, on_delete=models.CASCADE)
   pid=models.ForeignKey(Product, on_delete=models.CASCADE)
   position=models.IntegerField()
   quantity=models.IntegerField()
   pricesingle=models.FloatField()
   total=models.FloatField()
#author: Arsselan
class Wishlist(models.Model):
   id=models.AutoField(primary_key=True)
   userid=models.ForeignKey(User, on_delete=models.CASCADE)
   productid=models.ForeignKey(Product, on_delete=models.CASCADE)
#author: Arsselan
class Review(models.Model):
   id=models.AutoField(primary_key=True)
   product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
   userid=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   creationdate=models.DateField()
   content=models.CharField(max_length=500)
   rating=models.IntegerField(null=True)
#author: Arsselan
class Category(models.Model):
   id=models.AutoField(primary_key=True)
   categoryname=models.CharField(max_length=30)