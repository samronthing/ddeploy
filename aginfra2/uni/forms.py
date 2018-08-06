from django import forms
from django.core import validators

class emailform(forms.Form):
    name= forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Name','maxlength':30,'class':'formele'}))
    email=forms.EmailField(label="",widget=forms.EmailInput(attrs={'maxlength':60,'placeholder':'Email','class':'formele'}))
    subject=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Subject','maxlength':150,'class':'formele'}))
    message=forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder':'Message','class':'formele','rows':4,'maxlength':500}))
