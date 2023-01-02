from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index-url'),
    path('single/<int:pk>/', single, name='single-url'),
    path('reply-comment/<int:pk>/', reply_comment, name='reply-comment-url'),
]