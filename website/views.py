from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm, QuestionForm
from .models import Contact, Question


# Create your views here.

def home_page_view(request):
    return render(request, 'website/index.html')

def portfolio_page_view(request):
    return render(request, 'website/portfolio.html')

def services_page_view(request):
    return render(request, 'website/services.html')

def aboutus_page_view(request):
    return render(request, 'website/aboutus.html')

#Contact
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


# Quizz
def question_page_view(request):
    context = {'questions': Question.objects.all()}

    return render(request, 'website/quizz.html', context)

def do_question_page_view(request):
    form = QuestionForm(request.POST or None)

    if form.is_valid():

        #if Question.objects.get().best_selling_VR_game == "Beat Saber":
        #    Question.objects.get().points += 1

        #if Question.objects.get().most_popular_type_of_movement_in_VR == "Teleport":
        #    Question.objects.get().points += 1

        #if Question.objects.get().can_VR_cause_motion_sickness == True:
        #    Question.objects.get().points += 1

        #if Question.objects.get().bruhh_is_a_3D_ragdoll_physics_game == True:
        #    Question.objects.get().points += 1

        #if Question.objects.get().what_is_bloodthirst_game_perspective == "2D Sideview":
        #    Question.objects.get().points += 1

        #if Question.objects.get().which_services_we_do_not_offer == "AR Production":
        #    Question.objects.get().points += 1

        #if Question.objects.get().how_many_links_there_are_in_the_home_page == 6:
        #    Question.objects.get().points += 1

        #if Question.objects.get().what_is_anything_but_dark_genre == "Adventure":
        #    Question.objects.get().points += 1

        #if Question.objects.get().what_was_the_icon_used_in_anastasis == "Tree":
        #    Question.objects.get().points += 1

        #if Question.objects.get().is_there_a_demonstration_video_on_this_website == True:
        #    Question.objects.get().points += 1

        form.save()
        return HttpResponseRedirect(reverse('website:question'))

    context = {'question_form': form}

    return render(request, 'website/doquizz.html', context)