from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import EmailForm
from .models import MyLibrary, PhotoLibrary


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class PhotoView(ListView):
    template_name = "photos.html"
    queryset = PhotoLibrary.objects.order_by("id")
    context_object_name = "photo"


class PortfolioView(ListView):
    template_name = "portfolio.html"
    queryset = MyLibrary.objects.order_by("-posted_at")
    context_object_name = "portfolio"


class TemporaryView(TemplateView):
    template_name = "temporary.html"


class EmailView(FormView):
    template_name = "email.html"
    form_class = EmailForm
    success_url = "email_success"

    def form_valid(self, form):
        # フォームのデータを取得
        name = form.cleaned_data["name"]
        subject = form.cleaned_data["subject"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        # メール送信
        send_mail(subject, message, email, ["aokihayate20030709@gmail.com"])
        return super().form_valid(form)


class EmailSuccessView(TemplateView):
    template_name = "email_success.html"
