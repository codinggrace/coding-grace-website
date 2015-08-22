from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from codinggrace_django.views import get_chapters
from events.models import Chapter
from news.models import NewsPost

# Create your views here.
def index(request):
    context = {"active":"news"}
    news_objects = NewsPost.objects.filter(is_published=True)
    all_news = news_objects.order_by('published').reverse()[:5]
    context["all_news"] = all_news
    context["chapters"] = get_chapters()
    return render(request, 'news/index.html', context)


def news(request, slug, year, month, day):

    article = NewsPost.objects.filter(slug=slug).filter(published__year=year).filter(published__month=month).filter(published__day=day)
    if article:
        context = {"article":article[0]}
    else:
        context = {}
    return render(request, 'news/article.html', context)


def all_articles(request):
    context = {}
    articles = NewsPost.objects.filter(is_published=True)
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        news_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_items = paginator.page(paginator.num_pages)
    context["news_items"] = news_items

    context["chapters"] = get_chapters()
    context["page_title"] = "ALL NEWS"
    return render(request, 'news/all_articles.html', context)

def all_articles_chapter(request, chapter):
    context = {}
    if chapter == "other":
        articles = NewsPost.objects.filter(chapter=None).filter(is_published=True)
    else:
        articles = NewsPost.objects.filter(chapter__city__name=chapter).filter(is_published=True)

    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        news_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_items = paginator.page(paginator.num_pages)
    context["news_items"] = news_items

    # context["chapters"] = Chapter.objects.all()
    context["page_title"] = "ALL {} NEWS".format(chapter.upper())

    context["chapters"] = get_chapters()

    return render(request, 'news/all_articles.html', context)


