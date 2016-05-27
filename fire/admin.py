from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'score')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
