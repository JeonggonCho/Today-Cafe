from django import forms
from .models import Profile, Post, Comment, Review, ReComment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    address = forms.CharField(
        label='주소',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    phone_number = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    menu = forms.CharField(
        label='메뉴',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    menu = forms.CharField(
        label='메뉴',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    hours = forms.CharField(
        label='영업시간',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    
    information = forms.CharField(
        label='편의시설 정보',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
            },
        ),
    )
    
    class Meta:
        model = Post
        fields = ('title', 'address', 'phone_number', 'menu', 'hours', 'information', 'image',)



class ReviewForm(forms.ModelForm):
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
                'multiple': 'True',
            },
        ),
        required=False,
    )
    class Meta:
        model = Review
        fields = ('content','image',)


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