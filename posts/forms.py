from django import forms
from .models import Post, Comment, Review, ReComment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='카페명',
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


    rating = forms.FloatField(
        label='평점',
        widget=forms.Select(choices=[
            (1.0, '★' * 1 + '☆' * 4),
            (1.5, '★' * 1 + '½' + '☆' * 3),
            (2.0, '★' * 2 + '☆' * 3),
            (2.5, '★' * 2 + '½' + '☆' * 2),
            (3.0, '★' * 3 + '☆' * 2),
            (3.5, '★' * 3 + '½' + '☆' * 1),
            (4.0, '★' * 4 + '☆' * 1),
            (4.5, '★' * 4 + '½' + '☆' * 0),
            (5.0, '★' * 5),
        ]),
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
        fields = ('content', 'rating','image',)


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