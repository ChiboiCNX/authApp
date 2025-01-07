# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class CreateUserForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password',]

from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    # name = forms.CharField(max_length=150, required=True, label='Name')
    # email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email',]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm-password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user    
