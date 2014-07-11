from django.contrib import admin
from news.models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "slug", "short_description", "content", "published", "is_published")
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(NewsPost, NewsPostAdmin)
