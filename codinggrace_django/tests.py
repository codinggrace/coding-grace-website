import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.text import slugify
from django.utils.timezone import utc

from codinggrace_django.views import get_chapters
from events.models import Chapter, City, Country, Event, Levels, Location, Mentor, Organiser, Sponsor


class CodingGraceDjangoTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('lfh', 'lfh@codinggrace.com', 'lfhpassword')
        user.save()

        beginner_level = Levels.objects.create(description="Beginners")
        beginner_level.save()

        ireland = Country.objects.create(name = "Ireland")
        ireland.save()

        dublin = City.objects.create(name = "Dublin", country = ireland)
        dublin.save()

        location = Location.objects.create(
                    venue = "Test Venue",
                    address1 = "Address 1 for test venue",
                    address2 = "Address 2 for test venue",
                    city = dublin,
                    country = ireland,
                    slug = "test-venue"
        )
        location.save()

        organiser1 = Organiser.objects.create(
                    user = user,
                    first_name = "Lord",
                    last_name = "FlashHeart",
                    blurb = "Meow, I'm a kitty cat... and a meow meow meow... and a meow meow meow",
                    contact_number = "",
                    email = "lfh@codinggrace.com",
                    url = "http://lfh.com",
                    slug = "lord-flashheart"
        )
        organiser1.save()

        mentor1 = Mentor.objects.create(user = organiser1, slug = "lfh")
        mentor1.save()

        sponsor1 = Sponsor.objects.create(
                    name = "A Sponsor",
                    url = "http://asponsor.com",
                    blurb = "We are a sponsor.",
                    what = "Venue",
                    slug = "a-sponsor"

        )
        sponsor1.save()

        event1 = Event.objects.create(
                    title = "Title for event one",
                    short_description = "This is a short description.",
                    description = "This is the main description",
                    start_datetime = datetime.datetime.utcnow().replace(tzinfo=utc),
                    end_datetime = datetime.datetime.utcnow().replace(tzinfo=utc),
                    location = location,
                    organiser = organiser1,
                    cost = "20.00",
                    event_url = "http://codinggrace.com",
                    slug = "title-for-event-one"

        )
        event1.level_type.add(beginner_level)
        event1.mentors.add(mentor1)
        event1.sponsors.add(sponsor1)
        event1.save()


    def testing_event(self):
        e = Event.objects.get(slug="title-for-event-one")
        self.assertEqual(e.title, "Title for event one")

    def test_get_chapters(self):
        """Testing get_chapters function
        """
        # [(Ireland, [Dublin])
        self.assertEqual(len(get_chapters()), 1)

        # <Country: Ireland>
        self.assertEqual(get_chapters()[0][0].name, "Ireland")

        # [<City: Dublin>]
        self.assertEqual(len(get_chapters()[0][1]), 1)

        # <City: Dublin>
        self.assertEqual(get_chapters()[0][1][0].name, "Dublin")


def get_chapters():
    """Should return something like
        [(Ireland, [Dublin, Galway]), (UK, [London])]
    """
    location = Location.objects

    countries = Country.objects.all().order_by('name')
    cities = City.objects.all().order_by('name')

    country_chapters = []
    for country in countries:
        cities = City.objects.filter(country__name=country).order_by('name')
        country_chapters.append((country, cities))

    return country_chapters
