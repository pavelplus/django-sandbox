from django.forms import ModelForm

from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'sex', 'birth_date', 'email', 'phone_number', 'notes']