from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from fire.models import Question


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    c = { 'question': question, }

    return render(request, 'fire/question-detail.html', c)


