from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'At least 8 characters'
            }
        )
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat your password'
            }
        )
    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Maksuda'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Parvin'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'you@example.com'
                }
            ),
        }

    def clean_email(self):

        email = self.cleaned_data['email'].lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get(
            'password_confirm'
        )

        if password and password_confirm:

            if password != password_confirm:

                raise forms.ValidationError(
                    'Passwords do not match.'
                )

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

        return user