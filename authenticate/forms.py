from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

# Sign up form
class SignUpForm(UserCreationForm):
  email = forms.EmailField(
    label= "hier uw mailadres",
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'  })
  )
  first_name = forms.CharField(
    max_length=100,
    label='',
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'first name'}),
    help_text="<small>Enter your first name here</small>"
  )
  last_name  = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'lastname'})
  )

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
  
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    # self.fields['username'].label = 'hier uw gebruikersnaam'
    self.fields['username'].label = ''
    self.fields['username'].widget.attrs['placeholder'] = 'username'
    self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].label = ''
    self.fields['password1'].widget.attrs['placeholder'] = 'password'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].label = ''
    self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
    self.fields['password2'].help_text = '<small>Enter the same password as before, for verification.</small>'

class EditProfileForm(UserChangeForm):
  password = forms.CharField(label='', widget=forms.TextInput(attrs={'type': 'hidden'}))
  
  class Meta:
    model = User
    # exclude = ()
    fields = ('username',
              'first_name',
              'last_name',
              'email',
              'password')
