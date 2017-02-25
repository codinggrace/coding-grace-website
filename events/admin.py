from django.contrib import admin
from events.models import Chapter, City, Country, Event, Levels, Location, Mentor, Organiser, Sponsor, Sponsorship

# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("city", "country", "email", "url", "slug")
admin.site.register(Chapter, ChapterAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(City, CityAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Country, CountryAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_datetime", "start_datetime", "end_datetime", "location", "organiser", "slug", "is_cancelled", "is_published")
    list_filter = ["start_datetime"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "description"]
    raw_id_fields = ("location", "organiser")
admin.site.register(Event, EventAdmin)

class LevelsAdmin(admin.ModelAdmin):
    list_display = ("description",)
admin.site.register(Levels, LevelsAdmin)

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Location details",    {"fields": ["venue", "address1", "address2", "city", "country"]}),
        (None,                  {"fields": ["slug"]}),
    ]
    list_display = ("venue", "address1", "address2", "city", "country")
    search_fields = ["venue", "address1", "address2", "city", "country"]
admin.site.register(Location, LocationAdmin)

class MentorAdmin(admin.ModelAdmin):
    list_display = ("slug", "first_name", "last_name", "blurb", "url")
    search_fields = ["first_name", "last_name"]
admin.site.register(Mentor, MentorAdmin)

class OrganiserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "blurb", "url", "slug")
    search_fields = ["first_name", "last_name"]
admin.site.register(Organiser, OrganiserAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "blurb", "slug")
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Sponsor, SponsorAdmin)

class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ("sponsor", "sponsorship_type")
admin.site.register(Sponsorship, SponsorshipAdmin)
