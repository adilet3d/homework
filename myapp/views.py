
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from myapp.serializer import (
    BookCategorySerializer, BookSerializer,AuthorSerializer, RegistrationSerializer,AuthorizationSerializer
)
from myapp.models import (
    Book, BookCategory, Author
)
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import action
from myapp.send_mail import send_msg


class CategoryView(ModelViewSet):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer
    
    @action(methods=['post',],detail=True,serializer_class=BookSerializer,permission_classes=(permissions.IsAuthenticatedOrReadOnly,))
    def add_book(self ,request, *args,**kwargs):
        book_category =self.get_object()
        user = request.user
        serializer=BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        book=Book.objects.create(
            book_category=book_category,
            name= data.get('name'),
            author=user,
            date_of_issue=data.get('date_of_issue'),
            chapter_amount=data.get('chapter_amount'),
            preview=data.get('preview'),
            price=data.get('price'),
            discount=data.get('discount'),
        
        
        )
        return Response(BookSerializer(book).data)




class BookView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=(
        DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter
    )
    filterset_fields=(
        'date_of_issue',
    )
    search_fields=(
        'name','id','book_category__name',
    )
    ordering_fields=(
        'price','id',
    )

class AuthorView(ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class RegistrationView(APIView):
    def post(self,request):
        serializer= RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data


        username= data.get('username')
        email=data.get('email')
        password=data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'message':'User with such name is already exists'})
        user= User.objects.create_user(
            username=username,
            email=email,
            password=password

        )
        send_msg(email=email,username=username)
        token=Token.objects.create(user=user)
        return Response({'token':token.key})

class AuthorizationView(APIView):
    def post(self, requset):
        serializer=AuthorizationSerializer
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        
        
        username=data.get('username')
        password=data.get('password')
        user= User.objects.filter(username=username).first()
        
        if user is not None:
            if check_password(password, user.password):
                token,_=Token.objects.get_or_create(user=user)
                return Response({'token:':token.key})
            return Response ({'error':'Password is not valid'}, status=400)
        return Response({'error':'This username is not registred'},status=400)


