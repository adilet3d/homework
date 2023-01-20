from django.contrib import admin
from myapp.models import (
    BookCategory, Book,Author
)
# Register your models here.
admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Author)