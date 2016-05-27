from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

from fire.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the fire index.")


