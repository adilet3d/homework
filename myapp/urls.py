from django.urls  import path
from rest_framework.routers import DefaultRouter    as DR
from myapp.views import (BookView,CategoryView,AuthorView )

router=DR()
router.register('book categories',CategoryView,basename='book_category')
router.register('book',BookView,basename='book')
router.register('author',AuthorView,basename='author')


urlpatterns = []

urlpatterns += router.urls