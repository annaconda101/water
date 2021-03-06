from django import forms

from .models import Answer, Question


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super(AnswerForm, self).__init__(*args, **kwargs)

    def save(self):
        answer = super(AnswerForm, self).save(commit=False)
        answer.question = self.question
        answer.save()

        return answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'description',)

    def __init__(self, *args):
        super(QuestionForm, self).__init__(*args)

