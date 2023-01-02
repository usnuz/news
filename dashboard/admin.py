from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Comments)
admin.site.register(Category)
# admin.site.register(ReplyComment)
admin.site.register(Like)