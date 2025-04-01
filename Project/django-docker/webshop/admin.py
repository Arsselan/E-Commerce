from django.contrib import admin
from .models import *
# from actor.models import User 

# Register your models here.
# authors: Sarish, Arsselan
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Order)
admin.site.register(OrderPosition)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Category)
