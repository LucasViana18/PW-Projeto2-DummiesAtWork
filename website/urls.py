from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('portfolio', views.portfolio_page_view, name='portfolio'),
    path('services', views.services_page_view, name='services'),
    path('aboutus', views.aboutus_page_view, name='aboutus'),
    path('contact', views.contact_page_view, name='contact'),
    path('quizz', views.quizz_page_view, name='quizz'),
]