"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .models import Blog
from .models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=200)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол', 
                             choices=[('1', 'Мужской'), ('2', 'Женский')], 
                             widget=forms.RadioSelect, initial=1)
    quantity = forms.ChoiceField(label='Как часто вы путешествуете?', 
                             choices=(('1', 'Каждый месяц'),
                             ('2', 'Несколько раз в полгода'),
                             ('3', 'Несколько раз в год')), initial=1)
    tours = forms.CharField(label='Какие туры нашей компании Вы посетили?',
                               widget=forms.Textarea(attrs={'rows':5, 'cols':70}))
    norm = forms.CharField(label='Что вам понравилось?',
                               widget=forms.Textarea(attrs={'rows':8, 'cols':100}))
    nenorm = forms.CharField(label='Есть ли недостатки?',
                               widget=forms.Textarea(attrs={'rows':8, 'cols':100}))
    notice = forms.BooleanField(label='Хотите ли вы получать новости о новых турах на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)

class CommentForm (forms.ModelForm):
     class Meta:
         model = Comment # используемая модель
         fields = ('text',) # требуется заполнить только поле text
         labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
     class Meta:
         model = Blog # используемая модель
         fields = ('title','description', 'content', 'image',) 
         labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"} 