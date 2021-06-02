from django.db import models
from django import forms
import datetime


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=30)
    subject = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Quizz(models.Model):
    YES_OR_NO_CHOICE = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )

    GENRE_OPTIONS = (
        ("ACTION", "Action"),
        ("SHOOTER", "Shooter"),
        ("ROLE-PLAY", "Role-play"),
        ("SPORT", "Sport"),
        ("ADVENTURE", "Adventure"),
        ("FIGHTING", "Fighting"),
        ("RACING", "Racing"),
        ("STRATEGY", "Strategy"),
        ("OTHERS", "Others"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=datetime.date.today)
    have_you_played_VR_before = models.CharField(max_length=6, choices=YES_OR_NO_CHOICE, default='yes')
    select_your_favorite_game_genres = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                 choices=GENRE_OPTIONS)

    def __str__(self):
        return self.first_name + " " + self.last_name