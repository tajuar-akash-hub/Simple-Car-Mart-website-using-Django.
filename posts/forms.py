from posts.models import comments_Model
from django import forms

class Comment_form(forms.ModelForm):
    class Meta:
        model = comments_Model
        fields= ['name','email','body']