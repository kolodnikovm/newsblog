from django.contrib import admin

from .models import Author, Category, Tag, News, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Comment)
