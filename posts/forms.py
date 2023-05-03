from django import forms
from .models import Profile, Post, Comment, Review, ReComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image',)



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content','image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ('content', 'comment')
    


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='Comment',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)