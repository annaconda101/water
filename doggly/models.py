import json
import requests

from django.db import models
from rest_framework import status


class Fact(models.Model):
    text = models.CharField(max_length=200)
    image_url = models.URLField()

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        dog_api_url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(dog_api_url)
        assert response.status_code == status.HTTP_200_OK
        image_dict = json.loads(response.text)
        self.image_url = image_dict['message']

        super(Fact, self).save(*args, **kwargs)
