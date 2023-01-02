from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from dashboard.models import User, Region


def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        avatar = request.FILES.get('avatar')
        region = request.POST.get('region')
        bio = request.POST.get('bio')
        if password == repassword:
            new_region = Region.objects.create(name=region)
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                avatar=avatar,
                region=new_region,
                bio=bio,
            )
            return redirect('dashboard-index-url')
        else:
            return redirect('sign-up-url')
    return render(request, 'account/sign-up.html')


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('dashboard-index-url')
        else:
            a = {
                'msg': str('username yoki parol xato')
            }
            return render(request, 'account/sign-in.html', a)
    return render(request, 'account/sign-in.html')


def log_out(request):
    logout(request)
    return redirect('index-url')
