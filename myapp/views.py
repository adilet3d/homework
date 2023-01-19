from django.shortcuts import render
from myapp.serializer import (BookCategorySerializer, BookSerializer,AuthorSerializer)
from myapp.models import (Book, BookCategory, Author)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import action

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

class AuthorView(ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

