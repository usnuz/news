from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_base, name='chat-base-url'),
    path('user/<int:pk>/', chat, name='chat-url'),
]
