from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Name",'name':"username",'class':"form-control"}),
            'phone':TextInput(attrs={'placeholder':"Phone",'name':"phone",'class':"form-control"}),
            'address':Textarea(attrs={'placeholder':"Address",'name':"address",'class':"form-control",'row':"2"}),
            'message':Textarea(attrs={'placeholder':"Message",'name':"message",'class':"form-control",'row':"3"}),
         }