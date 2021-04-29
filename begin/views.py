from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail
from .forms import *
from django.db.models import Q

# Create your views here.
def home(request):
    list_of_articles = Articles.objects.order_by('-pub_date')
    list1 = {'list_of_articles': list_of_articles }
    return render(request, 'page1.html', list1)
    
def detail_view(request, id):
    article = get_object_or_404(Articles, id = id)
    photos = ArticlesImage.objects.filter(article= article)
    full_list = Articles.objects.order_by('-pub_date')

    return render(request, 'detail.html', {
        'article':article,
        'photos': photos,
        'full_list': full_list,
    }
    )

def profile(request):
    return render(request, 'profile.html')


def search(request):
    query = request.GET.get('q', None)
    if query:
        data = Articles.objects.filter(Q(topic__icontains = query) | Q(start_text__icontains = query))
    else: 
        data = Articles.objects.all()
    temp_data = {
        'data': data,
        'query': query
    }

    return render(request, 'search.html', temp_data)


# if request.method == "POST":
    