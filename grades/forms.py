from django.forms import ModelForm
from .models import Course, Bin

class Courseform(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credits']

class Binform(ModelForm):
    class Meta:
        model = Bin
        fields = ['name', 'weight', 'drop_n_lowest']