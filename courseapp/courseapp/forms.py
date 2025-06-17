from django import forms

class UserForm(forms.Form):
    num1=forms.CharField(label='Username', max_length=100)
    num2=forms.CharField(label='Password', max_length=100)

    