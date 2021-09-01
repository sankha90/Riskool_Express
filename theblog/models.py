from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from tinymce import models as tinymce_models


#from django_editorjs import EditorJsField




# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	#body = tinymce_models.HTMLField()
	#body = EditorJsField()
	post_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User,related_name='blog_posts')


	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')


class Comment(models.Model):
	post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

	def get_absolute_url(self):
		return reverse('home')	






