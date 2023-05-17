from django.forms import models

from .models import Comment


class CommentForm(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
