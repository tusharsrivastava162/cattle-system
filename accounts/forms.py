from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input tsinlineblock', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input tsinlineblock', 'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid credentials, try again")
            # if not user.check_password(password):
            #     raise forms.ValidationError("Incorrect passsword")
            # if not user.is_active:
            #     raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    # email = forms.EmailField(label='Email address')
    # email2 = forms.EmailField(label='Confirm Email')
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Last Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Password'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]




    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")

    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    # def clean_email2(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")
    #     return email
