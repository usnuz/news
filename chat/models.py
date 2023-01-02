from django.db import models
from dashboard.models import *

# Create your models here.
class Chat(models.Model):
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media//% Y/% m/% d/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to')
    date_created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str__(self):
        return self.text
