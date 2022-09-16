from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class Users(ModelForm):
    class Meta:
        model = User
        fields=['username','password']
    