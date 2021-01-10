from django.forms import ModelForm
from .models import Course, Bin, Assessment

class Courseform(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credits']

class Binform(ModelForm):
    class Meta:
        model = Bin
        fields = ['name', 'weight', 'drop_n_lowest']

class Assessmentform(ModelForm):
    class Meta:
        model = Assessment
        fields = ['name', 'weight', 'total', 'mark']