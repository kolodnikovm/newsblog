from django.db import models

from users.models import User
from .utilfuncs import main_news_pic, news_pics


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    description = models.CharField(max_length=140)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='author', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent_id = models.ForeignKey(
        'self', related_name='subcategories', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class News(models.Model):
    heading = models.CharField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        Author, related_name='articles', on_delete=models.CASCADE, blank=True, null=True)
    category = models.OneToOneField(
        Category,  on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    text_content = models.TextField()
    main_picture = models.ImageField(
        upload_to=main_news_pic, blank=True, null=True)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.heading


class PublishedNews(models.Model):
    heading = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        Author, related_name='p_articles', on_delete=models.CASCADE, blank=True, null=True)
    category = models.OneToOneField(
        Category,  on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    main_picture = models.ImageField(
        upload_to=main_news_pic, blank=True, null=True)

    draft_news = models.OneToOneField(
        News, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        verbose_name_plural = "published news"

    def save(self, *args, **kwargs):
        self.heading = self.draft_news.heading
        self.creation_date = self.draft_news.creation_date
        self.author = self.draft_news.author
        self.category = self.draft_news.category
        # self.tags = self.p_article.tags.set()
        self.text_content = self.draft_news.text_content

    def __str__(self):
        return self.heading


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class ExtraPics(models.Model):
    image = models.ImageField()
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='extra_pics')
