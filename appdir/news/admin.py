from django.contrib import admin

from .models import Author, Category, Tag, News, Comment, ExtraPics


class ExtraPicturesInline(admin.TabularInline):
    model = ExtraPics


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        ExtraPicturesInline,
    ]


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
