from django.shortcuts import render, redirect
from dashboard.models import *
from django.db.models import Count


def index(request):
    news = News.objects.all()
    usr = User.objects.all()
    likes = Like.objects.all()
    comments = Comments.objects.all()
    context = {
        'news': news,
        'usr': usr,
        'likes': likes,
        'comments': comments,

    }
    return render(request, 'dashboard/index.html', context)


def news(request):
    uz = News.objects.filter(category__name="O'zbekiston").last()
    jahon = News.objects.filter(category__name="Jahon").last()
    siyosiy = News.objects.filter(category__name="Siyosiy").last()
    texnologiya = News.objects.filter(category__name="Texnologiya").last()
    popular_news = News.objects.annotate(like_count=Count('like')).order_by('-like_count')[:4]
    context = {
        'uz': uz,
        'jahon': jahon,
        'siyosiy': siyosiy,
        'texnologiya': texnologiya,
        'popular_news': popular_news
    }
    return render(request, 'dashboard/blog-posts.html', context)
    
    
def add_news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        img = request.FILES.get('img')
        user = request.user
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        News.objects.create(
            title=title,
            body=body,
            img=img,
            user=user,
            category=category,
        )
        return redirect('news-url')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/add-news.html', context)


def user_profile(request):
    context = {
        'usr': request.user
    }
    return render(request, 'dashboard/user-profile.html', context)
