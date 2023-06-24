from django import forms
from pizza.models import Pizza


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ('company', 'name', 'dough_type', 'description', 'image')
