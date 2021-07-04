from django import forms
from django.db.models import Q
from main.models import *
from django.forms import ModelForm

class GuestForm(forms.Form):
    firstname = forms.CharField(label='First Name', strip=True)
    lastname = forms.CharField(label='Last Name', strip=True)
    foodselection = forms.ChoiceField(choices=[(0, "Pork Tenderloin"), (1, "Sirloin"), (2, "Ahi Tuna"), (3, "Vegetarian")], label='Food Selection', widget=forms.Select(attrs={'class' : 'form-control'}))
    corn = forms.BooleanField(required=False, label='Corn on the Cob?', widget=forms.CheckboxInput())
    plusone = forms.BooleanField(required=False, label='Plus One?', widget=forms.CheckboxInput(attrs={'id':'plusOneCheck'}))
    firstnameplusone = forms.CharField(required=False, label='First Name', strip=True)
    lastnameplusone = forms.CharField(required=False, label='Last Name', strip=True)
    foodselectionplusone = forms.ChoiceField(choices=[(0, "Pork Tenderloin"), (1, "Sirloin"), (2, "Ahi Tuna"), (3, "Vegetarian")], label='Food Selection', widget=forms.Select(attrs={'class' : 'form-control'}))
    cornplusone = forms.BooleanField(required=False, label='Corn on the Cob?', widget=forms.CheckboxInput())
    
class MessageForm(forms.Form):
     name = forms.CharField(label='Name', strip=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter Name"}))
     message = forms.CharField(label='Message', strip=True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : "Type Your Message", 'rows' : "4"}))

class SongForm(forms.Form):
     name = forms.CharField(label='Name', strip=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter Name"}))
     title = forms.CharField(label='Title', strip=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Title"}))
     artist = forms.CharField(label='Artist', strip=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Artist"})) 
