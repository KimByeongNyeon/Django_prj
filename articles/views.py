import random
from django.shortcuts import render
from .models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육', ]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # 사용자가 요청보낸 데이터를 추출해서 context 딕셔너리에 세팅
    context = {
        'message': request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)
