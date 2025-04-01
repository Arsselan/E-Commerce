# edited by Miles Sasportas
from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Product, Review , User , Seller , Buyer , Wishlist



# to map json objects to our entries in the db
# wroted Junior Woguia edited 
# co author: Miles Sasportas 
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User  
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True }  # we dont want to show the password after the registration 
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) # validated data without the extracted password 
        if password is not None :
            instance.set_password(password)
        instance.save()
        
        return instance 
# author: Sarish
# co-author: Arsselan
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "seller", "name", "desc", "price", "stock", "get_image", "image")
# author: Arsselan
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
#author: Arsselan
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
