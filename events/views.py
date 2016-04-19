from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils.timezone import now

from events.models import Event, Location, Organiser
from news.models import NewsPost

# Create your views here.
def index(request):
    """Events page listins, upcoming and past events"""
    events_list = Event.objects.filter(is_published=True)
    context = {'events_list': events_list, 'active':'events'}

    context["current_events"] = events_list.filter(start_datetime__gte=now()).order_by('start_datetime')

    ## Get past events
    past_events = events_list.filter(start_datetime__lt=now())

    # Get sorted list of months from pre-defined dict; get sorted list of years in descending order from Event model
    month_dict = {1:"jan", 2:"feb", 3:"mar", 4:"apr", 5:"may", 6:"jun", 7:"jul", 8:"aug", 9:"sep", 10:"oct", 11:"nov", 12:"dec"}
    month_list = list(set(month_dict.keys()))
    years_list = list(set([e.start_datetime.year for e in events_list]))
    years_list.sort()
    years_list.reverse()

    # Return list to template, e.g.
    # ((2014, ("jan":(<event>,<event2>,...)), ((2013, (...))) )
    yearly_events = []
    for y in years_list:
        monthly_events = []
        for m in month_list:
            m_events = events_list.filter(start_datetime__lte=now()).filter(start_datetime__year=y).filter(start_datetime__month=m).order_by("start_datetime")
            if len(m_events) > 0:
                monthly_events.append( (month_dict[m], m_events ) )
        yearly_events.append( (y, monthly_events) )

    context["past_events"] = yearly_events

    return render(request, 'events/index.html', context)

def event(request, slug, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event":event}

    if ("/ti.to/" in event.event_url) or ("/tito/" in event.event_url):
        event_name = event.event_url.split("/")[-1]
        event_org = event.event_url.split("/")[-2]
        tito_css = '<link rel="stylesheet" type="text/css" href="https://css.tito.io/v1" />'
        context["tito_css"] = tito_css
        tito_js = '<script src="https://js.tito.io/v1" async></script>'
        context["tito_js"] = tito_js
        tito_form = '<tito-widget event="{}/{}"></tito-widget>'.format(event_org, event_name)
        context["tito_form"] = tito_form

    workshop_ended = True
    if now() < event.end_datetime:
        workshop_ended = False
    context["workshop_ended"] = workshop_ended

    # If the workshop has ended, get its related news article if it exists
    # if workshop_ended:
    try:
        context["news"] = NewsPost.objects.filter(event__pk=event_id)
    except NewsPost.DoesNotExist:

        pass

    return render(request, 'events/event.html', context)

def registered(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event":event, "success":True}
    return render(request, 'events/event.html', context)
