from django.db import models

class BookCategory(models.Model):
    name= models.CharField(max_length=120)
    image=models.ImageField()
    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    book_amount=models.PositiveIntegerField()
    date_birthday=models.DateField
    pseudonym=models.CharField(max_length=120,verbose_name='Псевдоним')
    avatar= models.ImageField
    book_category=models.ForeignKey(BookCategory,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pseudonym

class Book(models.Model):
    name= models.CharField(max_length=120)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    date_of_issue= models.DateField(auto_now_add=True)
    chapter_amount=models.PositiveIntegerField
    preview=models.CharField(max_length=120)
    book_category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    price=models.PositiveIntegerField
    discount=models=models.PositiveIntegerField
