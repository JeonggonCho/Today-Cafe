from django import forms
from .models import Post, Comment, Review, ReComment
from taggit.forms import TagField, TagWidget


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

    CHOICES=[('카공 모각코', '카공/모각코'), ('펫 카페', '펫 카페'), ('북 카페', '북 카페')]
    category = forms.ChoiceField(
        label='카테고리',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
        choices=CHOICES,
    )

    image = forms.ImageField(
        label='이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
            },
        )
    )

    tags = forms.CharField(
        label='태그',
        widget=TagWidget(
            attrs={
                'class': 'form-control',
                'placeholder': '태그는 콤마(,)로 구분하여 작성해주세요' 
            }
        )
    )


    class Meta:
        model = Post
        fields = ('title', 'address', 'phone_number', 'menu', 'hours', 'information', 'category', 'image', 'tags',)


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
        widget=forms.Select(
            choices=[
                (1.0, '★' * 1 + '☆' * 4),
                (1.5, '★' * 1 + '½' + '☆' * 3),
                (2.0, '★' * 2 + '☆' * 3),
                (2.5, '★' * 2 + '½' + '☆' * 2),
                (3.0, '★' * 3 + '☆' * 2),
                (3.5, '★' * 3 + '½' + '☆' * 1),
                (4.0, '★' * 4 + '☆' * 1),
                (4.5, '★' * 4 + '½' + '☆' * 0),
                (5.0, '★' * 5),
            ],
            attrs={
                'class': 'form-select',
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