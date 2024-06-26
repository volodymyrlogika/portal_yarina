from django.contrib import admin

from forum.models import Topic, Message

# Register your models here.
admin.site.register(Topic)
admin.site.register(Message)