from rest_framework import serializers , exceptions
from myapp.models import Book,BookCategory, Author



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields=(
            'id', 'book_amount','date_birthday','pseudonym','avatar',
        )
        read_only_fields=(
            'book_category',
        )
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'
        # fields=(
        #     'id', 'name','date_of_issue','chapter_amount','preview','price','discount'
        # )
        read_only_fields=(
            'book_category','author',
        )
class BookCategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model=BookCategory
        fields=(
            '__all__'
        )
class RegistrationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
    email= serializers.CharField()
    def validate_password(self,value):
        if len(value) <8:
            raise exceptions.ValidationError('Password is too short')
        elif len (value) >24:
            raise exceptions.ValidationError ('Password is too long')
        return value

class AuthorizationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()