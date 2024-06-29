from .models import CommentsPost, Post
from django import forms
from ckeditor.fields import RichTextField

class TextForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea,required=True)



class BlogForm(forms.ModelForm):
    description = RichTextField()
    class Meta:
        model = Post
        fields = (
            'post_title',
            'category',
            'banner',
            'description',
        )