from django import forms

def check_for_m(value):
    if value[0]=='m':
        raise forms.ValidationError('data not inserted')

class student(forms.Form):
    NAME=forms.CharField(max_length=100,validators=[check_for_m])
    AGE=forms.IntegerField()
    EMAIL=forms.EmailField()
    RE_ENTER_EMAIL=forms.EmailField()
    
    def clean(self):
        e=self.cleaned_data['EMAIL']
        r=self.cleaned_data['RE_ENTER_EMAIL']

        if e!=r:
            raise forms.ValidationError('RE ENTER EMAIL NOT MATCHED IN SPECIFIC MAIL ')