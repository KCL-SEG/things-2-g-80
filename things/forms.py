"""Forms of the project."""
from django.forms import ModelForm, Textarea
from .models import Thing
# Create your forms here.

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': Textarea()}