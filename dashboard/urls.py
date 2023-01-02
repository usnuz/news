from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='dashboard-index-url'),
    path('news', news, name='news-url'),
    path('add-news', add_news, name='add-news-url'),
    path('user-profile/', user_profile, name='user-profile-url'),
]