from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answers')

    def __unicode__(self):
        return '%s - %s' %(self.text, self.question) 
