import members
from django import forms

from .models import Post
from members.models import Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description','image']

        widgets = {
        
            'title': forms.Textarea(attrs={'class': 'editable medium-editor-textarea','style':'font-weight: bold; font-size: 150%;','rows':'3' ,'cols':'30'})
        }
