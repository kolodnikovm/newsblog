from django.db import models
from .utilfuncs import main_news_pic, news_pics
from users.models import User

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    description = models.CharField(max_length=140)

class Category(models.Model):
    name = models.CharField(max_length=20)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

class Tag(models.Model):
    name = models.CharField(max_length=20)

class News(models.Model):
    creation_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    text_content = models.TextField()
    main_picture = models.ImageField(upload_to=main_news_pic)
    additional_pictures = models.ImageField(upload_to=news_pics)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()