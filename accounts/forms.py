from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label='Birthday',
        required=False,
        widget=forms.DateInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width: 250px',
            'type': 'date',
        }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2',)
    username = forms.CharField(
        label='ID',
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width: 250px',
            'placeholder' : 'id',
        }
        )
    )

    email = forms.EmailField(
        label='Email address',
        widget= forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width: 250px',
            'placeholder' : 'email@example.com',
        }
        )
    )

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
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

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput({
        'class' : 'form-control',
        'style' : 'width: 250px',
        'placeholder' : 'password'
        }
        )
    )

    password2 = forms.CharField(
        label='Verify Password',
        widget=forms.PasswordInput({
        'class' : 'form-control',
        'style' : 'width: 250px',
        'placeholder' : 'password'
        }
        )
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
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