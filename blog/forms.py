from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Post, Category, Comment

#retrieve all category names and store in a tuple
choices = Category.objects.all().values_list('name','name')

choices_list = []

for item in choices:
    choices_list.append(item)

#Adding a form to create posts
class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'header_image', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"this is the title"}),
            'header_image': ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'This is where you can post your content'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'})
        }

#Adding a form to update posts
class UpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'header_image', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"this is the title"}),
            'header_image': ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'This is where you can post your content'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'})
        }

#Adding a form to add comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'placeholder': 'Leave a comment'}),
        }