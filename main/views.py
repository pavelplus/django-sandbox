from django.shortcuts import redirect, get_object_or_404
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


def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:persons')
    else:
        form = PersonForm()

    context = {
        'form': form,
        'title': 'Создание новой персоны',
    }
    return TemplateResponse(request, 'main/person_edit.html', context)
    


def person_edit(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('main:persons')
    else:
        form = PersonForm(instance=person)

    context = {
        'form': form,
        'title': 'Редактирование персоны',
    }
    return TemplateResponse(request, 'main/person_edit.html', context)



def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('main:persons')