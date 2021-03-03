import members
from django import forms

from .models import Post
from members.models import Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
