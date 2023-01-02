from django.urls import path
from .views import *


urlpatterns = [
    path('sign-up/', sign_up, name='sign-up-url'),
    path('sign-in/', sign_in, name='sign-in-url'),
    path('logout/', log_out, name='logout-url'),
]