from django.forms import ModelForm
from .models import Posts, Contact


class PostForm(ModelForm):
    class Meta:
        model = Posts
        exclude = ["author"]


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ["date_created"]
