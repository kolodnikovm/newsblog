from django.contrib import admin

from .models import Author, Category, Tag, DraftNews, Comment, ExtraPics, PublishedNews


class ExtraPicturesInline(admin.TabularInline):
    model = ExtraPics


class DraftNewsAdmin(admin.ModelAdmin):
    inlines = [
        ExtraPicturesInline,
    ]
    actions = ['make_published']

    def make_published(self, request, queryset):
        for draft_news in queryset:
            if hasattr(draft_news, 'published_news'):
                draft_news.published_news.save()
            else:
                pub = PublishedNews(draft_news=draft_news)
                pub.save()
        self.message_user(
            request, "Selected news were successfully published")
    make_published.short_description = "Mark selected news as published"


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(DraftNews, DraftNewsAdmin)
admin.site.register(Comment)
admin.site.register(PublishedNews)
