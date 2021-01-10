from django.forms import ModelForm
from .models import Course

class Courseform(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credits']