from django import forms

from . import models


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class UserForm(forms.ModelForm):
    confirm_email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="leave empty",
        validators=[must_be_empty]
    )

    class Meta:
        model = models.CustomUser
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'library_name',
            'message',
            'street_address',
            'city',
            'state',
            'zip_code',
            'image',
        ]

    field_order = [
        'email',
        'confirm_email',
        'password',
        'confirm_password',
        'first_name',
        'last_name',
        'library_name',
        'message',
        'street_address',
        'city',
        'state',
        'zip_code',
        'image',
    ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if email != confirm_email:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )
        elif password != confirm_password:
            raise forms.ValidationError(
                "You need to enter the same password in both fields"
            )
