# edited by Miles Sasportas
from django.urls import include, path
# import routers
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
 
# import everything from views
from .views import *
from webshop import views 
 
# authors: Sarish, Arsselan
urlpatterns = [
    path('product/', product_list),
    path('product/<int:id>', product_detail),
    path('product/seller/<int:id>', product_list_seller),
    path('seller/upload_product/', upload_product),
    #path('seller/delete_product/', delete_product),
    #path('seller/update_product/', update_product),
    path('product/seller/', product_list_seller),
    path('seller/delete_product/<int:product_id>', delete_product),
    path('seller/update_product/<int:product_id>', update_product),
    path('search/', search_products),
    # path('login/', login ), alte Version 
    # path('signup/', signup ), alte  Version 
    path('test_token/', test_token ),
    path('register' , Register.as_view()),
    # co-author : Junior Woguia
    path('login' , Login.as_view()),
    path('user' , UserView.as_view()),
    path('logout' , Logout.as_view()),
    path('product/<int:product_id>/review/', product_review_list_create),
    path('product/delete_review/<int:review_id>/', delete_review),
    path('product/update_review/<int:review_id>/', update_review),
    path('register/email_validation/', check_email_availability),
    path('product/add_favorite/<int:product_id>/', add_favorite),
    path('product/delete_favorite/<int:product_id>/', delete_favorite),
    path('product/list_favorite/', list_favorite),

    # added by Miles Sasportas
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]