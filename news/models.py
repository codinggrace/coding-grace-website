from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from events.models import Chapter, Event, Organiser

class NewsPost(models.Model):
    title = models.CharField(max_length=250)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(Organiser)
    chapter = models.ForeignKey(Chapter, null=True, blank=True)
    slug = models.SlugField(max_length=250)
    short_description = models.TextField(null=True)
    content = models.TextField(null=True)
    event = models.ForeignKey(Event, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:news_article", kwargs={"slug": self.slug, "year": self.published.year, "month": self.published.month, "day": self.published.day})
