import datetime
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from My.models import Book

# Create your views here.

def hello(request):

    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()

    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    hour_offset = offset
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)

    return render_to_response('future_datetime.html', locals())

def athlete_list(request):

    athlete_list = [
        {'name' : 'benzema', 'sports_played' : ['football', 'basketball', 'tennis']},
        {'name' : 'kaka', 'sports_played' : ['football']},
        {'name' : 'bale', 'sports_played' : []},
    ]

    return render_to_response('athlete_list.html', locals())

def country_city_list(request):

    country_city_list = [
        {'country' : 'America', 'city' : ['NewYork', 'Crafornia']},
        {'country' : 'China', 'city' : ['Shanghai', 'GuangDong', 'TaiWan']},
    ]

    return render_to_response('country_city_list.html', locals())

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    html.sort()

    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 10:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)

            return render_to_response('search_results.html', {'books': books, 'query': q})

    return render_to_response('search_form.html',
                {'error': error})