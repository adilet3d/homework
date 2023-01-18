from django.db import models

class BookCategory(models.Model):
    name= models.CharField(max_length=120)
    image=models.ImageField(upload_to="image/")
    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    book_amount=models.PositiveIntegerField(default=0)
    date_birthday=models.DateField(verbose_name="Дата рождения")
    pseudonym=models.CharField(max_length=120,verbose_name='Псевдоним')
    avatar= models.ImageField(upload_to="image/")
    book_category=models.ForeignKey(BookCategory,on_delete=models.CASCADE,related_name='Author')

    def __str__(self) -> str:
        return self.pseudonym

class Book(models.Model):
    name= models.CharField(max_length=120,verbose_name='Имя')
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='Book')
    date_of_issue= models.DateField(auto_now_add=True)
    chapter_amount=models.PositiveIntegerField(default=0, null=True)
    preview=models.CharField(max_length=120,verbose_name='оглавление')
    book_category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    discount=models.PositiveIntegerField(default=0)
