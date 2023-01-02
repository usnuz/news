from django.shortcuts import render, redirect
from dashboard.models import *
from chat.models import Chat


def chat_base(request):
    return render(request, 'chat.html')


def chat(request, pk):
    if request.method == "POST":
        text = request.POST.get('text')
        author = request.user
        Chat.objects.create(
            text=text,
            author=author,
            to=User.objects.get(id=pk)
        )
    usr = User.objects.get(id=pk)
    mymsg = Chat.objects.filter(author=request.user, to=usr)
    msg = Chat.objects.filter(author=usr, to=request.user)
    context = {
        'mymsg': mymsg,
        'msg': msg,
        'usr': usr
    }
    print(msg)
    return render(request, 'chat.html', context)


