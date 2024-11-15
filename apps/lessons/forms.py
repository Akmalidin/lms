from django import forms
from django.db import models
from .models import Comment, CommentReply, Question
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }