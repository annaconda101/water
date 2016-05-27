from django.shortcuts import render_to_response

from fire.models import Question


def index(request):
    questions = Question.objects.all()
    c = { 'questions': questions, }

    return render_to_response('index.html', c)
