from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from imagekit.models import ImageSpecField
from imagekit.forms import ProcessedImageField
from imagekit.processors import Thumbnail
from imagekit.processors import ResizeToFill
from django import forms


class CustomUserCreationForm(UserCreationForm):
    # profile_image = ProcessedImageField(
    # spec_id='profile_image_thumbnail',
    # processors=[ResizeToFill(70,70)],
    # format='JPEG',
    # options={'quality' : 90},
    # required=False,
    # )
    
    birthday = forms.DateField(
        label='Birthday',
        required=False,
        widget=forms.DateInput(
        attrs={
            'class' : 'form-control w-100 p-1',
            'type': 'date',
        }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2',)
    username = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control w-100 p-1',
            'placeholder' : 'id',
        }
        )
    )

    email = forms.EmailField(
        widget= forms.EmailInput(
        attrs={
            'class' : 'form-control w-100 p-1',
            'placeholder' : 'email@example.com',
        }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control w-100 p-1',
            'placeholder' : 'firstname',
        }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control w-100 p-1',
            'placeholder' : 'lastname',
        }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput({
        'class' : 'form-control w-100 p-1',
        'placeholder' : 'password'
        }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput({
        'class' : 'form-control w-100 p-1',
        'placeholder' : 'password'
        }
        )
    )

class CustomUserChangeForm(UserChangeForm):
    profile_image = ProcessedImageField(
    spec_id='profile_image_thumbnail',
    processors=[ResizeToFill(70,70)],
    format='JPEG',
    options={'quality' : 90},
    required=False,
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'profile_image',
        )
    email = forms.EmailField(
        label='Email address',
        widget= forms.EmailInput(
        attrs={
            'class' : 'form-control ',
            'style' : 'width: 250px',
            'placeholder' : 'email@example.com',
        }
        )
    )

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control ',
            'style' : 'width: 250px',
            'placeholder' : 'firstname',
        }
        )
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width: 250px',
            'placeholder' : 'lastname',
        }
        )
    )

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100 p-2 mb-2',
                'placeholder': '아이디',
            },
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-100 p-2',
                'type': 'password',
                'placeholder': '비밀번호',
            },
        ),
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )