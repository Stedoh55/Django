from django import forms
from .models import UserComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'comment']