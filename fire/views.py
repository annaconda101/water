from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User

from fire.models import Question
from .forms import AnswerForm


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(data=request.POST, question=question)
        if form.is_valid():
            form.save()
            return redirect('fire_question-detail', id=id)

    else:
        form = AnswerForm(question=question)

    c = { 'question': question, 'form': form, }

    return render(request, 'fire/question-detail.html', c)


