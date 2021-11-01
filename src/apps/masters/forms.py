from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

from .models import Master


class MasterCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = Master
        fields = ('username', 'sex', 'age')

    def clean_password2(self):
        """ Check that the two password entries match """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """ Save the provided password in hashed format """
        user = super(MasterCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MasterChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Master
        fields = ('username', 'sex', 'age')

    def clean_password(self):
        return self.initial["password"]