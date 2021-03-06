from django.shortcuts import get_object_or_404, render, redirect

from fire.models import Question, Answer
from .forms import AnswerForm, QuestionForm


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(data=request.POST, question=question)
        if form.is_valid():
            form.save()
            return redirect('fire_question-detail', id=id)

    else:
        form = AnswerForm(question=question)

    c = {'question': question, 'form': form,}

    return render(request, 'fire/question-detail.html', c)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():  
            question = form.save()
            return redirect('fire_question-detail', question.id)

    else:
        form = QuestionForm()

    c = {'form': form}

    return render(request, 'fire/question-new.html', c)
    

def answer_upvote(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.upvote()

    return redirect('fire_question-detail', answer.question.id)


def answer_downvote(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.downvote()

    return redirect('fire_question-detail', answer.question.id)
