from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm, QuizzForm


# Create your views here.
def home_page_view(request):
    return render(request, 'website/index.html')

def portfolio_page_view(request):
    return render(request, 'website/portfolio.html')

def services_page_view(request):
    return render(request, 'website/services.html')

def aboutus_page_view(request):
    return render(request, 'website/aboutus.html')

def contact_page_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'website/contact.html', context)

def quizz_page_view(request):
    form = QuizzForm(request.POST or None)

    context = {'quizz_form': form}
    return render(request, 'website/quizz.html', context)
