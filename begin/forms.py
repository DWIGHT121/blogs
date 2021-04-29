from django import forms
from .models import *

class CommentsForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()