from django.forms import ModelForm
from .models import Contact
from .models import Quizz

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'