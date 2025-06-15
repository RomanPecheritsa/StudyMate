from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")


class ConfirmRegistrationForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=150)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data
