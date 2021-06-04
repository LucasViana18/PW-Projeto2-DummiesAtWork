from django.contrib import admin
from website.models import Contact, Question, Comment

# Register your models here.
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Comment)