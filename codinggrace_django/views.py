from django.shortcuts import redirect, render
from django.utils.timezone import now

from events.models import Chapter, City, Country, Event, Location, Organiser
from news.models import NewsPost

def home(request):
    events_list = Event.objects.filter(start_datetime__gte=now()).order_by('start_datetime')

    context = {'events_list': events_list, 'active':'home'}
    return render(request, 'codinggrace_django/index.html', context)

def chapters(request):
	context = {"active":"chapters"}
	context["country_chapters"] = get_chapters()
	return render(request, 'codinggrace_django/chapters.html', context)

def chapter(request, chapter):
	context = {"active":"about"}

	chapter_objects = Event.objects.filter(location__city__name=chapter)

	# Get chapter's upcoming events
	current_upcoming_events = chapter_objects.filter(start_datetime__gte=now()).order_by('start_datetime').reverse()
	context["current_upcoming_events"] = current_upcoming_events

	# Get past events for this chapter
	past_events = chapter_objects.filter(start_datetime__lt=now()).order_by('start_datetime')
	context["past_events"] = past_events

	# Get Organisers from this chapter
	chapter_organisers = list(set([i.organiser for i in chapter_objects]))
	context["chapter_organisers"] = chapter_organisers

	# Get the latest 5 chapter-related news
	news_post_objects = NewsPost.objects.filter(chapter__city__name=chapter).order_by('published').reverse()
	context["news_post_objects"] = news_post_objects.order_by('published')[:5]

	# Get the chapter object if it exists, if not, just return the string
	try:
		context["chapter"] = Chapter.objects.get(city__name = chapter)
	except Chapter.DoesNotExist:
		context["chapter"] = chapter

	# Get list of countries and its chapters
	context["country_chapters"] = get_chapters()

	return render(request, 'codinggrace_django/chapter.html', context)

def news_redirect(request, year, month, day, slug):
    # return redirect('news', year=year, month=month, day=day, slug=slug)
    special_redirects = ["introduction-to-f-sharp-with-phil-trelford"]
    print(slug)
    print("ERWERWE")
    if slug in special_redirects:
    	print("SSSSSSS")
    	slug = "introduction-to-f-with-phil-trelford"
    return redirect("/news/{}-{}-{}-{}/".format(slug, year, month, day))

def codeofconduct(request):
	context = {"active":"conduct"}
	return render(request, 'codinggrace_django/codeofconduct_longer.html', context)

def get_chapters():
	# Get countries with its cities and return the list
	# [(Ireland, [Dublin, Galway]), (UK, [London])]
	location = Location.objects

	countries = Country.objects.all().order_by('name')
	cities = City.objects.all().order_by('name')

	country_chapters = []
	for country in countries:
		cities = City.objects.filter(country__name=country).order_by('name')
		country_chapters.append((country, cities))

	return country_chapters

