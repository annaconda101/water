from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from fire.models import Question


def index(request):
    questions = Question.objects.all()
    c = { 'questions': questions, }

    return render_to_response('fire/index.html', c)


