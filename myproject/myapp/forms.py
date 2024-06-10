from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    subject = forms.CharField(label="Subject", max_length=100)
    email = forms.EmailField(label="E-Mail Address")
    message = forms.CharField(label="Message", widget=forms.Textarea)
