from django import forms

def check_for_m(value):
    if value[0]=='m':
        raise forms.ValidationError('data not inserted')

class student(forms.Form):
    NAME=forms.CharField(max_length=100,validators=[check_for_m])
    AGE=forms.IntegerField()
    EMAIL=forms.EmailField()
    RE_ENTER_EMAIL=forms.EmailField()
    BOTCATCHER=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    
    def clean(self):
        e=self.cleaned_data['EMAIL']
        r=self.cleaned_data['RE_ENTER_EMAIL']

        if e!=r:
            raise forms.ValidationError('RE ENTER EMAIL NOT MATCHED IN SPECIFIC MAIL')
        
    def clean_BOTCATCHER(self):
        bot=self.cleaned_data['BOTCATCHER']
        if len(bot)>0:
            raise forms.ValidationError('inserted by bot or hacker')