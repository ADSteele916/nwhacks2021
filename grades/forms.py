from django import forms

class Courseform(forms.Form):
    course_name = forms.CharField(label="Course name", max_length=20)
    course_credits = forms.IntegerField(label="Course credits")