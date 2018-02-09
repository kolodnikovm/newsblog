from django.contrib import admin

from .models import Author, Category, Tag, News, Comment, ExtraPics, PublishedNews


class ExtraPicturesInline(admin.TabularInline):
    model = ExtraPics


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        ExtraPicturesInline,
    ]
    actions = ['make_published']

    def make_published(self, request, queryset):
        for draft_news in queryset:
            if hasattr(draft_news, 'publishednews'):
                pass
                # Update publish news
            else:
                pass
                # Create publish news from draft one
        self.message_user(
            request, "Selected news were successfully published")
    make_published.short_description = "Mark selected news as published"


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
admin.site.register(PublishedNews)
