from django.forms import ModelForm
from django.forms.renderers import DjangoTemplates

from .models import Person


renderer = DjangoTemplates

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'sex', 'birth_date', 'email', 'phone_number', 'notes']