from django import forms

from .models import Answer, Question
from textblob import TextBlob


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
        answer.sentiment_polarity = self.get_sentiment_polarity(answer.text)
        answer.save()

        return answer

    @staticmethod
    def get_sentiment_polarity(text):
        blob = TextBlob(text)
        sentiment_scores = [sentence.polarity for sentence in blob.sentences]

        return sum(sentiment_scores)/len(sentiment_scores)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'description',)

    def __init__(self, *args):
        super(QuestionForm, self).__init__(*args)

