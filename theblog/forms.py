from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','body')

		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Please Enter a Title'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Specify a Tag'}),
			'author' : forms.Select(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Thoughts'}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','body')

		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Edit The Title'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Edit The Tag'}),
			'body' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Edit The Description'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')
		widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name'}),
			'body' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Comment'}),
		}				