from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm, QuizzForm
from .models import Contact

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
    context = {'contacts': Contact.objects.all()}

    return render(request, 'website/contact.html', context)

def new_contact_page_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contact'))

    context = {'form': form}
    return render(request, 'website/addcontact.html', context)

def edit_contact_page_view(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contact'))

    context = {'form': form, 'contact_id': contact_id}
    return render(request, 'website/editcontact.html', context)

def delete_contact_page_view(request, contact_id):
    Contact.objects.get(pk=contact_id).delete()
    return HttpResponseRedirect(reverse('website:contact'))

def quizz_page_view(request):
    form = QuizzForm(request.POST or None)

    context = {'quizz_form': form}
    return render(request, 'website/quizz.html', context)
