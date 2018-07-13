from django.db import models
from django.core.urlresolvers import reverse

from textblob import TextBlob


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fire_question-detail', kwargs={'id': self.pk})


class Answer(models.Model):
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answers')
    sentiment_polarity = models.DecimalField(max_digits=5, decimal_places=3)

    def __unicode__(self):
        return '%s - %s' %(self.text, self.question) 
    
    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.sentiment_polarity = self.get_sentiment_polarity()
        super(Answer, self).save(*args, **kwargs)

    def get_upvote_url(self):
        return reverse('fire_answer-upvote', kwargs={'id': self.pk})

    def get_downvote_url(self):
        return reverse('fire_answer-downvote', kwargs={'id': self.pk})

    def upvote(self):
        new_score = self.score + 1
        self.score = new_score

        self.save()

    def downvote(self):
        new_score = self.score - 1
        self.score = new_score

        self.save()

    def get_sentiment_polarity(self):
        blob = TextBlob(self.text)
        sentiment_scores = [sentence.polarity for sentence in blob.sentences]

        return sum(sentiment_scores)/len(sentiment_scores)


