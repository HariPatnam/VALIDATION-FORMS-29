from django import forms

def check_for_m(value):
    if value[0]=='m':
        raise forms.ValidationError('data not inserted')

class student(forms.Form):
    NAME=forms.CharField(max_length=100,validators=[check_for_m])
    AGE=forms.IntegerField()