from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        
        
