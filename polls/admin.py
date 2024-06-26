from django.contrib import admin

from polls.models import Question, Poll, Answer, PollResult

# Register your models here.
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(PollResult)