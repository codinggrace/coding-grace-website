import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250, null=True)
    country = models.ForeignKey(Country, null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    venue = models.CharField(max_length=250)
    address1 = models.CharField(blank=True, max_length=250)
    address2 = models.CharField(blank=True, max_length=250)
    city =models.ForeignKey(City, null=True)
    country = models.ForeignKey(Country, null=True)
    slug = models.SlugField(null=True, help_text="E.G. some-building-dublin")

    def __str__(self):
        return "{} {}".format(self.venue, self.city)

class Organiser(models.Model):
    user = models.ForeignKey(User, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    blurb = models.TextField(blank=True, null=True)
    contact_number = models.CharField(blank=True, null=True, max_length=25)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, max_length=250)
    slug = models.SlugField(null=True, help_text="E.G. firstname-lastname")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Chapter(models.Model):
    city = models.ForeignKey(City, null=True)
    country = models.ForeignKey(Country, null=True)
    organisers = models.ManyToManyField(Organiser, null=True)
    email = models.EmailField(null=True)
    url = models.URLField(max_length=250)
    slug = models.SlugField(null=True, help_text="E.G. dublin")

    def __str__(self):
        return self.city.name

class Levels(models.Model):
    description = models.CharField(null=True, max_length=300)

    def __str__(self):
        return self.description

class Mentor(models.Model):
    user = models.ForeignKey(Organiser, blank=True, null=True, help_text="Only choos this if mentor is an organiser also. No need to fill rest of form.")
    first_name = models.CharField(max_length=250, blank=True, null=True, help_text="If not an organiser, fill in this")
    last_name = models.CharField(max_length=250, blank=True, null=True, help_text="If not an organiser, fill in this")
    blurb = models.TextField(blank=True, null=True, help_text="If not an organiser, fill in this. Markdown text supported.")
    url = models.URLField(blank=True, max_length=250, null=True, help_text="If not an organiser, fill in this")
    slug = models.SlugField(null=True, help_text="E.G. firstname-lastname")

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug

class Sponsor(models.Model):
    name = models.CharField(null=True, max_length=250)
    url = models.URLField(null=True)
    blurb = models.TextField(null=True, help_text="Markdown text")
    what = models.CharField(null=True, max_length=250)
    slug = models.SlugField(null=True, help_text="E.G. microsoft-ireland")

    def __str__(self):
        return self.slug

class Event(models.Model):
    title = models.CharField(max_length=250)
    level_type = models.ManyToManyField(Levels)
    short_description = models.TextField(null=True, help_text="Markdown text")
    description = models.TextField(help_text="Markdown text")
    faq = models.TextField(null=True, blank=True, help_text="Markdown text. This field is optional.")
    pub_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
    start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey(Location)
    organiser = models.ForeignKey(Organiser)
    mentors = models.ManyToManyField(Mentor, null=True)
    sponsors = models.ManyToManyField(Sponsor, blank=True)
    cost = models.DecimalField(null=True, decimal_places=2, max_digits=6, help_text="E.G. 10.00")
    embed_ticket = models.TextField(null=True, blank=True, help_text="Just paste in the html embed ticket, or just place instructions in HTML/Markdown here to display in ticket section.")
    event_url = models.URLField()
    slug = models.SlugField(help_text="E.G. this-this-an-event")

    def __str__(self):
        return "[{}] {} - {}".format(self.location.city, self.title, self.start_datetime)

    def current_event(self):
        return self.start_datetime >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ["-start_datetime"]
