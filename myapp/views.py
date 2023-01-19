from django.shortcuts import render
from myapp.serializer import (BookCategorySerializer, BookSerializer,AuthorSerializer)
from myapp.models import (Book, BookCategory, Author)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework import permissions
# from rest_framework.decorators import action

class CategoryView(ModelViewSet):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer

class BookView(ModelViewSet):
    queryset=BookCategory.objects.all()
    serializer_class=BookSerializer

class AuthorView(ModelViewSet):
    queryset=AuthorSerializer
    serializer_class=AuthorSerializer
    