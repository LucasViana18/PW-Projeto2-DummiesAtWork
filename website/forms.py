from django.forms import ModelForm
from .models import Contact
from .models import Question

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'