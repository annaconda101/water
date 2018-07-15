from django.shortcuts import get_object_or_404, render, redirect

from .forms import FactForm
from .models import Fact


def fact_list(request):
    facts = Fact.objects.all()

    if request.method == "POST":
        form = FactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('doggly-fact-list')

    else:
        form = FactForm()

    c = {
            'facts': facts,
            'form': form
    }

    return render(request, 'doggly/fact_list.html', c)
