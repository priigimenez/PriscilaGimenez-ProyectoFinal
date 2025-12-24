from django import forms
from .models import Post, Category, Tag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre de la categoría',
            'description': 'Descripción (ej: "Artículos sobre calidad de datos, gobierno de datos, etc.")'
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': 'Etiqueta (ej: "Data Quality", "Metadata", "Stewardship")'
        }

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Buscar posts', max_length=100, required=False)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=100, required=True)
    last_name = forms.CharField(label="Apellido", max_length=100, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user