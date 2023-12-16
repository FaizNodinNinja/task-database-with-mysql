from django.forms import ModelForm
from .models import Studentrecord
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Studentrecord
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),

        }
