# edited by Miles Sasportas
from django.http import JsonResponse
from .permissions import IsSellerOrReadOnly
from .serializers import ProductSerializer, ReviewSerializer, UserSerializer, WishlistSerializer
from .models import Product ,User , Seller , Buyer  ,Seller , Review, Wishlist
from rest_framework.decorators import api_view, permission_classes, parser_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication , TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from .mockdata import get_mock_products
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token 
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView
# @permission_classes([IsAuthenticated])  # Add this line to require authentication

#author: Junior Woguia
class Register(APIView):
    def post ( self , request):
     serializer = UserSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     user = serializer.save()
        #co-author:Arsselan
        # Hier können Sie Ihre eigene Logik hinzufügen, um den Benutzer als Käufer oder Verkäufer zu identifizieren
     if 'is_seller' in request.data and request.data['is_seller']:
         Seller.objects.create(account=user)
     else:
         Buyer.objects.create(account=user)

     return Response(serializer.data)

#author: Junior Woguia
class Login(APIView):
    def post (self , request ):
        email = request.data['email']
        password = request.data['password']             # we take both email and password from the frontend 
        user = User.objects.filter(email=email).first() # we want to find the first email because email are unique so the first is also the only one we are looking for 
        
        if user is None:
            raise AuthenticationFailed('HUMMM ! This user was not found !')  # when the user is not found 

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password , try again !')
        
        payload = {
            'id': user.id, 
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),    # How long do we want a user to be connected on the web APP ? 15 minutes 
            'iat': datetime.datetime.utcnow()                                      # Time when we created the token 
        }
        token = jwt.encode(payload  , 'secret' , algorithm='HS256')
        #.decode('utf-8')
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True )  # we dont want the front end to acces our token haha 
        response.data = {
            'jwt': token 
        }
        
        
        return response
    
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt

#author: Junior Woguia
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()

        seller_id = user.seller.id if user.is_seller else None

        # Hier erstellen Sie ein benutzerdefiniertes Serializer-Objekt und geben die gewünschte Reihenfolge der Felder an
        user_serializer = UserSerializer(user)
        serialized_user = user_serializer.data
        serialized_user['seller_id'] = seller_id

        return Response(serialized_user)


#author:Wael
class Logout(APIView):
    def post(self , request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'SUCCESS'
        }
        
        return response
        

    

        
        







'''
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User , username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user) 
    serializer = UserSerializer(instance=user)
    return Response({"toen": token.key , "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return Response({"token": token.key , "user": serializer.data['username']}) 
    return Response(serializer.errors  , status = status.HTTP_400_BAD_REQUEST)
    '''

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
#author: Junior Woguia
def test_token(request):
    return Response("passed for {}".format(request.user.email))


# author: Sarish
# co-author: Arsselan
@api_view(['GET'])
#Listing all products in json format
def product_list(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        #products = get_mock_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("POST request without data")

# author: Sarish
@api_view(['GET', 'PUT', 'DELETE'])        
def product_detail(request, id, format=None):
    #make sure we have a valid object
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP)

#author: Arsselan
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsSellerOrReadOnly])
def product_list_seller(request):
    if request.method == 'GET':
        # products = Product.objects.all()
        seller = request.user.seller
        products = Product.objects.filter(seller = seller)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
#author: Arsselan    
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsSellerOrReadOnly])
def upload_product(request):
    #print(hasattr(request.user, 'seller'))
    if not request.user.is_authenticated or not hasattr(request.user, 'seller'):
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=request.user.seller)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#author: Arsselan    
@api_view(['Put'])
@permission_classes([IsAuthenticated, IsSellerOrReadOnly])
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    #if request.user != product.seller.user:
    #    return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = ProductSerializer(product, data =request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#author: Arsselan    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsSellerOrReadOnly])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    #if request.user != product.seller.user:
    #    return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)
#author: Sarish, Arsselan
@api_view(['GET'])
def search_products(request):
    try:
        query = request.GET.get('q', '')

        if not query:
            return Response({'error': 'Search query is required in the request parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        #products = Product.objects.annotate(search=SearchVector("name", "desc")).filter(search=query)
        products = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#author: Arsselan
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_review_list_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['product_id'] = product_id
        request.data['userid'] = request.user.pk
        serializer = ReviewSerializer(data=request.data)
        if request.data['content'] == '':
            return Response({'message': 'Content should not be empty'}, status=400)
        if serializer.is_valid():
            if 1 <= int(request.data['rating']) <= 5:
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response({'message': 'Rating should be between 1 and 5'}, status=400)
        return Response(serializer.errors, status=400)

#author: Sarish, Arsselan
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    # Überprüfen, ob der eingeloggte Benutzer der Besitzer der Bewertung ist
    if review.userid.id == request.user.id:
        review.delete()
        return Response({'message': 'Review deleted successfully'}, status=204)
    else:
        return Response({'message': 'You are not authorized to delete this review'}, status=403)
#author: Arsselan
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    # Überprüfen, ob der eingeloggte Benutzer der Besitzer der Bewertung ist
    if review.user == request.user:
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    else:
        return Response({'message': 'You are not authorized to update this review'}, status=403)
# author:Arsselan
# edited by Miles Sasportas
@api_view(['GET'])
def check_email_availability(request):
    email = request.query_params.get('email', None)
    if User.objects.filter(email = email):
        return Response({'message': 'Email already exists'}, status=403)
    else:
        return Response({'message': 'Email is available'}, status=200)
# author: Arsselan    
# co-author: Sarish
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_favorite(request, product_id):
    favorite = get_object_or_404(Wishlist, productid=product_id, userid=request.user.id)
    favorite.delete()
    return Response({'message': 'Unmarked from favorites'}, status=204)
#author: Arsselan
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if Wishlist.objects.filter(userid=request.user, productid=product).exists():
        return Response({'message': 'Product is already in favorites'}, status=400)
    serializer = WishlistSerializer(data={'userid': request.user.id, 'productid': product.id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
#author: Arsselan
# co-author: Sarish    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_favorite(request):
        products = Wishlist.objects.filter(userid = request.user.id)
        serializer = WishlistSerializer(products, many=True)
        return Response(serializer.data)