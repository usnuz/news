from dashboard.models import User


def all_users(request):
    return {'all_users': User.objects.all()}
