import members
from django import forms

from .models import Post
from members.models import Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
        
class PrfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
