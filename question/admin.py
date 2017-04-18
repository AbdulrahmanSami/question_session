from django.contrib import admin
from .models import Question,Question_sessions
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','question_session']
admin.site.register(Question,QuestionAdmin)
class Qustion_sessionsAdmin(admin.ModelAdmin):
    fields = ['title']
admin.site.register(Question_sessions,Qustion_sessionsAdmin)