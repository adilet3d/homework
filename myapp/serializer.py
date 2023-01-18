from rest_framework import serializers , exceptions
from myapp.models import Book,BookCategory, Author


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCategory
        fields=(
            'id','name','image'
        )
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields=(
            'id', 'book_amount','date_birthday','pseudonym','avatar',
        )
        read_only_fields=(
            'book_category'
        )
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=(
            'id', 'name','date_of_issue','chapter_ammount','preview','price','discount'
        )
        read_only_fields=(
            'book_category','author'
        )