from django.shortcuts import render, redirect
from dashboard.models import *


def index(request):
    uz = News.objects.filter(category__name="O'zbekiston").last()
    jahon = News.objects.filter(category__name="Jahon").last()
    texnologiya = News.objects.filter(category__name="Texnologiya").last()
    news = News.objects.all()
    print(uz.id)
    context = {
        'news': news,
        'uz': uz,
        'jahon': jahon,
        'texnologiya': texnologiya,
    }
    return render(request, 'font/index.html', context)


def single(request, pk):
    print(request.user.id)
    if request.method == "POST":
        post = News.objects.get(pk=pk)
        text = request.POST.get('text')
        new_comment = Comments.objects.create(
            text=text,
            post=post,
            author=request.user,
        )
        return redirect('single-url', post.id)
    post = News.objects.get(pk=pk)
    comments = Comments.objects.filter(post=post)
    context = {
        'comments': comments,
        'post': post,
    }
    return render(request, 'font/single.html', context)


def reply_comment(request, pk):
    if request.method == "POST":
        text = request.POST.get('reply_text')
        comment_id = request.POST.get('comment_id')
        post = News.objects.get(pk=pk)
        comment = Comments.objects.get(id=comment_id)
        new_comment = Comments.objects.create(
            post=post,
            author=request.user,
            text=text,
            parent=comment,
        )
        print(comment.parent)
        print(123)
        return redirect('single-url', post.id)
    post = News.objects.get(pk=pk)
    return render(request, 'single.html', post.pk)
