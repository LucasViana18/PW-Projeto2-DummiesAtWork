from django.forms import ModelForm
from .models import Contact, Comment, Question

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['points']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'