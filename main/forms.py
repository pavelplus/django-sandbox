from django.forms import ModelForm, DateInput

from .models import Person


""" class DateInput(DateInput):
    input_type = 'date' """

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'sex', 'birth_date', 'email', 'phone_number', 'notes']
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
        }