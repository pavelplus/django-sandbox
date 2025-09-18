from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Person
from .forms import PersonForm


# Create your views here.
def index(request):
    return TemplateResponse(request, 'main/index.html', {})


def person_database(request):
    persons = Person.objects.all()
    form = PersonForm()
    context = {
        'persons': persons,
        'form': form,
    }
    return TemplateResponse(request, 'main/persons.html', context)