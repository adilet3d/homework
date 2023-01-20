from django.db import models
from django.contrib.auth.models import AbstractUser
class BookCategory(models.Model):
    name= models.CharField(max_length=120)
    image=models.ImageField(upload_to="image/")
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name= 'Категория'
        verbose_name= 'Категории'

class Author(AbstractUser):
    book_amount=models.PositiveIntegerField(default=0,null=True,blank=True)
    date_birthday=models.DateField(verbose_name="Дата рождения",null=True,blank=True)
    pseudonym=models.CharField(max_length=120,verbose_name='Псевдоним',null=True,blank=True)
    avatar= models.ImageField(upload_to="image/",null=True,blank=True)
    book_category=models.ForeignKey(BookCategory,on_delete=models.CASCADE,related_name='authors',null=True,blank=True)

    def __str__(self) -> str:
        return self.username
    class Meta:
        verbose_name="Автор"
        verbose_name_plural='Авторы'

class Book(models.Model):
    name= models.CharField(max_length=120,verbose_name='Имя')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    date_of_issue= models.DateField(auto_now_add=True)
    chapter_amount=models.PositiveIntegerField(default=0, null=True)
    preview=models.CharField(max_length=120,verbose_name='оглавление')
    book_category = models.ForeignKey(BookCategory,on_delete=models.CASCADE, related_name='books')
    price=models.PositiveIntegerField(default=0)
    discount=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'
