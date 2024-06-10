from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("photos/", views.PhotoView.as_view(), name="photos"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("temporary/", views.TemporaryView.as_view(), name="temporary"),
    path("email/", views.EmailView.as_view(), name="email"),
    path(
        "email/email_success/", views.EmailSuccessView.as_view(), name="email_success"
    ),
]
