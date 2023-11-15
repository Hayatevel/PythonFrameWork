from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from .models import PhotoLibrary
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.
class IndexView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('myapp:email_success')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        subject ='Contact'
        message = \
            f'{name}\n {email}\n {message}\n'
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=to_list
        )
        message.send()
        messages.success(self.request, 'Your message has been sent!')
        return super().form_valid(form)
    
    
class PhotoView(ListView):
    template_name = 'photos.html'
    queryset = PhotoLibrary.objects.order_by('id')
    
    
class PortfolioView(TemplateView):
    template_name = 'portfolio.html'
    
    
class EmailSuccessView(TemplateView):
    template_name = 'email_success.html'
    
    
