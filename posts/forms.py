from django import forms
from .models import Profile, Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
            },
        ),
    )

    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
                'multiple': 'True'
            },
        ),
        required=False,
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'image',)


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